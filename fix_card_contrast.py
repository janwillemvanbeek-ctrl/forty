#!/usr/bin/env python3
"""Add border and contrast to verhaal cards on overview page."""

filepath = "verhalen/index.html"

with open(filepath, "r", encoding="utf-8") as f:
    html = f.read()

# Add card styling - find the existing .verhaal-card style and add border
# We need to inject CSS that gives cards a visible border and the visual a warmer bg

inject_css = """
    <style>
      .verhaal-card { border: 1px solid #e7e5e4; border-radius: 12px; overflow: hidden; }
      .verhaal-card__visual { background: #f5f0ea !important; }
    </style>
"""

# Insert before </head>
html = html.replace("</head>", inject_css + "</head>")

with open(filepath, "w", encoding="utf-8") as f:
    f.write(html)

print("✓ Card contrast styling added to verhalen/index.html")
