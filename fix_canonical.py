#!/usr/bin/env python3
"""Fix canonical URL on verhalen overview page."""

filepath = "verhalen/index.html"

with open(filepath, "r", encoding="utf-8") as f:
    html = f.read()

# Fix canonical from forty.nl to github pages
old = 'https://www.forty.nl/verhalen'
new = 'https://janwillemvanbeek-ctrl.github.io/forty/verhalen/'
html = html.replace(old, new)

with open(filepath, "w", encoding="utf-8") as f:
    f.write(html)

print(f"✓ Canonical updated: {old} → {new}")
