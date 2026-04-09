// Batch image downloader using CDP proxy
import http from 'node:http';
import https from 'node:https';
import fs from 'node:fs';
import path from 'node:path';

const OUT = 'C:/Users/gongjue/tiktok-reports/2026-04-09/trend_images';
fs.mkdirSync(OUT, { recursive: true });

function proxyGet(urlPath) {
  return new Promise((resolve, reject) => {
    http.get(`http://localhost:3456${urlPath}`, res => {
      let d = ''; res.on('data', c => d += c); res.on('end', () => resolve(d));
    }).on('error', reject);
  });
}

function proxyPost(urlPath, body) {
  return new Promise((resolve, reject) => {
    const req = http.request({ hostname: 'localhost', port: 3456, path: urlPath, method: 'POST' }, res => {
      let d = ''; res.on('data', c => d += c); res.on('end', () => resolve(d));
    });
    req.on('error', reject);
    req.write(body);
    req.end();
  });
}

function download(url, fp) {
  return new Promise(resolve => {
    const mod = url.startsWith('https') ? https : http;
    const doReq = (u, redirects = 0) => {
      if (redirects > 5) return resolve(false);
      mod.get(u, { headers: { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)' }, timeout: 15000 }, res => {
        if (res.statusCode >= 300 && res.statusCode < 400 && res.headers.location) {
          const loc = res.headers.location;
          const nextMod = loc.startsWith('https') ? https : http;
          return nextMod === mod ? doReq(loc, redirects + 1) : resolve(false);
        }
        const chunks = [];
        res.on('data', c => chunks.push(c));
        res.on('end', () => {
          const buf = Buffer.concat(chunks);
          if (buf.length > 3000) { fs.writeFileSync(fp, buf); resolve(true); }
          else resolve(false);
        });
      }).on('error', () => resolve(false)).on('timeout', () => resolve(false));
    };
    doReq(url);
  });
}

const sleep = ms => new Promise(r => setTimeout(r, ms));

async function getImagesViaGoogleSearch(query) {
  const searchUrl = `https://www.google.com/search?q=${encodeURIComponent(query)}&tbm=isch&tbs=isz:l`;
  let tid;
  try {
    const r = JSON.parse(await proxyGet(`/new?url=${encodeURIComponent(searchUrl)}`));
    tid = r.targetId || r.id;
  } catch (e) { console.log('  open failed:', e.message); return []; }

  await sleep(3000);

  // Scroll to load more images
  await proxyGet(`/scroll?target=${tid}&y=2000`);
  await sleep(1000);

  // Extract image URLs - Google Images stores full-size URLs in various places
  const js = `(() => {
    const urls = new Set();
    // Method 1: data-src on thumbnails (these are often base64 or small)
    // Method 2: Find links to full images in the page metadata
    document.querySelectorAll('a').forEach(a => {
      const href = a.href || '';
      const m = href.match(/imgurl=([^&]+)/);
      if (m) urls.add(decodeURIComponent(m[1]));
    });
    // Method 3: Look for larger images in the page
    document.querySelectorAll('img').forEach(img => {
      const s = img.src || img.getAttribute('data-src') || '';
      if (s.startsWith('http') && !s.includes('google.com') && !s.includes('gstatic.com') && !s.includes('googleapis.com') && s.length > 30) {
        urls.add(s);
      }
    });
    // Method 4: Check for data attributes that might contain image URLs
    document.querySelectorAll('[data-tbnid]').forEach(el => {
      const img = el.querySelector('img');
      if (img) {
        const s = img.src || img.getAttribute('data-src') || '';
        if (s.startsWith('http') && !s.includes('google') && !s.includes('gstatic')) urls.add(s);
      }
    });
    return JSON.stringify([...urls].slice(0, 15));
  })()`;

  let imgUrls = [];
  try {
    const result = await proxyPost(`/eval?target=${tid}`, js);
    imgUrls = JSON.parse(result);
  } catch (e) {
    console.log('  eval parse error');
  }

  // If we didn't get URLs from links, try clicking individual images to get full URLs
  if (imgUrls.length < 3) {
    console.log('  Trying click method to get full-res URLs...');
    const clickJs = `(() => {
      const thumbs = document.querySelectorAll('[data-tbnid]');
      const results = [];
      // Just get the first 5 thumbnail containers
      for (let i = 0; i < Math.min(5, thumbs.length); i++) {
        const t = thumbs[i];
        const tbnid = t.getAttribute('data-tbnid');
        results.push(tbnid);
      }
      return JSON.stringify(results);
    })()`;

    let tbnids = [];
    try { tbnids = JSON.parse(await proxyPost(`/eval?target=${tid}`, clickJs)); } catch {}

    for (const tbnid of tbnids.slice(0, 5)) {
      // Click this thumbnail
      await proxyPost(`/click?target=${tid}`, `[data-tbnid="${tbnid}"]`);
      await sleep(1500);

      // Now look for the full-size image in the side panel
      const fullJs = `(() => {
        const imgs = document.querySelectorAll('img[src]');
        const big = [];
        for (const img of imgs) {
          const s = img.src;
          if (s.startsWith('http') && !s.includes('google') && !s.includes('gstatic') && !s.includes('googleapis') && (img.naturalWidth > 200 || img.width > 200)) {
            big.push(s);
          }
        }
        return JSON.stringify(big);
      })()`;

      try {
        const bigUrls = JSON.parse(await proxyPost(`/eval?target=${tid}`, fullJs));
        for (const u of bigUrls) {
          if (!imgUrls.includes(u)) imgUrls.push(u);
        }
      } catch {}
    }
  }

  try { await proxyGet(`/close?target=${tid}`); } catch {}
  return imgUrls;
}

