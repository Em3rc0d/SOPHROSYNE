import fs from 'node:fs';
import vm from 'node:vm';
import crypto from 'node:crypto';

const path = new URL('./index.html', import.meta.url);
const html = fs.readFileSync(path, 'utf8');

function assert(name, condition) {
  if (!condition) {
    console.error('FAIL:', name);
    process.exitCode = 1;
  } else {
    console.log('PASS:', name);
  }
}

assert('doctype/html closes', html.startsWith('<!doctype html>') && html.includes('</html>'));
assert('research boundary visible', html.includes('PROTOTIPO DE INVESTIGACIÓN PRE-MK0'));
assert('no live trading promise', html.includes('Sin trading'));
assert('no personalized recommendations promise', html.includes('Sin recomendaciones personalizadas'));
assert('runtime record forbids recommendation', html.includes('recommendation: null'));
assert('runtime record forbids live trade', html.includes('live_trade: false'));
assert('no external JavaScript', !/<script[^>]+src=/i.test(html));
assert('seven Q00 arms preserved', ['A','B','C','D','E','F','G'].every(x => html.includes(`data-arm="${x}"`)));
assert('five scenario corpus present', ['SYN-01','SYN-02','SYN-03','SYN-04','SYN-05'].every(x => html.includes(x)));
assert('locked rehearsal assignment present', html.includes('assignmentLocked') && html.includes('ASIGNACIÓN BLOQUEADA'));
assert('task timing captured', html.includes('completion_seconds') && html.includes('scenarioStartedAt'));
assert('cognitive cost captured', html.includes('workload_rating') && html.includes('help_requested'));
assert('simple feedback arm hides and reveals outcome', html.includes('simplePrediction') && html.includes('simple_feedback_revealed') && html.includes('hiddenOutcome'));
assert('memory ablation surfaces present', html.includes('shortMemoryContext') && html.includes('fullMemoryContext'));
assert('comparator proxy cannot impersonate promotable G', html.includes('comparator_g_promotable: false') && html.includes('UAT proxy solamente'));
assert('novice quick summary present', ['quickKnown','quickMissing','quickTakeaway'].every(x => html.includes(x)));
assert('progressive depth preserved', ['data-depth="beginner"','data-depth="investor"','data-depth="trader"','data-depth="quant"'].every(x => html.includes(x)));
assert('detail does not imply certainty', html.includes('más detalle no implica más certeza'));
assert('local-only persistence boundary', html.includes('localStorage'));
assert('low-information guard present', html.includes('decision_record_rejected_low_information') && html.includes('looksLowInformation'));
assert('explicit evidence divergence guard present', html.includes('evidence_alignment') && html.includes('divergenceAck'));
assert('internal process labels mapped for display', html.includes('processLabels'));
assert('confidence semantics clarified', html.includes('No es una probabilidad de que el mercado suba o baje'));
assert('Q03-compatible core events', [
  'session_started',
  'evidence_expanded',
  'opposing_evidence_opened',
  'uncertainty_opened',
  'invalidation_opened',
  'decision_record_created',
  'decision_record_revisited',
  'session_ended'
].every(x => html.includes(x)));
assert('v2.0 version frozen', html.includes('research-prototype-v2.0.0'));

const matches = [...html.matchAll(/<script>([\s\S]*?)<\/script>/g)];
assert('exactly one inline application script', matches.length === 1);
if (matches.length === 1) {
  try {
    new vm.Script(matches[0][1]);
    console.log('PASS: JavaScript syntax');
  } catch (error) {
    console.error('FAIL: JavaScript syntax', error.message);
    process.exitCode = 1;
  }
}

const digest = crypto.createHash('sha256').update(html).digest('hex');
console.log('SHA256:', digest);

if (process.exitCode) process.exit(process.exitCode);
