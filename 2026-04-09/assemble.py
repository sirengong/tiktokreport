#!/usr/bin/env python3
"""Assemble hub.html from section files and Vol.001 template."""
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

BASE = 'C:/Users/gongjue/tiktok-reports'

# Read Vol.001 CSS (lines 1-600)
with open(f'{BASE}/2026-04-01/hub.html', 'r', encoding='utf-8') as f:
    vol001 = f.readlines()
css_block = ''.join(vol001[:600])

# Read section files
sections = {}
for name in ['trends', 'tiktok', 'youtube', 'memes', 'ads']:
    with open(f'{BASE}/2026-04-09/_section_{name}.html', 'r', encoding='utf-8') as f:
        sections[name] = f.read()

# Build HTML parts
parts = []

# Part 1: CSS
parts.append(css_block)

# Part 2: Body start + Header + Sidebar
parts.append("""</style>
</head>
<body>

<header class="hub-header">
  <div class="header-brand">
    <span class="dot">\u25cf</span>
    <div class="name">\u6b27\u7f8e\u5185\u5bb9\u60c5\u62a5\u7ad9<small>Western Content Intel</small></div>
  </div>
  <div class="header-meta">
    <span class="header-tag">Vol.002</span>
    <span class="header-tag">\u00b7</span>
    <span class="header-tag">2026-04-09</span>
    <span class="header-badge">Live</span>
  </div>
  <div class="header-right">
    <a class="header-back" href="../index.html">\u2190 \u5f52\u6863\u9996\u9875</a>
  </div>
</header>

<div class="hub-layout">
  <nav class="hub-sidebar">
    <div class="sidebar-group">
      <div class="sidebar-group-label">Vol.002 \u00b7 2026-04-09</div>
      <button class="nav-item active" data-target="s-overview" onclick="switchSection('s-overview',this)">
        <span class="ni-icon">\ud83c\udf10</span><span class="ni-label">\u672c\u671f\u603b\u89c8</span>
      </button>
      <button class="nav-item" data-target="s-trends" onclick="switchSection('s-trends',this)">
        <span class="ni-icon">\ud83d\udd25</span><span class="ni-label">\u70ed\u641c\u5206\u6790</span><span class="ni-badge-new">NEW</span>
      </button>
      <button class="nav-item" data-target="s-tiktok" onclick="switchSection('s-tiktok',this)">
        <span class="ni-icon">\ud83c\udfb5</span><span class="ni-label">TikTok \u70ed\u95e8</span><span class="ni-badge-new">NEW</span>
      </button>
      <button class="nav-item" data-target="s-youtube" onclick="switchSection('s-youtube',this)">
        <span class="ni-icon">\u25b6\ufe0f</span><span class="ni-label">YouTube Shorts</span><span class="ni-badge-new">NEW</span>
      </button>
      <button class="nav-item" data-target="s-memes" onclick="switchSection('s-memes',this)">
        <span class="ni-icon">\ud83d\ude02</span><span class="ni-label">\u8868\u60c5\u5305 Memes</span><span class="ni-badge-new">NEW</span>
      </button>
      <button class="nav-item" data-target="s-ads" onclick="switchSection('s-ads',this)">
        <span class="ni-icon">\ud83d\udce2</span><span class="ni-label">\u5e73\u53f0\u5e7f\u544a</span><span class="ni-badge-new">NEW</span>
      </button>
    </div>
    <div class="sidebar-divider"></div>
    <div class="sidebar-group">
      <div class="sidebar-group-label">\u5f80\u671f</div>
      <a class="nav-item" href="../2026-04-01/hub.html">
        <span class="ni-icon">\ud83d\udccb</span><span class="ni-label">Vol.001<span class="sidebar-issue"> \u00b7 04-01</span></span>
      </a>
    </div>
    <div class="sidebar-spacer"></div>
    <div class="sidebar-footer">
      <p>\u6b27\u7f8e\u5185\u5bb9\u60c5\u62a5\u7ad9 \u00b7 Westradar<br>\u6e38\u620f\u7814\u53d1\u56e2\u961f\u7684\u6587\u5316\u4fe1\u53f7\u96f7\u8fbe<br>Vol.002 \u00b7 2026-04-09</p>
    </div>
  </nav>

  <main class="hub-content">
""")

