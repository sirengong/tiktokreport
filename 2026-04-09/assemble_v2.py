#!/usr/bin/env python3
"""Assemble hub.html from template + section files. V2: uses template file for emoji safety."""
import sys, io
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

BASE = Path('C:/Users/gongjue/tiktok-reports')
DIR = BASE / '2026-04-09'

# Read Vol.001 CSS (first 600 lines)
with open(BASE / '2026-04-01/hub.html', 'r', encoding='utf-8') as f:
    css_block = ''.join(f.readlines()[:600])

# Read template shell (with proper emoji)
with open(DIR / '_template_shell.html', 'r', encoding='utf-8') as f:
    template = f.read()

# Read section content files
sections = {}
for name in ['trends', 'tiktok', 'youtube', 'memes', 'ads']:
    p = DIR / f'_section_{name}.html'
    sections[name] = p.read_text(encoding='utf-8') if p.exists() else ''

# Read overview synthesis if exists
synth_path = DIR / '_section_overview_synthesis.html'
overview_synthesis = synth_path.read_text(encoding='utf-8') if synth_path.exists() else ''

# Extract template parts
import re

# Get sidebar nav buttons
sidebar_match = re.search(r'<!-- SIDEBAR NAV -->(.*?)<!-- OVERVIEW SECTION -->', template, re.DOTALL)
sidebar_nav = sidebar_match.group(1).strip() if sidebar_match else ''

# Get overview section
overview_match = re.search(r'<!-- OVERVIEW SECTION -->(.*?)<!-- TRENDS WRAPPER -->', template, re.DOTALL)
overview_html = overview_match.group(1).strip() if overview_match else ''
overview_html = overview_html.replace('{{OVERVIEW_SYNTHESIS}}', overview_synthesis)

# Get section wrappers
def get_wrapper(tag_start, tag_end):
    m = re.search(f'<!-- {tag_start} -->(.*?)<!-- {tag_end} -->', template, re.DOTALL)
    return m.group(1).strip() if m else ''

trends_wrap = get_wrapper('TRENDS WRAPPER', 'TIKTOK WRAPPER')
tiktok_wrap = get_wrapper('TIKTOK WRAPPER', 'YOUTUBE WRAPPER')
youtube_wrap = get_wrapper('YOUTUBE WRAPPER', 'MEMES WRAPPER')
memes_wrap = get_wrapper('MEMES WRAPPER', 'ADS WRAPPER')
ads_wrap = template[template.find('<!-- ADS WRAPPER -->'):].replace('<!-- ADS WRAPPER -->', '').strip()

# Inject content
trends_wrap = trends_wrap.replace('{{TRENDS_CONTENT}}', sections['trends'])
tiktok_wrap = tiktok_wrap.replace('{{TIKTOK_CONTENT}}', sections['tiktok'])
youtube_wrap = youtube_wrap.replace('{{YOUTUBE_CONTENT}}', sections['youtube'])
memes_wrap = memes_wrap.replace('{{MEMES_CONTENT}}', sections['memes'])
ads_wrap = ads_wrap.replace('{{ADS_CONTENT}}', sections['ads'])

