from pathlib import Path
import re

ROOT = Path(".")


def replace_once(path: Path, pattern: str, replacement: str, label: str) -> bool:
    text = path.read_text(encoding="utf-8")
    updated, count = re.subn(pattern, replacement, text, count=1, flags=re.S)
    if count == 0:
        print(f"SKIP: {label} marker not found in {path}")
        return False
    path.write_text(updated, encoding="utf-8")
    print(f"UPDATED: {label} in {path}")
    return True


def update_home() -> bool:
    path = ROOT / "index.html"
    text = path.read_text(encoding="utf-8")
    changed = False

    old_description = (
        'content="Ghostline Technology LLC develops operational software through '
        'Ghostline Software, original games through Haunted Echoes Studios, and '
        'experimental projects through Ghostline Labs."'
    )
    new_description = (
        'content="Ghostline Technology LLC is an Arizona software development company '
        'building operational software, logistics systems, developer tools, original games, '
        'and technology prototypes."'
    )
    if old_description in text:
        text = text.replace(old_description, new_description, 1)
        changed = True
        print("UPDATED: homepage meta description")

    if 'href="software-development.html"' not in text:
        pattern = (
            r'(<a\s+class="btn btn-ghostline mr-2 mb-2"\s+href="software\.html">'
            r'.*?Explore Ghostline Software.*?</a>)'
        )
        replacement = (
            r'\1\n'
            '                    <a class="btn btn-ghostline-outline mr-2 mb-2" href="software-development.html">\n'
            '                        Software Development Services\n'
            '                    </a>'
        )
        text, count = re.subn(pattern, replacement, text, count=1, flags=re.S)
        if count:
            changed = True
            print("UPDATED: homepage software-development CTA")
        else:
            print("SKIP: homepage software CTA marker not found")

    if changed:
        path.write_text(text, encoding="utf-8")
    return changed


def update_software() -> bool:
    path = ROOT / "software.html"
    text = path.read_text(encoding="utf-8")
    changed = False

    old_title = "<title>\n        Ghostline Software | Ghostline Technology LLC\n    </title>"
    new_title = "<title>\n        Software Development | Ghostline Software | Ghostline Technology LLC\n    </title>"
    if old_title in text:
        text = text.replace(old_title, new_title, 1)
        changed = True
        print("UPDATED: software page title")

    old_description = (
        'content="Ghostline Software develops practical operational software for '
        'transportation, construction, logistics, fleet management, and field operations."'
    )
    new_description = (
        'content="Ghostline Software is the software development division of Ghostline Technology LLC, '
        'building operational software for transportation, construction, logistics, fleet management, '
        'and field operations."'
    )
    if old_description in text:
        text = text.replace(old_description, new_description, 1)
        changed = True
        print("UPDATED: software page meta description")

    if 'Software Development Services' not in text:
        pattern = (
            r'(<a\s+href="#products"\s+class="btn btn-ghostline btn-lg mr-2 mb-2">'
            r'.*?Explore Software Products.*?</a>)'
        )
        replacement = (
            r'\1\n\n'
            '                            <a\n'
            '                                href="software-development.html"\n'
            '                                class="btn btn-ghostline-outline btn-lg mr-2 mb-2">\n\n'
            '                                Software Development Services\n\n'
            '                            </a>'
        )
        text, count = re.subn(pattern, replacement, text, count=1, flags=re.S)
        if count:
            changed = True
            print("UPDATED: software page service CTA")
        else:
            print("SKIP: software hero CTA marker not found")

    if changed:
        path.write_text(text, encoding="utf-8")
    return changed


def update_company() -> bool:
    path = ROOT / "company.html"
    text = path.read_text(encoding="utf-8")
    if 'View Software Development Services' in text:
        print("SKIP: company software-development CTA already present")
        return False

    pattern = (
        r'(<a\s+href="contact\.html"\s+class="btn btn-ghostline-outline btn-lg mb-2">'
        r'.*?Contact Ghostline Tech.*?</a>)'
    )
    replacement = (
        '                            <a\n'
        '                                href="software-development.html"\n'
        '                                class="btn btn-ghostline-outline btn-lg mr-2 mb-2">\n\n'
        '                                View Software Development Services\n\n'
        '                            </a>\n\n'
        r'                            \1'
    )
    updated, count = re.subn(pattern, replacement, text, count=1, flags=re.S)
    if count:
        path.write_text(updated, encoding="utf-8")
        print("UPDATED: company software-development CTA")
        return True

    print("SKIP: company contact CTA marker not found")
    return False


def update_footers() -> int:
    targets = [
        "index.html",
        "software.html",
        "software-development.html",
        "company.html",
        "labs.html",
        "choicemaker.html",
        "contact.html",
        "haunted-echoes.html",
        "development-log.html",
        "construction-ops.html",
        "load-board.html",
        "broker-operations.html",
        "ghostline-chess.html",
        "arizona-paranormal.html",
        "boston-ripper.html",
    ]

    changed = 0
    for name in targets:
        path = ROOT / name
        if not path.exists():
            print(f"SKIP: footer target missing: {name}")
            continue

        text = path.read_text(encoding="utf-8")
        if 'href="software-development.html">Software Development</a>' in text:
            continue

        marker = '<a href="software.html">Ghostline Software</a>'
        if marker not in text:
            print(f"SKIP: standard footer marker not found in {name}")
            continue

        text = text.replace(
            marker,
            marker + '\n                <a href="software-development.html">Software Development</a>',
            1,
        )
        path.write_text(text, encoding="utf-8")
        changed += 1
        print(f"UPDATED: footer software-development link in {name}")

    return changed


home = update_home()
software = update_software()
company = update_company()
footer_count = update_footers()

print(
    "SEO update complete:",
    f"home={home}, software={software}, company={company}, footers={footer_count}"
)
