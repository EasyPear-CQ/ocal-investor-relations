# -*- coding: utf-8 -*-
"""Patch 5 (24 Oct 2026, QA pass): every title tag at or under 60 characters and every meta description at or under 155,
each still carrying the brand string and the ticker. Kept for the record."""
import ast, os, re
p = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'content.py')
s = open(p, encoding='utf-8').read()

NEW = {
    "/": ("OCAL Financial (TSXV: OCAL) Investor Relations",
          "OCAL Financial (TSXV: OCAL): the approval-first online car dealer with zero standing inventory. Stock, filings, operating metrics, news, alerts."),
    "/why-ocal/": ("Why Invest in OCAL Financial (TSXV: OCAL)",
                   "The investment case for OCAL: approval first, car second, zero standing inventory, audited revenue growth and a plan to copy one machine into new markets."),
    "/how-it-works/": ("How OCAL Works | OCAL Financial (TSXV: OCAL)",
                       "How OCAL sells and finances a used vehicle online: apply, qualify, approve, match through OPENLANE, deliver. Who carries the risk, how OCAL earns."),
    "/stock/": ("OCAL Stock: Price, Chart, Share Structure (TSXV: OCAL)",
                "OCAL share price and chart (TSXV: OCAL, Frankfurt: JC3), shares outstanding, warrants, options, escrow schedule and transfer agent."),
    "/financials/": ("OCAL Financial Reports and SEDAR+ Filings (TSXV: OCAL)",
                     "Audited statements, MD&A, interims and the Filing Statement with SEDAR+ links. FY2025 revenue $6.48M audited; FY2026 results due 29 December."),
    "/operating-metrics/": ("OCAL Operating Metrics (TSXV: OCAL)",
                            "Vehicles funded, average selling price, gross profit per vehicle and gross margin, published monthly under fixed definitions. Historical, unaudited."),
    "/news/": ("OCAL Financial News Releases (TSXV: OCAL)",
               "Every OCAL Financial news release since the TSXV listing on 21 July 2026, filed on SEDAR+ and distributed by Newsfile. Get releases by email."),
    "/news/2026-10-22-ocal-showroom/": ("OCAL Financial Introduces OCAL Showroom | News, 22 Oct 2026",
                                        "OCAL Financial (TSXV: OCAL) introduces OCAL Showroom, a live virtual view of sales activity, lender approvals and deal status."),
    "/events/": ("OCAL Financial Events and AGM (TSXV: OCAL)",
                 "OCAL Financial's AGM on 10 December 2026, filing deadlines, monthly operating updates and conferences, with materials posted the same day."),
    "/presentations/": ("OCAL Investor Presentation and Fact Sheet (TSXV: OCAL)",
                        "OCAL Financial's current investor presentation, one-page fact sheet, four-page brief and long-form briefing. Dated and versioned."),
    "/fact-sheet/": ("OCAL Financial Fact Sheet, October 2026 (TSXV: OCAL)",
                     "One-page OCAL fact sheet: audited FY2025 revenue $6.48M, zero standing inventory, 1,500+ funded deals, the five steps and the roll-out. Printable."),
    "/governance/": ("OCAL Financial Governance (TSXV: OCAL)",
                     "OCAL Financial's board of directors, audit and governance committees, policies, AGM materials, auditor, counsel and transfer agent."),
    "/leadership/": ("OCAL Financial Leadership and Board (TSXV: OCAL)",
                     "The people running OCAL Financial: CEO Mehdi Moghareh, Executive Chairman Matthew Friesen, CFO Terence Lee, the team and the board."),
    "/faq/": ("OCAL Financial Investor FAQ (TSXV: OCAL)",
              "Thirty investor questions answered plainly: is OCAL a broker, where the cars come from, who takes the credit risk, going concern, escrow, insiders."),
    "/contact/": ("Contact OCAL Investor Relations (TSXV: OCAL)",
                  "Contact OCAL investor relations: investors@ocal.ca, 1 (604) 687-7765, book a call with the founders, transfer agent details and email alerts."),
    "/subscribe/": ("OCAL Financial Email Alerts (TSXV: OCAL)",
                    "Every OCAL Financial news release, operating update and filing by email within the hour of distribution. Double opt-in, unsubscribe any time."),
    "/facts/": ("OCAL Financial Company Facts (TSXV: OCAL)",
                "Reference facts for OCAL Financial Inc.: legal name, TSXV and Frankfurt symbols, ISIN, CUSIP, LEI, head office, officers, auditor, transfer agent."),
    "/legal/": ("Legal Notices | OCAL Financial Investor Site",
                "Forward-looking information, non-IFRS measures, no offer of securities, third-party data, privacy and terms for the OCAL Financial investor site."),
}
for slug, (t, d) in NEW.items():
    assert len(t) <= 60, (slug, len(t)); assert len(d) <= 155, (slug, len(d))
    m = re.search(r'slug="%s",\n(.*?\n)*?    title="(.*?)",\n    description="(.*?)",' % re.escape(slug), s)
    assert m, slug
    block = m.group(0)
    new = block.replace('title="%s"' % m.group(2), 'title="%s"' % t).replace('description="%s"' % m.group(3), 'description="%s"' % d)
    s = s.replace(block, new, 1)
open(p, 'w', encoding='utf-8').write(s)
ast.parse(s)
print("titles and descriptions patched:", len(NEW))
