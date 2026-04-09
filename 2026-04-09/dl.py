"""Download trend topic images via CDP proxy."""
import json, os, time, urllib.request, urllib.parse

OUT = r'C:\Users\gongjue\tiktok-reports\2026-04-09\trend_images'
os.makedirs(OUT, exist_ok=True)
PROXY = 'http://localhost:3456'

def proxy_get(path):
    with urllib.request.urlopen(f'{PROXY}{path}', timeout=30) as r:
        return r.read().decode()

def proxy_post(path, body):
    req = urllib.request.Request(f'{PROXY}{path}', data=body.encode(), method='POST')
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read().decode()

def download_img(url, filepath):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        with urllib.request.urlopen(req, timeout=20) as r:
            data = r.read()
            if len(data) > 3000:
                with open(filepath, 'wb') as f:
                    f.write(data)
                return True
    except Exception:
        pass
    return False

def get_images_from_page(page_url):
    try:
        resp = json.loads(proxy_get(f'/new?url={urllib.parse.quote(page_url, safe="")}'))
        tid = resp.get('targetId') or resp.get('id')
    except Exception as e:
        print(f'    open failed: {e}')
        return []
    if not tid:
        return []
    time.sleep(3)
    try:
        proxy_get(f'/scroll?target={tid}&y=1500')
    except Exception:
        pass
    time.sleep(0.5)
    js = '''(() => {
        const urls = [];
        document.querySelectorAll('img').forEach(img => {
            const s = img.src || img.getAttribute('data-src') || img.getAttribute('data-lazy-src') || '';
            if (s.startsWith('http') && s.length > 50) {
                const w = img.naturalWidth || img.width || 0;
                const h = img.naturalHeight || img.height || 0;
                urls.push({ src: s, w, h, area: w * h });
            }
        });
        urls.sort((a, b) => b.area - a.area);
        return JSON.stringify(urls.slice(0, 10).map(u => u.src));
    })()'''
    urls = []
    try:
        result = proxy_post(f'/eval?target={tid}', js)
        urls = json.loads(result)
    except Exception:
        pass
    try:
        proxy_get(f'/close?target={tid}')
    except Exception:
        pass
    return urls

def search_google_images(query):
    search_url = f'https://www.google.com/search?q={urllib.parse.quote(query)}&tbm=isch&tbs=isz:l'
    try:
        resp = json.loads(proxy_get(f'/new?url={urllib.parse.quote(search_url, safe="")}'))
        tid = resp.get('targetId') or resp.get('id')
    except Exception as e:
        print(f'    search open failed: {e}')
        return []
    if not tid:
        return []
    time.sleep(3)
    try:
        proxy_get(f'/scroll?target={tid}&y=2000')
    except Exception:
        pass
    time.sleep(1)
    # Extract image URLs
    js = '''(() => {
        const urls = new Set();
        document.querySelectorAll('a').forEach(a => {
            const href = a.href || '';
            const m = href.match(/imgurl=([^&]+)/);
            if (m) urls.add(decodeURIComponent(m[1]));
        });
        document.querySelectorAll('img').forEach(img => {
            const s = img.src || img.getAttribute('data-src') || '';
            if (s.startsWith('http') && !s.includes('google.com') && !s.includes('gstatic.com') && !s.includes('googleapis.com') && s.length > 30) {
                urls.add(s);
            }
        });
        return JSON.stringify([...urls].slice(0, 15));
    })()'''
    urls = []
    try:
        result = proxy_post(f'/eval?target={tid}', js)
        urls = json.loads(result)
    except Exception:
        pass
    # Try clicking thumbnails for full-res
    if len(urls) < 3:
        click_js = '''(() => {
            const thumbs = document.querySelectorAll('[data-tbnid]');
            return JSON.stringify([...thumbs].slice(0, 5).map(t => t.getAttribute('data-tbnid')));
        })()'''
        tbnids = []
        try:
            tbnids = json.loads(proxy_post(f'/eval?target={tid}', click_js))
        except Exception:
            pass
        for tbnid in tbnids[:5]:
            try:
                proxy_post(f'/click?target={tid}', f'[data-tbnid="{tbnid}"]')
            except Exception:
                pass
            time.sleep(1.5)
            full_js = '''(() => {
                const imgs = [];
                document.querySelectorAll('img[src]').forEach(img => {
                    const s = img.src;
                    if (s.startsWith('http') && !s.includes('google') && !s.includes('gstatic') && !s.includes('googleapis') && (img.naturalWidth > 200 || img.width > 200)) {
                        imgs.push(s);
                    }
                });
                return JSON.stringify(imgs);
            })()'''
            try:
                big_urls = json.loads(proxy_post(f'/eval?target={tid}', full_js))
                for u in big_urls:
                    if u not in urls:
                        urls.append(u)
            except Exception:
                pass
    try:
        proxy_get(f'/close?target={tid}')
    except Exception:
        pass
    return urls

