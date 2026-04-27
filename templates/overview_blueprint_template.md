# Overview 板块 · 写作蓝图模板（Template v2 · Vol.004 起）

> **版本说明**：v2 是 Vol.004 重构后的形式。2026-04-23 老板反馈 v1 (9 卡 ov-syn-card) 信息密度过高、缺判断、像信息汇总，重构为 **3 个跨源观察卡 + 图文 + 跳转**，定位从「指令式输出」改为「参考式启发」。
> 适用于 Vol.005+ 所有 overview（s-overview）板块生成。
> v1 (9 卡) 结构已废弃，CSS 残留在 hub.html 中保留作向后兼容，**不要再生成 v1 形式**。

---

## ⚠️ 工作流约定（防 subagent 误判 · 必读）

### 关于"3 个观察"的选取
- 严格按事实：从 5 板块蓝图中挑出 **跨源印证最密集** 的 3 个题目（必为 ★★★ 三来源）
- 三个观察必须**分别覆盖角色 / 玩法 / 广告三个维度**（不要 3 个都是同维度）
- 如果某期某维度找不到 ★★★ 三来源信号 → 退而求其次取 ★★ 双来源最强项 + 在 v2-judg-tier 标注「★★ 双来源印证」

### 关于文案语气（v2 核心红线 · 全板块同步执行）

> **同步范围**：本节约束**不仅适用于 Overview 板块，还适用于 Trends/TikTok/YouTube/Memes/Ads 5 个数据板块**。Vol.004 实战教训：5 数据板块 subagent 写卡片时也容易掉回指令式语言（Vol.004 hub.html 5 板块清洗后净改 95 处）。每个板块 subagent 写 fragment 前必须读本节。

- 平台定位：**情报雷达**（information broker），不是策略指令交付
- 全部文案使用 **参考式 / 启发式** 语气，**严禁指令式**

#### ✅ 允许的措辞（鼓励复用）
- 价值判断：「值得关注」「值得纳入选题池」「较有代表性」「较突出」「较有效」
- 行动建议：「可以参考」「不妨联想到」「是个不错的起点」「可作为...的候选」「可衍生出」「可借鉴」
- 程度描述：「契合度高」「通用节奏」「成熟参考模板」「长期高互动公式」
- 比较表达：「优于」「相比...更具」

#### ❌ 禁用的措辞（命中即改）

**硬指令类**：必须 / 立刻 / 严禁（反向参考除外）/ 硬规则 / 现成模板 / 碾压 / 最强判断 / 不能 / DRD 必须 / 务必 / 一定要 / 王炸 / 完胜 / 必胜 / 终极

**绝对化类**：直接套用 / 直接抄 / 直接落地 / 直接挪用 / 直接复用 / 永久流量公式 / 最高优先级 / 最优起点 / 最优 / 最强 / 顶级 / 至高 / 史上 / 永远

**verb 替换清单**（subagent 在 v1 经常写错的，需主动改写）：
| 原 verb | 改写为 |
|---------|--------|
| 碾压 | 优于 / 突出 |
| 最强 X | 较有代表性的 X / 较突出的 X |
| 印证 / 验证 X | 呈现 / 反映 X |
| 直接套用 / 直接抄 / 直接复用 | 可参考 / 可联想到 |
| 顶级 | 突出 / 代表性 |
| 永久流量公式 | 长期高互动公式 |
| 反向碾压 | 反向反杀 |

#### ❌ 数字建议禁用（2026-04-30 新增）

**不要给具体产出量建议**——出多少图/方案/视频不是 westradar 说了算的。

| 错误模式 | 正确改写 |
|---------|---------|
| 一周可出 50+ 草图 | 较值得纳入 AI 角色快验候选池的方向 |
| 一周可出 30+ 方案 | 可借助 AI 出图工具尝试不同组合 |
| 一周可出 20+ 变体 | 可衍生黑化/反派/对偶等多种变体方向 |
| 验证最具市场穿透力的版本 | 观察哪类版本更具传播潜力 |

通用模式：`一周/每周/每天 + 可出/可跑/可验证 + N+ + 量词` 都是禁止的，应改为"可借助 X 工具尝试不同 Y"。

#### A/B/C 标签命名（2026-04-30 起）

