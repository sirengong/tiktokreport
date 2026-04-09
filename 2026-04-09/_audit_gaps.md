# Vol.002 vs Vol.001 Gap Audit
**Generated:** 2026-04-08  
**Reference:** `2026-04-01/hub.html`  
**Target:** `2026-04-09/hub.html`  
**Index:** `tiktok-reports/index.html`

---

## SUMMARY VERDICT

Vol.002 is structurally complete but has **7 major gaps** and **several minor issues**:

| Area | Status |
|------|--------|
| 总览 Overview | MISSING: 3 synthesis cards + signal matrix |
| 热搜 Trends | MISSING: all 10 real images (placeholder divs only) |
| TikTok | MISSING: engagement metrics, method-box, data table, trend analysis |
| YouTube | MISSING: data summary table at bottom |
| Memes | BETTER than Vol.001 (has conclusion-box that Vol.001 lacks) |
| Ads | MISSING: method-box explaining data source |
| index.html | NOT UPDATED (still shows Vol.002 as "即将发布") |
| share-card.html | NOT CREATED (Vol.001 has it, Vol.002 does not) |
| Emoji rendering | All stat-pill icons show as `??` instead of real emoji |

---

## 1. 总览 (Overview) Section

**Vol.001 lines 682–897 | Vol.002 lines 658–688**

Vol.002 overview contains ONLY the quick-nav grid (5 clickable cards to each section). It is missing:

### 1a. Cross-Platform Synthesis Cards (MISSING entirely)
Vol.001 has a 3-column `.ov-synthesis` grid (lines 697–806) with:
- **角色设计方向 card** (`ov-syn-char`) — blue (`#25f4ee`) themed, shows top signal, 3 platform-tagged `ov-signal` items, a conclusion paragraph
- **玩法/留存方向 card** (`ov-syn-play`) — gold (`#ffd700`) themed, same structure
- **广告创意方向 card** (`ov-syn-ad`) — red (`#fe2c55`) themed, same structure