# Part 3: Overview
parts.append("""    <div id="s-overview" class="section-panel active">
      <div class="sec-inner">
        <div class="sec-kicker">\ud83c\udf10 \u672c\u671f\u603b\u89c8 \u00b7 Vol.002</div>
        <div class="sec-title">\u6b27\u7f8e\u5185\u5bb9\u60c5\u62a5\u7ad9 \u00b7 2026-04-09</div>
        <div class="sec-desc">\u672c\u671f\u8986\u76d6 4 \u5927\u5185\u5bb9\u677f\u5757\uff08\u5e7f\u544a\u677f\u5757\u5df2\u6062\u590d\uff09\uff0c\u5171 <strong>50 \u6761</strong>\u5206\u6790\u6761\u76ee\u3002\u6bcf\u6761\u6309\u6e38\u620f\u7814\u53d1\u7075\u611f SOP \u62c6\u89e3\uff0c\u670d\u52a1\u4e8e\u897f\u5e7b\u5361\u724c\u6e38\u620f\u7684\u89d2\u8272\u8bbe\u8ba1\u3001\u73a9\u6cd5\u673a\u5236\u548c\u5e7f\u544a\u521b\u610f\u3002</div>
        <div class="stats-row">
          <div class="stat-pill">\ud83d\udcc5 <strong>\u6570\u636e\u5468\u671f</strong> 2026.04.02 \u2013 04.09</div>
          <div class="stat-pill">\ud83c\udf0e <strong>\u5730\u533a</strong> \u7f8e\u56fd</div>
          <div class="stat-pill">\ud83d\udcca <strong>\u677f\u5757\u6570</strong> 5</div>
          <div class="stat-pill">\ud83c\udfae <strong>\u89c6\u89d2</strong> \u6e38\u620f\u7814\u53d1 \u00b7 \u5185\u5bb9\u60c5\u62a5</div>
        </div>
        <div class="ov-nav-label">\u5feb\u901f\u5bfc\u822a \u00b7 \u5404\u677f\u5757\u5165\u53e3</div>
        <div class="ov-nav-grid">
          <div class="ov-nav-card" onclick="switchSection('s-trends', document.querySelector('[data-target=s-trends]'))">
            <span class="onc-icon">\ud83d\udd25</span><span class="onc-label">\u70ed\u641c\u5206\u6790</span><span class="onc-count">10 \u6761 \u00b7 Google Trends</span><span class="onc-arrow">\u2192</span>
          </div>
          <div class="ov-nav-card" onclick="switchSection('s-tiktok', document.querySelector('[data-target=s-tiktok]'))">
            <span class="onc-icon">\ud83c\udfb5</span><span class="onc-label">TikTok \u70ed\u95e8</span><span class="onc-count">10 \u6761 \u00b7 Explore</span><span class="onc-arrow">\u2192</span>
          </div>
          <div class="ov-nav-card" onclick="switchSection('s-youtube', document.querySelector('[data-target=s-youtube]'))">
            <span class="onc-icon">\u25b6\ufe0f</span><span class="onc-label">YouTube Shorts</span><span class="onc-count">10 \u6761 \u00b7 US Trending</span><span class="onc-arrow">\u2192</span>
          </div>
          <div class="ov-nav-card" onclick="switchSection('s-memes', document.querySelector('[data-target=s-memes]'))">
            <span class="onc-icon">\ud83d\ude02</span><span class="onc-label">\u8868\u60c5\u5305 Memes</span><span class="onc-count">10 \u6761 \u00b7 Reddit</span><span class="onc-arrow">\u2192</span>
          </div>
          <div class="ov-nav-card" onclick="switchSection('s-ads', document.querySelector('[data-target=s-ads]'))">
            <span class="onc-icon">\ud83d\udce2</span><span class="onc-label">\u5e73\u53f0\u5e7f\u544a</span><span class="onc-count">10 \u6761 \u00b7 \u5e7f\u5927\u5927</span><span class="onc-arrow">\u2192</span>
          </div>
        </div>
      </div>
    </div>

""")

