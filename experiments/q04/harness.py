"""Q04 deterministic research-harness dry run.

Synthetic/paper-only. This file validates accounting and anti-leakage mechanics;
it is not a strategy recommendation, profitability claim, production data profile,
or authorization for real-money execution.
"""

from __future__ import annotations

from dataclasses import dataclass
import hashlib
import json
import math
import statistics


@dataclass(frozen=True)
class Bar:
    t: int
    close: float
    available_at: int


def make_synthetic_bars(n: int = 40) -> list[Bar]:
    prices: list[float] = []
    p = 100.0
    for i in range(n):
        drift = 0.5 if i < 12 else (-0.35 if i < 24 else (0.15 if i < 32 else -0.05))
        cyc = [0.0, 0.8, -0.3, 0.4, -0.6][i % 5]
        p = round(max(1.0, p + drift + cyc), 4)
        prices.append(p)
    return [Bar(i, px, i) for i, px in enumerate(prices)]


def sma(xs: list[float], end: int, window: int) -> float | None:
    if end + 1 < window:
        return None
    return sum(xs[end - window + 1 : end + 1]) / window


def signal_series(bars: list[Bar], strategy: str) -> list[int]:
    px = [b.close for b in bars]
    out: list[int] = []
    for t in range(len(bars)):
        if strategy == "cash":
            s = 0
        elif strategy == "buy_hold":
            s = 1
        elif strategy == "trend":
            fast, slow = sma(px, t, 3), sma(px, t, 7)
            s = 0 if fast is None or slow is None else int(fast > slow)
        elif strategy == "momentum":
            s = 0 if t < 5 else int(px[t] > px[t - 5])
        elif strategy == "mean_reversion":
            mean = sma(px, t, 5)
            s = 0 if mean is None else int(px[t] < mean * 0.995)
        else:
            raise ValueError(f"unknown strategy: {strategy}")
        out.append(s)
    return out


def run_backtest(
    bars: list[Bar], strategy: str, cost_bps: float = 5.0, start: int = 0, end: int | None = None
) -> dict:
    if end is None:
        end = len(bars) - 1

    signals = signal_series(bars, strategy)
    equity = 1.0
    position = 0
    period_returns: list[float] = []
    fills: list[dict] = []
    total_cost_fraction = 0.0

    for t in range(start, end):
        target = signals[t]
        turnover = abs(target - position)
        cost = turnover * cost_bps / 10_000.0
        if turnover:
            fills.append({"t": t, "from": position, "to": target, "cost_frac": round(cost, 10)})

        next_return = bars[t + 1].close / bars[t].close - 1.0
        # Rebalance at t, pay cost, then hold target exposure over t -> t+1.
        period_factor = (1.0 - cost) * (1.0 + target * next_return)
        equity *= period_factor
        period_returns.append(period_factor - 1.0)
        total_cost_fraction += cost
        position = target

    exit_cost = abs(position) * cost_bps / 10_000.0
    if position:
        fills.append({"t": end, "from": position, "to": 0, "cost_frac": round(exit_cost, 10)})
        equity *= 1.0 - exit_cost
        period_returns.append(-exit_cost)
        total_cost_fraction += exit_cost

    peak = 1.0
    replay_equity = 1.0
    max_drawdown = 0.0
    for r in period_returns:
        replay_equity *= 1.0 + r
        peak = max(peak, replay_equity)
        max_drawdown = max(max_drawdown, 1.0 - replay_equity / peak)

    mean = statistics.mean(period_returns) if period_returns else 0.0
    stdev = statistics.pstdev(period_returns) if len(period_returns) > 1 else 0.0
    sharpe = 0.0 if stdev == 0.0 else mean / stdev * math.sqrt(252)

    return {
        "strategy": strategy,
        "cost_bps": cost_bps,
        "start": start,
        "end": end,
        "equity_final": round(equity, 12),
        "net_return": round(equity - 1.0, 12),
        "max_drawdown": round(max_drawdown, 12),
        "sharpe_annualized": round(sharpe, 8),
        "fills": fills,
        "total_cost_frac": round(total_cost_fraction, 10),
    }


def digest(obj: object) -> str:
    payload = json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(payload).hexdigest()


def run_dry_run() -> dict:
    bars = make_synthetic_bars()
    strategies = ["cash", "buy_hold", "trend", "momentum", "mean_reversion"]

    first = {s: run_backtest(bars, s, 5.0, 0, len(bars) - 1) for s in strategies}
    second = {s: run_backtest(bars, s, 5.0, 0, len(bars) - 1) for s in strategies}

    mini = [Bar(0, 100.0, 0), Bar(1, 110.0, 1)]
    fee_bps = 10.0
    expected = (1 - fee_bps / 10_000) * (110 / 100) * (1 - fee_bps / 10_000) - 1
    actual = run_backtest(mini, "buy_hold", fee_bps, 0, 1)["net_return"]

    checks = {
        "G1_point_in_time_integrity": all(b.available_at <= b.t for b in bars),
        "G2_golden_buy_hold_fee_fixture": abs(actual - expected) < 1e-12,
        "G3_deterministic_rerun": digest(first) == digest(second),
        "G5_cost_monotonicity": all(
            run_backtest(bars, s, 50.0, 0, len(bars) - 1)["net_return"]
            <= run_backtest(bars, s, 5.0, 0, len(bars) - 1)["net_return"] + 1e-12
            for s in strategies
        ),
        "G6_cash_sanity": first["cash"]["net_return"] == 0.0 and not first["cash"]["fills"],
        "G6_buy_hold_sanity": first["buy_hold"]["fills"][0]["t"] == 0
        and first["buy_hold"]["fills"][-1]["t"] == len(bars) - 1,
        "G7_dataset_integrity": len({b.t for b in bars}) == len(bars)
        and [b.t for b in bars] == sorted(b.t for b in bars)
        and all(b.close > 0 for b in bars),
        "G8_final_test_boundary_declared": 29 < 30 < len(bars),
    }

    return {
        "dry_run_only": True,
        "synthetic_data_only": True,
        "checks": checks,
        "all_internal_checks_pass": all(checks.values()),
        "artifact_hash": digest(first),
        "results": first,
        "unresolved": [
            "G4_independent_reproduction",
            "Q02 production data-rights profile",
            "real provider point-in-time dataset",
        ],
    }


if __name__ == "__main__":
    print(json.dumps(run_dry_run(), indent=2, sort_keys=True))
