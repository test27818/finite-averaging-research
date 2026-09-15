'use strict';

const vm = require('node:vm');
const readline = require('node:readline');
const { performance } = require('node:perf_hooks');
const { webcrypto } = require('node:crypto');

let context;
let messages;
const lines = readline.createInterface({ input: process.stdin, crlfDelay: Infinity });
lines.on('line', line => {
  try {
    const request = JSON.parse(line);
    let result;
    if (request.action === 'initialize') {
      messages = [];
      context = vm.createContext({ performance, crypto: webcrypto, onmessage: null,
        postMessage: value => messages.push(value) });
      for (const source of request.scripts) vm.runInContext(source, context);
      result = { ready: true };
    } else if (request.action === 'selftest') {
      messages.length = 0;
      context.onmessage({ data: { type: 'selftest' } });
      const error = messages.find(item => item.type === 'error');
      if (error) throw new Error(error.message);
      result = messages.find(item => item.type === 'selftested').data;
    } else if (request.action === 'solve') {
      messages.length = 0;
      result = context.solveOne(request.input, request.options || {});
    } else if (request.action === 'lower-bounds') {
      result = request.states.map(state => context.lowerBound(state.map(BigInt)));
    } else {
      throw new Error('Unknown harness action');
    }
    process.stdout.write(JSON.stringify({ ok: true, result },
      (_, value) => typeof value === 'bigint' ? value.toString() : value) + '\n');
  } catch (error) {
    process.stdout.write(JSON.stringify({ ok: false, error: error.stack }) + '\n');
  }
});