# Part 4: Trends
parts.append("""    <div id="s-trends" class="section-panel">
      <div class="sec-inner">
        <div class="sec-kicker">\ud83d\udd25 US Google Trends \u00b7 \u6587\u5316\u70ed\u70b9\u60c5\u62a5</div>
        <div class="sec-title">\u7f8e\u533a\u70ed\u641c Top 10</div>
        <div class="sec-desc">\u57fa\u4e8e Google Trends \u7f8e\u56fd\u5730\u533a\u6570\u636e\uff0c\u7cbe\u9009 4 \u6708\u521d\u641c\u7d22\u91cf\u5cf0\u503c\u6700\u9ad8\u7684 10 \u5927\u8bdd\u9898\u3002\u6bcf\u6761\u6309<strong>\u6e38\u620f\u7814\u53d1\u7075\u611f SOP</strong> \u62c6\u89e3\uff0c\u4f18\u5148\u7ea7\uff1a\u73a9\u6cd5/\u6d3b\u52a8 > \u89d2\u8272\u8bbe\u8ba1 > \u5e7f\u544a\u3002</div>
        <div class="stats-row">
          <div class="stat-pill">\ud83d\udcc5 <strong>\u6570\u636e\u5468\u671f</strong> 2026.04.02 \u2013 04.09</div>
          <div class="stat-pill">\ud83c\udf0e <strong>\u5730\u533a</strong> \u7f8e\u56fd</div>
          <div class="stat-pill">\ud83d\udcca <strong>\u6765\u6e90</strong> Google Trends RSS + Web</div>
          <div class="stat-pill">\ud83c\udfae <strong>\u89c6\u89d2</strong> \u6e38\u620f\u7814\u53d1 \u00b7 \u5185\u5bb9\u60c5\u62a5</div>
        </div>
""")
parts.append(sections['trends'])
parts.append("      </div>\n    </div><!-- /s-trends -->\n\n")

# Part 5: TikTok
parts.append("""    <div id="s-tiktok" class="section-panel">
      <div class="sec-inner">
        <div class="sec-kicker">\ud83c\udfb5 TikTok Explore \u00b7 \u70ed\u95e8\u89c6\u9891\u5206\u6790</div>
        <div class="sec-title">TikTok Explore \u70ed\u95e8 Top 10</div>
        <div class="sec-desc">\u901a\u8fc7 CDP \u6d4f\u89c8\u5668\u5b9e\u65f6\u6293\u53d6 TikTok Explore \u9875\u9762\u5f53\u524d\u70ed\u95e8\u5185\u5bb9\uff0c\u6309<strong>\u6e38\u620f\u7814\u53d1\u7075\u611f SOP</strong> \u62c6\u89e3\uff0c\u4f18\u5148\u7ea7\uff1a\u89d2\u8272\u8bbe\u8ba1 > \u5e7f\u544a > \u73a9\u6cd5\u5305\u88c5\u3002</div>
        <div class="stats-row">
          <div class="stat-pill">\ud83d\udcc5 <strong>\u91c7\u96c6\u65f6\u95f4</strong> 2026-04-09</div>
          <div class="stat-pill">\ud83c\udf0e <strong>\u6765\u6e90</strong> TikTok Explore \u9875\u9762</div>
          <div class="stat-pill">\ud83c\udfae <strong>\u89c6\u89d2</strong> \u6e38\u620f\u7814\u53d1 \u00b7 \u5185\u5bb9\u60c5\u62a5</div>
        </div>
""")
parts.append(sections['tiktok'])
parts.append("      </div>\n    </div><!-- /s-tiktok -->\n\n")