| 等级 | 标签文字 | css class | 含义 |
|------|---------|----------|------|
| A | **A 契合度高** | `ga-label-a` | 与游戏题材关联性强（不再用"A 直接可用"） |
| B | **B 结构借鉴** | `ga-label-b` | 内容本身不能直接搬，骨架/公式可参考 |
| C | **C 观察储备** | `ga-label-c` | 暂时弱关联，留作长期观察 |

#### Section 内部命名

- "本周策划行动" → 改为 "**💡 可联想的方向**"
- "反信号 / 严禁" → 改为 "**⚠ 反向参考**"

### 关于卡 id 命名（跳转功能依赖）
- 每张数据卡（5 板块各 10 张）必须有 id：
  - TikTok video-card → `id="tt-1"` ~ `id="tt-10"`
  - YouTube yt-card → `id="yt-1"` ~ `id="yt-10"`
  - Memes meme-card → `id="meme-1"` ~ `id="meme-10"`
  - Trends trend-topic-card → `id="trend-1"` ~ `id="trend-10"`
  - Ads ad-card → `id="ad-1"` ~ `id="ad-10"`
- 编号严格按 rank 顺序（与各板块数据总览表 rank 一致）
- 各板块写作 subagent 必须负责给本板块 10 张卡加 id（已写入对应模板说明）

---

### 🕊️ 留白机制（Vol.005+ 起 · 全板块同步执行）

> **核心原则**：当某条数据**与某维度（角色 / 玩法 / 广告）关联较弱**时，**允许该栏诚实留白**，不要硬编借鉴方向。
> 老板/同事反馈触发该机制：原三栏强制分析导致 meta 类、政治类、合规类内容被硬编（如 TikTok #3 BGM hunt meta 被硬编成"影视/角色高燃混剪"）。
> Vol.004 实战：50 张卡中 14 张应用留白（28%，72% 仍保留实质分析），不影响内容密度。

#### 何时启用留白？

| 触发场景 | 例子 | 全留白还是部分留白 |
|---------|------|-----------------|
| 政治议题 | Trump-Iran 停火 / Trump 选举 / 国际地缘冲突 | **全留白**（三栏都不输出） |
| 政要肖像 + 国家政策 | Tuvalu Minister 气候发言 / 美国就业政策 meme | **全留白** |
| 合规风险品类 | 博彩（Zynga Poker / Casino）/ 加密货币 / 烟酒 | **全留白** |
| 文化/宗教敏感 | 古兰经经文 / 宗教仪式 | **部分留白**（角色玩法可保留情绪结构，广告维度留白） |
| meta 共鸣 / 平台自指 | "When you decide to play the full song" | **部分留白**（角色维度留白，玩法/广告可保留） |
| 评分≤2 的纯休闲玩法 | Nut Sort / 拼图类无角色信号 | **部分留白**（角色单栏） |
| 强行扯不出干货 | 体育赛事日常报道 / 文化节事件 | **部分留白** 或 **全留白** 视实际 |

#### 留白卡 vs 保留卡的判断顺序

1. 先看本条数据的核心价值在哪个维度（角色 / 玩法 / 广告）
2. 该维度有具体可借鉴的方向 → 保留
3. 找不到具体方向，只能靠"硬扯角色原型 / 套用一个游戏类比" → 该维度留白
4. **三个维度都找不到** = 全留白卡 = 强制 `ga-label-c`「C 观察储备」

#### CSS Class（与 hub.html 同步）

3 列板块（trends / tiktok / youtube / ads）：
```html
<!-- 留白栏 -->
<div class="ga-col ga-col-empty">
  <div class="ga-col-header">🎭 角色设计</div>
  <div class="ga-empty-note">本条 X 维度关联较弱（一句解释 ≤25 字）</div>
</div>

<!-- 评分行留白项 -->
<span class="ga-score ga-score-empty">角色 —</span>
```

4 列板块（memes ma4 结构）：
```html
<div class="ma4-col-empty">
  <div class="ma4-col-header">📐 视觉模板</div>
  <div class="ma4-empty-note">说明文字</div>
</div>
```

