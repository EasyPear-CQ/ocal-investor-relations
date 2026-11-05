# -*- coding: utf-8 -*-
"""
patch_build_7_turnkey_nov2026.py (4 November 2026): build_site.py for the turnkey rebuild.
  - TODAY 2026-11-04; schema and llms.txt without "exclusive" (Garrett Lee, 31 October 2026); llms roadmap and metrics lines;
  - subscribe(): a working email-request fallback until Has pastes the Brevo form action into SITE["form_action"];
  - filings(): every link opens SEDAR+ with a clear label.
Backup: build_site_2026-11-04 (pre turnkey rebuild).py.bak
"""
import io, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(HERE, "build_site.py")
src = io.open(PATH, encoding="utf-8").read()
N = 0
def rep(old, new):
    global src, N
    c = src.count(old)
    if c != 1:
        print("REPLACE FAILED (%d found): %s" % (c, old[:90])); sys.exit(1)
    src = src.replace(old, new); N += 1

rep("TODAY = datetime.date(2026, 10, 30)", "TODAY = datetime.date(2026, 11, 4)")

rep('''def subscribe(depth, large=False, slug="/"):
    action = C.SITE["form_action"]
    ph = inline("[[Brevo or Mailchimp form action URL]]", slug, depth) if action.startswith("[[") else ""
    cls = "sub large" if large else "sub"
    return ('<div class="%s" id="subscribe"><div><h3>Email alerts</h3><p>Every news release, operating update and filing, within the hour. One field, double opt-in, unsubscribe any time.</p></div>'
            '<form method="post" action="%s" onsubmit="return this.action.indexOf(\\'[[\\')<0">'
            '<label for="em-%s" class="visually-hidden" style="position:absolute;left:-9999px">Email address</label>'
            '<input type="email" id="em-%s" name="EMAIL" placeholder="you@example.com" required autocomplete="email">'
            '<button type="submit">Subscribe</button></form>'
            '<div class="fine">Issued by OCAL Financial Inc., %s. We send what we file and nothing else. %s</div></div>'
            % (cls, esc(action if not action.startswith("[[") else "#"), "l" if large else "s", "l" if large else "s", esc(C.SITE["address"]), ph))''',
'''def subscribe(depth, large=False, slug="/"):
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
            '%s<div class="fine">Issued by OCAL Financial Inc., %s. %s</div></div>' % (cls, form, esc(C.SITE["address"]), fine))''')

rep('''    rows = [[f[0], f[1], f[2], "[Download](%s)" % f[3] if not f[3].startswith("[[") else f[3]] for f in C.FILINGS]
    return render_table(["Document", "Type", "Note", "Link"], rows, "Direct links go to the document on SEDAR+. The full filing history is on OCAL's SEDAR+ profile.", slug, depth)''',
'''    rows = [[f[0], f[1], f[2], "[Open on SEDAR+](%s)" % f[3]] for f in C.FILINGS]
    return render_table(["Document", "Type", "Note", "Link"], rows, "Each link opens SEDAR+. Search the issuer name OCAL Financial Inc. and open the document from the issuer profile, where the full filing history is kept.", slug, depth)''')

rep('''the vehicle is then sourced through OPENLANE, OCAL's exclusive auction and sourcing channel, and delivered.''',
'''the vehicle is then sourced through OPENLANE, OCAL's auction and sourcing channel, and delivered.''')

rep('''through OPENLANE, its exclusive auction and sourcing channel, and delivers it. OCAL holds no standing inventory and no consumer loans. It is not a broker.''',
'''through OPENLANE, its auction and sourcing channel, and delivers it. OCAL holds no standing inventory and no consumer loans. It is not a broker.''')
rep('''- Roadmap: Manitoba dealer licence application filed; Ontario registration in progress, targeted for 2027, subject to registration and capital; then the Maritimes; United States from 2028, after the Canadian roll-out. No forecast is published.''',
'''- Funded vehicle transactions: more than 1,500 since 2021. {C.FUNDED_DEF}
- Repossession rate under one percent and about 99 percent of signed contracts funded, from the first funded transaction in 2021 to 30 September 2026 (management information, lender reporting; 3 November 2026 release).
- Lenders on the panel: RBC, Santander, iA Auto Finance, Eden Park, LendCare, Rifco and Iceberg.
- Roadmap: British Columbia and Alberta now; Manitoba next (dealer permit application under way, opening targeted for December 2026 when the permit is granted; also serves Saskatchewan and northwestern Ontario); Ontario registration under way, targeted for 2027, subject to registration and capital; then the Maritimes; the United States from 2028, after the Canadian roll-out. No forecast is published.''')
rep('''- Leadership: Mehdi Moghareh, Co-Founder and Chief Executive Officer; Matthew Friesen, Co-Founder, Executive Chairman and Director; Terence Lee, CPA, Chief Financial Officer; Hasneen Jalil leads technology and the demand engine. Independent directors Michael Stier (audit chair) and Robert Birmingham.''',
'''- Leadership: Mehdi Moghareh, Co-Founder and Chief Executive Officer; Matthew Friesen, Co-Founder, Executive Chairman and Director; Terence Lee, CPA, Chief Financial Officer; Ryan McDonald, Vice President of Sales; Hasneen Jalil leads technology and the demand engine. Independent directors Michael Stier (audit chair) and Robert Birmingham.
- Annual general and special meeting: 10 December 2026, 9:00 am Vancouver time, Suite 1600, 925 West Georgia Street, Vancouver; record date 2 November 2026.''')
rep('''- Operating metrics (vehicles funded, average vehicle price, gross profit per vehicle, gross margin per vehicle) are published with every news release: {BASE}/operating-metrics/''',
'''- Operating metrics (vehicles funded and delivered, average vehicle selling price, gross profit per vehicle, gross margin) are published in a monthly results release, the first on 10 November 2026 for October 2026, and kept at {BASE}/operating-metrics/''')

io.open(PATH, "w", encoding="utf-8", newline="\n").write(src)
print("build_site.py patched: %d edits" % N)