# Part 6: YouTube (with inline styles)
yt_styles = """        <style>
        .yt-card { background: var(--bg3); border: 1px solid var(--border2); border-radius: 16px; overflow: hidden; margin-bottom: 20px; display: grid; grid-template-columns: 200px 1fr; align-items: stretch; transition: border-color 0.2s; }
        .yt-card:hover { border-color: var(--gray3); }
        .yt-card.top { border-color: #ff0000; }
        .yt-thumb { position: relative; width: 200px; height: 356px; background: #000; overflow: hidden; flex-shrink: 0; }
        .yt-iframe { width: 100%; height: 100%; border: 0; display: block; }
        .yt-rank-badge { position: absolute; top: 8px; left: 8px; z-index: 10; background: rgba(0,0,0,0.8); color: #fff; font-size: 14px; font-weight: 900; width: 30px; height: 30px; border-radius: 7px; display: flex; align-items: center; justify-content: center; border: 1px solid rgba(255,255,255,0.15); pointer-events: none; }
        .yt-rank-badge.yt-gold { background: var(--gold); color: #000; border-color: transparent; }
        .yt-views-chip { position: absolute; bottom: 8px; left: 8px; right: 8px; background: rgba(0,0,0,0.82); color: #fff; font-size: 11px; font-weight: 700; padding: 3px 7px; border-radius: 6px; display: flex; align-items: center; gap: 5px; pointer-events: none; }
        .yt-play-icon { color: #ff0000; font-size: 12px; }
        .yt-info { padding: 18px 22px; display: flex; flex-direction: column; gap: 12px; }
        .yt-header { display: flex; justify-content: space-between; align-items: flex-start; gap: 10px; }
        .yt-title { font-size: 15px; font-weight: 700; color: var(--white); line-height: 1.4; }
        .yt-channel { font-size: 12px; font-weight: 600; color: #ff4444; white-space: nowrap; }
        .yt-meta { display: flex; gap: 14px; background: var(--bg4); border-radius: 9px; padding: 9px 14px; flex-wrap: wrap; }
        .yt-stat { display: flex; flex-direction: column; align-items: center; gap: 2px; min-width: 52px; }
        .yt-stat .sv { font-size: 14px; font-weight: 800; color: var(--white); }
        .yt-stat .sv.hot { color: #ff4444; }
        .yt-stat .sl { font-size: 9px; color: var(--gray3); }
        .yt-tags { display: flex; flex-wrap: wrap; gap: 5px; }
        .yt-tag { font-size: 10px; font-weight: 600; padding: 2px 8px; border-radius: 20px; letter-spacing: 0.3px; }
        .yt-tag.hook { background: rgba(255,68,68,0.1); color: #ff8080; border: 1px solid rgba(255,68,68,0.2); }
        .yt-tag.fmt { background: rgba(74,158,255,0.1); color: #8ac4ff; border: 1px solid rgba(74,158,255,0.2); }
        </style>
"""
parts.append("""    <div id="s-youtube" class="section-panel">
      <div class="sec-inner">
        <div class="sec-kicker">\u25b6\ufe0f YouTube Shorts \u00b7 \u70ed\u95e8\u89c6\u9891\u5206\u6790</div>
        <div class="sec-title">\u7f8e\u533a YouTube Shorts \u70ed\u95e8 Top 10</div>
        <div class="sec-desc">\u901a\u8fc7 YouTube Data API mostPopular chart \u83b7\u53d6\u7f8e\u533a\u771f\u5b9e\u70ed\u95e8 Shorts\uff0c\u6309<strong>\u6e38\u620f\u7814\u53d1\u7075\u611f SOP</strong> \u62c6\u89e3\uff0c\u4f18\u5148\u7ea7\uff1a\u5e7f\u544a > \u73a9\u6cd5\u6f14\u51fa > \u89d2\u8272\u5c55\u793a\u3002</div>
        <div class="stats-row">
          <div class="stat-pill">\ud83d\udcc5 <strong>\u6570\u636e\u5468\u671f</strong> 2026.04.02 \u2013 04.09</div>
          <div class="stat-pill">\ud83c\udf0e <strong>\u5730\u533a</strong> \u7f8e\u56fd</div>
          <div class="stat-pill">\ud83d\udcca <strong>\u6765\u6e90</strong> YouTube Data API v3 \u00b7 mostPopular</div>
          <div class="stat-pill">\ud83c\udfae <strong>\u89c6\u89d2</strong> \u6e38\u620f\u7814\u53d1 \u00b7 \u5185\u5bb9\u60c5\u62a5</div>
        </div>
""")
parts.append(yt_styles)
parts.append(sections['youtube'])
parts.append("      </div>\n    </div><!-- /s-youtube -->\n\n")