# Build final HTML
parts = [
    css_block,
    '</style>\n</head>\n<body>\n',
    # Header
    '<header class="hub-header">\n'
    '  <div class="header-brand">\n'
    '    <span class="dot">●</span>\n'
    '    <div class="name">欧美内容情报站<small>Western Content Intel</small></div>\n'
    '  </div>\n'
    '  <div class="header-meta">\n'
    '    <span class="header-tag">Vol.002</span>\n'
    '    <span class="header-tag">·</span>\n'
    '    <span class="header-tag">2026-04-09</span>\n'
    '    <span class="header-badge">Live</span>\n'
    '  </div>\n'
    '  <div class="header-right">\n'
    '    <a class="header-back" href="../index.html">← 归档首页</a>\n'
    '  </div>\n'
    '</header>\n\n',
    # Layout
    '<div class="hub-layout">\n',
    # Sidebar
    '  <nav class="hub-sidebar">\n'
    '    <div class="sidebar-group">\n'
    '      <div class="sidebar-group-label">Vol.002 · 2026-04-09</div>\n',
    sidebar_nav,
    '    </div>\n'
    '    <div class="sidebar-divider"></div>\n'
    '    <div class="sidebar-group">\n'
    '      <div class="sidebar-group-label">全部期刊</div>\n'
    '      <a class="nav-item" href="../2026-04-09/hub.html" style="background:rgba(254,44,85,0.08);">\n'
    '        <span class="ni-icon">📌</span><span class="ni-label">Vol.002<span class="sidebar-issue"> · 04-09 当前</span></span>\n'
    '      </a>\n'
    '      <a class="nav-item" href="../2026-04-01/hub.html">\n'
    '        <span class="ni-icon">📋</span><span class="ni-label">Vol.001<span class="sidebar-issue"> · 04-01</span></span>\n'
    '      </a>\n'
    '    </div>\n'
    '    <div class="sidebar-spacer"></div>\n'
    '    <div class="sidebar-footer">\n'
    '      <p>欧美内容情报站 · Westradar<br>游戏研发团队的文化信号雷达<br>Vol.002 · 2026-04-09</p>\n'
    '    </div>\n'
    '  </nav>\n\n',
    # Content
    '  <main class="hub-content">\n\n',
    '    ', overview_html, '\n\n',
    '    ', trends_wrap, '\n\n',
    '    ', tiktok_wrap, '\n\n',
    '    ', youtube_wrap, '\n\n',
    '    ', memes_wrap, '\n\n',
    '    ', ads_wrap, '\n\n',
    '  </main>\n</div>\n\n',
    # Modals
    '<div id="lightbox" onclick="closeLightbox()">\n'
    '  <span id="lightbox-close" onclick="closeLightbox()">&times;</span>\n'
    '  <img id="lightbox-img" src="" alt="">\n'
    '</div>\n\n'
    '<div id="vmbox" onclick="closeVbox()">\n'
    '  <span id="vmbox-close" onclick="closeVbox()">&times;</span>\n'
    '  <div id="vmbox-inner" onclick="event.stopPropagation()">\n'
    '    <iframe id="vmbox-iframe" src="" allowfullscreen></iframe>\n'
    '    <video id="vmbox-video" src="" controls></video>\n'
    '  </div>\n'
    '</div>\n\n',
    # JS
    '<script>\n'
    'function openLightbox(img){var lb=document.getElementById("lightbox");document.getElementById("lightbox-img").src=img.src;document.getElementById("lightbox-img").alt=img.alt;lb.classList.add("open");document.body.style.overflow="hidden";}\n'
    'function closeLightbox(){document.getElementById("lightbox").classList.remove("open");document.body.style.overflow="";}\n'
    'function openVbox(src,type){var m=document.getElementById("vmbox"),i=document.getElementById("vmbox-iframe"),v=document.getElementById("vmbox-video");if(type==="video"){i.style.display="none";i.src="";v.style.display="block";v.src=src;v.play();}else{v.style.display="none";v.pause();v.src="";i.style.display="block";i.src=src;}m.classList.add("open");document.body.style.overflow="hidden";}\n'
    'function closeVbox(){var m=document.getElementById("vmbox"),i=document.getElementById("vmbox-iframe"),v=document.getElementById("vmbox-video");m.classList.remove("open");i.src="";v.pause();v.src="";v.style.display="none";i.style.display="block";document.body.style.overflow="";}\n'
    'document.addEventListener("keydown",function(e){if(e.key==="Escape"){closeLightbox();closeVbox();}});\n'
    'function switchSection(t,b){document.querySelectorAll(".section-panel").forEach(function(p){p.classList.remove("active");});document.querySelectorAll(".nav-item").forEach(function(n){n.classList.remove("active");});document.getElementById(t).classList.add("active");if(b)b.classList.add("active");closeVbox();closeLightbox();window.scrollTo(0,0);var v=JSON.parse(localStorage.getItem("hub_visited")||"{}");v[t]=true;localStorage.setItem("hub_visited",JSON.stringify(v));if(b){var bg=b.querySelector(".ni-badge-new");if(bg)bg.remove();}}\n'
    '(function(){var v=JSON.parse(localStorage.getItem("hub_visited")||"{}");document.querySelectorAll(".nav-item[data-target]").forEach(function(i){var t=i.getAttribute("data-target");if(v[t]){var bg=i.querySelector(".ni-badge-new");if(bg)bg.remove();}});})();\n'
    '</script>\n'
    '</body>\n</html>\n'
]

html = ''.join(parts)
out = DIR / 'hub.html'
with open(out, 'w', encoding='utf-8') as f:
    f.write(html)

lines = html.count('\n') + 1
emoji_ok = '📅' in html and '🔥' in html and '🎵' in html
broken = html.count('??')
print(f'hub.html: {lines} lines, emoji={"OK" if emoji_ok else "BROKEN"}, broken_chars={broken}')
