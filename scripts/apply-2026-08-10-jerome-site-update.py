from pathlib import Path

PAGES = [Path("arizona-paranormal.html"), Path("arizona-paranormal-v2.html")]
DEVLOG = Path("development-log.html")


def resolve_head_conflicts(text: str) -> str:
    """Resolve any accidentally committed Git conflict blocks by keeping HEAD."""
    marker = "<<<<<<< HEAD"
    while marker in text:
        start = text.index(marker)
        sep = text.index("=======", start)
        end = text.index(">>>>>>>", sep)
        end_line = text.find("\n", end)
        if end_line == -1:
            end_line = len(text)
        else:
            end_line += 1
        head = text[start + len(marker):sep]
        if head.startswith("\n"):
            head = head[1:]
        text = text[:start] + head + text[end_line:]
    return text


ANCHOR_CSS = r'''

    /* EIGHT ANCHOR POINTS GALLERY */
    .anchor-card{height:100%;overflow:hidden;padding:0;border:1px solid var(--az-border);border-top:4px solid #704b36;border-radius:14px;background:#fff;box-shadow:0 10px 28px rgba(15,23,42,.07)}
    .anchor-shot{position:relative;margin:0;aspect-ratio:16/10;overflow:hidden;background:#050608;border-bottom:1px solid var(--az-border)}
    .anchor-shot a{display:block;width:100%;height:100%;cursor:zoom-in}
    .anchor-shot img{display:block;width:100%;height:100%;object-fit:cover;transition:transform .22s ease,filter .22s ease}
    .anchor-shot:hover img{transform:scale(1.035);filter:brightness(1.06)}
    .anchor-shot figcaption{position:absolute;top:.55rem;left:.55rem;margin:0;padding:.3rem .55rem;border-radius:999px;background:rgba(7,9,13,.86);color:#f3eadc;font-size:.65rem;font-weight:900;letter-spacing:.04rem;text-transform:uppercase;pointer-events:none}
    .anchor-body{padding:1.25rem 1.35rem 1.45rem}
    .anchor-id{display:inline-flex;align-items:center;justify-content:center;min-width:44px;height:32px;padding:0 .65rem;border-radius:999px;background:var(--az-midnight);color:#f2c067;font-weight:900;font-size:.75rem;letter-spacing:.04rem}
    .anchor-type{display:inline-block;padding:.3rem .55rem;border-radius:999px;background:rgba(125,31,48,.1);color:var(--az-oxblood);font-size:.65rem;font-weight:800;text-transform:uppercase}
    .anchor-body h3{margin:.85rem 0 .35rem;color:var(--az-text)!important;font-size:1.18rem}
    .anchor-body .miner-name{margin:0 0 .7rem;color:#704b36!important;font-weight:800}
    .anchor-body p{color:var(--az-muted)!important}
    body.arizona-page.dark-mode .anchor-card{background:#171c26;border-color:#3b4657}
    body.arizona-page.dark-mode .anchor-body h3{color:#f6efe7!important}
    body.arizona-page.dark-mode .anchor-body p{color:#bdc7d2!important}
    body.arizona-page.dark-mode .anchor-body .miner-name{color:#d2aa8f!important}
    body.arizona-page.dark-mode .anchor-type{color:#ef9dac;background:rgba(125,31,48,.23)}
    /* END EIGHT ANCHOR POINTS GALLERY */
'''

