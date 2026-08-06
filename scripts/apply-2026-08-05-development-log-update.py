from pathlib import Path

MAIN_MARKER = "<!-- 2026-08-05-transitlogic-and-chess -->"
CHESS_MARKER = "<!-- 2026-08-05-chess-faction-artwork -->"

MAIN_ENTRY = r'''
                    <!-- 2026-08-05-transitlogic-and-chess -->
                    <article class="timeline-entry">
                        <span class="timeline-marker" aria-hidden="true"></span>
                        <div class="timeline-card">
                            <header class="timeline-header">
                                <span class="timeline-date">August 5, 2026 · Ghostline Software</span>
                                <h2>TransitLogic Carrier Workflow and Freight Intelligence Expansion</h2>
                            </header>
                            <div class="timeline-body">
                                <p>
                                    TransitLogic advanced from a basic freight-board concept into a connected carrier,
                                    broker, shipper, receiver, and facility workflow prototype. The latest pass reduces
                                    the primary carrier search to the lane, equipment, pickup date, and one search action,
                                    while preserving detailed postal and profitability controls under More Filters.
                                </p>
                                <section class="entry-section">
                                    <h3>Carrier workflow improvements</h3>
                                    <ul class="improvement-list">
                                        <li>Added quick presets for a home terminal, saved lanes, low deadhead, highest profit, and recently posted freight.</li>
                                        <li>Made KPI cards interactive so carriers can immediately filter, sort, or edit operating assumptions.</li>
                                        <li>Moved the Carrier Marketplace above regional and directional freight intelligence.</li>
                                        <li>Kept major freight markets visible while ZIP3, FSA, ZIP5, and postal-code intelligence operates underneath.</li>
                                    </ul>
                                </section>
                                <section class="entry-section">
                                    <h3>Connected data and operations</h3>
                                    <ul class="improvement-list">
                                        <li>Centralized customer profiles, load drafts, preferences, posted loads, and last-used settings.</li>
                                        <li>Added postal-based route-mile estimates and carrier profitability calculations.</li>
                                        <li>Built broker, shipper, receiver, and facility registration workflows with compliance and operating details.</li>
                                        <li>Added facility requirements, driver-restroom status, and nearby truck-stop or washout information.</li>
                                        <li>Expanded selectable Lower 48, Canada, Alaska, state heat, major-market, and directional-lane map views.</li>
                                    </ul>
                                </section>
                                <div class="timeline-links">
                                    <a href="load-board.html">View TransitLogic product page &rarr;</a>
                                    <a href="transitlogic-updates/2026-08-05/README.md">Open technical update &rarr;</a>
                                </div>
                            </div>
                        </div>
                    </article>

                    <article class="timeline-entry">
                        <span class="timeline-marker" aria-hidden="true"></span>
                        <div class="timeline-card">
                            <header class="timeline-header">
                                <span class="timeline-date">August 5, 2026 · Haunted Echoes Studios</span>
                                <h2>Ghostline Chess Faction Artwork and Source Structure Updated</h2>
                            </header>
                            <div class="timeline-body">
                                <p>
                                    Ghostline Chess received a new faction-art pass and source update built around the
                                    Hallowed and the Damned. The piece assets, sprite-loading code, theme hooks, Chronicle,
                                    game logic references, project file, documentation, and current gameplay presentation
                                    were prepared together so the visual identity remains consistent throughout the game.
                                </p>
                                <section class="entry-section">
                                    <h3>What changed</h3>
                                    <ul class="improvement-list">
                                        <li>Standardized the twelve active piece files around white and black faction asset names.</li>
                                        <li>Updated sprite loading, theme integration, Chronicle hooks, and supporting form code.</li>
                                        <li>Refreshed the project file, README, and current gameplay screenshot.</li>
                                        <li>Prepared full-source and patch archives for the Hallowed-versus-Damned milestone.</li>
                                    </ul>
                                </section>
                                <div class="timeline-links">
                                    <a href="ghostline-chess.html">View Ghostline Chess &rarr;</a>
                                    <a href="ghostline-chess-development-log.html">Detailed chess log &rarr;</a>
                                </div>
                            </div>
                        </div>
                    </article>
'''