#### 必备 CSS（hub.html `<style>` 末尾，已沉淀）
```css
.ga-col-empty .ga-col-header { opacity: 0.92; }
.ga-empty-note { color: #aaa; font-size: 11px; line-height: 1.6; padding: 6px 0 0; font-style: italic; }
.ga-score-empty { opacity: 0.88; color: var(--gray2); }
.ga-score-empty b { color: var(--gray2); font-weight: 400; }
.ma4-cols > div.ma4-col-empty .ma4-col-header { opacity: 0.92; }
.ma4-cols > div.ma4-col-empty .ma4-empty-note { color: #aaa; font-size: 11px; line-height: 1.6; padding: 6px 0 0; font-style: italic; }
```

#### 留白文案风格

- **诚实**：直接说"本条 X 维度关联较弱"，不回避
- **简短**：≤25 字一句话，再补一个"为什么"
- **柔和**：不用"严禁/禁止"，用"不建议/不输出/仅作"
- **保留警告功能**：政治/合规类要带 ⚠️，明确"不建议直接复用"

参考已落地的 14 张卡（Vol.004）：
- "本条是 meta 共鸣类内容，与角色设计维度无明显关联"
- "本条为国际政治议题，不适合直接转化为角色设计"
- "⚠️ 涉及具体国家民生议题，视觉模板不建议直接挪用"
- "博彩品类合规风险高，不输出玩法借鉴方向"

#### 评分行处理

- 留白栏对应的评分项用 `<span class="ga-score ga-score-empty">X —</span>`
- **不要用 0/5 或 1/5**（暗示低分），用 `—` 表示该维度无评分
- 全留白卡的所有 4 项评分都用 `—`
- 部分留白卡只有留白栏对应的评分项用 `—`

#### 全留白卡 = 强制 C 观察储备

- 全留白卡的 `ga-label` **必须**改为 `ga-label-c`，文字 `C 观察储备`
- 部分留白卡（单栏空）维持原评级（A/B/C），评级不应被一栏拖累

#### 数据总览表评级同步

- 各板块数据总览表（如 Memes 表第 7 列）的评级要和卡片端 `ga-label` 同步
- 全留白卡 → 表中评级颜色 `#888`（灰）+ 字母 `C`
- subagent 改 `ga-label` 时**必须同时检查并更新数据总览表对应行**

#### conclusion-box 引用留白卡的措辞规则

留白卡若被 conclusion-box 引用，**必须用反向措辞**，不要再当借鉴模板讨论：

- ✅ 允许措辞：「已三栏全留白」「不输出借鉴方向」「仅作情绪信号观察」「⚠️ 行业现象记录」「玩家集体焦虑情绪信号」
- ❌ 禁止措辞：「借鉴模板」「可参考」「值得套用」（哪怕加 ⚠️ 前缀也不行）

参考 Vol.004 hub.html 的 3 个 conclusion 重写示例（Memes 社媒/UGC 栏 / Trends 广告栏 / Ads 广告栏）。

#### 留白率监控

- 健康区间：**留白覆盖率 < 30%**
- Vol.004 实测 28%（健康但偏高）
- 留白率 > 30% 表示采集层面引入了过多无关内容，需考虑前置过滤（见 PROJECT.md "下期待办"）

---

## 0. CSS Class 完整审计（必须 100% 复用 · 唯一真相源 = 上期 hub.html）

> 写作 subagent **第一步**：Read 上期 hub.html overview 区间，输出此清单作为审计痕迹。
> v2 引入了 v2-* 前缀的全新 class，需要在 hub.html `<style>` 中保留。

### 0.1 板块顶层（保留 v1 通用）
- `section-panel` `sec-inner` `sec-kicker` `sec-title` `sec-desc`
- `stats-row` `stat-pill`
- `tk-section-title` `num`

### 0.2 v2 判断卡（核心新结构）
- `v2-judgments`（3 卡容器，flex column gap 18px）
- `v2-judg`（单卡根，配修饰类）
- `v2-judg-char` / `v2-judg-play` / `v2-judg-ad`（修饰类，**顺序固定**）
- `v2-judg-head`（卡头：圆形序号 + 类目 + tier 徽章）
- `v2-judg-num`（圆形序号 1/2/3）
- `v2-judg-meta`
- `v2-judg-cat`（类目文字，含「灵感」字样）
- `v2-judg-tier`（★ 三来源印证徽章，每卡颜色不同）
- `v2-judg-body`
- `v2-judg-claim`（观察主张，含 `<em>` 高亮关键短语）

