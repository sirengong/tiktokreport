import http from 'http';
import https from 'https';
import fs from 'fs';
import path from 'path';

const CDP_BASE = 'http://localhost:3456';
const OUT_DIR = 'C:/Users/gongjue/tiktok-reports/2026-04-09/trend_images';

const topics = [
  { id: '01', slug: 'star_wars_maul', query: 'Star Wars Maul Shadow Lord animated series' },
  { id: '02', slug: 'the_boys_s5', query: 'The Boys Season 5 TV show' },
  { id: '03', slug: 'invincible_s4', query: 'Invincible Season 4 animated series' },
  { id: '04', slug: 'daredevil_born_again', query: 'Daredevil Born Again Season 2' },
  { id: '05', slug: 'hades_ii', query: 'Hades II game' },
  { id: '06', slug: 'diablo_iv_hatred', query: 'Diablo IV Vessel of Hatred expansion' },
  { id: '07', slug: 'pokemon_champions', query: 'Pokemon Champions game 2026' },
  { id: '08', slug: 'agentic_ai', query: 'Agentic AI technology' },
  { id: '09', slug: 'stranger_things_85', query: 'Stranger Things Tales from 1985' },
  { id: '10', slug: 'kenny_omega', query: 'Kenny Omega AEW wrestling return' },
];

function cdpGet(endpoint) {
  return new Promise((resolve, reject) => {
    http.get(`${CDP_BASE}${endpoint}`, res => {
      let data = '';
      res.on('data', c => data += c);
      res.on('end', () => {
        try { resolve(JSON.parse(data)); }
        catch { resolve(data); }
      });
    }).on('error', reject);
  });
}

function cdpPost(endpoint, body) {
  return new Promise((resolve, reject) => {
    const url = new URL(`${CDP_BASE}${endpoint}`);
    const req = http.request({
      hostname: url.hostname,
      port: url.port,
      path: url.pathname + url.search,
      method: 'POST',
      headers: { 'Content-Type': 'text/plain' }
    }, res => {
      let data = '';
      res.on('data', c => data += c);
      res.on('end', () => {
        try { resolve(JSON.parse(data)); }
        catch { resolve(data); }
      });
    });
    req.on('error', reject);
    req.write(body);
    req.end();
  });
}

function downloadFile(url, filepath) {
  return new Promise((resolve, reject) => {
    const protocol = url.startsWith('https') ? https : http;
    const request = (reqUrl, redirectCount = 0) => {
      if (redirectCount > 5) return reject(new Error('Too many redirects'));
      protocol.get(reqUrl, { headers: { 'User-Agent': 'Mozilla/5.0' } }, res => {
        if (res.statusCode >= 300 && res.statusCode < 400 && res.headers.location) {
          return request(res.headers.location, redirectCount + 1);
        }
        if (res.statusCode !== 200) {
          return reject(new Error(`HTTP ${res.statusCode}`));
        }
        const stream = fs.createWriteStream(filepath);
        res.pipe(stream);
        stream.on('finish', () => {
          stream.close();
          const stats = fs.statSync(filepath);
          resolve(stats.size);
        });
      }).on('error', reject);
    };
    request(url);
  });
}

function sleep(ms) {
  return new Promise(r => setTimeout(r, ms));
}

async function extractImagesFromGoogleImages(targetId) {
  // Try to extract image URLs from Google Images thumbnails
  const js = `
    JSON.stringify((() => {
      const urls = [];
      // Method 1: img tags with src starting with http (actual loaded images)
      const imgs = document.querySelectorAll('img');
      for (const img of imgs) {
        const src = img.src || '';
        const w = img.naturalWidth || img.width || 0;
        const h = img.naturalHeight || img.height || 0;
        if (src.startsWith('http') && !src.includes('google') && !src.includes('gstatic') && w > 50 && h > 50) {
          urls.push(src);
        }
      }
      // Method 2: data-src attributes
      const dataSrcImgs = document.querySelectorAll('img[data-src]');
      for (const img of dataSrcImgs) {
        const src = img.getAttribute('data-src');
        if (src && src.startsWith('http') && !src.includes('google') && !src.includes('gstatic')) {
          urls.push(src);
        }
      }
      // Method 3: Google encrypted thumbnails (data:image or encrypted_tbn)
      const gImgs = document.querySelectorAll('img[src*="encrypted-tbn"]');
      for (const img of gImgs) {
        urls.push(img.src);
      }
      return [...new Set(urls)];
    })())
  `;
  const result = await cdpPost(`/eval?target=${targetId}`, js);
  if (result.value) {
    try { return JSON.parse(result.value); }
    catch { return []; }
  }
  return [];
}

