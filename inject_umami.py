#!/usr/bin/env python3
"""Inject Umami analytics + CTA event tracking into all pages."""
import os
import re

UMAMI_SCRIPT = '''
    <script defer src="https://cloud.umami.is/script.js" data-website-id="418949bf-833f-4b75-b74e-f9d3f68b195e"></script>
    <script>
    document.addEventListener('click', function(e) {
      var link = e.target.closest('a');
      if (!link) return;
      var href = link.getAttribute('href') || '';
      var text = link.textContent.trim();
      // Track CTA clicks
      if (text.indexOf('Plan een gesprek') !== -1 || href.indexOf('calendly') !== -1 || href.indexOf('plan-een-gesprek') !== -1) {
        if (typeof umami !== 'undefined') umami.track('cta-plan-gesprek', { page: location.pathname });
      }
      // Track case clicks from overview
      if (href.indexOf('/cases/') !== -1 && location.pathname.indexOf('/cases/') !== -1 && !location.pathname.match(/cases\\/[a-z]/)) {
        if (typeof umami !== 'undefined') umami.track('case-click', { case: href });
      }
      // Track verhaal clicks from overview
      if (href.indexOf('/verhalen/') !== -1 && location.pathname.indexOf('/verhalen/') !== -1 && !location.pathname.match(/verhalen\\/[a-z]/)) {
        if (typeof umami !== 'undefined') umami.track('verhaal-click', { verhaal: href });
      }
    });
    </script>
'''

root = '.'
count = 0

for dirpath, dirnames, filenames in os.walk(root):
    # Skip hidden dirs, node_modules, etc
    dirnames[:] = [d for d in dirnames if not d.startswith('.') and d != 'node_modules' and d != '__pycache__']
    
    for f in filenames:
        if f != 'index.html':
            continue
        filepath = os.path.join(dirpath, f)
        
        with open(filepath, 'r', encoding='utf-8') as fh:
            html = fh.read()
        
        # Skip if already has umami
        if 'umami' in html:
            print(f"  SKIP {filepath} (already has umami)")
            continue
        
        # Skip if no </body> tag
        if '</body>' not in html:
            print(f"  SKIP {filepath} (no </body>)")
            continue
        
        # Inject before </body>
        html = html.replace('</body>', UMAMI_SCRIPT + '\n</body>')
        
        with open(filepath, 'w', encoding='utf-8') as fh:
            fh.write(html)
        
        count += 1
        print(f"  ✓ {filepath}")

print(f"\nDone! Injected Umami into {count} pages.")