### 0.3 v2 图片三连
- `v2-judg-imgs`（grid 3 列 gap 10px）
- `v2-judg-img-card`（单图卡 150px 高，含 onclick="jumpTo(...)"）
- `v2-judg-img-overlay`（底部渐变蒙版）
- `v2-judg-img-pill`（左上来源徽章）
- `v2-judg-img-cap`（说明文字）

### 0.4 v2 证据区
- `v2-judg-evidence`（证据容器，背景 var(--bg3)，左边框 3px）
- `v2-judg-ev-label`（顶部 "📌 跨源证据" 小标）
- `v2-judg-ev-row`（单条证据行：pill + 文字）
- `v2-judg-ev-pill`（左侧来源 pill 56px 等宽）
- `v2-judg-ev-trend` / `v2-judg-ev-tt` / `v2-judg-ev-yt` / `v2-judg-ev-meme` / `v2-judg-ev-ad`（5 色固定）
- `v2-judg-ev-num`（高亮数字）

### 0.5 v2 行动建议 + 反向参考
- `v2-judg-action`（红色渐变背景，含 💡 icon）
- `v2-judg-act-icon` `v2-judg-act-body`
- `v2-judg-act-label`（"可联想的方向"）
- `v2-judg-act-text`
- `v2-judg-warn`（黄色边框，仅判断 #2 玩法卡可能用，反向参考用）

### 0.6 v2 跳转链接 + 末尾说明
- `v2-jump`（关键词包裹 span，蓝色虚线下划线，hover 变红色实线）
- `v2-aux-note`（末尾灰色虚线说明卡）

### 0.7 信号矩阵（保留 v1）
- `ov-matrix-wrap` `ov-matrix-label` `ov-matrix` `plat-name`
- `sig-1` ~ `sig-5`（5 级，**必须使用 `<td><span class="sig-N">…</span></td>`** 写法）

### 0.8 快捷导航（保留 v1）
- `ov-nav-label` `ov-nav-grid` `ov-nav-card`
- `onc-icon` `onc-label` `onc-count` `onc-arrow`

### 0.9 必备 JS 函数
- `switchSection(sectionId, btn)`（已存在）
- `jumpTo(sectionId, anchorId)`（v2 新增 · 切板块 + scrollIntoView + 1.8s 红框高亮）

---

## 1. DOM 嵌套伪代码（v2 关键结构）

```
section-panel#s-overview.active
└── sec-inner
    ├── sec-kicker                         「🌐 跨平台综合分析 · VOL.XXX」
    ├── sec-title                           「本期情报总览」
    ├── sec-desc                            一段约 50-80 字
    ├── stats-row > stat-pill × 4
    ├── tk-section-title (mb 14px)
    │   ├── span                            「本期最值得关注的 3 个跨源观察」
    │   └── span.num                        「三来源印证 · 重点参考」
    ├── v2-judgments
    │   └── v2-judg.{char|play|ad} × 3 (顺序固定)
    │       ├── v2-judg-head
    │       │   ├── v2-judg-num             1 / 2 / 3
    │       │   ├── v2-judg-meta > v2-judg-cat   「🎭 角色设计灵感 · XX 优先」/「⚔️ 活动/玩法灵感」/「📢 广告制作灵感」
    │       │   └── v2-judg-tier            ★★★ 三来源印证（颜色随卡变）
    │       └── v2-judg-body
    │           ├── v2-judg-claim           1-2 句观察主张（含 <em> 高亮 2-3 个关键短语）
    │           ├── v2-judg-imgs
    │           │   └── v2-judg-img-card × 3  (img/video + overlay + onclick=jumpTo)
    │           ├── v2-judg-evidence
    │           │   ├── v2-judg-ev-label    「📌 跨源证据」
    │           │   └── v2-judg-ev-row × 3  (pill + 文本，关键词包 v2-jump)
    │           ├── v2-judg-action
    │           │   ├── v2-judg-act-icon    💡
    │           │   └── v2-judg-act-body
    │           │       ├── v2-judg-act-label  「可联想的方向」
    │           │       └── v2-judg-act-text   2-3 句参考式启发
    │           └── v2-judg-warn (可选)     ⚠ 反向参考: …（仅在该卡有反信号时才加）
    ├── v2-aux-note                         末尾灰色说明卡（说明 9 项完整信号已散落在板块中）
    ├── ov-matrix-wrap                      信号矩阵（保留 v1）
    ├── ov-nav-label                        「前往各板块」
    └── ov-nav-grid > ov-nav-card × 5
```

