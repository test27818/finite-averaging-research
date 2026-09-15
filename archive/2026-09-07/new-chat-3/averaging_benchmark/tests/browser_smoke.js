// Optional end-to-end test. Requires Playwright, not needed by the solver itself.
// NODE_PATH=/workspace/browser-lab/node_modules node tests/browser_smoke.js
'use strict';
const {chromium}=require('playwright');
const assert=require('node:assert/strict');
const path=require('node:path');
const fs=require('node:fs');
const root=path.resolve(__dirname,'..');
(async()=>{
  const browser=await chromium.launch({headless:true,args:['--no-sandbox','--disable-gpu','--disable-dev-shm-usage']});
  try{
    const page=await browser.newPage({viewport:{width:1280,height:900},acceptDownloads:true});
    const errors=[],remote=[];
    page.on('pageerror',e=>errors.push(String(e)));
    page.on('request',r=>{if(/^https?:/.test(r.url()))remote.push(r.url());});
    await page.goto('file://'+path.join(root,'solver.html'));
    await page.fill('#inputArray','0, 0, 0, 1, 9');
    await page.click('#solveBtn');
    await page.waitForFunction(()=>window.averagingLab.getResult()?.status==='solved');
    await page.waitForFunction(()=>!document.body.classList.contains('busy'));
    const r=await page.evaluate(()=>window.averagingLab.getResult());
    assert.equal(r.steps,9);assert(r.verified&&r.optimal);
    await page.click('#lastBtn');
    assert.equal(await page.evaluate(()=>window.averagingLab.getStep()),9);
    const nums=await page.locator('#nodeGrid .num').allTextContents();assert(nums.every(x=>x==='2'));
    await page.click('#firstBtn');assert.equal(await page.evaluate(()=>window.averagingLab.getStep()),0);
    const [download]=await Promise.all([page.waitForEvent('download'),page.click('#jsonSingle')]);
    const exported=JSON.parse(fs.readFileSync(await download.path(),'utf8'));assert.equal(exported.steps,9);
    await page.click('[data-tab="verify"]');await page.click('#loadCurrent');await page.click('#verifyBtn');
    await page.waitForFunction(()=>document.querySelector('#verifyResults').textContent.includes('独立验解通过'));
    await page.waitForFunction(()=>!document.body.classList.contains('busy'));
    await page.click('#selftestBtn');
    await page.waitForFunction(()=>document.querySelector('#verifyResults').textContent.includes('16 / 16'));
    await page.waitForFunction(()=>!document.body.classList.contains('busy'));
    await page.fill('#inputArray','0,1,5');await page.click('#solveBtn');
    await page.waitForFunction(()=>window.averagingLab.getResult()?.status==='impossible');
    await page.waitForFunction(()=>!document.body.classList.contains('busy'));
    await page.click('[data-tab="batch"]');await page.fill('#batchCount','3');
    await page.selectOption('#searchMode','fast');await page.click('#batchBtn');
    await page.waitForFunction(()=>window.averagingLab.getBatch().length===3);
    await page.waitForFunction(()=>!document.body.classList.contains('busy'));
    const batch=await page.evaluate(()=>window.averagingLab.getBatch());assert(batch.every(x=>x.verified));
    await page.click('#batchBody [data-case="0"]');
    await page.waitForFunction(()=>window.averagingLab.getResult()?.verified===true);
    await page.setViewportSize({width:390,height:844});
    assert(await page.locator('#solveBtn').isVisible());
    await page.screenshot({path:path.join(root,'results/migration_mobile.png'),fullPage:true});
    assert.deepEqual(errors,[]);assert.deepEqual(remote,[]);
    console.log('Chromium PASS: solve/replay/zero energy/JSON download/import verification/selftests/impossible/batch/mobile; no remote requests, no page errors.');
  }finally{await browser.close();}
})().catch(e=>{console.error(e);process.exit(1);});
