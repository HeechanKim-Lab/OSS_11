/**
 * @heechankim-lab/oss-11
 * JavaScript/Node.js SDK for Micro-Tom Rhizosphere Amplicon Manifest Validation & Deterministic Feature Flags
 */

const crypto = require('crypto');

function computeBucket(key) {
  const hash = crypto.createHash('sha256').update(String(key)).digest('hex');
  return parseInt(hash.substring(0, 8), 16) % 100;
}

function assignAbVariant(userId, experimentId = 'exp_pcoa_workbench_v1') {
  if (!userId || !String(userId).trim()) {
    throw new Error('userId must be a non-empty string');
  }
  const bucket = computeBucket(`${experimentId}:${String(userId).trim()}`);
  return bucket < 50 ? 'variant_B' : 'variant_A';
}

function validateCasavaRecord(record) {
  const hasId = Boolean(record && record.sampleId && String(record.sampleId).trim());
  const validR1 = Boolean(record && record.forwardFastq && record.forwardFastq.endsWith('.fastq.gz') && record.forwardFastq.includes('_R1_'));
  const validR2 = Boolean(record && record.reverseFastq && record.reverseFastq.endsWith('.fastq.gz') && record.reverseFastq.includes('_R2_'));
  return {
    isValid: hasId && validR1 && validR2,
    sampleId: record ? record.sampleId : null,
  };
}

function selfTest() {
  const v1 = assignAbVariant('researcher_01');
  const v2 = assignAbVariant('researcher_01');
  if (v1 !== v2) {
    throw new Error('Deterministic A/B variant test failed');
  }
  const qc = validateCasavaRecord({
    sampleId: 'GJ_01',
    forwardFastq: 'GJ_01_S1_L001_R1_001.fastq.gz',
    reverseFastq: 'GJ_01_S1_L001_R2_001.fastq.gz',
  });
  if (!qc.isValid) {
    throw new Error('Casava validation self-test failed');
  }
  console.log('[PASS] @heechankim-lab/oss-11 SDK selfTest succeeded (variant=' + v1 + ')');
}

function getPackageVersion() {
  return '1.0.1';
}

module.exports = {
  getPackageVersion,
  computeBucket,
  assignAbVariant,
  validateCasavaRecord,
  selfTest,
};