CHESS_ENTRY = r'''

                    <!-- 2026-08-05-chess-faction-artwork -->
                    <article class="timeline-entry">
                        <span class="timeline-marker" aria-hidden="true"></span>
                        <div class="timeline-card">
                            <header class="timeline-header">
                                <span class="timeline-date">August 5, 2026</span>
                                <h2>Hallowed and Damned Faction Artwork Source Update</h2>
                            </header>
                            <div class="timeline-body">
                                <p>
                                    A coordinated source and artwork pass replaced the legacy pale and shadow asset naming
                                    with a standardized white and black faction set while preserving the gothic identity of
                                    the Hallowed and the Damned. The update touched the sprite loader, main form, theme,
                                    Chronicle integration, chess logic references, project configuration, documentation,
                                    and current gameplay presentation.
                                </p>
                                <div class="row mt-4">
                                    <div class="col-md-6">
                                        <h3 class="h5">Artwork and Interface</h3>
                                        <ul class="milestone-list">
                                            <li>Twelve standardized faction-piece assets</li>
                                            <li>Updated sprite-loading and fallback behavior</li>
                                            <li>Refined form, theme, and Chronicle hooks</li>
                                            <li>Updated current gameplay screenshot</li>
                                        </ul>
                                    </div>
                                    <div class="col-md-6 mt-4 mt-md-0">
                                        <h3 class="h5">Source Packaging</h3>
                                        <ul class="milestone-list">
                                            <li>Updated project asset mappings</li>
                                            <li>Refreshed README documentation</li>
                                            <li>Prepared a complete source archive</li>
                                            <li>Prepared a smaller patch archive</li>
                                        </ul>
                                    </div>
                                </div>
                                <p class="image-caption">
                                    This milestone documents the coordinated source and artwork update. A new automated .NET build was not run in the publishing environment.
                                </p>
                            </div>
                        </div>
                    </article>
'''


def insert_after(text: str, needle: str, block: str) -> str:
    index = text.find(needle)
    if index < 0:
        raise RuntimeError(f"Could not locate insertion marker: {needle}")
    return text[: index + len(needle)] + "\n" + block + text[index + len(needle):]


def insert_after_article_containing(text: str, phrase: str, block: str) -> str:
    start = text.find(phrase)
    if start < 0:
        raise RuntimeError(f"Could not locate chess milestone: {phrase}")
    end = text.find("</article>", start)
    if end < 0:
        raise RuntimeError("Could not locate the end of the chess milestone article")
    end += len("</article>")
    return text[:end] + block + text[end:]


def update_main_log() -> bool:
    path = Path("development-log.html")
    text = path.read_text(encoding="utf-8")
    if MAIN_MARKER in text:
        return False

    text = text.replace(
        "                                August 4, 2026\n",
        "                                August 5, 2026\n",
        1,
    )
    text = text.replace(
        "                                Ghostline Chess audio curation and visual polish\n",
        "                                TransitLogic carrier workflow and Ghostline Chess artwork\n",
        1,
    )
    text = text.replace(
        '<span class="status-badge status-research">Product Research</span>\n                            <h3>Ghostline Load Board</h3>',
        '<span class="status-badge status-active">Active Prototype</span>\n                            <h3>TransitLogic Load Board</h3>',
        1,
    )
    text = insert_after(text, '                <div class="company-timeline">', MAIN_ENTRY)
    path.write_text(text, encoding="utf-8")
    return True


def update_chess_log() -> bool:
    path = Path("ghostline-chess-development-log.html")
    text = path.read_text(encoding="utf-8")
    if CHESS_MARKER in text:
        return False

    text = text.replace(
        "                                Layered audio system — August 4, 2026\n",
        "                                Hallowed and Damned artwork source update — August 5, 2026\n",
        1,
    )
    text = text.replace(
        "                                Audio routing works; cue curation and visual polish next\n",
        "                                Updated faction assets and source packaging prepared; cue curation remains next\n",
        1,
    )
    text = insert_after_article_containing(
        text,
        '<span class="timeline-date">August 4, 2026</span>',
        CHESS_ENTRY,
    )
    path.write_text(text, encoding="utf-8")
    return True


if __name__ == "__main__":
    changed = []
    if update_main_log():
        changed.append("development-log.html")
    if update_chess_log():
        changed.append("ghostline-chess-development-log.html")
    print("Updated:", ", ".join(changed) if changed else "nothing (markers already present)")
