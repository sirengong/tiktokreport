// Download images for trend topics via CDP Google Images
const http = require('http');
const https = require('https');
const fs = require('fs');
const path = require('path');

const PROXY = 'http://localhost:3456';
const DIR = 'C:/Users/gongjue/tiktok-reports/2026-04-09/trend_images';

const TOPICS = [
  ['01', 'star_wars_maul', 'Star Wars Maul Shadow Lord animated series'],
  ['02', 'the_boys_s5', 'The Boys Season 5 TV show'],
  ['03', 'invincible_s4', 'Invincible Season 4 animated series'],
  ['04', 'daredevil_born_again', 'Daredevil Born Again Season 2'],
  ['05', 'hades_ii', 'Hades II game'],
  ['06', 'diablo_iv_hatred', 'Diablo IV Vessel of Hatred expansion'],
  ['07', 'pokemon_champions', 'Pokemon Champions game 2026'],
  ['08', 'agentic_ai', 'Agentic AI technology'],
  ['09', 'stranger_things_85', 'Stranger Things Tales from 1985'],
  ['10', 'kenny_omega', 'Kenny Omega AEW wrestling return'],
];

function get(url) {
  return new Promise((ok, fail) => {
    http.get(url, r => {
      let d = ''; r.on('data', c => d += c);
      r.on('end', () => { try { ok(JSON.parse(d)); } catch { ok(d); } });
    }).on('error', fail);
  });
}

function post(url, body) {
  return new Promise((ok, fail) => {
    const u = new URL(url);
    const req = http.request({ hostname: u.hostname, port: u.port, path: u.pathname + u.search, method: 'POST', headers: { 'Content-Type': 'text/plain' } }, r => {
      let d = ''; r.on('data', c => d += c);
      r.on('end', () => { try { ok(JSON.parse(d)); } catch { ok(d); } });
    });
    req.on('error', fail); req.write(body); req.end();
  });
}

function dl(url, fp) {
  return new Promise((ok, fail) => {
    const go = (u, n) => {
      if (n > 5) return fail(new Error('redirects'));
      const mod = u.startsWith('https') ? https : http;
      mod.get(u, { headers: { 'User-Agent': 'Mozilla/5.0' } }, r => {
        if (r.statusCode >= 300 && r.statusCode < 400 && r.headers.location) return go(r.headers.location, n + 1);
        if (r.statusCode !== 200) return fail(new Error('HTTP ' + r.statusCode));
        const s = fs.createWriteStream(fp); r.pipe(s);
        s.on('finish', () => { s.close(); ok(fs.statSync(fp).size); });
      }).on('error', fail);
    };
    go(url, 0);
  });
}

const wait = ms => new Promise(r => setTimeout(r, ms));

async function doTopic(id, slug, query) {
  console.log(`\n=== ${id}: ${query} ===`);
  const q = encodeURIComponent(query);
  const surl = `https://www.google.com/search?q=${q}&tbm=isch`;
  const tab = await get(`${PROXY}/new?url=${encodeURIComponent(surl)}`);
  const tid = tab.targetId;
  console.log('tab:', tid);
  await wait(3000);
  await get(`${PROXY}/scroll?target=${tid}&y=800`);
  await wait(1500);

  // Extract encrypted-tbn thumbnail URLs
  const js1 = `JSON.stringify([...document.querySelectorAll('img[src*="encrypted-tbn"]')].map(i=>i.src).filter((v,i,a)=>a.indexOf(v)===i).slice(0,15))`;
  const r1 = await post(`${PROXY}/eval?target=${tid}`, js1);
  let urls = [];
  try { urls = JSON.parse(r1.value); } catch {}
  console.log(`thumbnails: ${urls.length}`);

  // Also extract from scripts
  const js2 = `JSON.stringify((() => { const u=[]; document.querySelectorAll('script').forEach(s => { const m = s.textContent.match(/https?:\\/\\/[^"'\\\\s]+\\.(?:jpg|jpeg|png|webp)/gi); if(m) m.forEach(x => { if(!x.includes('google')&&!x.includes('gstatic')) u.push(x); }); }); return [...new Set(u)].slice(0,20); })())`;
  const r2 = await post(`${PROXY}/eval?target=${tid}`, js2);
  let sUrls = [];
  try { sUrls = JSON.parse(r2.value); } catch {}
  console.log(`script urls: ${sUrls.length}`);

  const all = [...urls, ...sUrls];
  let got = 0;
  const used = new Set();
  for (const u of all) {
    if (got >= 3) break;
    if (used.has(u)) continue;
    const fp = path.join(DIR, `${id}_${slug}_${got + 1}.jpg`);
    try {
      const sz = await dl(u, fp);
      if (sz >= 5000) { console.log(`  OK ${got+1}: ${sz}b`); got++; used.add(u); }
      else { fs.unlinkSync(fp); }
    } catch (e) { try { fs.unlinkSync(fp); } catch {} }
  }

  // fallback: if not enough, click first result and extract full image
  if (got < 3) {
    console.log('  trying click fallback...');
    const jsClick = `JSON.stringify((() => {
      const items = document.querySelectorAll('[data-ri]');
      const results = [];
      for (let i = 0; i < Math.min(6, items.length); i++) {
        items[i].click();
      }
      return items.length;
    })())`;
    await post(`${PROXY}/eval?target=${tid}`, jsClick);
    await wait(2000);

    // After clicking, look for full-size image in side panel
    const jsFull = `JSON.stringify([...document.querySelectorAll('img[src^="http"]')].filter(i => i.naturalWidth > 200 && !i.src.includes('google') && !i.src.includes('gstatic')).map(i => i.src).filter((v,i,a) => a.indexOf(v) === i).slice(0, 10))`;
    const r3 = await post(`${PROXY}/eval?target=${tid}`, jsFull);
    let fullUrls = [];
    try { fullUrls = JSON.parse(r3.value); } catch {}
    console.log(`  full urls: ${fullUrls.length}`);

    for (const u of fullUrls) {
      if (got >= 3) break;
      if (used.has(u)) continue;
      const fp = path.join(DIR, `${id}_${slug}_${got + 1}.jpg`);
      try {
        const sz = await dl(u, fp);
        if (sz >= 5000) { console.log(`  OK ${got+1}: ${sz}b`); got++; used.add(u); }
        else { fs.unlinkSync(fp); }
      } catch { try { fs.unlinkSync(fp); } catch {} }
    }
  }

  await get(`${PROXY}/close?target=${tid}`);
  console.log(`  result: ${got}/3`);
  return got;
}

async function main() {
  let total = 0;
  for (const [id, slug, query] of TOPICS) {
    total += await doTopic(id, slug, query);
    await wait(1000);
  }
  console.log(`\n=== TOTAL: ${total}/30 ===`);
  const files = fs.readdirSync(DIR).filter(f => /\.(jpg|png)$/i.test(f));
  for (const f of files) {
    console.log(`  ${f}: ${fs.statSync(path.join(DIR, f)).size}b`);
  }
}

main().catch(e => { console.error(e); process.exit(1); });
