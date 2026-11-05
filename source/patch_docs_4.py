# -*- coding: utf-8 -*-
"""Patch 4 for build_docs.py: add document 08 (self-review and scorecard), the no-competitor rule in the wording guide,
the design note in the CQ handoff, and the index row. Kept for the record."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
p = os.path.join(HERE, "build_docs.py"); s = open(p, encoding="utf-8").read()

# wording guide: competitor rule row
s = s.replace('''        ["Em dashes, en dashes", "Commas, colons, periods, parentheses."],
    ], (W(2.8), W(4.0)))''', '''        ["Any named competitor (online retailers, dealer groups, lenders, other issuers) and any comparison to one", "Nothing. Industry statistics with a named source (Presidio-NCM, Cox, J.D. Power, TransUnion, Equifax, Angus Reid, Statistics Canada) carry the argument; other companies are never named or described on the investor site. Matthew's instruction, 23 October 2026."],
        ["Em dashes, en dashes", "Commas, colons, periods, parentheses."],
    ], (W(2.8), W(4.0)))''')

# CQ handoff: design section after hosting
s = s.replace('''    H.h("3. The pages: URL, title tag, meta description")''', '''    H.h("2a. Design: it matches ocalfinancial.ca")
    H.para("The investor site uses the live consumer site's design tokens, read from ocalfinancial.ca on 23 October 2026: Poppins body at 16px in #263340 on #FAFAFA; Outfit for headings, navigation, buttons and labels; Playfair Display italic for the accent word in hero headlines; navy #001240 panels and headings; green #017333 pill buttons (999px radius, 12px by 22px padding, 14px, weight 600); lime and mint accents for kickers; a white sticky header at 68px with the navy logo and a green pill; the dark #101510 footer at 72 percent white; 12px to 24px radii; the navy step cards with a small-caps step label. If the consumer site's tokens change, change them once in assets/css/style.css (the :root block) and the whole investor site follows. Fonts load from Google Fonts; self-host them if the consumer site does.")
    H.h("3. The pages: URL, title tag, meta description")''')

# index row in document 00
s = s.replace('''        ["site folder", "The website", "CQ",''', '''        ["08", "Self-review and scorecard", "Matthew", "The site scored against the 12 October 14-element checklist (the old page scored 38 of 100) as delivered and at go-live, against the ideas lists in the three research files, and an honest view of how it will rank in search and why."],
        ["site folder", "The website", "CQ",''')

# document 08
doc08 = '''
# =====================================================================================================
# 08 SELF-REVIEW AND SCORECARD
# =====================================================================================================
def doc_08():
    H.new_doc("INVESTOR SITE  ·  SELF-REVIEW AND SCORECARD", FOOT)
    H.band("Self-review and scorecard", "October 23, 2026  ·  the new site against the 12 October checklist and today's research")
    H.kicker("Scored the same way the old page was scored, by the same hand, with the same scepticism")
    H.para("On 12 October the live investor page scored 43 of 140 on a fourteen-element checklist built from the IR Magazine and Q4 best-investor-website criteria, NIRI and CIRI guidance and the TSX Venture issuer resources, reported as 38 of 100 after rounding for the quality of its FAQ and design. The same checklist is applied below to the new site twice: as delivered today, with 54 placeholders still open, and at go-live with every gate cleared. The second column is the one that matters and the first is the honest one.", size=10.5)
    H.stat_cards([("38", "old page, 12 October", "43 of 140 points"), ("71", "new site as delivered", "99 of 140; placeholders open, nothing live"), ("89", "at go-live", "124 of 140 with the six gates cleared"), ("95", "reachable by January", "with the first two monthly updates and the vendor fixes")])
    H.h("1. The fourteen elements")
    H.table(["#", "Element", "Old", "Now", "Go-live", "Why, and what is still missing"], [
        ["1", "Stock quote and chart", "3", "8", "9", "Live TradingView chart and mini overview, listings table with ISIN, CUSIP and WKN, TMX and Frankfurt links, text fallback. Missing: market cap and 52-week range as text (add from the first monthly update), and a sticky quote bar on every page if the budget ever allows a feed."],
        ["2", "Share structure", "1", "7", "9", "Full capitalization table, escrow total and release schedule, warrants by strike and expiry, options, fully diluted, July financing, insider line. Missing until Terence confirms: share counts per escrow tranche, CPC escrow dates."],
        ["3", "Financial reports", "0", "5", "9", "Three-year summary from the audited statements, the interim period, the going-concern answer, the reporting calendar, the $6.84M reconciliation. Missing: the five SEDAR+ document links and the profile URL (placeholders). At go-live every document is one click away."],
        ["4", "Presentation and fact sheet", "4", "5", "8", "A printable one-page fact sheet exists on the site itself, dated and versioned. Missing: the deck, brief and long-form PDFs (placeholders), and the deck must be refreshed on audited figures before it is posted. Video comes in November."],
        ["5", "Why invest", "4", "9", "9", "Eight numbered sections with a sourced number in each, a market table, the plan table under the legend with assumptions and risks beside it, no superlatives, no competitors. The one-point gap: a quarterly letter from the founders, which belongs on the site after the first operating update."],
        ["6", "News and filings", "4", "6", "9", "All twenty releases since listing listed with dates and categories, one release page in the new pattern with the s8.6 statement, RSS and a news sitemap. Missing: the other nineteen per-release pages (links go to Newsfile meanwhile) and the operating update section, which the first November release brings."],
        ["7", "Email alerts and subscription", "0", "4", "9", "Subscribe blocks on seven pages, double opt-in copy, CASL identification. Missing: the list itself and the form action (Has, this week), the welcome email and the first send."],
        ["8", "Events and webcasts", "0", "7", "8", "Calendar with the AGM, both filing deadlines, the first monthly update and the past events, Event schema. Missing: materials and a replay for each event, which exist only once events happen."],
        ["9", "Analyst, market maker and IR disclosure", "2", "9", "9", "No analyst coverage stated plainly with a promise to list any; Integral Wealth and Signal Capital named exactly as released. Nothing missing."],
        ["10", "Governance", "4", "6", "9", "Board with independence and committees, corporate information, SEDI founder holdings, AGM section, disclosure practice. Missing: the charters and policies as PDFs (Garrett confirms what is adopted) and the circular when filed."],
        ["11", "FAQ", "7", "9", "9", "Thirty questions, the three hard ones first, every answer dated or sourced, FAQPage schema, the inventory-on-the-balance-sheet answer the old page could not give. The gap: answers will need dates refreshed monthly."],
        ["12", "Contact and response", "5", "7", "9", "Named people, a one-business-day promise, the selective-disclosure policy, the transfer agent card, a separate path for customers. Missing: the booking link and Endeavor's contact details (placeholders)."],
        ["13", "AI and search readability", "2", "9", "9", "Static HTML on every page, Corporation schema with ticker, ISIN, CUSIP and LEI, unique titles carrying 'TSXV: OCAL', a facts page, llms.txt, real 404. The last point depends on data vendors outside the site."],
        ["14", "Consistency with the public record", "3", "8", "9", "Audited figures only, escrow and warrants from the exchange record, 1,250+ as released, the monthly metric definitions from the release program, no competitor claims, Matthew's title correct everywhere. Open: the plan table awaits Garrett's read, and the CTO wording follows the appointment release."],
        ["", "Total", "43", "99", "124", "Out of 140: 31 percent, 71 percent, 89 percent"],
    ], (W(0.3), W(1.5), W(0.4), W(0.4), W(0.5), W(3.7)), size=7.5)
    H.h("2. Against today's research")
    H.para("The three site reviews each ended with a ranked list of ideas. The count of each list that is on the new site, with what was left out and why:")
    H.table(["List", "On the site", "Left out, deliberately or for later"], [
        ["A. Canadian fintech, auto and TSXV sites (12 ideas)", "11", "A calendar-file download for events (cheap; CQ can add an .ics per event)."],
        ["B. US auto retail and marketplaces (12 ideas)", "9", "A quarterly shareholder letter in a fixed structure (after the first update), a Key Figures workbook with eight quarters (after the first two), an evergreen introduction deck refreshed each quarter (the deck is being refreshed on audited figures first)."],
        ["C. Best-in-class and award winners (10 ideas)", "8", "A permanent founders' letter page and shareholder Q&A archive (the FAQ absorbs questions for now), and a document matrix by quarter (there is one audited year; the matrix starts when there are rows to fill)."],
        ["Design: match the consumer site", "Done", "Tokens read from ocalfinancial.ca on 23 October: Poppins body, Outfit headings, Playfair italic accent, navy panels, green pill buttons, dark footer. One :root block carries them."],
        ["Content rule: no competitors", "Done", "Every named company is gone from the site. The argument rests on sourced industry statistics and OCAL's own record."],
    ], (W(2.2), W(0.9), W(3.7)), size=8)
    H.h("3. How it will rank, honestly")
    H.bullet("Brand queries ('OCAL Financial', 'OCAL stock', 'OCAL TSXV', 'OCAL share price', 'OCAL Financial investor relations').", "Today OCAL's own pages are absent from the top nine for all of them. The new site is a new domain with no history, so it does not rank on day one. What moves it: the 301 redirects carrying the old page's small authority, the link from the consumer site's navigation and footer, the investor URL at the foot of every wire release (Newsfile, Yahoo, Stockhouse and the aggregators then link to it), unique titles carrying the brand string, and the Corporation schema. Expectation: top three for 'OCAL Financial investor relations' within two to four weeks of go-live; top five for 'OCAL Financial' and 'OCAL stock' within 60 to 90 days, after the S&P Capital IQ and TMX descriptions are corrected and two or three releases have pointed to the site. 'OCAL share price' will keep showing the Indian company UCAL until the TMX, Yahoo and Google Finance records are right; that is vendor work, not site work.")
    H.bullet("Category queries ('asset-light car dealer stock', 'online car dealership stock Canada', 'used car financing company TSXV').", "Low volume, held by generic articles. The Why OCAL and How it works pages carry the phrases naturally and will rank for the long-tail forms over three to six months. Ranking first for the head terms needs explainer pages written as disclosure-safe editorial through the Lawson and CIRO path; proposed in the SEO plan, not built, because they are promotional content and need that review.")
    H.bullet("AI answer engines.", "The facts page, the FAQ and llms.txt give ChatGPT, Perplexity and Google's AI features a plain, consistent set of facts to cite. Until the eight stale vendor profiles are corrected, those engines will keep blending 'powersports and healthcare financing' into their answers, because that text appears on more sites than OCAL's own. The monthly five-prompt check in Has's handoff measures it.")
    H.bullet("What would push the checklist score from 89 toward 95 by January.", "Two monthly operating updates published on time with the history table filled; the deck refreshed on audited figures and posted; the charters posted; the first founders' letter; the escrow tranche counts; 250 confirmed subscribers; the S&P, TMX and Yahoo descriptions corrected; the per-release pages for the nineteen earlier releases.")
    H.h("4. What I would still criticize")
    H.bullet("Placeholders.", "Fifty-four. They are the right call (nothing unverified goes public) but the site is not finished until they are zero, and the four that matter most (SEDAR+ links, the form action, the booking link, Terence's October figures) sit with four different people.")
    H.bullet("A new domain.", "Matthew's decision, and a clean one, but it costs ranking time. The redirects and the consumer-site links are the mitigation; they must go live at the same moment as the domain.")
    H.bullet("The plan table.", "Publishing FY2027 to FY2030 figures on a public page is a bigger step than anything the old page took. The legend, assumptions and risks are beside it, and Garrett reads it first; if he cuts it, the page still stands.")
    H.bullet("Thin history.", "One audited year, one interim period, one release page in the new pattern. The site is built to fill as the record grows; today it shows the shape more than the depth.")
    H.bullet("Nothing is live.", "A score on a staging folder is a forecast. The acceptance checklist in document 01 is where it becomes a fact.")
    closing("REVIEWER")
    return save("%s 08 Investor site - self-review and scorecard (38 to 89).docx" % STAMP)

'''
s = s.replace("# =====================================================================================================\ndef main():", doc08 + "# =====================================================================================================\ndef main():")
s = s.replace("paths = [doc_00(), doc_01(), doc_02(), doc_03(), doc_04(), doc_05(), doc_06(), doc_07()]", "paths = [doc_00(), doc_01(), doc_02(), doc_03(), doc_04(), doc_05(), doc_06(), doc_07(), doc_08()]")
# research synthesis: record the no-competitor rule
s = s.replace('''    H.bullet("Superlatives and comparative claims.", "'No. 1', 'largest', 'industry-leading' rest on third-party rankings. Every comparative on the new site is sourced or absent.")''',
              '''    H.bullet("Superlatives and comparative claims.", "'No. 1', 'largest', 'industry-leading' rest on third-party rankings. Every comparative on the new site is sourced or absent.")
    H.bullet("Named competitors.", "The peer sites and the first draft of this site used named online retailers and dealer groups as the cautionary tale. Matthew's rule of 23 October: no competitor is named or described on the investor site. The argument now rests on industry statistics with a source and on OCAL's own record.")''')
open(p, "w", encoding="utf-8").write(s)
print("docs patched")