---

## 2. 板块顶层（section_meta）

| 字段 | 示例值 | 是否变动 | 写作约束 |
|------|---|---|---|
| `panel_id` | `s-overview` | ❌ 固定 | div id 必须为 `s-overview`，且首屏带 `active` |
| `sec_kicker` | `🌐 跨平台综合分析 · VOL.004` | ⚠️ 期号每期换 | 格式：`🌐 跨平台综合分析 · VOL.XXX`（vol 全大写、含点号） |
| `sec_title` | `本期情报总览` | ❌ 固定 | 直接照抄 |
| `sec_desc` | 50-80 字 | ✏️ 每期重写 | 描述本期主线（如「AI 角色验证闭环」），结尾不要再写「输出最高优先级行动方向」（v2 改参考语气） |

---

## 3. stats_row 4 个 stat-pill（保留 v1）

| pill | 内容 | 备注 |
|------|------|------|
| 📅 数据周期 | `2026.04.16 – 04.23` | 起止日期需更新 |
| 🌎 覆盖平台 | `热搜 / TikTok / YouTube / Memes / 广告` | 5 平台 |
| 📊 内容条目 | `50 条精选` | 5 板块 × 10 条 |
| 🎮 分析视角 | `角色 / 玩法 / 广告三维度` | 不变 |

---

## 4. v2 区段标题

```html
<div class="tk-section-title" style="margin-bottom:14px;">
  <span>本期最值得关注的 3 个跨源观察</span>
  <span class="num" style="color:var(--gray3);">三来源印证 · 重点参考</span>
</div>
```

---

## 5. v2-judg 三个判断卡（核心 · 每卡字段表）

每个判断卡按下表填字段。**顺序：char → play → ad**（不可调换）。

### 卡 1 · v2-judg-char（角色设计灵感）

| 字段 | 取值规则 |
|------|---------|
| `v2-judg-num` | 数字 `1` |
| `v2-judg-cat` | `🎭 角色设计灵感 · XX 优先`（XX 视主源，常见 Trends/YouTube） |
| `v2-judg-tier` | `★★★ 三来源印证`（默认红色样式，无需 inline style） |
| `v2-judg-claim` | 1-2 句观察。**必须**：① 含跨源动词（如「同步爆发」「跨平台呼应」） ② 用 `<em>` 高亮 1-2 个关键短语 ③ 结尾用参考式（如「值得关注的角色组合方向」） |
| `v2-judg-imgs` | 3 张图（来自 trend_images / yt_images / tiktok_images / meme_images / ads_videos_gdd）。每张含 onclick="jumpTo('s-XX','XX-N')"，左上 pill 标 `🔥 热搜 #N` / `▶️ YouTube #N` / `🎵 TikTok #N` / `😂 Memes #N` / `📢 广告 #N`，底部 1 行说明 |
| `v2-judg-evidence` | 3 条证据行。每行 pill (热搜/YouTube/TikTok/Memes/广告) + 文本。文本内**关键词必须包 `<span class="v2-jump" onclick="jumpTo(...)">`**（蓝色虚线 → 跳转） |
| `v2-judg-action` | 💡 可联想的方向 + 2-3 句**参考式**启发文（80-150 字）。常用句式：「这个 X 对 Y 是个不错的起点 / 可以衍生出... / 不妨联想到 / 也值得纳入选题池」 |
| `v2-judg-warn` | 可选。仅当本卡主题确有反向参考时加。 |

### 卡 2 · v2-judg-play（活动/玩法灵感）

| 字段 | 取值规则 |
|------|---------|
| `v2-judg-tier` | inline style 黄色：`background:rgba(255,197,51,0.15);color:#ffc533;border-color:rgba(255,197,51,0.4);` |
| 其余 | 同卡 1 规则。`v2-judg-cat` = `⚔️ 活动/玩法灵感 · XX 优先` |
| `v2-judg-warn` | **本卡常见反向参考**：Memes 板块的"假希望"类信号通常落在玩法维度，记得检查蓝图中是否有对应反信号 |

