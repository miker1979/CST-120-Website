from pathlib import Path

GAME_PAGE = Path("arizona-paranormal.html")
DEV_LOG = Path("development-log.html")


def update_game_page() -> None:
    text = GAME_PAGE.read_text(encoding="utf-8")

    css = """
    /* GAMEPLAY CONCEPT TEASER */
    .gameplay-teaser-card{
      overflow:hidden;
      border:1px solid var(--az-border);
      border-top:4px solid var(--az-oxblood);
      border-radius:18px;
      background:#050608;
      box-shadow:0 22px 50px rgba(0,0,0,.20);
    }
    .gameplay-teaser-video{
      display:block;
      width:100%;
      background:#000;
    }
    .gameplay-teaser-copy{
      padding:1.25rem 1.4rem 1.4rem;
      background:#0d0e12;
    }
    .gameplay-teaser-copy p{color:#c9c1bb!important;}
    body.arizona-page.dark-mode .gameplay-teaser-card{border-color:#3b4657;}
    /* END GAMEPLAY CONCEPT TEASER */
"""

    section = """
<section id="gameplay-teaser" class="az-section">
  <div class="container">
    <div class="text-center mb-5">
      <p class="section-label">Gameplay Concept Teaser</p>
      <h2 class="section-title">A first look at the <span class="az-accent">Haunted Hamburger investigation.</span></h2>
      <p class="lead az-lead">This work-in-progress visual concept explores the first-person atmosphere, pacing, and paranormal tension planned for The 9th Vessel. It is AI-assisted concept footage and does not represent final in-engine gameplay.</p>
    </div>
    <div class="gameplay-teaser-card">
      <video class="gameplay-teaser-video" controls preload="metadata" poster="images/the-9th-vessel-cover.png">
        <source src="Video/the-9th-vessel-gameplay-concept.mp4" type="video/mp4">
        Your browser does not support the video element.
      </video>
      <div class="gameplay-teaser-copy">
        <div class="mb-2">
          <span class="az-tag">Work in Progress</span>
          <span class="az-tag">Concept Footage</span>
          <span class="az-tag">First-Person Horror</span>
        </div>
        <p class="mb-0">Haunted Hamburger is one of the Jerome investigation locations. This teaser is a visual-development experiment used to explore mood, movement, sound, and encounter pacing.</p>
      </div>
    </div>
  </div>
</section>
"""

    if "/* GAMEPLAY CONCEPT TEASER */" not in text:
        marker = "\n</style>"
        if marker not in text:
            raise SystemExit("Could not find style closing tag in game page")
        text = text.replace(marker, css + marker, 1)

    if 'id="gameplay-teaser"' not in text:
        marker = '<section id="canon" class="az-section">'
        if marker not in text:
            raise SystemExit("Could not find canon section in game page")
        text = text.replace(marker, section + marker, 1)

    GAME_PAGE.write_text(text, encoding="utf-8")


def update_dev_log() -> None:
    text = DEV_LOG.read_text(encoding="utf-8")

    text = text.replace(
        '<span class="status">Updated August 13, 2026</span>',
        '<span class="status">Updated August 14, 2026</span>',
        1,
    )

    old_snapshot = '<p><strong>Haunted Echoes:</strong> War of the Damned is now a playable prototype with complete WAR logic, Auto-War, Blood Ledger history, card audio, and a custom gothic deck-art pass underway</p>'
    new_snapshot = '<p><strong>Haunted Echoes:</strong> The 9th Vessel now has a public AI-assisted first-person gameplay concept teaser for the Haunted Hamburger investigation; War of the Damned remains a playable prototype with its custom gothic deck-art pass underway</p>'
    if old_snapshot in text:
        text = text.replace(old_snapshot, new_snapshot, 1)

    entry = """
<!-- 2026-08-14-9th-vessel-gameplay-concept -->
<article class="entry"><div class="cardlog"><header class="head"><span class="date">August 14, 2026 &middot; Haunted Echoes Studios / The 9th Vessel</span><h2>First public gameplay-concept teaser explores the Haunted Hamburger investigation</h2></header><div class="bodycopy">
<p>A new short visual-development teaser is now live on The 9th Vessel project page, using AI-assisted concept footage to test the first-person mood and pacing planned for the Jerome investigation experience.</p>
<ul><li>Built the sequence around a player-perspective approach and investigation at Haunted Hamburger.</li><li>Focused the experiment on flashlight movement, environmental tension, sound-driven suspense, and restrained paranormal presentation.</li><li>Kept the public teaser spoiler-free and avoided revealing story-critical identities, ritual mechanics, ending logic, or deeper canon.</li><li>Published the footage as a clearly labeled work-in-progress concept rather than presenting it as final Unity gameplay.</li><li>Used the experiment to establish a practical visual target for later in-engine environment, camera, lighting, and encounter work.</li></ul>
<p><strong>Next:</strong> carry the strongest pacing and atmosphere lessons from the concept footage into Unity prototyping while continuing environment planning for the Jerome vertical slice.</p>
<p><a href="arizona-paranormal.html#gameplay-teaser">Watch the gameplay concept teaser &rarr;</a></p>
</div></div></article>

"""

    if "2026-08-14-9th-vessel-gameplay-concept" not in text:
        marker = '<section class="pad alt"><div class="container"><div class="timeline">\n'
        if marker not in text:
            raise SystemExit("Could not find timeline start in development log")
        text = text.replace(marker, marker + "\n" + entry, 1)

    DEV_LOG.write_text(text, encoding="utf-8")


update_game_page()
update_dev_log()
