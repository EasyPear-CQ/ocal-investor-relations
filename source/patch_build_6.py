# -*- coding: utf-8 -*-
"""Patch 6 (26 Oct 2026): a flat review build. SITE_FLAT=1 writes every page as a root-level .html file
(why-ocal.html, news-2026-10-22-ocal-showroom.html) into ../site-review so the whole site can be published
as a single multi-file page for reviewers before the domain exists. Production build is unchanged."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
p = os.path.join(HERE, "build_site.py"); s = open(p, encoding="utf-8").read()

s = s.replace('OUT = os.path.normpath(os.path.join(HERE, "..", "site"))',
              'FLAT = os.environ.get("SITE_FLAT") == "1"\nOUT = os.path.normpath(os.path.join(HERE, "..", "site-review" if FLAT else "site"))')

old = '''    if path.startswith("[["):
        return "#"
    prefix = "../" * depth if depth else "./"'''
new = '''    if path.startswith("[["):
        return "#"
    if FLAT:
        q = path.strip("/")
        if q == "":
            return "index.html"
        if q.endswith(".html") or "." in q.split("/")[-1]:
            return q
        return q.replace("/", "-") + ".html"
    prefix = "../" * depth if depth else "./"'''
assert old in s; s = s.replace(old, new)

old = '''def depth_of(slug):
    return slug.strip("/").count("/") + (1 if slug.strip("/") else 0)'''
new = '''def depth_of(slug):
    if FLAT:
        return 0
    return slug.strip("/").count("/") + (1 if slug.strip("/") else 0)'''
assert old in s; s = s.replace(old, new)

old = '''    for pg in C.PAGES:
        out_path = (pg["slug"].strip("/") + "/index.html") if pg["slug"] != "/" else "index.html"
        write(out_path, render_page(pg))'''
new = '''    for pg in C.PAGES:
        if FLAT:
            out_path = "index.html" if pg["slug"] == "/" else pg["slug"].strip("/").replace("/", "-") + ".html"
        else:
            out_path = (pg["slug"].strip("/") + "/index.html") if pg["slug"] != "/" else "index.html"
        write(out_path, render_page(pg))'''
assert old in s; s = s.replace(old, new)
# copy assets into the flat output too
old = '''    write("404.html", not_found())'''
new = '''    if FLAT:
        import shutil
        src = os.path.normpath(os.path.join(HERE, "..", "site", "assets"))
        dst = os.path.join(OUT, "assets")
        if os.path.exists(src):
            shutil.copytree(src, dst, dirs_exist_ok=True)
    write("404.html", not_found())'''
assert old in s; s = s.replace(old, new)
open(p, "w", encoding="utf-8").write(s)
print("flat mode added")
