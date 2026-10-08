#!/usr/bin/env python3
"""Fail if TikTok-review brand identity drifts across public site pages."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAGES = [
    ROOT / "index.html",
    ROOT / "how-it-works" / "index.html",
    ROOT / "privacy" / "index.html",
    ROOT / "terms" / "index.html",
    ROOT / "contact" / "index.html",
]
LOGO = ROOT / "assets/watcherfeed-crest.webp"
FAVICON = ROOT / "assets/watcherfeed-favicon.png"

def main() -> int:
    problems = []
    if not LOGO.is_file() or LOGO.read_bytes()[:4] != b"RIFF":
        problems.append("Logo is missing or is not a RIFF/WebP image")
    elif LOGO.read_bytes()[8:12] != b"WEBP":
        problems.append("Logo WebP signature invalid")
    if not FAVICON.is_file() or FAVICON.read_bytes()[:8] != b"\\x89PNG\\r\\n\\x1a\\n":
        problems.append("Favicon is missing or is not PNG")

    for page in PAGES:
        if not page.is_file():
            problems.append(f"Page missing: {page.relative_to(ROOT)}")
            continue
        html = page.read_text(encoding="utf-8")
        prefix = "./" if page.parent == ROOT else "../"
        for target in (
            f'{prefix}assets/watcherfeed-crest.webp',
            f'{prefix}assets/watcherfeed-favicon.png',
        ):
            if target not in html:
                problems.append(f"Missing asset reference {target} in {page.relative_to(ROOT)}")
        if 'class="brandicon"' not in html:
            problems.append(f"Official header icon missing: {page.relative_to(ROOT)}")
        if 'rel="icon"' not in html:
            problems.append(f"Browser favicon declaration missing: {page.relative_to(ROOT)}")
    home = PAGES[0].read_text(encoding="utf-8") if PAGES[0].is_file() else ""
    if '<div class="mark">WF</div>' in home:
        problems.append("Home page still uses the generic WF placeholder")
    if 'class="mark"' not in home or "official app logo" not in home:
        problems.append("Home hero missing official branded image")
    for page in ("privacy", "terms", "contact", "how-it-works"):
        if not (ROOT / page / "index.html").is_file():
            problems.append(f"Review URL missing: /{page}/")
    if problems:
        for problem in problems:
            print("FAIL", problem)
        return 1
    print("WATCHERFEED_PUBLIC_SITE_BRAND_REVIEW_PASS")
    print("Pages checked:", len(PAGES))
    print("Brand + favicon: PRESENT AND REFERENCED")
    print("TikTok portal resubmission: STILL REQUIRED")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
