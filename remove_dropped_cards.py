#!/usr/bin/env python3
"""Remove the two dropped verhalen cards from the overview page."""
import re
import sys

filepath = "verhalen/index.html"

with open(filepath, "r", encoding="utf-8") as f:
    html = f.read()

original_len = len(html)

# Remove card: "Het opstellen van aannames"
# Match the full <a> card that contains this title
pattern1 = r'<a\s+href="/forty/verhalen/behavioral-design-principes/"[^>]*class="verhaal-card[^"]*"[^>]*data-type="analyse"[^>]*>.*?</a>'
html_new = re.sub(pattern1, '', html, count=1, flags=re.DOTALL)

if len(html_new) == len(html):
    print("WARNING: Could not find 'Het opstellen van aannames' card")
else:
    print(f"Removed 'Het opstellen van aannames' card ({len(html) - len(html_new)} chars)")

html = html_new

# Remove card: "Kleinste probleem, grootste frustratie"  
pattern2 = r'<a\s+href="/forty/verhalen/kies-en-ontwerp-je-experiment/"[^>]*class="verhaal-card[^"]*"[^>]*data-type="gesprek"[^>]*>.*?</a>'
html_new = re.sub(pattern2, '', html, count=1, flags=re.DOTALL)

if len(html_new) == len(html):
    print("WARNING: Could not find 'Kleinste probleem' card")
else:
    print(f"Removed 'Kleinste probleem' card ({len(html) - len(html_new)} chars)")

html = html_new

with open(filepath, "w", encoding="utf-8") as f:
    f.write(html)

print(f"\nDone! {original_len} -> {len(html)} chars ({original_len - len(html)} removed)")