topics = [
    {'num': '01', 'slug': 'star_wars_maul',
     'queries': ['Star Wars Maul Shadow Lord animated series poster 2026'],
     'pages': ['https://www.starwars.com/news/star-wars-maul-shadow-lord-first-trailer-poster-art',
               'https://www.starwars.com/series/star-wars-maul-shadow-lord']},
    {'num': '02', 'slug': 'the_boys_s5',
     'queries': ['The Boys Season 5 final season poster 2026 Homelander'],
     'pages': ['https://heroichollywood.com/the-boys-battlelines-posters-final-season/',
               'https://cosmicbook.news/the-boys-final-season-posters-ccxp']},
    {'num': '03', 'slug': 'invincible_s4',
     'queries': ['Invincible Season 4 animated poster key art 2026'],
     'pages': ['https://bleedingcool.com/tv/invincible-season-4-key-art-poster-offers-episode-release-schedule/']},
    {'num': '04', 'slug': 'daredevil_born_again',
     'queries': ['Daredevil Born Again Season 2 poster 2026 MCU'],
     'pages': ['https://thefutureoftheforce.com/2026/03/14/the-latest-daredevil-born-again-season-2-poster-unleashes-the-kingpin/',
               'https://www.marvel.com/articles/tv-shows/daredevil-born-again-season-2-every-vigilante-character-posters']},
    {'num': '05', 'slug': 'hades_ii',
     'queries': ['Hades II game key art Melinoe Supergiant'],
     'pages': ['https://www.creativeuncut.com/art_hades-2_a.html',
               'https://www.creativeuncut.com/gallery-47/hades2-melinoe.html']},
    {'num': '06', 'slug': 'diablo_iv_hatred',
     'queries': ['Diablo IV Lord of Hatred expansion key art 2026'],
     'pages': ['https://diablo4.blizzard.com/en-us/lord-of-hatred']},
    {'num': '07', 'slug': 'pokemon_champions',
     'queries': ['Pokemon Champions game 2026 Nintendo Switch art'],
     'pages': ['https://champions.pokemon.com/en-us/']},
    {'num': '08', 'slug': 'agentic_ai',
     'queries': ['Agentic AI revolution 2026 concept illustration'],
     'pages': ['https://machinelearningmastery.com/7-agentic-ai-trends-to-watch-in-2026/']},
    {'num': '09', 'slug': 'stranger_things_85',
     'queries': ['Stranger Things Tales from 85 animated Netflix poster 2026'],
     'pages': ['https://www.justjared.com/2026/03/27/netflix-shares-new-trailer-photos-poster-for-stranger-things-tales-from-85/']},
    {'num': '10', 'slug': 'kenny_omega',
     'queries': ['Kenny Omega AEW return 2026 wrestling'],
     'pages': ['https://www.allelitewrestling.com/post/aew-dynamite-preview-april-8-2026']},
]

total = 0
for topic in topics:
    print(f"\n=== {topic['num']} {topic['slug']} ===")
    downloaded = 0
    all_urls = []

    # Try pages first
    for page_url in topic['pages']:
        if downloaded >= 3:
            break
        print(f"  Page: {page_url[:70]}...")
        urls = get_images_from_page(page_url)
        print(f"    Found {len(urls)} images")
        all_urls.extend(urls)
        for url in urls:
            if downloaded >= 3:
                break
            fn = f"{topic['num']}_{topic['slug']}_{downloaded + 1}.jpg"
            fp = os.path.join(OUT, fn)
            ok = download_img(url, fp)
            if ok:
                downloaded += 1
                sz = os.path.getsize(fp)
                print(f"    SAVED: {fn} ({sz} bytes)")

    # Google Images fallback
    if downloaded < 3:
        for query in topic['queries']:
            if downloaded >= 3:
                break
            print(f"  Google: {query}")
            urls = search_google_images(query)
            print(f"    Found {len(urls)} image URLs")
            for url in urls:
                if downloaded >= 3:
                    break
                if url in all_urls:
                    continue
                fn = f"{topic['num']}_{topic['slug']}_{downloaded + 1}.jpg"
                fp = os.path.join(OUT, fn)
                ok = download_img(url, fp)
                if ok:
                    downloaded += 1
                    sz = os.path.getsize(fp)
                    print(f"    SAVED: {fn} ({sz} bytes)")

    print(f"  Result: {downloaded}/3")
    total += downloaded
    time.sleep(0.5)

# Final report
files = sorted(os.listdir(OUT))
print(f"\n=== COMPLETE: {total}/30 images, {len(files)} files ===")
for f in files:
    sz = os.path.getsize(os.path.join(OUT, f))
    print(f"  {f} ({sz}b)")