ANCHOR_SECTION = r'''
<section id="anchors" class="az-section">
  <div class="container">
    <div class="text-center mb-5">
      <p class="section-label">The Eight Anchor Points</p>
      <h2 class="section-title">Eight fictionalized locations built for <span class="az-accent">Jerome's mining landscape.</span></h2>
      <p class="lead az-lead">The Anchor Points are original game locations rather than surviving historic buildings. Their architecture and terrain draw from the mining character of Jerome while each environment is designed around a different investigation style.</p>
    </div>
    <div class="row">
      <div class="col-lg-6 mb-4"><article class="anchor-card"><figure class="anchor-shot"><a href="images/jerome-locations/Anchors/A1-old-foremans-office.webp" target="_blank" rel="noopener noreferrer"><img src="images/jerome-locations/Anchors/A1-old-foremans-office.webp" alt="Game render of the fictional Old Foreman's Office anchor point"></a><figcaption>Game Render</figcaption></figure><div class="anchor-body"><div class="d-flex justify-content-between align-items-center"><span class="anchor-id">A1</span><span class="anchor-type">Fictional Anchor</span></div><h3>Old Foreman's Office</h3><p class="miner-name">Jack &ldquo;Ironhand&rdquo; Calloway</p><p class="mb-0">A weathered mining administration office built around records, accountability, and the foreman's final investigation trail.</p></div></article></div>
      <div class="col-lg-6 mb-4"><article class="anchor-card"><figure class="anchor-shot"><a href="images/jerome-locations/Anchors/A2-powder-magazine.webp" target="_blank" rel="noopener noreferrer"><img src="images/jerome-locations/Anchors/A2-powder-magazine.webp" alt="Game render of the fictional Powder Magazine anchor point"></a><figcaption>Game Render</figcaption></figure><div class="anchor-body"><div class="d-flex justify-content-between align-items-center"><span class="anchor-id">A2</span><span class="anchor-type">Fictional Anchor</span></div><h3>Powder Magazine</h3><p class="miner-name">Samuel &ldquo;Blaze&rdquo; McKenna</p><p class="mb-0">An isolated reinforced explosives bunker cut into the hillside, with blast doors, firing equipment, and narrow service corridors.</p></div></article></div>
      <div class="col-lg-6 mb-4"><article class="anchor-card"><figure class="anchor-shot"><a href="images/jerome-locations/Anchors/A3-company-survey-archive.webp" target="_blank" rel="noopener noreferrer"><img src="images/jerome-locations/Anchors/A3-company-survey-archive.webp" alt="Game render of the fictional Company Survey Archive anchor point"></a><figcaption>Game Render</figcaption></figure><div class="anchor-body"><div class="d-flex justify-content-between align-items-center"><span class="anchor-id">A3</span><span class="anchor-type">Fictional Anchor</span></div><h3>Company Survey Archive</h3><p class="miner-name">Mateo Ruiz</p><p class="mb-0">A forgotten engineering and map archive filled with drafting tables, mine plans, survey instruments, and geometry that becomes increasingly unreliable.</p></div></article></div>
      <div class="col-lg-6 mb-4"><article class="anchor-card"><figure class="anchor-shot"><a href="images/jerome-locations/Anchors/A4-level-3200-barricade.webp" target="_blank" rel="noopener noreferrer"><img src="images/jerome-locations/Anchors/A4-level-3200-barricade.webp" alt="Game render of the fictional Level 3200 Barricade anchor point"></a><figcaption>Game Render</figcaption></figure><div class="anchor-body"><div class="d-flex justify-content-between align-items-center"><span class="anchor-id">A4</span><span class="anchor-type">Fictional Anchor</span></div><h3>Level 3200 Barricade</h3><p class="miner-name">Walter &ldquo;Timber&rdquo; Briggs</p><p class="mb-0">A timbered mine portal descending toward a dead-end barricade, unstable supports, and a progressively tighter underground route.</p></div></article></div>
      <div class="col-lg-6 mb-4"><article class="anchor-card"><figure class="anchor-shot"><a href="images/jerome-locations/Anchors/A5-main-shaft-hoist-house.webp" target="_blank" rel="noopener noreferrer"><img src="images/jerome-locations/Anchors/A5-main-shaft-hoist-house.webp" alt="Game render of the fictional Main Shaft Hoist House anchor point"></a><figcaption>Game Render</figcaption></figure><div class="anchor-body"><div class="d-flex justify-content-between align-items-center"><span class="anchor-id">A5</span><span class="anchor-type">Fictional Anchor</span></div><h3>Main Shaft Hoist House</h3><p class="miner-name">Emil Novak</p><p class="mb-0">A heavy industrial shaft complex dominated by winding drums, steel cable, brake systems, and an elevated operator station.</p></div></article></div>
      <div class="col-lg-6 mb-4"><article class="anchor-card"><figure class="anchor-shot"><a href="images/jerome-locations/Anchors/A6-lower-pump-house.webp" target="_blank" rel="noopener noreferrer"><img src="images/jerome-locations/Anchors/A6-lower-pump-house.webp" alt="Game render of the fictional Lower Drainage Station anchor point"></a><figcaption>Game Render</figcaption></figure><div class="anchor-body"><div class="d-flex justify-content-between align-items-center"><span class="anchor-id">A6</span><span class="anchor-type">Fictional Anchor</span></div><h3>Lower Drainage Station</h3><p class="miner-name">Thomas &ldquo;Pumps&rdquo; Hale</p><p class="mb-0">A low-elevation mine utility station of pipes, valves, pumps, standing water, gauges, and drainage machinery beneath the industrial hillside.</p></div></article></div>
      <div class="col-lg-6 mb-4"><article class="anchor-card"><figure class="anchor-shot"><a href="images/jerome-locations/Anchors/A7-assay-office.webp" target="_blank" rel="noopener noreferrer"><img src="images/jerome-locations/Anchors/A7-assay-office.webp" alt="Game render of the fictional Assay Office and Specimen Vault anchor point"></a><figcaption>Game Render</figcaption></figure><div class="anchor-body"><div class="d-flex justify-content-between align-items-center"><span class="anchor-id">A7</span><span class="anchor-type">Fictional Anchor</span></div><h3>Assay Office &amp; Specimen Vault</h3><p class="miner-name">Nathaniel Crowe</p><p class="mb-0">A compact mining laboratory combining ore preparation, furnace work, chemical analysis, and a secure specimen vault.</p></div></article></div>
      <div class="col-lg-6 mb-4"><article class="anchor-card"><figure class="anchor-shot"><a href="images/jerome-locations/Anchors/A8-old-infirmary-chapel.webp" target="_blank" rel="noopener noreferrer"><img src="images/jerome-locations/Anchors/A8-old-infirmary-chapel.webp" alt="Game render of the fictional Old Infirmary and Chapel Annex anchor point"></a><figcaption>Game Render</figcaption></figure><div class="anchor-body"><div class="d-flex justify-content-between align-items-center"><span class="anchor-id">A8</span><span class="anchor-type">Fictional Anchor</span></div><h3>Old Infirmary &amp; Chapel Annex</h3><p class="miner-name">Isaiah Brooks</p><p class="mb-0">A decaying medical facility that transitions into a small rock-set chapel, blending emergency care spaces with the spiritual side of the investigation.</p></div></article></div>
    </div>
  </div>
</section>
'''