Each card has:
- Header with icon, title, priority badge (e.g. "TikTok 优先")
- A bold big-text signal summary (e.g. "陪伴型受难 NPC × 反差搭档公式")
- 3 × `ov-signal` items, each with platform badge pills (color-coded: Memes=#ff4500, 广告=#e76e22, TikTok=#222/border, 热搜=#4285f4, YouTube=#ff0000) + star rating + signal text
- A `ov-syn-conclusion` paragraph

Vol.002 has NONE of this. The section jumps directly to the nav grid.

### 1b. Signal Strength Matrix Table (MISSING entirely)
Vol.001 has `.ov-matrix-wrap` (lines 809–859):
- Label: "平台 × 维度 · 信号强度矩阵"
- A `<table class="ov-matrix">` with columns: 平台 / 🎭角色设计 / ⚔️玩法/留存 / 🎬广告创意 / 本期最强关键词
- 5 rows: 热搜 / TikTok / YouTube / Memes / 广告
- Color-coded strength bars: `sig-5` (red), `sig-4` (cyan), `sig-3` (green), `sig-2` (gray)

Vol.002 has NONE of this.

### 1c. Stats Row — Wrong Content
Vol.001 stats-row (line 687–692): 数据周期 / 覆盖平台 / 内容条目 / 分析视角  
Vol.002 stats-row (lines 663–668): 数据周期 / 地区 / 板块数 / 视角 — uses generic data rather than the synthesis-specific stats. Minor but inconsistent.

### 1d. Section Heading Style
Vol.001 has `<div class="tk-section-title">本期最强跨平台信号 <span class="num">多来源印证 = 更高优先级</span></div>` before the synthesis grid (line 695). Vol.002 has no such header — the nav grid has only a label.

---

## 2. 热搜 Trends Section

**Vol.001 lines 902–1502 | Vol.002 lines 690–1316**

### 2a. Images — All 10 Topics Are Placeholders (CRITICAL)
Vol.001 has **3 real images per topic** (30 images total) in `trend_images/` folder, using `.img-trio` with actual `<img>` tags. Example (lines 939–942):
```html
<img src="trend_images/01_zootopia2_1.jpg" ...>
<img src="trend_images/01_zootopia2_2.jpg" ...>
<img src="trend_images/01_zootopia2_3.jpg" ...>
```

Vol.002 has placeholder divs for ALL 10 topics (lines 728, 787, 846, 905, 964, 1023, 1084, 1141, 1200, 1259):
```html
<div style="width:190px;height:230px;background:var(--bg4);...">图片待补充</div>
```
No `trend_images/` folder exists in the `2026-04-09/` directory. All 10 topics need 3 real images each = **30 missing images**.

### 2b. Analysis Depth Difference (Structural)
Vol.001 trend cards use a **compact** 3-column game-analysis with 2 bullet points per column.  
Vol.002 trend cards use a **more detailed** 4-bullet-point-per-column format. This is an improvement, not a gap — but the image absence negates the visual value.

---

## 3. TikTok Section

**Vol.001 lines 1503–2124 | Vol.002 lines 1317–1848**

### 3a. Stats Row — Engagement Totals (MISSING)
Vol.001 stats-row (lines 1509–1513) shows aggregate engagement across all 10 videos:
- ❤️ **82.3M** 总点赞
- 💬 **807K** 总评论  
- ⭐ **7.1M** 总收藏
- 🔗 **18.1M** 总分享

Vol.002 stats-row (lines 1323–1326) shows only: 采集时间 / 来源 / 视角 — no aggregate numbers.

### 3b. Method-Box (MISSING)
Vol.001 has a `.method-box` (lines 1515–1521) explaining the ranking methodology:
> "排名方法论 · 综合传播力评分 — 公式：综合分 = 点赞 + 评论×3 + 收藏×2 + 分享×2"

Vol.002 has NO method-box in the TikTok section. The section goes directly from stats to conclusion-box.

### 3c. Per-Video Engagement Metrics (MISSING on most cards)
Vol.001 shows a `.metrics` row on every video card with 4 metrics: 点赞 / 评论 / 收藏 / 分享 — and each video shows a "综合分 XM" score badge.

Vol.002 videos only show "XM 播放" (view count) in the score badge and have NO `.metrics` row. The raw engagement data (likes/comments/bookmarks/shares) is completely absent from all 10 video cards.

### 3d. Data Summary Table (MISSING)
Vol.001 has a full `.data-table` at the bottom of TikTok (lines 2089–2104):
- Title: "数据总览 · 综合分排行榜"
- Columns: # / 账号 / 内容 / 点赞 / 评论 / 收藏 / 分享 / 综合分
- All 10 videos listed with raw numbers + 🏆 champion markers

Vol.002 has NO data summary table. The section ends after the 10th video card.

### 3e. Trend Analysis Section (MISSING)
Vol.001 has a `.trend-grid` (lines 2107–2121) after the data table with 2 cards:
- "📊 内容类型分布" — bar chart showing content type breakdown (4 categories with percentages)
- "🏆 各指标冠军" — bar chart showing champion for 点赞/评论/收藏/分享

Vol.002 has NONE of this trend analysis section.

---

## 4. YouTube Shorts Section

**Vol.001 lines 2130–2839 | Vol.002 lines 1850–2570**

### 4a. Data Summary Table (MISSING)
Vol.001 has a `.data-table` at the bottom of YouTube section (lines 2821–2836):
- Title: "数据总览 · 播放量排行"
- Columns: # / 频道 / 标题 / 播放量 / 点赞 / 发布日期 / 内容类型
- All 10 videos listed

Vol.002 ends after the 10th video card (yt-card for Unicorn Ball, around line 2568) with NO data summary table.

### 4b. Stats Row Difference
Vol.001 stats (lines 2136–2140): 数据周期 / 地区 / 来源 / 视角  
Vol.002 stats (lines 1856–1860): 数据周期 / 地区 / 来源 / 视角 — same structure, acceptable.

### 4c. Inline `<style>` Block (Minor)
Vol.002 has an extra `<style>` block inline inside the section panel (lines 1862–1884) defining `.yt-card`, `.yt-thumb`, etc. Vol.001 has these styles in the main CSS block. Functionally equivalent, but messy — those styles should move to the `<head>` CSS section.

---

## 5. Memes Section

**Vol.001 lines 2844–3445 | Vol.002 lines 2572–3196**

### 5a. Conclusion-Box — Vol.002 is BETTER
Vol.001 has: method-box only (no conclusion-box)  
Vol.002 has: method-box + conclusion-box with 3-column game-dev analysis  
This is an improvement. No gap here.

### 5b. Stats Row — One Extra Pill Missing
Vol.001 stats-row (lines 2850–2854) has 4 pills: 数据周期 / 来源 / 视角 / **展示数量 (10条精选)**  
Vol.002 stats-row (lines 2578–2581) has 3 pills: 数据周期 / 来源 / 视角  
Missing: the "展示数量" pill.

### 5c. Source Breadth Difference
Vol.001 lists sources: Reddit / Know Your Meme / TikTok / X  
Vol.002 lists sources: Reddit (r/memes, r/dankmemes, r/gaming, r/MemeEconomy) only  
Not a visual gap but worth noting for accuracy.

---

## 6. Ads Section

**Vol.001 lines 3450–3851 | Vol.002 lines 3198–3935**

### 6a. Method-Box (MISSING)
Vol.001 has a `.method-box` (lines 3462–3468) explaining the metrics:
> "关于数据来源 — 人气值 = 曝光量 × 互动率 × 投放持续性综合评分（46万 = 极爆量级）；展示估值 = 平台抽样估算的实际触达量级；热度 = 当前投放活跃程度（满分 100）"

Vol.002 has NO method-box in the Ads section. The section goes: sec-kicker → sec-title → sec-desc → stats-row → inline `<style>` → conclusion-box → ads-grid. The method-box is missing between stats-row and conclusion-box.

### 6b. Stats Row Completeness
Vol.001 stats (lines 3455–3460): 数据日期 / 筛选条件 (Top1%·7天·最新创意) / 平台覆盖 / 展示数量  
Vol.002 stats (lines 3203–3208): 采集日期 / 来源 / 筛选 / 视角  
Missing: "筛选条件 Top1%·7天" specificity, "平台覆盖" list, "展示数量" count.

### 6c. Inline `<style>` Block (Minor)
Vol.002 has an inline `<style>` block (lines 3210–3214) inside the section panel overriding `.ads-grid .ad-card`. Functionally acceptable but should be in `<head>`.

### 6d. Per-Ad Metrics — Mostly Dashes
Many Vol.002 ad cards show `—` for 人气值 and 展示估值 (e.g. Angry Birds 2 card lines 3883–3888). This appears intentional (data not available for some), but is less complete than Vol.001 which had real numbers.

---

## 7. index.html — NOT UPDATED

**File:** `C:\Users\gongjue\tiktok-reports\index.html`

### 7a. Vol.002 Card Is Placeholder (NEEDS UPDATE)
Line 297–303: The "下一期占位" card shows:
```html
<div class="report-card coming-card">
  Vol.002 · 即将发布
  每周更新，敬请期待
</div>
```
This needs to become a real `<a class="report-card featured">` linking to `./2026-04-09/hub.html`, with proper card-header, card-body, card-sections pills, card-metrics, and card-footer — exactly matching the Vol.001 card structure (lines 260–294).

### 7b. hero-stat Counter (NEEDS UPDATE)
Line 222: `<span id="total-editions">1</span>` — dynamically counted by JS from `.report-card:not(.coming-card)`, but since the Vol.002 card is currently a `.coming-card`, this counter will still show `1` after update until the JS logic is correct.

### 7c. Latest Edition Nav Link (NEEDS UPDATE)
Line 202: `<a class="nav-cta" href="#reports">查看最新一期 →</a>` — should link directly to `./2026-04-09/hub.html`

### 7d. Footer Latest Link (NEEDS UPDATE)
Line 368: `<a href="./2026-04-01/hub.html">最新一期 ↗</a>` — should update to `./2026-04-09/hub.html`

### 7e. Vol.001 Card Edition Badge (NEEDS DEMOTE)
Line 263: `<div class="card-edition"><span class="dot"></span> Latest · Vol.001</div>` — once Vol.002 is added, Vol.001 should lose the "Latest" label and the animated `.dot` pulse, becoming a standard past edition card.

---

## 8. share-card.html — NOT CREATED

Vol.001 directory contains: `share-card.html` (a standalone 1080px-wide static HTML designed for social media screenshot sharing)  
Vol.002 directory: NO `share-card.html`

Vol.001's `share-card.html` is a self-contained file with:
- 1080px fixed-width layout
- Header with brand + Vol.001 date badge
- Red banner section
- Content summary cards

A corresponding `share-card.html` for Vol.002 should be created in `2026-04-09/` if the workflow requires it.

---

## 9. Emoji Rendering — All Sections

Throughout Vol.002's `hub.html`, stat-pills and section kickers use `??` instead of actual emoji characters. Examples:
- Line 660: `?? 本期总览 · Vol.002` (should be an emoji)
- Line 664: `?? 数据周期`
- Line 692: `?? US Google Trends`
- Line 696–699: All 4 stat-pills use `??`
- Line 1319: `?? TikTok Explore`
- Lines 1323–1325: stat-pills use `??`
- Lines 1856–1859: YouTube stat-pills use `??`
- Lines 2574: `?? Meme 格式情报`
- Lines 2578–2581: Memes stat-pills use `??`
- Line 3200: `?? 平台热门广告`
- Lines 3203–3208: Ads stat-pills use `??`

**Root cause:** The emoji characters were likely corrupted or stripped during file generation. All `??` should be replaced with proper emoji.

Correct emoji for reference (from Vol.001):
- 总览: 🌐
- 热搜 kicker: 🔥
- 热搜 stats: 📅 / 🌎 / 📊 / 🎮
- TikTok kicker: 🎵
- TikTok stats: ❤️ / 💬 / ⭐ / 🔗 (and 📅 / 🌎 / 📊 / 🎮 for context pills)
- YouTube kicker: ▶️ (present in Vol.002 — correct)
- Memes kicker: 😂
- Memes stats: 📅 / 🌎 / 🎮
- Ads kicker: 📢
- Ads stats: 📅 / 🏆 / 🌐 / 📢

---

## 10. Other Files in Vol.002 Directory

Vol.002 has 5 `_section_*.html` draft files that do NOT exist in Vol.001:
- `_section_tiktok.html`
- `_section_memes.html`
- `_section_youtube.html`
- `_section_trends.html`
- `_section_ads.html`

These appear to be intermediate/draft files used in generation. They are not linked from anywhere and are not part of the published product. They can be cleaned up or kept as build artifacts.

Vol.001 has a `trends.html` file that Vol.002 does not. Unknown what `trends.html` in Vol.001 contains — it may be a legacy standalone trends page that was replaced by the hub structure.

---

## Prioritized Fix Checklist

### P0 — Breaks User Experience
- [ ] Fix all `??` emoji rendering across all stat-pills and kickers in `hub.html`
- [ ] Update `index.html`: convert placeholder card to real Vol.002 card with link to `2026-04-09/hub.html`
- [ ] Add trend images to `2026-04-09/trend_images/` (3 per topic × 10 topics = 30 images)

### P1 — Major Missing Features (parity with Vol.001)
- [ ] **总览**: Add 3-column synthesis cards (`ov-synthesis` grid) with per-signal platform badge pills
- [ ] **总览**: Add signal strength matrix table (`ov-matrix`)
- [ ] **总览**: Add `tk-section-title` header "本期最强跨平台信号" above synthesis grid
- [ ] **TikTok**: Add aggregate stats to stats-row (总点赞/总评论/总收藏/总分享)
- [ ] **TikTok**: Add method-box explaining ranking formula (综合分 = 点赞 + 评论×3 + 收藏×2 + 分享×2)
- [ ] **TikTok**: Add `.metrics` row to each video card (点赞/评论/收藏/分享 breakdown)
- [ ] **TikTok**: Change score badge from "XM 播放" to "综合分 XM" format
- [ ] **TikTok**: Add data summary table at bottom (all 10 videos, 8 columns)
- [ ] **TikTok**: Add trend analysis section (内容类型分布 + 各指标冠军 bar charts)
- [ ] **YouTube**: Add data summary table at bottom (all 10 videos, 7 columns)
- [ ] **Ads**: Add method-box explaining 人气值/展示估值/热度 metrics

### P2 — Minor Polish
- [ ] **index.html**: Demote Vol.001 card — remove "Latest" from edition badge, stop dot animation
- [ ] **index.html**: Update nav-cta and footer link to point to Vol.002
- [ ] **总览**: Update stats-row content to match synthesis-specific metrics
- [ ] **总览**: Add `tk-section-title` header before nav grid
- [ ] **Memes**: Add "展示数量 10条" stat-pill to stats-row
- [ ] **Ads**: Expand stats-row to include Top1%/7天 filter specifics + platform coverage count
- [ ] Move inline `<style>` blocks (YouTube yt-card styles, Ads ad-card override) to `<head>` CSS

### P3 — New Files
- [ ] Create `2026-04-09/share-card.html` following Vol.001 template
- [ ] (Optional) Clean up `_section_*.html` draft files from `2026-04-09/` directory