async function extractImagesFromGoogleImagesFull(targetId) {
  // Click on first few image results to get full-size URLs
  const js = `
    JSON.stringify((() => {
      const urls = [];
      // Get all image thumbnails from Google Images results
      const thumbs = document.querySelectorAll('img[src*="encrypted-tbn"]');
      for (const t of thumbs) {
        urls.push(t.src);
      }
      // Also check for data URIs in img tags (Google sometimes embeds base64)
      const allImgs = document.querySelectorAll('#search img, #islrg img, .islrc img, [data-ri] img');
      for (const img of allImgs) {
        if (img.src && img.src.startsWith('data:image')) {
          urls.push(img.src);
        }
        if (img.src && img.src.startsWith('http') && !img.src.includes('google.com/') && img.naturalWidth > 80) {
          urls.push(img.src);
        }
      }
      return [...new Set(urls)].slice(0, 20);
    })())
  `;
  const result = await cdpPost(`/eval?target=${targetId}`, js);
  if (result.value) {
    try { return JSON.parse(result.value); }
    catch { return []; }
  }
  return [];
}

async function downloadImagesForTopic(topic) {
  console.log(`\n--- Topic ${topic.id}: ${topic.query} ---`);

  const query = encodeURIComponent(topic.query);
  const searchUrl = `https://www.google.com/search?q=${query}&tbm=isch`;

  // Open new tab with Google Images
  const tab = await cdpGet(`/new?url=${encodeURIComponent(searchUrl)}`);
  const targetId = tab.targetId;
  console.log(`  Tab opened: ${targetId}`);

  await sleep(3000); // Wait for images to load

  // Scroll down to trigger lazy loading
  await cdpGet(`/scroll?target=${targetId}&y=1000`);
  await sleep(1500);

  // Extract image URLs
  let urls = await extractImagesFromGoogleImagesFull(targetId);
  console.log(`  Found ${urls.length} image URLs`);

  if (urls.length < 3) {
    // Try scrolling more
    await cdpGet(`/scroll?target=${targetId}&y=2000`);
    await sleep(2000);
    urls = await extractImagesFromGoogleImagesFull(targetId);
    console.log(`  After scroll: found ${urls.length} image URLs`);
  }

  // Filter out data URIs and tiny images, prefer encrypted-tbn URLs (Google thumbnails)
  const httpUrls = urls.filter(u => u.startsWith('http'));
  const dataUrls = urls.filter(u => u.startsWith('data:image'));

  console.log(`  HTTP URLs: ${httpUrls.length}, Data URLs: ${dataUrls.length}`);

  // Try downloading HTTP URLs first
  let downloaded = 0;
  const usedUrls = new Set();

  for (const url of httpUrls) {
    if (downloaded >= 3) break;
    if (usedUrls.has(url)) continue;

    const filename = `${topic.id}_${topic.slug}_${downloaded + 1}.jpg`;
    const filepath = path.join(OUT_DIR, filename);

    try {
      const size = await downloadFile(url, filepath);
      if (size >= 5000) { // At least 5KB
        console.log(`  Downloaded ${filename} (${size} bytes)`);
        usedUrls.add(url);
        downloaded++;
      } else {
        console.log(`  Too small (${size} bytes), skipping: ${url.substring(0, 80)}`);
        fs.unlinkSync(filepath);
      }
    } catch (e) {
      console.log(`  Failed to download: ${e.message} - ${url.substring(0, 80)}`);
      try { fs.unlinkSync(filepath); } catch {}
    }
  }

  // If not enough images from HTTP URLs, save data URIs
  if (downloaded < 3) {
    for (const dataUrl of dataUrls) {
      if (downloaded >= 3) break;
      if (usedUrls.has(dataUrl)) continue;

      const filename = `${topic.id}_${topic.slug}_${downloaded + 1}.jpg`;
      const filepath = path.join(OUT_DIR, filename);

      try {
        // Extract base64 data
        const matches = dataUrl.match(/^data:image\/(\w+);base64,(.+)$/);
        if (matches) {
          const buffer = Buffer.from(matches[2], 'base64');
          if (buffer.length >= 5000) {
            fs.writeFileSync(filepath, buffer);
            console.log(`  Saved data URI ${filename} (${buffer.length} bytes)`);
            usedUrls.add(dataUrl);
            downloaded++;
          }
        }
      } catch (e) {
        console.log(`  Failed data URI: ${e.message}`);
      }
    }
  }

  // If still not enough, try a different approach: use /screenshot on individual results
  if (downloaded < 3) {
    console.log(`  Only ${downloaded} images downloaded. Trying to click results for full-size images...`);

    // Try extracting from page scripts (Google stores full res URLs in JS)
    const scriptJs = `
      JSON.stringify((() => {
        const urls = [];
        const scripts = document.querySelectorAll('script');
        for (const s of scripts) {
          const text = s.textContent;
          // Look for image URLs in script content
          const matches = text.match(/https?:\\/\\/[^"'\\s]+\\.(?:jpg|jpeg|png|webp)/gi);
          if (matches) {
            for (const m of matches) {
              if (!m.includes('google') && !m.includes('gstatic') && !m.includes('favicon')) {
                urls.push(m);
              }
            }
          }
        }
        return [...new Set(urls)].slice(0, 20);
      })())
    `;
    const scriptResult = await cdpPost(`/eval?target=${targetId}`, scriptJs);
    let scriptUrls = [];
    if (scriptResult.value) {
      try { scriptUrls = JSON.parse(scriptResult.value); }
      catch {}
    }
    console.log(`  Found ${scriptUrls.length} URLs from scripts`);

    for (const url of scriptUrls) {
      if (downloaded >= 3) break;
      if (usedUrls.has(url)) continue;

      const filename = `${topic.id}_${topic.slug}_${downloaded + 1}.jpg`;
      const filepath = path.join(OUT_DIR, filename);

      try {
        const size = await downloadFile(url, filepath);
        if (size >= 5000) {
          console.log(`  Downloaded from script ${filename} (${size} bytes)`);
          usedUrls.add(url);
          downloaded++;
        } else {
          fs.unlinkSync(filepath);
        }
      } catch (e) {
        try { fs.unlinkSync(filepath); } catch {}
      }
    }
  }

  // Close the tab
  await cdpGet(`/close?target=${targetId}`);

  console.log(`  Topic ${topic.id} complete: ${downloaded}/3 images`);
  return downloaded;
}

async function main() {
  console.log('Starting image downloads...');

  const results = {};
  for (const topic of topics) {
    const count = await downloadImagesForTopic(topic);
    results[topic.id] = count;
    await sleep(1000); // Be polite between topics
  }

  console.log('\n=== RESULTS ===');
  for (const [id, count] of Object.entries(results)) {
    console.log(`  ${id}: ${count}/3 images`);
  }

  // List all downloaded files
  const files = fs.readdirSync(OUT_DIR).filter(f => f.endsWith('.jpg') || f.endsWith('.png'));
  console.log(`\nTotal files: ${files.length}`);
  for (const f of files) {
    const stats = fs.statSync(path.join(OUT_DIR, f));
    console.log(`  ${f}: ${stats.size} bytes`);
  }
}

main().catch(console.error);