### 卡 3 · v2-judg-ad（广告制作灵感）

| 字段 | 取值规则 |
|------|---------|
| `v2-judg-tier` | inline style 青色：`background:rgba(37,244,238,0.12);color:#25f4ee;border-color:rgba(37,244,238,0.4);` |
| 其余 | 同卡 1。`v2-judg-cat` = `📢 广告制作灵感 · XX 优先` |

---

## 6. 图片三连选图规则

每个判断卡顶部 3 张图选自 5 板块图片资产，规则：

1. **每张图必须对应 1 条证据**（强关联，不要拿无关图凑数）
2. **优先用静态 img**：`<img src="...jpg">`
3. **广告板块用 video**：因 `ads_raw.json` thumbUrl 字段当前失效（DOM 抓不到），缩略图全空。改用 `<video src="ads_videos_gdd/{rank:02d}_{slug}.mp4" autoplay muted loop playsinline>`，浏览器会自动循环播放（与广告板块一致）
4. **每张图必须可点击 jumpTo**：onclick + title 提示
5. **底部 overlay 文案**：`{Pill 标 来源 #N}` + 1 行短说明（≤ 25 字）

### 选图模板示例
```html
<div class="v2-judg-img-card" onclick="jumpTo('s-trends','trend-4')" title="跳转到热搜 #4 Pragmata">
  <img src="trend_images/04_pragmata_1.jpg" alt="Pragmata">
  <div class="v2-judg-img-overlay">
    <span class="v2-judg-img-pill v2-judg-ev-trend">🔥 热搜 #4</span>
    <div class="v2-judg-img-cap">Pragmata · AI 少女搭档</div>
  </div>
</div>
```

---

## 7. 跳转关键词（v2-jump）写法

证据行文本中，**所有可点击的关键词**必须包：
```html
<span class="v2-jump" onclick="jumpTo('s-XX','XX-N')"><strong>关键词</strong></span>
```

- `s-XX` 是目标板块 id（s-trends / s-tiktok / s-youtube / s-memes / s-ads）
- `XX-N` 是目标卡 id（trend-4 / tt-5 / yt-1 / meme-3 / ad-2 等）
- 包 `<strong>` 让关键词加粗（与未点击的描述文字区分）
- 跨平台同维度多个引用（如四条广告）可分别包：
  ```html
  (<span class="v2-jump" onclick="jumpTo('s-ads','ad-4')">Cash Merge</span> /
   <span class="v2-jump" onclick="jumpTo('s-ads','ad-6')">Nut Sort</span>)
  ```

---

## 8. v2-aux-note 末尾说明卡

```html
<div class="v2-aux-note">
  📂 <strong>本期完整 9 项跨源信号</strong>(含 6 项 ★★ 双来源信号与 3 项反向参考) 已分散在下方 5 个板块的结论框中, 可点击「前往各板块」按需深入。本页聚焦的是跨源印证最强的 3 个观察 —— 围绕主线「<strong style="color:#ff6b6b">{本期主线}</strong>」, 它们刚好分别落在<strong>角色 / 玩法 / 广告</strong>三个维度, 可作为本期参考思考的起点。
</div>
```

字段 `{本期主线}` 由分析阶段决定（如 Vol.004 = "AI 角色验证闭环"）。

---

## 9. 信号矩阵 + 快捷导航（保留 v1，无变更）

详见 v1 模板第 6/7 节（git 历史 commit 921a416 之前的版本可查），结构 100% 复用。

---

## 10. 必备 JS 函数（写入 hub.html `<script>` 末尾）

```js
function jumpTo(sectionId, anchorId) {
  var btn = document.querySelector('[data-target="' + sectionId + '"]');
  if (btn) switchSection(sectionId, btn);
  setTimeout(function() {
    var el = document.getElementById(anchorId);
    if (el) {
      el.scrollIntoView({behavior: 'smooth', block: 'center'});
      el.style.transition = 'box-shadow 0.4s';
      el.style.boxShadow = '0 0 0 3px #fe2c55';
      setTimeout(function() { el.style.boxShadow = ''; }, 1800);
    }
  }, 80);
  return false;
}
```