async function getImagesFromPage(pageUrl) {
  let tid;
  try {
    const r = JSON.parse(await proxyGet(`/new?url=${encodeURIComponent(pageUrl)}`));
    tid = r.targetId || r.id;
  } catch (e) { return []; }

  await sleep(3000);
  await proxyGet(`/scroll?target=${tid}&y=1500`);
  await sleep(500);

  const js = `(() => {
    const urls = [];
    document.querySelectorAll('img').forEach(img => {
      const s = img.src || img.getAttribute('data-src') || img.getAttribute('data-lazy-src') || '';
      if (s.startsWith('http') && s.length > 50) {
        const w = img.naturalWidth || img.width || 0;
        const h = img.naturalHeight || img.height || 0;
        urls.push({ src: s, w, h, area: w * h });
      }
    });
    // Sort by image area (largest first)
    urls.sort((a, b) => b.area - a.area);
    return JSON.stringify(urls.slice(0, 10).map(u => u.src));
  })()`;

  let urls = [];
  try { urls = JSON.parse(await proxyPost(`/eval?target=${tid}`, js)); } catch {}
  try { await proxyGet(`/close?target=${tid}`); } catch {}
  return urls;
}

// Topic definitions with search queries and fallback page URLs
const topics = [
  { num: '01', slug: 'star_wars_maul',
    queries: ['Star Wars Maul Shadow Lord animated series poster 2026 Disney Plus'],
    pages: ['https://www.starwars.com/news/star-wars-maul-shadow-lord-first-trailer-poster-art', 'https://www.starwars.com/series/star-wars-maul-shadow-lord']
  },
  { num: '02', slug: 'the_boys_s5',
    queries: ['The Boys Season 5 final season poster 2026 Homelander Butcher'],
    pages: ['https://heroichollywood.com/the-boys-battlelines-posters-final-season/', 'https://cosmicbook.news/the-boys-final-season-posters-ccxp']
  },
  { num: '03', slug: 'invincible_s4',
    queries: ['Invincible Season 4 animated poster key art 2026 Thragg'],
    pages: ['https://bleedingcool.com/tv/invincible-season-4-key-art-poster-offers-episode-release-schedule/']
  },
  { num: '04', slug: 'daredevil_born_again',
    queries: ['Daredevil Born Again Season 2 poster 2026 MCU Disney Plus'],
    pages: ['https://thefutureoftheforce.com/2026/03/14/the-latest-daredevil-born-again-season-2-poster-unleashes-the-kingpin/', 'https://www.marvel.com/articles/tv-shows/daredevil-born-again-season-2-every-vigilante-character-posters']
  },
  { num: '05', slug: 'hades_ii',
    queries: ['Hades II game key art Melinoe Supergiant Games'],
    pages: ['https://www.creativeuncut.com/art_hades-2_a.html', 'https://www.creativeuncut.com/gallery-47/hades2-melinoe.html']
  },
  { num: '06', slug: 'diablo_iv_hatred',
    queries: ['Diablo IV Lord of Hatred expansion key art 2026 Paladin Warlock'],
    pages: ['https://diablo4.blizzard.com/en-us/lord-of-hatred']
  },
  { num: '07', slug: 'pokemon_champions',
    queries: ['Pokemon Champions game 2026 Nintendo Switch official art'],
    pages: ['https://champions.pokemon.com/en-us/']
  },
  { num: '08', slug: 'agentic_ai',
    queries: ['Agentic AI revolution 2026 concept artificial intelligence'],
    pages: ['https://machinelearningmastery.com/7-agentic-ai-trends-to-watch-in-2026/']
  },
  { num: '09', slug: 'stranger_things_85',
    queries: ['Stranger Things Tales from 85 animated Netflix poster 2026'],
    pages: ['https://www.justjared.com/2026/03/27/netflix-shares-new-trailer-photos-poster-for-stranger-things-tales-from-85/', 'https://www.netflix.com/tudum/articles/stranger-things-animated-series-news']
  },
  { num: '10', slug: 'kenny_omega',
    queries: ['Kenny Omega AEW return 2026 wrestling'],
    pages: ['https://www.allelitewrestling.com/post/aew-dynamite-preview-april-8-2026']
  }
];

