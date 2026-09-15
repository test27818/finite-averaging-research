'use strict';

const fs = require('node:fs');
const vm = require('node:vm');
const { performance } = require('node:perf_hooks');
const { webcrypto } = require('node:crypto');

const root = 'C:/Users/19226/Documents/Codex/2026-09-07/new-chat-3';
const projectHtml = fs.readFileSync(root + '/averaging_benchmark/solver.html', 'utf8');
const externalHtml = fs.readFileSync('C:/Users/19226/Documents/Tencent Files/1250148178/FileRecv/2_average_solver.html', 'utf8');

function scriptById(html, id) {
  const match = html.match(new RegExp('<script id="' + id + '"[^>]*>([\\s\\S]*?)</script>'));
  if (!match) throw new Error('Missing script: ' + id);
  return match[1];
}

function makeProjectEngine() {
  const source = ['solver-source', 'verifier-source', 'runner-source']
    .map(id => scriptById(projectHtml, id)).join('\n');
  const context = { performance, crypto: webcrypto, console };
  vm.createContext(context);
  vm.runInContext(source, context, { filename: 'project-web-engine.js' });
  return context;
}

function makeExternalEngine() {
  const context = { performance, crypto: webcrypto, console };
  vm.createContext(context);
  vm.runInContext(scriptById(externalHtml, 'engineScript') + '\n;globalThis.__engine = Engine; globalThis.__idaOptimize = idaOptimize; globalThis.__beamOptimize = beamOptimize;', context, { filename: 'external-web-engine.js' });
  return { engine: context.__engine, idaOptimize: context.__idaOptimize, beamOptimize: context.__beamOptimize };
}

const cases = [
  ['case_1', ['-98', '96', '36', '23', '67', '-38', '-83', '77', '-32', '7']],
  ['case_2', ['-87', '-61', '57', '94', '-76', '85', '96', '7', '-79', '-91']],
  ['case_3', ['-74', '-50', '92', '-42', '57', '23', '55', '35', '81', '-2']],
];

const runBudgetMs = Number(process.argv[2] || 60000);
const requestedCase = process.argv[3];
const requestedEngine = process.argv[4] || 'both';
const project = makeProjectEngine();
const external = makeExternalEngine();

function runProject(input) {
  return project.solveOne(input, { hardMs: runBudgetMs, optMs: runBudgetMs - 1000 });
}

function runExternal(input) {
  return external.engine.solve(input, { mode: 'deep', budgetMs: runBudgetMs, constructMs: runBudgetMs + 1000 });
}

for (const [name, input] of cases.filter(([name]) => !requestedCase || name === requestedCase)) {
  const p = requestedEngine === 'external' ? null : runProject(input);
  if (p) console.error(name + ': project complete (' + p.steps + ' steps, optimal=' + p.optimal + ')');
  const e = requestedEngine === 'project' ? null : runExternal(input);
  if (e) console.error(name + ': external complete (' + e.steps + ' steps, optimal=' + e.optimal + ')');
  console.log(JSON.stringify({
    name,
    input,
    project: p && {
      status: p.status,
      steps: p.steps,
      optimal: p.optimal,
      lowerBound: p.lowerBound,
      initialSteps: p.initialSteps,
      metrics: p.metrics,
      algorithm: p.algorithm,
    },
    external: e && {
      status: e.status,
      steps: e.steps,
      optimal: e.optimal,
      lowerBound: e.lowerBound,
      baselineSteps: e.baselineSteps,
      solveMs: e.solveMs,
      verifyMs: e.verifyMs,
      nodes: e.nodes,
      algorithm: e.algorithm,
    },
  }));
}
