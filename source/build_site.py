# -*- coding: utf-8 -*-
"""
Build the OCAL investor site (investors.ocal.ca) as static HTML from content.py.

    python -X utf8 build_site.py            -> writes ../site/ (relative links, opens from disk or any host)

Every page is index.html in its own folder, so the production URL is the folder path.
Also writes sitemap.xml, robots.txt, llms.txt, feed.xml, 404.html, site.webmanifest and PLACEHOLDERS.txt.
No framework, no build step for CQ: upload the site folder as-is, or port the HTML into the CMS page by page.
"""
import os, re, json, html, datetime, shutil
import content as C

HERE = os.path.dirname(os.path.abspath(__file__))
FLAT = os.environ.get("SITE_FLAT") == "1"
OUT = os.path.normpath(os.path.join(HERE, "..", "site-review" if FLAT else "site"))
BASE = C.SITE["base_url"]
TODAY = datetime.date(2026, 11, 4)
PLACEHOLDERS = []   # (page slug, text)

# ------------------------------------------------------------------ helpers
def esc(t):
    return html.escape(t, quote=True)

def rel(path, depth):
    """Site-absolute path ('/stock/') to a relative href for a page at the given folder depth."""
    if not path or path.startswith(("http", "mailto:", "javascript:", "#", "tel:")):
        return path
    if path.startswith("[["):
        return "#"
    if FLAT:
        q = path.strip("/")
        if q == "":
            return "index.html"
        if q.endswith(".html") or "." in q.split("/")[-1]:
            return q
        return q.replace("/", "-") + ".html"
    prefix = "../" * depth if depth else "./"
    p = path.lstrip("/")
    if p == "":
        return prefix
    if p.endswith("/"):
        return prefix + p
    return prefix + p

def depth_of(slug):
    if FLAT:
        return 0
    return slug.strip("/").count("/") + (1 if slug.strip("/") else 0)

