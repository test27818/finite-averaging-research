'use strict';

const fs = require('node:fs');
const vm = require('node:vm');
const { performance } = require('node:perf_hooks');
const { webcrypto } = require('node:crypto');

const html = fs.readFileSync('C:/Users/19226/Documents/Tencent Files/1250148178/FileRecv/2_average_solver.html', 'utf8');
const source = html.match(/<script id="engineScript"[^>]*>([\s\S]*?)<\/script>/)[1];
const context = { performance, crypto: webcrypto, console };
vm.createContext(context);
vm.runInContext(source + '\n;globalThis.__engine=Engine;globalThis.__ida=idaOptimize;globalThis.__beam=beamOptimize;', context);

const cases = {
  case_1: ['-98', '96', '36', '23', '67', '-38', '-83', '77', '-32', '7'],
  case_2: ['-87', '-61', '57', '94', '-76', '85', '96', '7', '-79', '-91'],
  case_3: ['-74', '-50', '92', '-42', '57', '23', '55', '35', '81', '-2'],
};
const budgetMs = Number(process.argv[2] || 120000);
const caseName = process.argv[3] || 'case_1';
const beamMs = Number(process.argv[4] || 10000);
const input = cases[caseName];
if (!input) throw new Error('Unknown case');

const started = performance.now();
const a = context.__engine.inspect(input).e.map(BigInt);
const base = context.__engine.constructive(a, { constructMs: budgetMs });
let best = base.ops;
const beamStart = performance.now();
const beam = context.__beam(a, best, { deadline: beamStart + beamMs, width: 64, maxStates: 200000 });
best = beam.ops;
const ida = context.__ida(a, best, Math.max(0, budgetMs - (performance.now() - started)));
best = ida.ops;
const operations = best.map(([i, j]) => [i + 1, j + 1]);
const verify = context.__engine.independentVerify(input, operations);
console.log(JSON.stringify({
  caseName,
  budgetMs,
  beamMs,
  baselineSteps: base.ops.length,
  afterBeamSteps: beam.ops.length,
  constructChecks: base.checks,
  beamNodes: beam.nodes,
  idaNodes: ida.nodes,
  idaIterations: ida.iterations,
  steps: operations.length,
  optimal: ida.optimal,
  lowerBound: ida.lower,
  solveMs: performance.now() - started,
  verified: verify.ok,
}));
