// Image downloader for trend topics using CDP proxy
import http from 'http';
import https from 'https';
import fs from 'fs';
import path from 'path';

const OUT = 'C:/Users/gongjue/tiktok-reports/2026-04-09/trend_images';
fs.mkdirSync(OUT, { recursive: true });

function httpReq(url, opts = {}) {
  return new Promise((resolve, reject) => {
    const mod = url.startsWith('https') ? https : http;
    const req = mod.request(url, opts, res => {
      if (res.statusCode >= 300 && res.statusCode < 400 && res.headers.location) {
        return httpReq(res.headers.location, opts).then(resolve, reject);
      }
      const chunks = [];
      res.on('data', c => chunks.push(c));
      res.on('end', () => resolve({ status: res.statusCode, data: Buffer.concat(chunks) }));
    });
    req.on('error', reject);
    if (opts.body) req.write(opts.body);
    req.end();
  });
}

async function proxyGet(path) {
  const r = await httpReq(`http://localhost:3456${path}`);
  return r.data.toString();
}

async function proxyPost(path, body) {
  const r = await httpReq(`http://localhost:3456${path}`, { method: 'POST', body });
  return r.data.toString();
}

async function downloadImg(url, filepath) {
  try {
    const r = await httpReq(url, { headers: { 'User-Agent': 'Mozilla/5.0' } });
    if (r.data.length > 5000) {
      fs.writeFileSync(filepath, r.data);
      return true;
    }
  } catch (e) {}
  return false;
}

async function getImagesFromPage(targetId) {
  await new Promise(r => setTimeout(r, 3000));
  const js = `(() => {
    const all = [];
    document.querySelectorAll('img').forEach(img => {
      const s = img.src || img.getAttribute('data-src') || '';
      if (s.startsWith('http') && !s.includes('google.com') && !s.includes('gstatic') && !s.includes('googleapis') && !s.includes('favicon')) {
        const w = img.naturalWidth || img.width || 0;
        const h = img.naturalHeight || img.height || 0;
        if (w >= 200 || h >= 200 || s.length > 100) all.push(s);
      }
    });
    return JSON.stringify([...new Set(all)]);
  })()`;
  const result = await proxyPost(`/eval?target=${targetId}`, js);
  try { return JSON.parse(result); } catch { return []; }
}

const topics = [
  { num: '01', slug: 'star_wars_maul', urls: [
    'https://www.starwars.com/news/star-wars-maul-shadow-lord-first-trailer-poster-art',
    'https://www.starwars.com/series/star-wars-maul-shadow-lord',
    'https://www.imdb.com/title/tt36594331/'
  ]},
  { num: '02', slug: 'the_boys_s5', urls: [
    'https://heroichollywood.com/the-boys-battlelines-posters-final-season/',
    'https://cosmicbook.news/the-boys-final-season-posters-ccxp',
    'https://www.imdb.com/title/tt1190634/'
  ]},
  { num: '03', slug: 'invincible_s4', urls: [
    'https://www.imdb.com/title/tt6741278/',
    'https://bleedingcool.com/tv/invincible-season-4-key-art-poster-offers-episode-release-schedule/',
    'https://tvseriesfinale.com/tv-show/invincible-season-four-trailer-and-poster-released-for-prime-video-superhero-series/'
  ]},
  { num: '04', slug: 'daredevil_born_again', urls: [
    'https://www.marvel.com/tv-shows/daredevil-born-again/2',
    'https://thefutureoftheforce.com/2026/03/14/the-latest-daredevil-born-again-season-2-poster-unleashes-the-kingpin/',
    'https://www.imdb.com/title/tt14164846/'
  ]},
  { num: '05', slug: 'hades_ii', urls: [
    'https://www.creativeuncut.com/art_hades-2_a.html',
    'https://www.creativeuncut.com/gallery-47/hades2-melinoe.html',
    'https://store.steampowered.com/app/1145350/Hades_II/'
  ]},
  { num: '06', slug: 'diablo_iv_hatred', urls: [
    'https://diablo4.blizzard.com/en-us/lord-of-hatred',
    'https://fextralife.com/diablo-4-lord-of-hatred-release-date-and-new-content-revealed/',
    'https://www.imdb.com/title/tt36804600/'
  ]},
  { num: '07', slug: 'pokemon_champions', urls: [
    'https://champions.pokemon.com/en-us/',
    'https://www.pokemon.com/us/pokemon-news/pokemon-champions-releases-on-nintendo-switch-and-nintendo-switch-2-on-april-8-2026',
    'https://www.nintendo.com/us/store/products/pokemon-champions-switch/'
  ]},
  { num: '08', slug: 'agentic_ai', urls: [
    'https://www.nextgov.com/artificial-intelligence/2025/12/2026-set-be-year-agentic-ai-industry-predicts/410324/',
    'https://machinelearningmastery.com/7-agentic-ai-trends-to-watch-in-2026/',
    'https://www.tiledb.com/blog/what-is-agentic-ai'
  ]},
  { num: '09', slug: 'stranger_things_85', urls: [
    'https://www.netflix.com/tudum/articles/stranger-things-animated-series-news',
    'https://www.justjared.com/2026/03/27/netflix-shares-new-trailer-photos-poster-for-stranger-things-tales-from-85/',
    'https://www.imdb.com/title/tt27486290/'
  ]},
  { num: '10', slug: 'kenny_omega', urls: [
    'https://www.allelitewrestling.com/post/aew-dynamite-preview-april-8-2026',
    'https://www.ewrestlingnews.com/news/aew/kenny-omega-returns-to-aew-at-revolution-2026',
    'https://www.postwrestling.com/2026/01/07/kenny-omega-return-darby-allin-vs-pac-among-new-additions-to-aew-maximum-carnage-2026/'
  ]}
];