def inline(t, slug, depth):
    """Escape, then apply **bold**, [text](url), [[placeholder]] and <em> passthrough."""
    t = esc(t)
    # restore the one tag we allow in content
    t = t.replace("&lt;em&gt;", "<em>").replace("&lt;/em&gt;", "</em>")
    def ph(m):
        PLACEHOLDERS.append((slug, m.group(1)))
        return '<span class="ph" title="To be confirmed or filled before go-live">[[' + m.group(1) + ']]</span>'
    t = re.sub(r"\[\[(.+?)\]\]", ph, t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    def link(m):
        href = rel(html.unescape(m.group(2)), depth)
        ext = ' target="_blank" rel="noopener"' if href.startswith("http") else ""
        return '<a href="%s"%s>%s</a>' % (esc(href), ext, m.group(1))
    t = re.sub(r"\[([^\]]+?)\]\(([^)]+?)\)", link, t)
    return t

def fmt_date(iso):
    d = datetime.date.fromisoformat(iso)
    return d.strftime("%-d %B %Y") if os.name != "nt" else d.strftime("%d %B %Y").lstrip("0")

# ------------------------------------------------------------------ CSS
CSS = r"""
:root{--navy:#001240;--navy2:#001240;--ink:#263340;--green:#017333;--green2:#0A8A40;--lime:#80B838;--mint:#8CD17D;--slate:#263340;--dark:#101510;--muted:#5F6B78;--border:#DDE3E8;--tint:#EEF5F0;--pale:#DFE5EE;--pale2:#AAB4C4;--bg:#FAFAFA;--card:#FFFFFF;--maxw:1180px;--r:12px;--r2:24px;--shadow:0 10px 30px -10px rgba(0,18,64,.18)}
*{box-sizing:border-box}
html{scroll-behavior:smooth;-webkit-text-size-adjust:100%}
body{margin:0;font-family:Poppins,system-ui,-apple-system,"Segoe UI",Roboto,Arial,sans-serif;color:var(--ink);background:var(--bg);font-size:16px;line-height:1.65}
img{max-width:100%;height:auto;display:block}
a{color:var(--green);text-decoration:none}
a:hover{text-decoration:underline}
h1,h2,h3,h4{font-family:Outfit,Poppins,system-ui,sans-serif;color:var(--navy);line-height:1.15;margin:0 0 .5em;font-weight:500;letter-spacing:-.01em}
h1{font-size:clamp(2.2rem,5vw,3.8rem);font-weight:500}
h2{font-size:clamp(1.6rem,3vw,2.4rem);margin-top:1.8em;font-weight:500}
h3{font-size:1.2rem;margin-top:1.4em;font-weight:600}
p{margin:0 0 1em}
.wrap{max-width:var(--maxw);margin:0 auto;padding:0 20px}
.kicker{display:block;font-family:Outfit,sans-serif;color:var(--green);font-size:.74rem;letter-spacing:.2em;text-transform:uppercase;font-weight:600;margin:2.4rem 0 .6rem}
.kicker.first{margin-top:0}
em{font-style:normal;color:var(--green)}
.hero em{font-family:"Playfair Display",Georgia,serif;font-style:italic;font-weight:500;color:var(--mint)}
/* ticker bar */
.tbar{background:var(--navy);color:rgba(255,255,255,.78);font-size:.78rem;font-family:Outfit,sans-serif}
.tbar .wrap{display:flex;align-items:center;justify-content:space-between;gap:12px;min-height:36px;flex-wrap:wrap;padding-top:4px;padding-bottom:4px}
.tbar a{color:#fff}
.tbar .ids{display:flex;gap:16px;align-items:center;flex-wrap:wrap}
.tbar .ids b{color:var(--mint);font-weight:600;letter-spacing:.06em}
.tbar .util{display:flex;gap:14px}
/* header */
header.site{background:rgba(250,250,250,.92);backdrop-filter:saturate(1.4) blur(10px);border-bottom:1px solid var(--border);position:sticky;top:0;z-index:50}
header.site .wrap{display:flex;align-items:center;justify-content:space-between;min-height:68px;gap:16px}
.logo img{height:30px;width:auto}
.logo span{display:block;font-family:Outfit,sans-serif;font-size:.6rem;letter-spacing:.22em;text-transform:uppercase;color:var(--muted);margin-top:3px;font-weight:600}
nav.main ul{list-style:none;margin:0;padding:0;display:flex;gap:2px;flex-wrap:wrap;align-items:center}
nav.main a{display:block;padding:9px 11px;color:var(--navy);font-family:Outfit,sans-serif;font-weight:500;font-size:.92rem;border-radius:999px}
nav.main a:hover,nav.main a.on{background:var(--tint);color:var(--green);text-decoration:none}
nav.main a.btn{background:var(--green);color:#fff;margin-left:8px;padding:11px 20px;font-size:.88rem;font-weight:600}
nav.main a.btn:hover{background:var(--navy)}
.navtoggle{display:none}
.burger{display:none;width:44px;height:44px;border:1px solid var(--border);border-radius:999px;background:#fff;cursor:pointer;align-items:center;justify-content:center}
.burger span{display:block;width:18px;height:2px;background:var(--navy);position:relative}
.burger span:before,.burger span:after{content:"";position:absolute;left:0;width:18px;height:2px;background:var(--navy)}
.burger span:before{top:-6px}.burger span:after{top:6px}
@media(max-width:1120px){
  .burger{display:flex}
  nav.main{display:none;position:absolute;left:0;right:0;top:100%;background:#fff;border-bottom:1px solid var(--border);box-shadow:var(--shadow)}
  nav.main ul{flex-direction:column;align-items:stretch;padding:10px 20px 16px}
  nav.main a{border-radius:10px}
  nav.main a.btn{margin:8px 0 0;text-align:center}
  .navtoggle:checked ~ nav.main{display:block}
}
/* hero */
.hero{background:var(--navy);color:#fff;position:relative;overflow:hidden}
.hero.home{background:var(--dark) center/cover no-repeat}
.hero.home:before{content:"";position:absolute;inset:0;background:linear-gradient(90deg,rgba(0,18,64,.985) 0%,rgba(0,18,64,.96) 55%,rgba(16,21,16,.86) 100%)}
.hero .wrap{position:relative;padding-top:64px;padding-bottom:64px}
.hero.home .wrap{padding-top:104px;padding-bottom:104px}
.hero .kicker{margin-top:0;color:var(--mint)}
.hero h1{color:#F4F3EE;max-width:880px;font-family:"Playfair Display",Georgia,serif;font-weight:400;font-size:clamp(2.4rem,5.6vw,4.2rem);line-height:1.08}
.hero.home h1{font-size:clamp(2.6rem,6.2vw,4.8rem)}
.hero p.hsub{color:rgba(255,255,255,.82);font-size:1.08rem;max-width:720px;margin:1.2rem 0 1.8rem}
.hero.home p.hsub{font-size:1.15rem}
.ctas{display:flex;gap:12px;flex-wrap:wrap}
.btn{display:inline-block;padding:12px 22px;border-radius:999px;font-family:Outfit,sans-serif;font-weight:600;font-size:.9rem;border:1.5px solid transparent;transition:.15s;line-height:1.3}
.btn.p{background:var(--green);color:#fff;border-color:var(--green)}
.btn.p:hover{background:var(--navy);border-color:var(--navy);text-decoration:none}
.btn.s{background:transparent;color:var(--navy);border-color:var(--pale2)}
.btn.s:hover{border-color:var(--navy);text-decoration:none}
.hero .btn.s,.cta .btn.s{color:#fff;border-color:rgba(255,255,255,.45)}
.hero .btn.s:hover,.cta .btn.s:hover{border-color:#fff;background:rgba(255,255,255,.08)}
.hero .btn.p,.cta .btn.p{background:var(--green);color:#fff;border-color:var(--green)}
.hero .btn.p:hover,.cta .btn.p:hover{background:#fff;color:var(--navy);border-color:#fff}
/* main */
main .wrap{padding-top:44px;padding-bottom:64px}
main .wrap > p,main .wrap > ul{max-width:820px}
main p.lead{font-size:1.15rem;color:var(--navy)}
/* kpis */
.kpis{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:16px;margin:1rem 0 2.2rem}
.kpi{background:var(--card);border:1px solid var(--border);border-radius:20px;padding:24px 24px 20px;box-shadow:0 1px 0 rgba(0,18,64,.03)}
.kpi .fig{font-family:Outfit,sans-serif;font-size:2.3rem;font-weight:700;color:var(--green);line-height:1.05;letter-spacing:-.02em}
.kpi .lab{font-family:Outfit,sans-serif;font-weight:600;color:var(--navy);margin-top:8px;font-size:.98rem}
.kpi .cap{color:var(--muted);font-size:.8rem;margin-top:4px;line-height:1.45}
/* cards */
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:16px;margin:1rem 0 2.2rem}
.card{display:block;background:var(--card);border:1px solid var(--border);border-radius:20px;padding:26px;color:var(--ink);transition:.18s;position:relative}
.card:hover{text-decoration:none;border-color:var(--green);box-shadow:var(--shadow);transform:translateY(-2px)}
.card .k{display:block;font-family:Outfit,sans-serif;color:var(--green);font-size:.7rem;letter-spacing:.2em;font-weight:600;text-transform:uppercase;margin-bottom:10px}
.card h3{margin:0 0 8px;font-size:1.12rem}
.card p{margin:0;font-size:.93rem}
.card .more{display:block;margin-top:14px;color:var(--green);font-family:Outfit,sans-serif;font-weight:600;font-size:.85rem}
/* bullets */
ul.bul{list-style:none;padding:0;margin:0 0 1.6rem}
ul.bul li{position:relative;padding-left:24px;margin-bottom:12px}
ul.bul li:before{content:"";position:absolute;left:0;top:.62em;width:9px;height:9px;border-radius:50%;background:var(--green)}
ul.bul b{color:var(--navy);font-family:Outfit,sans-serif;font-weight:600}
/* tables */
.tbl{overflow-x:auto;margin:1rem 0 .4rem;border:1px solid var(--border);border-radius:16px;background:#fff}
table{border-collapse:collapse;width:100%;font-size:.92rem;background:#fff}
th{background:var(--navy);color:#fff;text-align:left;padding:13px 16px;font-family:Outfit,sans-serif;font-size:.72rem;letter-spacing:.12em;text-transform:uppercase;font-weight:600;white-space:nowrap}
td{padding:13px 16px;border-top:1px solid var(--border);vertical-align:top}
tbody tr:nth-child(even) td{background:#F6F9F7}
td:first-child{font-weight:600;color:var(--navy);font-family:Outfit,sans-serif}
.tnote{font-size:.8rem;color:var(--muted);margin:0 0 1.8rem;max-width:860px}
/* steps: navy panels like the live site's step cards */
.steps{display:grid;grid-template-columns:repeat(auto-fit,minmax(190px,1fr));gap:14px;margin:1rem 0 2.2rem}
.step{background:var(--navy);color:#fff;border-radius:20px;padding:22px 20px}
.step .n{font-family:Outfit,sans-serif;font-size:.7rem;letter-spacing:.2em;text-transform:uppercase;color:var(--mint);font-weight:600}
.step .n:before{content:"Step "}
.step h3{margin:8px 0 8px;font-size:1.3rem;color:#fff;font-weight:500}
.step p{margin:0;font-size:.9rem;color:rgba(255,255,255,.8)}
/* faq */
.faq details{border:1px solid var(--border);border-radius:16px;margin-bottom:10px;background:#fff}
.faq summary{cursor:pointer;padding:16px 22px;font-family:Outfit,sans-serif;font-weight:600;color:var(--navy);list-style:none;display:flex;justify-content:space-between;gap:12px}
.faq summary::-webkit-details-marker{display:none}
.faq summary:after{content:"+";color:var(--green);font-size:1.4rem;line-height:1}
.faq details[open] summary:after{content:"\2212"}
.faq .a{padding:0 22px 18px;max-width:900px}
/* quote: navy panel */
.quote{background:var(--navy);color:#fff;padding:32px 36px;margin:1.6rem 0 2.2rem;border-radius:var(--r2);max-width:960px;border:0}
.quote p{font-family:"Playfair Display",Georgia,serif;font-style:italic;font-size:1.5rem;color:#fff;font-weight:400;margin:0 0 .6rem;line-height:1.35}
.quote cite{font-style:normal;color:var(--mint);font-size:.82rem;font-family:Outfit,sans-serif;letter-spacing:.08em;text-transform:uppercase}
/* cta band */
.cta{background:var(--navy);color:#fff;border-radius:var(--r2);padding:40px;margin:2.6rem 0 1rem;display:flex;justify-content:space-between;align-items:center;gap:24px;flex-wrap:wrap}
.cta h2{color:#fff;margin:0 0 .4rem;font-weight:500}
.cta p{color:rgba(255,255,255,.8);margin:0;max-width:620px}
/* note */
.note{font-size:.78rem;color:var(--muted);border-top:1px solid var(--border);padding-top:12px;margin:1.6rem 0 0;max-width:900px}
/* placeholders */
.ph{background:#FFF1A8;color:#5A4A00;padding:0 4px;border-radius:3px;font-weight:600}
/* subscribe */
.sub{background:#fff;border:1px solid var(--border);border-radius:20px;padding:28px;margin:2rem 0;display:flex;gap:20px;align-items:center;flex-wrap:wrap;justify-content:space-between}
.sub h3{margin:0 0 4px}
.sub p{margin:0;font-size:.9rem}
.sub form{display:flex;gap:8px;flex-wrap:wrap}
.sub input[type=email]{padding:12px 18px;border:1px solid var(--pale2);border-radius:999px;font:inherit;min-width:260px;background:#fff}
.sub button{padding:12px 22px;border:0;border-radius:999px;background:var(--green);color:#fff;font-family:Outfit,sans-serif;font-size:.9rem;font-weight:600;cursor:pointer}
.sub button:hover{background:var(--navy)}
.sub.large{flex-direction:column;align-items:flex-start}
.sub .fine{font-size:.75rem;color:var(--muted);width:100%}
/* news */
.news{list-style:none;padding:0;margin:0 0 1.5rem}
.news li{display:grid;grid-template-columns:130px 1fr auto;gap:16px;padding:14px 0;border-bottom:1px solid var(--border);align-items:baseline}
.news time{color:var(--muted);font-size:.85rem;white-space:nowrap}
.news a{color:var(--navy);font-family:Outfit,sans-serif;font-weight:500;font-size:1.02rem}
.news a:hover{color:var(--green)}
.chip{font-family:Outfit,sans-serif;font-size:.68rem;letter-spacing:.12em;text-transform:uppercase;color:var(--green);background:var(--tint);padding:4px 10px;border-radius:999px;white-space:nowrap;font-weight:600}
@media(max-width:640px){.news li{grid-template-columns:1fr}.news .chip{justify-self:start}}
.yearh{margin-top:2rem;font-size:.9rem;color:var(--muted);letter-spacing:.14em;text-transform:uppercase;font-weight:600}
/* events */
.events{list-style:none;padding:0;margin:0 0 1.5rem}
.events li{display:grid;grid-template-columns:92px 1fr;gap:18px;padding:16px 0;border-bottom:1px solid var(--border)}
.events .d{background:var(--navy);color:#fff;border-radius:14px;text-align:center;padding:10px 4px;height:fit-content;font-family:Outfit,sans-serif}
.events .d b{display:block;font-size:1.6rem;line-height:1.1;font-weight:600}
.events .d span{font-size:.68rem;letter-spacing:.12em;text-transform:uppercase;color:var(--mint)}
.events h3{margin:0 0 4px;font-size:1.08rem}
.events p{margin:0;font-size:.92rem}
.events li.past .d{background:var(--pale)}
.events li.past .d b,.events li.past .d span{color:var(--navy)}
/* team */
.team{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:18px;margin:1rem 0 2.2rem}
.member{background:#fff;border:1px solid var(--border);border-radius:20px;overflow:hidden}
.member img,.member .noimg{width:100%;aspect-ratio:1/1;object-fit:cover;background:var(--pale)}
.member .noimg{display:flex;align-items:center;justify-content:center;color:var(--navy);font-family:Outfit,sans-serif;font-size:3rem;font-weight:600}
.member .b{padding:18px 22px 24px}
.member h3{margin:0 0 2px;font-size:1.15rem}
.member .role{color:var(--green);font-family:Outfit,sans-serif;font-weight:600;font-size:.85rem;margin-bottom:10px}
.member p{font-size:.9rem;margin:0}
/* chart frame */
.chart{border:1px dashed var(--pale2);border-radius:16px;padding:24px;margin:1rem 0 1.5rem;background:#fff;color:var(--muted);font-size:.9rem}
.chart svg{width:100%;height:auto;display:block}
/* tradingview */
.tv{border:1px solid var(--border);border-radius:16px;overflow:hidden;margin:0 0 1.5rem;background:#fff;min-height:120px}
.tv .fallback{padding:14px 18px;font-size:.85rem;color:var(--muted)}
/* footer */
footer.site{background:var(--dark);color:rgba(255,255,255,.72);margin-top:40px;font-size:.88rem;font-family:Outfit,Poppins,sans-serif}
footer .cols{display:grid;grid-template-columns:1.4fr 1fr 1fr 1fr;gap:28px;padding:52px 0 28px}
footer h4{color:#fff;font-size:.72rem;letter-spacing:.18em;text-transform:uppercase;margin:0 0 12px;font-weight:600}
footer ul{list-style:none;margin:0;padding:0}
footer li{margin-bottom:8px}
footer a{color:rgba(255,255,255,.72)}
footer a:hover{color:#fff}
footer .brand img{height:28px;margin-bottom:14px}
footer .legal{border-top:1px solid rgba(255,255,255,.12);padding:20px 0 28px;font-size:.74rem;color:rgba(255,255,255,.55);line-height:1.6}
@media(max-width:860px){footer .cols{grid-template-columns:1fr 1fr}}
@media(max-width:520px){footer .cols{grid-template-columns:1fr}}
/* breadcrumb */
.crumbs{font-size:.78rem;color:var(--muted);margin:0 0 1.2rem;font-family:Outfit,sans-serif}
.crumbs a{color:var(--muted)}
/* print (fact sheet) */
@media print{
  .tbar,header.site,footer.site,.ctas,.sub,.crumbs,.cta{display:none!important}
  body{font-size:10.5pt;color:#222;background:#fff}
  .hero{background:#001240!important;-webkit-print-color-adjust:exact;print-color-adjust:exact}
  .hero .wrap{padding:22px 0}
  h1{font-size:22pt}
  main .wrap{padding-top:10px}
  .kpis{grid-template-columns:repeat(4,1fr);gap:8px}
  .kpi{padding:10px}.kpi .fig{font-size:16pt}
  .steps{grid-template-columns:repeat(5,1fr);gap:6px}.step{padding:8px}
  .tbl{break-inside:avoid}
  a{color:inherit}
}
"""

JS = r"""
// Minimal, dependency-free. External year in footer, and nothing else that could break if blocked.
document.addEventListener('DOMContentLoaded',function(){
  var y=document.querySelector('[data-year]'); if(y){y.textContent=new Date().getFullYear();}
});
"""

# ------------------------------------------------------------------ widgets
def tradingview(depth, kind="chart"):
    sym = C.SITE["tradingview_symbol"]
    if kind == "mini":
        cfg = {"symbol": sym, "width": "100%", "height": 220, "locale": "en", "dateRange": "3M", "colorTheme": "light", "isTransparent": False, "autosize": True, "largeChartUrl": BASE + "/stock/"}
        src = "https://s3.tradingview.com/external-embedding/embed-widget-mini-symbol-overview.js"
    else:
        cfg = {"symbol": sym, "interval": "D", "timezone": "America/Vancouver", "theme": "light", "style": "1", "locale": "en", "width": "100%", "height": 520, "allow_symbol_change": False, "hide_top_toolbar": False, "withdateranges": True, "range": "6M", "calendar": False, "support_host": "https://www.tradingview.com"}
        src = "https://s3.tradingview.com/external-embedding/embed-widget-advanced-chart.js"
    return ('<div class="tv"><div class="tradingview-widget-container"><div class="tradingview-widget-container__widget"></div>'
            '<script type="text/javascript" src="%s" async>%s</script></div>'
            '<div class="fallback">Chart by TradingView (delayed). Quote and trade history: <a href="%s" target="_blank" rel="noopener">TMX Money</a> · '
            '<a href="%s" target="_blank" rel="noopener">Frankfurt (JC3)</a>. Market data is supplied by third parties and may be delayed.</div></div>'
            % (src, json.dumps(cfg), C.SITE["tmx"], C.SITE["frankfurt"]))

def subscribe(depth, large=False, slug="/"):
    """Email alerts block. With SITE["form_action"] set to the list provider's form action URL (Brevo), the form posts there.
    Until Has pastes that one string, the Subscribe button opens an email to investors@ocal.ca carrying the address, so the
    block works from day one and no visitor meets a dead form."""
    action = C.SITE["form_action"]
    cls = "sub large" if large else "sub"
    sid = "l" if large else "s"
    label = '<label for="em-%s" style="position:absolute;left:-9999px">Email address</label>' % sid
    if action.startswith("http"):
        form = ('<form method="post" action="%s">%s<input type="email" id="em-%s" name="EMAIL" placeholder="you@example.com" required autocomplete="email">'
                '<button type="submit">Subscribe</button></form>' % (esc(action), label, sid))
        fine = "We send what we file and nothing else."
    else:
        form = ('<form method="post" action="mailto:%s?subject=Subscribe%%20to%%20OCAL%%20investor%%20alerts" enctype="text/plain">%s'
                '<input type="email" id="em-%s" name="Email" placeholder="you@example.com" required autocomplete="email">'
                '<button type="submit">Subscribe</button></form>' % (C.SITE["email"], label, sid))
        fine = "Subscribe opens an email to investors@ocal.ca with your address; reply to the confirmation to complete the double opt-in. We send what we file and nothing else."
    return ('<div class="%s" id="subscribe"><div><h3>Email alerts</h3><p>Every news release, monthly results release and filing, within the hour. One field, double opt-in, unsubscribe any time.</p></div>'
            '%s<div class="fine">Issued by OCAL Financial Inc., %s. %s</div></div>' % (cls, form, esc(C.SITE["address"]), fine))

def kpi_table(depth, slug):
    # 30 October 2026: per-vehicle figures stay off the site until the CFO reconciles the vehicle count; the widget now renders the audited totals.
    return audited_table(depth, slug)

def audited_table(depth, slug):
    rows = [
        ["Revenue", "$6,480,254", "$5,454,893", "+18.8%"],
        ["Of which vehicle sales", "$5,630,980", "$4,774,670", "+17.9%"],
        ["Of which finance, insurance and other", "$849,274", "$680,223", "+24.9%"],
        ["Gross profit", "$810,751", "$610,787", "+32.7%"],
        ["Gross margin", "12.5%", "11.2%", "+1.3 pts"],
        ["Of which gross profit from finance, insurance and other", "$701,727 (87% of gross profit)", "", ""],
        ["Vehicle write-downs included in cost of sales", "$353,094", "$67,243", ""],
        ["Operating expenses", "$1,114,195", "$1,234,843", "(9.8%)"],
        ["Operating loss", "($303,444)", "($624,056)", "Halved"],
        ["Net loss", "($322,090)", "($586,206)", "Down 45%"],
        ["Cash from operating activities", "$64,121", "($85,157)", "Positive"],
        ["Cash at year end", "$266,936", "$161,680", "+65%"],
    ]
    return render_table(["Fiscal year ended 31 August", "FY2025 (audited)", "FY2024 (audited)", "Change"], rows,
                        "From the audited financial statements for the year ended 31 August 2025 and their FY2024 comparatives (DMCL LLP), filed on SEDAR+. No per-vehicle figures are shown until the first monthly operating update; nothing from fiscal 2026 until the audited statements are filed.", slug, depth)

def deals_chart():
    bars = "".join('<rect x="%d" y="150" width="34" height="0" fill="#80B838"/>' % (40 + i * 46) for i in range(12))
    labels = "".join('<text x="%d" y="172" font-size="10" fill="#8B93A3" text-anchor="middle">M%d</text>' % (57 + i * 46, i + 1) for i in range(12))
    svg = ('<svg viewBox="0 0 620 190" role="img" aria-label="Funded vehicles per month, filled in as periods are reported">'
           '<line x1="30" y1="150" x2="600" y2="150" stroke="#AAB4C4"/><line x1="30" y1="20" x2="30" y2="150" stroke="#AAB4C4"/>'
           '<text x="34" y="30" font-size="11" fill="#8B93A3">Vehicles funded per month</text>' + bars + labels + '</svg>')
    return '<div class="chart">' + svg + '<p style="margin:10px 0 0">The chart fills in from the first reported period. Twelve trailing months are shown once available; nothing is projected.</p></div>'

def news_list(depth, slug, limit=None, full=False):
    items = C.NEWS[:limit] if limit else C.NEWS
    out = []
    if full:
        years = sorted({n[0][:4] for n in items}, reverse=True)
        for y in years:
            out.append('<h2 class="yearh">%s</h2><ul class="news">' % y)
            for d, h, u, cat in items:
                if d[:4] == y:
                    out.append(news_li(d, h, u, cat, depth, slug))
            out.append('</ul>')
        return "".join(out)
    out.append('<ul class="news">')
    for d, h, u, cat in items:
        out.append(news_li(d, h, u, cat, depth, slug))
    out.append('</ul><p><a href="%s"><strong>All news releases</strong></a></p>' % rel("/news/", depth))
    return "".join(out)

def news_li(d, h, u, cat, depth, slug):
    href = rel(u, depth)
    if u.startswith("[["):
        PLACEHOLDERS.append((slug, u.strip("[]")))
    ext = ' target="_blank" rel="noopener"' if href.startswith("http") else ""
    return '<li><time datetime="%s">%s</time><a href="%s"%s>%s</a><span class="chip">%s</span></li>' % (d, fmt_date(d), esc(href), ext, esc(h), esc(cat))

def events_list(depth, slug, full=False):
    up = [e for e in C.EVENTS if e[3] == "upcoming"]
    past = [e for e in C.EVENTS if e[3] == "past"]
    def li(e):
        d = datetime.date.fromisoformat(e[0])
        return ('<li class="%s"><div class="d"><b>%d</b><span>%s %d</span></div><div><h3>%s</h3><p>%s</p></div></li>'
                % (e[3], d.day, d.strftime("%b"), d.year, esc(e[1]), inline(e[2], slug, depth)))
    out = ['<h2 class="first">Upcoming</h2><ul class="events">'] + [li(e) for e in sorted(up)] + ['</ul>']
    if full:
        out += ['<h2>Past</h2><ul class="events">'] + [li(e) for e in sorted(past, reverse=True)] + ['</ul>']
    else:
        out.append('<p><a href="%s"><strong>All events and materials</strong></a></p>' % rel("/events/", depth))
    return "".join(out)

def filings(depth, slug):
    rows = [[f[0], f[1], f[2], "[Open on SEDAR+](%s)" % f[3]] for f in C.FILINGS]
    return render_table(["Document", "Type", "Note", "Link"], rows, "Each link opens SEDAR+. Search the issuer name OCAL Financial Inc. and open the document from the issuer profile, where the full filing history is kept.", slug, depth)

def team(depth, slug):
    out = ['<div class="team">']
    for name, role, photo, bio in C.TEAM:
        if photo and not photo.startswith("[["):
            fn = os.path.splitext(photo)[0].replace(" ", "-").lower() + ".webp"
            img = '<img src="%sassets/team/%s" alt="%s" width="480" height="480" loading="lazy">' % ("../" * depth if depth else "./", fn, esc(name))
        else:
            if photo.startswith("[["):
                PLACEHOLDERS.append((slug, photo.strip("[]")))
            img = '<div class="noimg" aria-hidden="true">%s</div>' % "".join(w[0] for w in name.split()[:2])
        out.append('<article class="member" itemscope itemtype="https://schema.org/Person">%s<div class="b"><h3 itemprop="name">%s</h3><div class="role" itemprop="jobTitle">%s</div><p>%s</p></div></article>'
                   % (img, esc(name), esc(role), inline(bio, slug, depth)))
    out.append('</div>')
    return "".join(out)

# ------------------------------------------------------------------ block renderers
def render_table(headers, rows, note, slug, depth):
    h = "".join("<th>%s</th>" % inline(x, slug, depth) for x in headers)
    body = "".join("<tr>%s</tr>" % "".join("<td>%s</td>" % inline(str(c), slug, depth) for c in r) for r in rows)
    out = '<div class="tbl"><table><thead><tr>%s</tr></thead><tbody>%s</tbody></table></div>' % (h, body)
    if note:
        out += '<p class="tnote">%s</p>' % inline(note, slug, depth)
    return out

def render_blocks(blocks, slug, depth):
    out = []
    first_kicker = True
    for b in blocks:
        t = b[0]
        if t == "kicker":
            out.append('<span class="kicker%s">%s</span>' % (" first" if first_kicker else "", esc(b[1]))); first_kicker = False
        elif t == "h2":
            out.append("<h2>%s</h2>" % inline(b[1], slug, depth))
        elif t == "h3":
            out.append("<h3>%s</h3>" % inline(b[1], slug, depth))
        elif t == "lead":
            out.append('<p class="lead">%s</p>' % inline(b[1], slug, depth))
        elif t == "p":
            out.append("<p>%s</p>" % inline(b[1], slug, depth))
        elif t == "note":
            out.append('<p class="note">%s</p>' % inline(b[1], slug, depth))
        elif t == "anchor":
            out.append('<span id="%s"></span>' % esc(b[1]))
        elif t == "kpis":
            out.append('<div class="kpis">' + "".join('<div class="kpi"><div class="fig">%s</div><div class="lab">%s</div><div class="cap">%s</div></div>' % (inline(f, slug, depth), inline(l, slug, depth), inline(c, slug, depth)) for f, l, c in b[1]) + "</div>")
        elif t == "bullets":
            out.append('<ul class="bul">' + "".join("<li>%s%s</li>" % (("<b>%s</b> " % inline(l, slug, depth)) if l else "", inline(bd, slug, depth)) for l, bd in b[1]) + "</ul>")
        elif t == "table":
            out.append(render_table(b[1], b[2], b[3], slug, depth))
        elif t == "steps":
            out.append('<div class="steps">' + "".join('<div class="step"><div class="n">%s</div><h3>%s</h3><p>%s</p></div>' % (esc(n), esc(ti), inline(bd, slug, depth)) for n, ti, bd in b[1]) + "</div>")
        elif t == "faq":
            out.append('<div class="faq">' + "".join('<details><summary>%s</summary><div class="a"><p>%s</p></div></details>' % (inline(q, slug, depth), inline(a, slug, depth)) for q, a in b[1]) + "</div>")
        elif t == "cards":
            cs = []
            for k, ti, bd, href in b[1]:
                h = rel(href, depth)
                if href.startswith("[["):
                    PLACEHOLDERS.append((slug, href.strip("[]")))
                ext = ' target="_blank" rel="noopener"' if h.startswith("http") else ""
                cs.append('<a class="card" href="%s"%s><span class="k">%s</span><h3>%s</h3><p>%s</p><span class="more">Read more</span></a>' % (esc(h), ext, esc(k), esc(ti), inline(bd, slug, depth)))
            out.append('<div class="cards">' + "".join(cs) + "</div>")
        elif t == "quote":
            out.append('<blockquote class="quote"><p>%s</p><cite>%s</cite></blockquote>' % (inline(b[1], slug, depth), esc(b[2])))
        elif t == "cta":
            btns = "".join(cta_btn(l, h, p, depth, slug) for l, h, p in b[3])
            out.append('<div class="cta"><div><h2>%s</h2><p>%s</p></div><div class="ctas">%s</div></div>' % (esc(b[1]), inline(b[2], slug, depth), btns))
        elif t == "widget":
            w = b[1]
            if w == "tradingview": out.append(tradingview(depth))
            elif w == "kpi-strip": out.append(tradingview(depth, "mini"))
            elif w == "subscribe": out.append(subscribe(depth, slug=slug))
            elif w == "subscribe-large": out.append(subscribe(depth, True, slug))
            elif w == "kpi-table": out.append(kpi_table(depth, slug))
            elif w == "audited-table": out.append(audited_table(depth, slug))
            elif w == "deals-chart": out.append(deals_chart())
            elif w == "news-list": out.append(news_list(depth, slug, limit=4))
            elif w == "news-list-full": out.append(news_list(depth, slug, full=True))
            elif w == "filings": out.append(filings(depth, slug))
            elif w == "events": out.append(events_list(depth, slug))
            elif w == "events-full": out.append(events_list(depth, slug, True))
            elif w == "team": out.append(team(depth, slug))
        elif t == "html":
            out.append(b[1])
    return "\n".join(out)

def cta_btn(label, href, primary, depth, slug):
    if href.startswith("[["):
        PLACEHOLDERS.append((slug, href.strip("[]")))
    h = rel(href, depth)
    ext = ' target="_blank" rel="noopener"' if h.startswith("http") else ""
    return '<a class="btn %s" href="%s"%s>%s</a>' % ("p" if primary else "s", esc(h), ext, esc(label))

# ------------------------------------------------------------------ schema
def schema_graph(pg, url):
    org = {
        "@type": "Corporation", "@id": BASE + "/#org",
        "name": "OCAL Financial", "legalName": C.SITE["legal_name"], "alternateName": ["OCAL", "OCAL Financial Inc."],
        "url": BASE + "/", "logo": BASE + "/assets/img/icon-512.png",
        "tickerSymbol": ["TSXV:OCAL", "FRA:JC3"],
        "foundingDate": "2021-04", "foundingLocation": "Vancouver, British Columbia, Canada",
        "description": "OCAL Financial Inc. (TSXV: OCAL) is a technology-enabled automotive financing and purchasing platform licensed in British Columbia and Alberta. Customers are approved by a lender first; the vehicle is then sourced through OPENLANE, OCAL's auction and sourcing channel, and delivered. OCAL holds no standing inventory and no consumer loans.",
        "address": {"@type": "PostalAddress", "streetAddress": "Suite 500, 885 Dunsmuir Street", "addressLocality": "Vancouver", "addressRegion": "BC", "postalCode": "V6C 1N5", "addressCountry": "CA"},
        "email": C.SITE["email"], "telephone": C.SITE["phone_tel"],
        "founder": [{"@type": "Person", "name": "Mehdi Moghareh", "jobTitle": "Chief Executive Officer"}, {"@type": "Person", "name": "Matthew Friesen", "jobTitle": "Executive Chairman and Director"}],
        "identifier": [{"@type": "PropertyValue", "propertyID": "LEI", "value": C.SITE["lei"]}, {"@type": "PropertyValue", "propertyID": "ISIN", "value": C.SITE["isin"]}, {"@type": "PropertyValue", "propertyID": "CUSIP", "value": C.SITE["cusip"]}, {"@type": "PropertyValue", "propertyID": "WKN", "value": C.SITE["wkn"]}],
        "sameAs": [C.SITE["tmx"], C.SITE["frankfurt"], C.SITE["linkedin"], C.SITE["consumer_site"], "https://finance.yahoo.com/quote/OCAL.V/", "https://search.gleif.org/#/record/" + C.SITE["lei"], "https://www.newsfilecorp.com/company/12553/OCAL-Financial", "https://www.tradingview.com/symbols/TSXV-OCAL/"],
        "parentOrganization": None,
    }
    org = {k: v for k, v in org.items() if v is not None}
    site = {"@type": "WebSite", "@id": BASE + "/#site", "url": BASE + "/", "name": C.SITE["name"], "publisher": {"@id": BASE + "/#org"}, "inLanguage": "en-CA"}
    crumbs = [{"@type": "ListItem", "position": 1, "name": "Investors", "item": BASE + "/"}]
    if pg["slug"] != "/":
        parts = pg["slug"].strip("/").split("/")
        acc = ""
        for i, p in enumerate(parts):
            acc += "/" + p
            name = pg.get("nav_label") or pg["hero"]["h1"] if i == len(parts) - 1 else p.capitalize()
            crumbs.append({"@type": "ListItem", "position": i + 2, "name": re.sub("<.*?>", "", name), "item": BASE + acc + "/"})
    page = {"@type": "WebPage", "@id": url + "#page", "url": url, "name": pg["title"], "description": pg["description"], "isPartOf": {"@id": BASE + "/#site"}, "about": {"@id": BASE + "/#org"}, "dateModified": TODAY.isoformat(), "inLanguage": "en-CA"}
    graph = [org, site, page, {"@type": "BreadcrumbList", "itemListElement": crumbs}]
    faqs = [q for b in pg["blocks"] if b[0] == "faq" for q in b[1]]
    if faqs:
        graph.append({"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"\[\[.*?\]\]", "", a).strip()}} for q, a in faqs]})
    if pg.get("release"):
        r = pg["release"]
        graph.append({"@type": "NewsArticle", "headline": re.sub("<.*?>", "", pg["hero"]["h1"]), "datePublished": r["date"], "dateModified": r["date"], "author": {"@id": BASE + "/#org"}, "publisher": {"@id": BASE + "/#org"}, "mainEntityOfPage": url, "description": pg["description"], "articleSection": r["category"]})
    if pg["slug"] == "/events/":
        for d, n, desc, st in C.EVENTS:
            if st == "upcoming":
                graph.append({"@type": "Event", "name": n, "startDate": d, "eventStatus": "https://schema.org/EventScheduled", "organizer": {"@id": BASE + "/#org"}, "description": re.sub(r"\[\[.*?\]\]", "", desc), "location": {"@type": "Place", "name": "Vancouver, BC and online"}, "eventAttendanceMode": "https://schema.org/MixedEventAttendanceMode"})
    if pg["slug"] == "/leadership/":
        for name, role, photo, bio in C.TEAM:
            graph.append({"@type": "Person", "name": name, "jobTitle": role, "worksFor": {"@id": BASE + "/#org"}})
    return json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=1)

# ------------------------------------------------------------------ page shell
def header(depth, slug):
    root = "../" * depth if depth else "./"
    nav = "".join('<li><a href="%s"%s>%s</a></li>' % (rel(h, depth), ' class="on"' if h == slug else "", esc(l)) for l, h in C.NAV)
    return f'''<div class="tbar"><div class="wrap"><div class="ids"><span><b>TSXV: OCAL</b></span><span><b>FSE: JC3</b></span><span>OCAL Financial Inc.</span><a href="{esc(C.SITE['tmx'])}" target="_blank" rel="noopener">Quote on TMX Money</a></div><div class="util"><a href="{rel('/subscribe/', depth)}">Email alerts</a><a href="{rel('/contact/', depth)}">Contact IR</a><a href="{esc(C.SITE['consumer_site'])}" target="_blank" rel="noopener">ocalfinancial.ca</a></div></div></div>
<header class="site"><div class="wrap"><a class="logo" href="{rel('/', depth)}" aria-label="OCAL Financial investor relations home"><img src="{root}assets/img/logo-navy.png" alt="OCAL Financial" width="800" height="189" style="height:34px;width:auto"><span>Investor relations</span></a>
<input type="checkbox" id="navtoggle" class="navtoggle" aria-hidden="true"><label for="navtoggle" class="burger" aria-label="Menu"><span></span></label>
<nav class="main" aria-label="Investor pages"><ul>{nav}<li><a class="btn" href="{rel('/subscribe/', depth)}">Email alerts</a></li></ul></nav></div></header>'''

def footer(depth):
    root = "../" * depth if depth else "./"
    cols = "".join('<div><h4>%s</h4><ul>%s</ul></div>' % (esc(t), "".join('<li><a href="%s">%s</a></li>' % (rel(h, depth), esc(l)) for l, h in links)) for t, links in C.FOOTER_COLS)
    return f'''<footer class="site"><div class="wrap"><div class="cols"><div class="brand"><img src="{root}assets/img/logo-white.png" alt="OCAL Financial" width="800" height="189" style="height:30px;width:auto"><p>The technology-enabled automotive financing and purchasing platform. We solve the problem first; the vehicle follows. TSXV: OCAL · FSE: JC3.</p><p><a href="mailto:{C.SITE['email']}">{C.SITE['email']}</a><br><a href="tel:{C.SITE['phone_tel']}">{C.SITE['phone']}</a><br>{esc(C.SITE['address'])}</p></div>{cols}</div>
<div class="legal"><p>OCAL Financial Inc., licensed motor dealer, VSA D50207 (British Columbia). AMVIC-licensed business, AMVIC B2036050 (Alberta). Consumer financing is on approved credit; the lender makes the final approval. Customer information is at <a href="{esc(C.SITE['consumer_site'])}">ocalfinancial.ca</a>.</p>
<p>This site contains forward-looking statements and unaudited supplementary measures; see <a href="{rel('/legal/', depth)}">Legal notices</a>. Nothing here is an offer of securities or investment advice. Continuous disclosure documents are filed on <a href="{esc(C.SITE['sedar'])}" target="_blank" rel="noopener">SEDAR+</a>. Neither TSX Venture Exchange nor its Regulation Services Provider (as that term is defined in policies of the TSX Venture Exchange) accepts responsibility for the adequacy or accuracy of this site.</p>
<p>© <span data-year>2026</span> OCAL Financial Inc. Updated {C.SITE['updated']}.</p></div></div></footer>
<script src="{root}assets/js/main.js" defer></script>'''

def hero(pg, depth, slug):
    h = pg["hero"]
    home = pg["slug"] == "/"
    ctas = "".join(cta_btn(l, u, p, depth, slug) for l, u, p in h.get("ctas", []))
    style = (' style="background-image:url(%sassets/img/hero.jpg)"' % ("../" * depth if depth else "./")) if home else ""
    tag = "h1"
    return f'''<section class="hero{' home' if home else ''}"{style}><div class="wrap"><span class="kicker">{esc(h['kicker'])}</span><{tag}>{inline(h['h1'], slug, depth)}</{tag}><p class="hsub">{inline(h['sub'], slug, depth)}</p>{'<div class="ctas">' + ctas + '</div>' if ctas else ''}</div></section>'''

def crumbs_html(pg, depth):
    if pg["slug"] == "/":
        return ""
    parts = pg["slug"].strip("/").split("/")
    out = ['<a href="%s">Investors</a>' % rel("/", depth)]
    acc = ""
    for i, p in enumerate(parts):
        acc += "/" + p
        if i == len(parts) - 1:
            out.append(esc(pg.get("nav_label") or re.sub("<.*?>", "", pg["hero"]["h1"])))
        else:
            out.append('<a href="%s">%s</a>' % (rel(acc + "/", depth), esc(p.capitalize())))
    return '<nav class="crumbs" aria-label="Breadcrumb">' + " › ".join(out) + "</nav>"

def render_page(pg):
    slug = pg["slug"]
    depth = depth_of(slug)
    root = "../" * depth if depth else "./"
    url = BASE + slug
    body = render_blocks(pg["blocks"], slug, depth)
    title = pg["title"]
    desc = pg["description"]
    return f'''<!doctype html>
<html lang="en-CA">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{esc(url)}">
<meta name="robots" content="index,follow,max-image-preview:large">
<meta property="og:type" content="{'article' if pg.get('release') else 'website'}">
<meta property="og:site_name" content="{esc(C.SITE['name'])}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{esc(url)}">
<meta property="og:image" content="{BASE}/assets/img/og-image.jpg">
<meta property="og:locale" content="en_CA">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{root}assets/img/favicon.ico" sizes="any">
<link rel="apple-touch-icon" href="{root}assets/img/apple-touch-icon.png">
<link rel="manifest" href="{root}site.webmanifest">
<link rel="alternate" type="application/rss+xml" title="OCAL Financial news releases" href="{BASE}/feed.xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600&family=Outfit:wght@400;500;600;700&family=Playfair+Display:ital,wght@0,400;0,500;1,400;1,500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{root}assets/css/style.css">
<script type="application/ld+json">{schema_graph(pg, url)}</script>
</head>
<body class="light">
{header(depth, slug)}
<main>
{hero(pg, depth, slug)}
<div class="wrap">
{crumbs_html(pg, depth)}
{body}
</div>
</main>
{footer(depth)}
</body>
</html>
'''

# ------------------------------------------------------------------ extras
def write(path, text):
    full = os.path.join(OUT, path.lstrip("/").replace("/", os.sep))
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)

def sitemap():
    urls = []
    for pg in C.PAGES:
        pr = "1.0" if pg["slug"] == "/" else ("0.9" if pg["slug"] in ("/why-ocal/", "/stock/", "/financials/", "/operating-metrics/", "/news/") else "0.7")
        urls.append("<url><loc>%s%s</loc><lastmod>%s</lastmod><changefreq>%s</changefreq><priority>%s</priority></url>" % (BASE, pg["slug"], TODAY.isoformat(), "weekly" if pr >= "0.9" else "monthly", pr))
    return '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "\n".join(urls) + "\n</urlset>\n"

def news_sitemap():
    # Google News sitemap: releases from the last two days only; CQ regenerates this on every release.
    items = []
    for d, h, u, cat in C.NEWS:
        if u.startswith("/"):
            items.append('<url><loc>%s%s</loc><news:news><news:publication><news:name>OCAL Financial</news:name><news:language>en</news:language></news:publication><news:publication_date>%s</news:publication_date><news:title>%s</news:title></news:news></url>' % (BASE, u, d, esc(h)))
    return '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:news="http://www.google.com/schemas/sitemap-news/0.9">\n' + "\n".join(items) + "\n</urlset>\n"

def rss():
    items = []
    for d, h, u, cat in C.NEWS:
        link = (BASE + u) if u.startswith("/") else u
        if link.startswith("[["):
            continue
        pub = datetime.datetime.fromisoformat(d + "T12:00:00").strftime("%a, %d %b %Y %H:%M:%S -0400")
        items.append("<item><title>%s</title><link>%s</link><guid>%s</guid><pubDate>%s</pubDate><category>%s</category></item>" % (esc(h), esc(link), esc(link), pub, esc(cat)))
    return ('<?xml version="1.0" encoding="UTF-8"?>\n<rss version="2.0"><channel><title>OCAL Financial news releases</title><link>%s/news/</link><description>News releases of OCAL Financial Inc. (TSXV: OCAL)</description><language>en-ca</language>\n' % BASE) + "\n".join(items) + "\n</channel></rss>\n"

def robots():
    return "User-agent: *\nAllow: /\nSitemap: %s/sitemap.xml\nSitemap: %s/news-sitemap.xml\n" % (BASE, BASE)

def llms():
    return f"""# OCAL Financial Inc. (TSXV: OCAL, FSE: JC3)

> OCAL Financial Inc. is a Canadian public company (TSX Venture Exchange: OCAL, since 21 July 2026; Frankfurt: JC3) that runs a technology-enabled automotive financing and purchasing platform. It solves the customer's problem first; the vehicle follows. A customer is approved by a lender first; OCAL, the licensed motor dealer of record, then buys the one vehicle that approval supports through OPENLANE, its auction and sourcing channel, and delivers it. OCAL holds no standing inventory and no consumer loans. It is not a broker.

Key facts (as of {C.SITE['facts_date']}):
- Legal name: OCAL Financial Inc. Head office: {C.SITE['address']}. Edmonton hub: {C.SITE['edmonton']}.
- Listings: TSX Venture Exchange OCAL (Tier 2). Frankfurt JC3, WKN {C.SITE['wkn']}, ISIN {C.SITE['isin']}, CUSIP {C.SITE['cusip']}.
- Fiscal year end 31 August. FY2025 (audited, DMCL LLP): revenue $6,480,254, up 18.8% from $5,454,893; gross profit $810,751 (12.5%), up from $610,787 (11.2%); operating expenses $1,114,195, down 9.8%; operating loss $303,444 (FY2024: $624,056); net loss $322,090 (FY2024: $586,206); cash from operations $64,121; cash at year end $266,936. Nothing from FY2026 until the audited statements are filed (due 29 December 2026).
- Funded vehicle transactions: more than 1,500 since 2021. {C.FUNDED_DEF}
- Repossession rate under one percent and about 99 percent of signed contracts funded, from the first funded transaction in 2021 to 30 September 2026 (management information, lender reporting; 3 November 2026 release).
- Lenders on the panel: RBC, Santander, iA Auto Finance, Eden Park, LendCare, Rifco and Iceberg.
- Roadmap: British Columbia and Alberta now; Manitoba next (dealer permit application under way, opening targeted for December 2026 when the permit is granted; also serves Saskatchewan and northwestern Ontario); Ontario registration under way, targeted for 2027, subject to registration and capital; then the Maritimes; the United States from 2028, after the Canadian roll-out. No forecast is published.
- Shares outstanding 36,667,803; about 48.3 million fully diluted; 23,638,104 shares in escrow; founders hold about 54%.
- Licensed motor dealer in British Columbia (VSA D50207) and Alberta (AMVIC B2036050). Operating since April 2021.
- Leadership: Mehdi Moghareh, Co-Founder and Chief Executive Officer; Matthew Friesen, Co-Founder, Executive Chairman and Director; Terence Lee, CPA, Chief Financial Officer; Ryan McDonald, Vice President of Sales; Hasneen Jalil leads technology and the demand engine. Independent directors Michael Stier (audit chair) and Robert Birmingham.
- Annual general and special meeting: 10 December 2026, 9:00 am Vancouver time, Suite 1600, 925 West Georgia Street, Vancouver; record date 2 November 2026.
- Investor documents (October 2026): {BASE}/presentations/ . Filed record: SEDAR+ ({C.SITE['sedar_profile']}).
- Auditor DMCL LLP. Transfer agent Endeavor Trust Corporation. Counsel Lawson Lundell LLP. Investor relations Signal Capital Advisors.
- Operating metrics (vehicles funded and delivered, average vehicle selling price, gross profit per vehicle, gross margin) are published in a monthly results release, the first on 10 November 2026 for October 2026, and kept at {BASE}/operating-metrics/
- Investor contact: {C.SITE['email']}, {C.SITE['phone']}.

Pages:
""" + "\n".join("- [%s](%s%s): %s" % (re.sub("<.*?>", "", p["hero"]["h1"]), BASE, p["slug"], p["description"]) for p in C.PAGES) + f"""

Customer site: {C.SITE['consumer_site']} (consumer financing is on approved credit; the lender makes the final approval).
Continuous disclosure: SEDAR+ ({C.SITE['sedar']}).
"""

def manifest():
    return json.dumps({"name": "OCAL Financial Investors", "short_name": "OCAL IR", "icons": [{"src": "/assets/img/icon-512.png", "sizes": "512x512", "type": "image/png"}], "theme_color": "#0A1432", "background_color": "#ffffff", "display": "browser", "start_url": "/"}, indent=1)

def not_found():
    pg = {"slug": "/404/", "title": "Page not found | OCAL Financial Investor Relations", "description": "The page you asked for is not here.", "nav_label": "Not found",
          "hero": {"kicker": "404", "h1": "That page is <em>not here.</em>", "sub": "The address may have changed when the investor site moved to investors.ocal.ca. Try one of the pages below.", "ctas": [("Investor home", "/", True), ("News releases", "/news/", False)]},
          "blocks": [("cards", [("STOCK", "Share information", "Chart, listings, capitalization and escrow.", "/stock/"), ("REPORTS", "Financial reports", "Audited statements, MD&A and SEDAR+ links.", "/financials/"), ("ASK", "Investor FAQ", "The hard questions, answered first.", "/faq/")])]}
    html_ = render_page(pg)
    # 404 lives at the root and must use root-relative asset paths; it is rendered at depth 1, so fix the prefix
    return html_.replace('href="../', 'href="/').replace('src="../', 'src="/').replace("url(../", "url(/")

# ------------------------------------------------------------------ documents
def copy_documents():
    """Copy the investor documents listed in content.DOCUMENTS from the IR folder into site/assets/documents (never deletes).
    The flat review build copies the whole site/assets tree afterwards, so site-review carries the same files."""
    if FLAT:
        return
    dst = os.path.join(OUT, "assets", "documents")
    os.makedirs(dst, exist_ok=True)
    for _k, _t, _b, fn in C.DOCUMENTS:
        src = os.path.join(C.DOCUMENTS_SOURCE, fn)
        if os.path.exists(src):
            shutil.copy2(src, os.path.join(dst, fn))
            print("document:", fn)
        else:
            print("document MISSING in the IR folder (link kept, copy when it exists):", fn)

# ------------------------------------------------------------------ main
def main():
    os.makedirs(OUT, exist_ok=True)
    os.makedirs(os.path.join(OUT, "assets", "css"), exist_ok=True)
    os.makedirs(os.path.join(OUT, "assets", "js"), exist_ok=True)
    write("assets/css/style.css", CSS.strip() + "\n")
    write("assets/js/main.js", JS.strip() + "\n")
    copy_documents()
    for pg in C.PAGES:
        if FLAT:
            out_path = "index.html" if pg["slug"] == "/" else pg["slug"].strip("/").replace("/", "-") + ".html"
        else:
            out_path = (pg["slug"].strip("/") + "/index.html") if pg["slug"] != "/" else "index.html"
        write(out_path, render_page(pg))
    if FLAT:
        import shutil
        src = os.path.normpath(os.path.join(HERE, "..", "site", "assets"))
        dst = os.path.join(OUT, "assets")
        if os.path.exists(src):
            shutil.copytree(src, dst, dirs_exist_ok=True)
    write("404.html", not_found())
    write("sitemap.xml", sitemap())
    write("news-sitemap.xml", news_sitemap())
    write("feed.xml", rss())
    write("robots.txt", robots())
    write("llms.txt", llms())
    write("site.webmanifest", manifest())
    # placeholders report
    seen = []
    for slug, t in PLACEHOLDERS:
        if (slug, t) not in seen:
            seen.append((slug, t))
    with open(os.path.join(HERE, "PLACEHOLDERS.txt"), "w", encoding="utf-8") as f:
        f.write("Placeholders to fill or confirm before go-live (%d). Generated %s.\n\n" % (len(seen), TODAY.isoformat()))
        for slug, t in seen:
            f.write("%-32s %s\n" % (slug, t))
    # dash check across output
    bad = []
    for root, _, files in os.walk(OUT):
        for fn in files:
            if fn.endswith((".html", ".txt", ".xml")):
                s = open(os.path.join(root, fn), encoding="utf-8").read()
                if "—" in s or "–" in s:
                    bad.append(fn)
    print("pages:", len(C.PAGES), "| placeholders:", len(seen), "| dash violations:", bad or "none")

if __name__ == "__main__":
    main()
