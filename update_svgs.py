#!/usr/bin/env python3
"""
1. Replace SVGs in verhalen overview page (verhalen/index.html)
2. Add hero SVGs to each detail page
"""
import re
import sys
sys.path.insert(0, '/home/claude')
from verhaal_svgs import SVGS

# Mapping from href slug to SVGS key
HREF_TO_KEY = {
    "waar-switcht-je-klant-van-weg": "waar-switcht-je-klant-van-weg",
    "waarom-klanten-echt-overstappen": "waarom-klanten-echt-overstappen",
    "waarom-jouw-klant-niet-kiest-voor-winst": "waarom-jouw-klant-niet-kiest-voor-winst",
    "impact-investor-shift-invest": "impact-investor-shift-invest",
    "groei-zonder-groeipijn": "groei-zonder-groeipijn",
    "fake-door-testing": "fake-door-testing",
    "bamboi-zebra-show": "bamboi-zebra-show",
    "behavioral-design-principes": "behavioral-design-principes",
    "kies-en-ontwerp-je-experiment": "kies-en-ontwerp-je-experiment",
}

filepath = "verhalen/index.html"

with open(filepath, "r", encoding="utf-8") as f:
    html = f.read()

replaced = 0

for slug, key in HREF_TO_KEY.items():
    if key not in SVGS:
        print(f"  SKIP {slug} - no SVG defined")
        continue
    
    new_svg = SVGS[key]["card"].strip()
    
    # Find the card with this href and replace its SVG
    # Pattern: <a href="/forty/verhalen/{slug}/"...> ... <svg viewBox="0 0 360 180"...>...</svg> ... </a>
    # We need to replace just the SVG inside the .verhaal-card__visual div
    
    # Find the card link
    card_pattern = rf'(<a\s+href="/forty/verhalen/{re.escape(slug)}/"[^>]*>.*?<div class="verhaal-card__visual">)\s*<svg[^>]*>.*?</svg>'
    
    match = re.search(card_pattern, html, re.DOTALL)
    if match:
        old_section = match.group(0)
        new_section = match.group(1) + "\n                        " + new_svg
        html = html.replace(old_section, new_section)
        replaced += 1
        print(f"  ✓ {slug}")
    else:
        print(f"  MISS {slug} - card not found in HTML")

with open(filepath, "w", encoding="utf-8") as f:
    f.write(html)

print(f"\nReplaced {replaced}/9 card SVGs in {filepath}")