async function processTopic(topic) {
  console.log(`\n=== ${topic.num} ${topic.slug} ===`);
  let downloaded = 0;

  for (const pageUrl of topic.urls) {
    if (downloaded >= 3) break;
    console.log(`  Visiting: ${pageUrl}`);

    let targetId;
    try {
      const resp = await proxyGet(`/new?url=${encodeURIComponent(pageUrl)}`);
      const obj = JSON.parse(resp);
      targetId = obj.targetId || obj.id;
    } catch (e) {
      console.log(`  Failed to open: ${e.message}`);
      continue;
    }

    if (!targetId) { console.log('  No targetId'); continue; }

    const imgUrls = await getImagesFromPage(targetId);
    console.log(`  Found ${imgUrls.length} images`);

    for (const imgUrl of imgUrls) {
      if (downloaded >= 3) break;
      const fn = `${topic.num}_${topic.slug}_${downloaded + 1}.jpg`;
      const fp = path.join(OUT, fn);
      console.log(`  Downloading: ${imgUrl.substring(0, 80)}...`);
      const ok = await downloadImg(imgUrl, fp);
      if (ok) {
        downloaded++;
        console.log(`  SAVED: ${fn}`);
      }
    }

    // Close tab
    try { await proxyGet(`/close?target=${targetId}`); } catch {}
  }

  // If still not enough, try Google Images as fallback
  if (downloaded < 3) {
    console.log(`  Only ${downloaded}/3, trying Google Images fallback...`);
    const query = topic.slug.replace(/_/g, ' ');
    const searchUrl = `https://www.google.com/search?q=${encodeURIComponent(query)}&tbm=isch&tbs=isz:l`;
    let targetId;
    try {
      const resp = await proxyGet(`/new?url=${encodeURIComponent(searchUrl)}`);
      const obj = JSON.parse(resp);
      targetId = obj.targetId || obj.id;
    } catch { return; }

    if (targetId) {
      await new Promise(r => setTimeout(r, 3000));
      // Click first few images to get full-res URLs
      const js = `(() => {
        const imgs = [];
        document.querySelectorAll('[data-tbnid] img, .isv-r img').forEach(img => {
          const s = img.src || '';
          if (s.startsWith('http') && !s.includes('google') && !s.includes('gstatic')) imgs.push(s);
        });
        // Also get from anchor elements
        document.querySelectorAll('a[href*="imgurl="]').forEach(a => {
          const m = a.href.match(/imgurl=([^&]+)/);
          if (m) imgs.push(decodeURIComponent(m[1]));
        });
        return JSON.stringify([...new Set(imgs)].slice(0, 10));
      })()`;
      const result = await proxyPost(`/eval?target=${targetId}`, js);
      let urls = [];
      try { urls = JSON.parse(result); } catch {}

      for (const imgUrl of urls) {
        if (downloaded >= 3) break;
        const fn = `${topic.num}_${topic.slug}_${downloaded + 1}.jpg`;
        const fp = path.join(OUT, fn);
        const ok = await downloadImg(imgUrl, fp);
        if (ok) {
          downloaded++;
          console.log(`  SAVED: ${fn}`);
        }
      }
      try { await proxyGet(`/close?target=${targetId}`); } catch {}
    }
  }

  console.log(`  Final count: ${downloaded}/3`);
}

async function main() {
  // Process sequentially to avoid overwhelming the browser
  for (const topic of topics) {
    await processTopic(topic);
  }

  // List results
  const files = fs.readdirSync(OUT);
  console.log(`\n=== RESULTS: ${files.length} files ===`);
  files.forEach(f => console.log(`  ${f}`));
}

main().catch(console.error);