# Part 7: Memes
parts.append("""    <div id="s-memes" class="section-panel">
      <div class="sec-inner">
        <div class="sec-kicker">\ud83d\ude02 Meme \u683c\u5f0f\u60c5\u62a5 \u00b7 \u6e38\u620f\u7814\u53d1\u7075\u611f</div>
        <div class="sec-title">\u7f8e\u533a Meme \u70ed\u699c Top 10</div>
        <div class="sec-desc">\u8ffd\u8e2a 2026 \u5e74 4 \u6708\u521d\u7f8e\u533a\u6700\u5177\u4f20\u64ad\u529b\u7684 Meme \u683c\u5f0f\u4e0e\u8bdd\u9898\u3002\u6309 4 \u4e2a\u7ef4\u5ea6\u62c6\u89e3\uff1a<strong>\u89c6\u89c9\u6a21\u677f</strong>\u3001<strong>\u60c5\u7eea\u7ed3\u6784</strong>\u3001<strong>\u89d2\u8272\u539f\u578b</strong>\u3001<strong>Remix \u673a\u5236</strong>\u3002</div>
        <div class="stats-row">
          <div class="stat-pill">\ud83d\udcc5 <strong>\u6570\u636e\u5468\u671f</strong> 2026.04.02 \u2013 04.09</div>
          <div class="stat-pill">\ud83c\udf0e <strong>\u6765\u6e90</strong> Reddit (r/memes, r/dankmemes, r/gaming, r/MemeEconomy)</div>
          <div class="stat-pill">\ud83c\udfae <strong>\u89c6\u89d2</strong> \u6e38\u620f\u7814\u53d1 \u00b7 \u793e\u533a\u8fd0\u8425 \u00b7 UGC \u8bbe\u8ba1</div>
        </div>
""")
parts.append(sections['memes'])
parts.append("      </div>\n    </div><!-- /s-memes -->\n\n")

# Part 7.5: Ads
parts.append("""    <div id="s-ads" class="section-panel">
      <div class="sec-inner">
        <div class="sec-kicker">\ud83d\udce2 \u5e73\u53f0\u70ed\u95e8\u5e7f\u544a \u00b7 \u6e38\u620f\u5e7f\u544a\u60c5\u62a5</div>
        <div class="sec-title">\u5e7f\u5927\u5927 Top 10 \u6e38\u620f\u5e7f\u544a</div>
        <div class="sec-desc">\u901a\u8fc7\u5e7f\u5927\u5927 (guangdada.net) \u91c7\u96c6\u5f53\u65e5\u5c55\u793a\u5e7f\u544a\u70ed\u699c Top 10\uff0c\u8986\u76d6 TikTok / Google / AppLovin / UnityAds / Mintegral / IronSource \u7b49\u5e73\u53f0\u3002\u6bcf\u6761\u6309<strong>\u6e38\u620f\u7814\u53d1\u7075\u611f SOP</strong> \u62c6\u89e3\uff0c\u4f18\u5148\u7ea7\uff1a\u5e7f\u544a\u94a9\u5b50 > \u73a9\u6cd5\u7559\u5b58 > \u89d2\u8272\u3002</div>
        <div class="stats-row">
          <div class="stat-pill">\ud83d\udcc5 <strong>\u91c7\u96c6\u65e5\u671f</strong> 2026-04-09</div>
          <div class="stat-pill">\ud83c\udf0e <strong>\u6765\u6e90</strong> \u5e7f\u5927\u5927 guangdada.net</div>
          <div class="stat-pill">\ud83d\udcca <strong>\u7b5b\u9009</strong> \u89d2\u8272\u626e\u6f14/\u7b56\u7565/\u76ca\u667a/\u52a8\u4f5c/\u6a21\u62df/\u5192\u9669/\u6d88\u9664</div>
          <div class="stat-pill">\ud83c\udfae <strong>\u89c6\u89d2</strong> \u6e38\u620f\u7814\u53d1 \u00b7 \u5e7f\u544a\u60c5\u62a5</div>
        </div>
""")
parts.append(sections['ads'])
parts.append("      </div>\n    </div><!-- /s-ads -->\n\n")