DEVLOG_ENTRY = r'''
<!-- 2026-08-11-anchor-gallery -->
<article class="entry"><div class="cardlog"><header class="head"><span class="date">August 11, 2026 &middot; Haunted Echoes Studios / Arizona Paranormal Project</span><h2>Jerome anchor-point visual pass reaches the website</h2></header><div class="bodycopy">
<p>The Jerome environment pass now includes all eight dedicated miner Anchor Point renders alongside the real-location investigation gallery.</p>
<ul><li>Added eight original Anchor Point environments designed specifically for the game rather than presenting them as surviving historical buildings.</li><li>Kept the locations visually grounded in Jerome's mining landscape while giving each site a distinct investigation identity.</li><li>Finalized the public anchor set: Old Foreman's Office, Powder Magazine, Company Survey Archive, Level 3200 Barricade, Main Shaft Hoist House, Lower Drainage Station, Assay Office &amp; Specimen Vault, and Old Infirmary &amp; Chapel Annex.</li><li>Preserved spoiler-sensitive death events, ritual solutions, and ending conditions for discovery inside the game.</li></ul>
<p><strong>Next:</strong> continue environment refinement and synchronize the older ChoiceMaker console prototype with the current canon as a separate development task.</p>
<p><a href="arizona-paranormal.html#anchors">View the eight Anchor Point renders &rarr;</a></p>
</div></div></article>
'''


def update_page(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    original = text
    text = resolve_head_conflicts(text)

    # Keep the public meta description aligned with the spoiler-safe current presentation.
    text = text.replace(
        '<meta property="og:description" content="Four investigators explore real Jerome locations and uncover a fixed supernatural mystery through replayable evidence and adaptive encounters.">',
        '<meta property="og:description" content="Four investigators enter real Jerome locations and uncover a supernatural mystery whose roots reach much deeper than the town remembers.">'
    )

    if "/* EIGHT ANCHOR POINTS GALLERY */" not in text:
        css_marker = "    /* QA: LIGHT MODE HERO LIFT */"
        if css_marker not in text:
            raise RuntimeError(f"CSS insertion marker not found in {path}")
        text = text.replace(css_marker, ANCHOR_CSS + "\n" + css_marker, 1)

    if 'id="anchors"' not in text:
        system_marker = '<section class="az-section-alt"><div class="container"><div class="text-center mb-5"><p class="section-label">Spoiler-Free Systems Preview</p>'
        if system_marker not in text:
            raise RuntimeError(f"Anchor insertion marker not found in {path}")
        text = text.replace(system_marker, ANCHOR_SECTION + "\n" + system_marker, 1)

    # Current public terminology for A6.
    text = text.replace("Lower Pump House", "Lower Drainage Station")

    if text != original:
        path.write_text(text, encoding="utf-8")
        return True
    return False


def update_devlog(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    original = text
    text = resolve_head_conflicts(text)
    text = text.replace("Updated August 10, 2026", "Updated August 11, 2026")

    if "2026-08-11-anchor-gallery" not in text:
        timeline_marker = '<section class="pad alt"><div class="container"><div class="timeline">\n'
        if timeline_marker not in text:
            raise RuntimeError("Development-log timeline marker not found")
        text = text.replace(timeline_marker, timeline_marker + "\n" + DEVLOG_ENTRY + "\n", 1)

    # Remove a stale phrasing from an older public entry if present.
    text = text.replace(
        "Rebuilt the project preview around four investigators, 12 main locations, 10 secondary locations, eight miner Anchor Points, and a deeper historical mystery that predates the 1928 disaster.",
        "Rebuilt the project preview around four investigators, 12 main locations, 10 secondary locations, eight miner Anchor Points, and a deeper historical mystery that predates the 1928 disaster."
    )

    if text != original:
        path.write_text(text, encoding="utf-8")
        return True
    return False


changed = []
for page in PAGES:
    if update_page(page):
        changed.append(str(page))
if update_devlog(DEVLOG):
    changed.append(str(DEVLOG))

# Fail loudly if unresolved merge markers remain.
for path in [*PAGES, DEVLOG]:
    check = path.read_text(encoding="utf-8")
    for marker in ("<<<<<<<", "=======", ">>>>>>>"):
        if marker in check:
            raise RuntimeError(f"Unresolved merge marker {marker!r} remains in {path}")

print("Updated:", ", ".join(changed) if changed else "nothing")