async function processTopic(topic) {
  console.log(`\n=== ${topic.num} ${topic.slug} ===`);
  let downloaded = 0;
  let allUrls = [];

  // Strategy 1: Try official/news pages first for high quality images
  for (const pageUrl of topic.pages) {
    if (downloaded >= 3) break;
    console.log(`  Page: ${pageUrl.substring(0, 70)}...`);
    const urls = await getImagesFromPage(pageUrl);
    console.log(`    Found ${urls.length} images`);
    allUrls.push(...urls);

    for (const url of urls) {
      if (downloaded >= 3) break;
      const fn = `${topic.num}_${topic.slug}_${downloaded + 1}.jpg`;
      const fp = path.join(OUT, fn);
      const ok = await download(url, fp);
      if (ok) {
        downloaded++;
        console.log(`    SAVED: ${fn} (${fs.statSync(fp).size} bytes)`);
      }
    }
  }

  // Strategy 2: Google Images search if we still need more
  if (downloaded < 3) {
    for (const query of topic.queries) {
      if (downloaded >= 3) break;
      console.log(`  Google: ${query}`);
      const urls = await getImagesViaGoogleSearch(query);
      console.log(`    Found ${urls.length} image URLs`);

      for (const url of urls) {
        if (downloaded >= 3) break;
        if (allUrls.includes(url)) continue; // Skip dupes
        const fn = `${topic.num}_${topic.slug}_${downloaded + 1}.jpg`;
        const fp = path.join(OUT, fn);
        const ok = await download(url, fp);
        if (ok) {
          downloaded++;
          console.log(`    SAVED: ${fn} (${fs.statSync(fp).size} bytes)`);
        }
      }
    }
  }

  console.log(`  Result: ${downloaded}/3 images`);
  return downloaded;
}

async function main() {
  let total = 0;
  for (const topic of topics) {
    total += await processTopic(topic);
    await sleep(500); // Small delay between topics
  }

  const files = fs.readdirSync(OUT).sort();
  console.log(`\n=== COMPLETE: ${total}/30 images, ${files.length} files ===`);
  files.forEach(f => console.log(`  ${f} (${fs.statSync(path.join(OUT, f)).size}b)`));
}

main().catch(e => console.error('Fatal:', e));