# Part 8: Close + Modals + JS
parts.append("""  </main>
</div>

<div id="lightbox" onclick="closeLightbox()">
  <span id="lightbox-close" onclick="closeLightbox()">&times;</span>
  <img id="lightbox-img" src="" alt="">
</div>

<div id="vmbox" onclick="closeVbox()">
  <span id="vmbox-close" onclick="closeVbox()">&times;</span>
  <div id="vmbox-inner" onclick="event.stopPropagation()">
    <iframe id="vmbox-iframe" src="" allowfullscreen></iframe>
    <video id="vmbox-video" src="" controls></video>
  </div>
</div>

<script>
function openLightbox(img){var lb=document.getElementById('lightbox');document.getElementById('lightbox-img').src=img.src;document.getElementById('lightbox-img').alt=img.alt;lb.classList.add('open');document.body.style.overflow='hidden';}
function closeLightbox(){document.getElementById('lightbox').classList.remove('open');document.body.style.overflow='';}
function openVbox(src,type){var m=document.getElementById('vmbox'),i=document.getElementById('vmbox-iframe'),v=document.getElementById('vmbox-video');if(type==='video'){i.style.display='none';i.src='';v.style.display='block';v.src=src;v.play();}else{v.style.display='none';v.pause();v.src='';i.style.display='block';i.src=src;}m.classList.add('open');document.body.style.overflow='hidden';}
function closeVbox(){var m=document.getElementById('vmbox'),i=document.getElementById('vmbox-iframe'),v=document.getElementById('vmbox-video');m.classList.remove('open');i.src='';v.pause();v.src='';v.style.display='none';i.style.display='block';document.body.style.overflow='';}
document.addEventListener('keydown',function(e){if(e.key==='Escape'){closeLightbox();closeVbox();}});
function switchSection(t,b){document.querySelectorAll('.section-panel').forEach(function(p){p.classList.remove('active');});document.querySelectorAll('.nav-item').forEach(function(n){n.classList.remove('active');});document.getElementById(t).classList.add('active');if(b)b.classList.add('active');closeVbox();closeLightbox();window.scrollTo(0,0);var v=JSON.parse(localStorage.getItem('hub_visited')||'{}');v[t]=true;localStorage.setItem('hub_visited',JSON.stringify(v));if(b){var bg=b.querySelector('.ni-badge-new');if(bg)bg.remove();}}
(function(){var v=JSON.parse(localStorage.getItem('hub_visited')||'{}');document.querySelectorAll('.nav-item[data-target]').forEach(function(i){var t=i.getAttribute('data-target');if(v[t]){var bg=i.querySelector('.ni-badge-new');if(bg)bg.remove();}});})();
</script>
</body>
</html>
""")

# Write
html = ''.join(parts)
out = f'{BASE}/2026-04-09/hub.html'
with open(out, 'w', encoding='utf-8', errors='replace') as f:
    f.write(html)

print(f'hub.html written: {html.count(chr(10))+1} lines')
print(f'Path: {out}')
