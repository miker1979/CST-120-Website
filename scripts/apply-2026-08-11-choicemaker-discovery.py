from pathlib import Path

HOME = Path("index.html")
LABS = Path("labs.html")

HOME_SECTION = '''

        <!-- =================================================
             CHOICEMAKER DEVELOPER TOOL
             ================================================= -->

        <section class="section-padding">
            <div class="container">
                <div class="row align-items-center">
                    <div class="col-lg-7 mb-4 mb-lg-0">
                        <p class="section-label">Featured Ghostline Labs Developer Tool</p>
                        <h2 class="section-title">
                            ChoiceMaker: <span class="accent-text">Design the choices. Test the consequences.</span>
                        </h2>
                        <p class="lead">
                            ChoiceMaker helps game developers define state variables, outcome rules,
                            conditions, and priorities, then test whether player states resolve to the
                            endings they intended.
                        </p>
                        <p class="text-muted-custom mb-4">
                            The current developer preview validates project structure, evaluates every
                            ending, exposes overlapping matches, resolves priority, and explains why
                            rejected endings failed.
                        </p>
                        <div class="mb-4">
                            <span class="product-tag">Developer Preview</span>
                            <span class="product-tag">C# / .NET</span>
                            <span class="product-tag">46 Automated Tests</span>
                            <span class="product-tag">Branching Logic</span>
                        </div>
                        <a href="choicemaker.html" class="btn btn-ghostline">
                            Explore ChoiceMaker
                        </a>
                    </div>
                    <div class="col-lg-5">
                        <article class="ghostline-card h-100">
                            <span class="branch-code">CM</span>
                            <h3 class="mt-3">Developer Logic Validation</h3>
                            <ul class="product-list mb-0">
                                <li>Validate variables, endings, and rule definitions</li>
                                <li>Evaluate supplied game-state values</li>
                                <li>See every matching and rejected ending</li>
                                <li>Resolve overlapping outcomes by priority</li>
                                <li>Use rejection reasons to debug narrative logic</li>
                            </ul>
                        </article>
                    </div>
                </div>
            </div>
        </section>
'''

LABS_CARD = '''
                    <!-- ChoiceMaker -->
                    <div class="col-12 mb-4">
                        <article class="ghostline-card d-flex flex-column">
                            <div>
                                <span class="product-tag">Active Developer Preview</span>
                                <span class="product-tag">C# / .NET</span>
                                <span class="product-tag">46 Automated Tests</span>
                            </div>

                            <div class="row align-items-center mt-3">
                                <div class="col-lg-8 mb-3 mb-lg-0">
                                    <span class="branch-code">CM</span>
                                    <h3 class="mt-3">ChoiceMaker</h3>
                                    <p class="lead mb-3">Design the choices. Test the consequences.</p>
                                    <p class="text-muted-custom mb-0">
                                        A reusable game-development tool for designing, testing, simulating,
                                        and validating branching game-state logic. ChoiceMaker can detect
                                        configuration problems, evaluate multiple endings against the same
                                        state, resolve priority, and explain exactly why rejected outcomes failed.
                                    </p>
                                </div>
                                <div class="col-lg-4">
                                    <ul class="product-list mb-4">
                                        <li>Generic developer-defined variables</li>
                                        <li>Conditional ending rules</li>
                                        <li>Overlap and priority resolution</li>
                                        <li>Failure-reason reporting</li>
                                        <li>Interactive browser preview</li>
                                    </ul>
                                    <a href="choicemaker.html" class="btn btn-ghostline btn-block">
                                        Open ChoiceMaker Preview
                                    </a>
                                </div>
                            </div>
                        </article>
                    </div>

'''


def update_home():
    text = HOME.read_text(encoding="utf-8")
    if 'href="choicemaker.html"' in text and "CHOICEMAKER DEVELOPER TOOL" in text:
        print("Home page ChoiceMaker section already present.")
        return False

    marker = '''        <!-- =================================================\n             COMPANY\n             ================================================= -->'''
    if marker not in text:
        raise RuntimeError("Could not find COMPANY marker in index.html")

    text = text.replace(marker, HOME_SECTION + "\n\n" + marker, 1)
    HOME.write_text(text, encoding="utf-8")
    print("Added ChoiceMaker discovery section to index.html")
    return True


def update_labs():
    text = LABS.read_text(encoding="utf-8")
    if 'Open ChoiceMaker Preview' in text:
        print("Labs ChoiceMaker featured card already present.")
        return False

    marker = '''                <div class="row">\n\n                    <!-- FleetTrack Pro -->'''
    if marker not in text:
        raise RuntimeError("Could not find Featured Projects row marker in labs.html")

    replacement = '                <div class="row">\n\n' + LABS_CARD + '                    <!-- FleetTrack Pro -->'
    text = text.replace(marker, replacement, 1)
    LABS.write_text(text, encoding="utf-8")
    print("Added ChoiceMaker featured card to labs.html")
    return True


changed_home = update_home()
changed_labs = update_labs()

if not changed_home and not changed_labs:
    print("No changes required.")

# Triggered after workflow installation so the update runs on main.
