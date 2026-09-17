import fs from 'node:fs/promises';
import assert from 'node:assert/strict';

const html = await fs.readFile(new URL('./index.html', import.meta.url), 'utf8');

for (const id of [
  'scenarioNav','marketState','supportEvidence','opposeEvidence','uncertaintyCard',
  'invalidatorCard','decisionForm','ledgerDialog','exportBtn','resetBtn'
]) assert.ok(html.includes(`id="${id}"`), `missing DOM id: ${id}`);

for (const eventName of [
  'session_started','evidence_expanded','opposing_evidence_opened','uncertainty_opened',
  'invalidation_opened','decision_record_created','decision_record_revisited','session_ended'
]) assert.ok(html.includes(`'${eventName}'`), `missing Q03 event: ${eventName}`);

for (const arm of ['raw','friction','full'])
  assert.ok(html.includes(`'${arm}'`), `missing Q00 arm: ${arm}`);

assert.ok(html.includes('NOT_PROMOTABLE_EVIDENCE_UNLESS_RUN_UNDER_FROZEN_PREREGISTERED_PROTOCOL'));
assert.ok(html.includes('Sin trading'));
assert.ok(html.includes('Sin recomendaciones personalizadas'));
assert.ok(html.includes('localStorage'));

console.log('research prototype contract: PASS');
