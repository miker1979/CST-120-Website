from pathlib import Path

OLD = '''<div class="location-card-body"><div class="d-flex justify-content-between align-items-start"><span class="location-number">02</span><span class="location-status">Finale location</span></div><h3>Gold King Mine &amp; Ghost Town / Haynes</h3><p>The story ultimately returns to the historical Haynes site for the binding attempt and the final outcome.</p></div>'''
NEW = '''<div class="location-card-body"><div class="d-flex justify-content-between align-items-start"><span class="location-number">02</span><span class="location-status">Main investigation</span></div><h3>Gold King Mine &amp; Ghost Town / Haynes</h3><p>A major mining-history location connected to the deeper underground investigation. Its full importance is intentionally left for the game to reveal.</p></div>'''

changed = []
for name in ("arizona-paranormal.html", "arizona-paranormal-v2.html"):
    path = Path(name)
    text = path.read_text(encoding="utf-8")
    if OLD in text:
        path.write_text(text.replace(OLD, NEW, 1), encoding="utf-8")
        changed.append(name)

print("Updated:", ", ".join(changed) if changed else "nothing")