拼接 hub.html 时 `tail -n +M $VOL_PREV` 会自动把上期的 jumpTo 拷过来，**无需手动补丁**（同 openVbox 规则）。

校验：`grep -c "function jumpTo" hub.html` 应输出 1。

---

## 11. 写作 subagent 强制工作流

1. **Read 上期 hub.html overview 区间**（行号由主对话提供） → 输出 v2-* class 清单作为审计痕迹
2. **Read 本期 blueprints/overview.md** → 校验 3 个判断字段齐全（claim / 3 imgs / 3 evidence / action / 可选 warn）
3. **Read 本期各板块蓝图获取条目编号** → 确保 jumpTo 目标 id 对得上
4. **写 fragment**，严格遵守：
   - 文案语气检查（grep 禁用词：必须 / 立刻 / 严禁 / 硬规则 / 现成模板 / 碾压 → 0 命中）
   - 3 个判断卡必含图片三连（9 张）+ 跳转链接（≥ 9 处）
   - 矩阵 + 导航保留
5. **Write 到 `$REPORT_DIR/poc_overview_section.html`**
6. **返回审计报告**：v2-* class 清单 / 字段齐全度 / jumpTo 链接数 / 文案禁用词扫描结果 / 警告

---

## 12. 校验清单（写完后跑一次 · Vol.005+ 扩展）

### 12.1 Overview fragment 校验
```bash
OUT=$REPORT_DIR/poc_overview_section.html
echo "v2-judg 卡: $(grep -c 'class=\"v2-judg ' $OUT)  期望 3"
echo "图片三连: $(grep -c '<div class=\"v2-judg-img-card\"' $OUT)  期望 9"
echo "跳转链接: $(grep -c 'class=\"v2-jump\"' $OUT)  期望 ≥ 9"
echo "图片资源存在性:"
grep -oE 'src="(trend_images|yt_images|tiktok_images|meme_images|ads_videos_gdd)/[^"]+"' $OUT | \
  sed 's/src="//;s/"//' | while read f; do [ -f "$REPORT_DIR/$f" ] || echo "MISSING: $f"; done
```

### 12.2 全 hub.html 文案语气扫描（**全板块强制 · Vol.005+ 起入流水线**）

```bash
HUB=$REPORT_DIR/hub.html

echo "=== 硬指令禁用词扫描 ==="
grep -nE '必须|立刻|严禁|硬规则|现成模板|碾压|最强判断|DRD|务必|一定要|王炸|完胜|必胜|终极' $HUB \
  | grep -v '^\s*//' | head -10
echo "(期望 0 命中, 命中需手动审查; 注释和反向参考语境可保留)"

echo ""
echo "=== 绝对化禁用词扫描 ==="
grep -nE '直接套用|直接抄|直接落地|直接挪用|直接复用|永久流量公式|最高优先级|最优起点|最优|最强|顶级|至高|史上|永远' $HUB \
  | grep -v '^\s*//' | head -10
echo "(期望 ≤ 20 处保留语境: 政治警告/修辞描述/游戏内文案引用; 其余应改写)"

echo ""
echo "=== 数字建议扫描 (Vol.005+ 新增) ==="
grep -nE '一周(内)?\s*(可|能)?\s*(出|跑|完成|生成|验证)\s*\d+|每周\s*\d+|可\s*(批量)?\s*(产|跑|出|验证|生成|测试)\s*\d+' $HUB | head -5
echo "(期望 0 命中, 出多少图不是 westradar 说了算)"

echo ""
echo "=== A/B/C 标签命名校验 ==="
echo "  A 直接可用 (不应再有): $(grep -c 'A 直接可用' $HUB)  期望 0"
echo "  A 契合度高:           $(grep -c 'A 契合度高' $HUB)  期望 ≥ 1"
echo "  B 结构借鉴:           $(grep -c 'B 结构借鉴' $HUB)"
echo "  C 观察储备:           $(grep -c 'C 观察储备' $HUB)"
```

### 12.3 校验通过的标准

- 12.1 Overview 三件套全齐
- 12.2 硬指令 ≤ 5 处（可保留语境）/ 绝对化 ≤ 20 处（可保留语境）/ 数字建议 = 0
- 12.3 A 标签全部用 "契合度高" 不是 "直接可用"

如有未达标项，参考第 1 节"关于文案语气"逐处改写。
