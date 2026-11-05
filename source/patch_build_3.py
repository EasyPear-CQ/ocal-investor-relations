# -*- coding: utf-8 -*-
"""Patch 3 for build_site.py and build_docs.py: align the KPI block, the wording guide definitions and document 04
with the release program rebuilt the same day. Kept for the record."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))

# ---- build_site.py: the home and metrics KPI block
p = os.path.join(HERE, "build_site.py"); s = open(p, encoding="utf-8").read()
old = '''    rows = [
        ["Vehicles funded", "[[units]]", "[[units, prior year period]]"],
        ["Average vehicle price", "[[$]]", "[[$]]"],
        ["Gross profit per vehicle", "[[$]]", "[[$]]"],
        ["Gross margin per vehicle", "[[%]]", "[[%]]"],
    ]
    return render_table(["Metric", "[[Period ended ...]]", "Same period, prior year"], rows,
                        "Unaudited management information under the definitions on the Operating metrics page; confirmed by the CFO from the ledger before release. Updated with every news release.", slug, depth)'''
new = '''    rows = [
        ["Vehicles funded and delivered", "[[units]]", "[[units]]"],
        ["Average vehicle selling price", "[[$]]", "[[$]]"],
        ["Deal gross profit per vehicle (management basis), of which vehicle margin and finance, insurance and protection income", "[[$ ($ + $)]]", "[[$ ($ + $)]]"],
        ["Gross profit per vehicle (IFRS basis)", "[[$]]", "[[$]]"],
        ["Gross margin", "[[%]]", "[[%]]"],
    ]
    return render_table(["Metric", "[[October 2026]]", "[[September 2026]]"], rows,
                        "Approximate monthly figures; unaudited management information under the definitions on the Operating metrics page, confirmed by the CFO from the ledger before release. Updated with every monthly operating update.", slug, depth)'''
assert old in s; s = s.replace(old, new); open(p, "w", encoding="utf-8").write(s)

# ---- build_docs.py: definitions in document 03, document 04 as a companion, document 00 row
p = os.path.join(HERE, "build_docs.py"); s = open(p, encoding="utf-8").read()
old = '''    H.table(["Metric", "Definition"], [
        ["Vehicles funded", "The number of retail vehicle sale contracts for which the lender advanced funds to OCAL in the period. A deal counts once, in the period the lender funds it, regardless of when the contract was signed or the vehicle delivered."],
        ["Average vehicle price", "Total retail vehicle sale price of vehicles funded in the period, before taxes and before protection products, divided by vehicles funded."],
        ["Gross profit per vehicle", "Revenue recognized on vehicles funded in the period (vehicle sale price, lender reserve and program incentives, protection products, delivery and permitted fees) less the cost of the vehicle including reconditioning, transport and auction fees, divided by vehicles funded. Before commissions, media and overhead."],
        ["Gross margin per vehicle", "Gross profit per vehicle divided by total revenue per vehicle funded, as a percentage."],
        ["Period", "Calendar month or fiscal quarter: Matthew and Terence decide once before the first release and keep it. Fiscal quarters end 30 November, 28 February, 31 May and 31 August. Each release shows the period and the same period a year earlier."],
    ], (W(1.6), W(5.2)))'''
new = '''    H.table(["Metric", "Definition (the release program's block, 23 October 2026)"], [
        ["Vehicles funded and delivered", "Retail vehicle sale contracts funded by a lender and delivered to the customer in the calendar month. Counted once, in the month the lender funds it."],
        ["Average vehicle selling price", "Vehicle sales revenue in the month divided by vehicles funded and delivered, before taxes and protection products."],
        ["Deal gross profit per vehicle (management basis)", "Gross profit on the vehicle plus finance, insurance and protection product income, per funded vehicle, before inventory write-downs and before the auction, reconditioning and transport costs that IFRS places in cost of sales. Split into vehicle margin and finance, insurance and protection income. Non-IFRS; management information."],
        ["Gross profit per vehicle (IFRS basis)", "Gross profit as reported in the financial statements for the month, divided by vehicles funded and delivered, with the items making up the difference from the deal basis stated beside it. FY2025 audited: about $4,100 after $353,094 of write-downs, about $5,900 before."],
        ["Gross margin", "Gross profit (IFRS basis) as a percentage of total revenue in the month. FY2025 audited: 12.5 percent."],
        ["Period and cadence", "Calendar month; first release after the month closes; October 2026 first; each figure beside the prior month; monthly figures 'approximately'; once started, the series continues in weak months. Break-even appears only as the month's arithmetic ('fixed operating costs were equal to the contribution from about 28 funded vehicles'), never as a target, and only if Lawson keeps it."],
    ], (W(1.6), W(5.2)))
    H.para("Master source: OCAL\\\\Press Releases\\\\02 Scheduled\\\\00 Release program 2026-10-23 - calendar, operating update block and drafting notes (internal).md. Terence settles the exact definitions once before the October update; they then never change, and the site's Operating metrics page is updated to match in the same rebuild.", size=8.5, color=H.MUTED)'''
assert old in s; s = s.replace(old, new)

# document 04 becomes the companion
start = s.index("def doc_04():"); end = s.index("# =====================================================================================================\n# 05 SEO")
new04 = '''def doc_04():
    H.new_doc("OPERATING UPDATE  ·  SITE COMPANION TO THE RELEASE PROGRAM", FOOT)
    H.band("Operating update: site companion", "October 23, 2026  ·  how the monthly block appears on investors.ocal.ca")
    H.kicker("The master template lives with the release program; this is the site side of it")
    H.para("The news release structure, the ten-release calendar and the operating update block were rebuilt on 23 October 2026 in the release program (OCAL\\\\Press Releases\\\\02 Scheduled, notes file 00; generator build_release_program_oct2026.py). This document does not repeat them. It shows how the block lands on the investor site, how a release becomes a page, and what Terence fills in on sheet 04a so the release, the site and the email carry the same numbers on the same day.", size=10.5)
    H.h("1. Where the block appears on the site")
    H.table(["Place", "What is shown", "Updated"], [
        ["Home page, 'Operating update' section", "The latest month's table: vehicles funded and delivered, average selling price, deal gross profit per vehicle (split), gross profit per vehicle on the IFRS basis, gross margin; prior month beside each", "Same day as the release"],
        ["Operating metrics page, 'Latest period'", "The same table", "Same day"],
        ["Operating metrics page, 'History'", "One row per month, plus the fiscal 2025 audited row; the chart of vehicles funded per month fills in from the first month", "Same day"],
        ["Operating metrics page, 'Definitions, fixed'", "The definitions exactly as settled with Terence and Lawson; the non-IFRS note", "Only if a definition changes, which it should not"],
        ["Release page (/news/YYYY-MM-DD-slug/)", "The release as distributed, including its operating update section and the definitions sentence", "When the wire has carried it"],
        ["Email to the list", "Headline, first two paragraphs, the table, links to the release page and SEDAR+", "Within the hour of the wire"],
    ], (W(2.0), W(3.4), W(1.4)))
    H.h("2. The block as it reads on the site (placeholders until Terence's figures)")
    H.table(["Metric", "October 2026", "September 2026"], [
        ["Vehicles funded and delivered", "[X]", "[X]"],
        ["Average vehicle selling price", "$[X]", "$[X]"],
        ["Deal gross profit per vehicle (management basis), of which vehicle margin and finance, insurance and protection income", "$[X] ($[X] + $[X])", "$[X] ($[X] + $[X])"],
        ["Gross profit per vehicle (IFRS basis)", "$[X]", "$[X]"],
        ["Gross margin", "[X]%", "[X]%"],
    ], (W(3.6), W(1.6), W(1.6)))
    H.para("Approximate monthly figures; unaudited management information; definitions on the Operating metrics page; confirmed by the CFO from the ledger before release. " + C.NON_IFRS_NOTE, size=8.5)
    H.h("3. How a release becomes a page")
    H.numbered("Wait for the wire.", "Nothing is posted before Newsfile has distributed it.", restart=True)
    H.numbered("Add the release to content.py.", "One line in NEWS (date, headline, path, category) and one page entry on the pattern of the 22 October sample page; the description is the first sentence after the dateline.")
    H.numbered("Add the month to the metrics.", "The confirmed figures go into the home-page block and the history table (content.py, same change).")
    H.numbered("Rebuild and deploy.", "build_site.py updates the news list, RSS, sitemap and news sitemap; CQ deploys and pings IndexNow and Search Console.")
    H.numbered("Email and LinkedIn.", "Has sends the list email within the hour; the corporate LinkedIn post carries the headline and the link.")
    H.h("4. Who does what, each month")
    H.table(["Step", "Owner", "When"], [
        ["Pull and confirm the month's figures on sheet 04a", "Terence", "First two business days after month end"],
        ["Draft the operating update release from the program's content module", "Matthew (Shushu's version merged)", "Day 2 to 3"],
        ["Legal review and CIRO pre-file", "Garrett", "Before distribution"],
        ["Newsfile distribution, before 8:30 am ET", "Shushu", "Release day"],
        ["Release page, home block, history table, sitemap, IndexNow", "CQ", "Release day, after the wire"],
        ["Email to the list, LinkedIn post, fifteen-minute pickup check", "Has", "Release day"],
    ], (W(3.3), W(2.0), W(1.5)))
    closing("OWNER")
    path = save("%s 04 Operating update on the investor site - companion to the release program.docx" % STAMP)

'''
s = s[:start] + new04 + s[s.index("    # 04a fill-in sheet"):]
# 04a: rename the metric lines to the two-basis set
old_rows = '''        ["Vehicles funded (contracts funded by the lender in the period)", "", "", ""],
        ["Total retail vehicle sale price of those vehicles, before taxes and protection products", "", "", ""],
        ["Average vehicle price (line 2 divided by line 1)", "", "", ""],
        ["Revenue recognized on those vehicles (vehicle sale, lender reserve and incentives, protection products, delivery and permitted fees)", "", "", ""],
        ["Cost of those vehicles including reconditioning, transport and auction fees", "", "", ""],
        ["Gross profit (line 4 less line 5)", "", "", ""],
        ["Gross profit per vehicle (line 6 divided by line 1)", "", "", ""],
        ["Gross margin per vehicle (line 7 divided by line 4 per vehicle), percent", "", "", ""],
    ], (W(3.1), W(1.1), W(1.1), W(1.5)))'''
new_rows = '''        ["1. Vehicles funded and delivered in the month", "", "", ""],
        ["2. Vehicle sales revenue in the month, before taxes and protection products", "", "", ""],
        ["3. Average vehicle selling price (2 divided by 1)", "", "", ""],
        ["4. Vehicle margin per vehicle, deal basis (before write-downs and before auction, reconditioning and transport costs)", "", "", ""],
        ["5. Finance, insurance and protection product income per vehicle", "", "", ""],
        ["6. Deal gross profit per vehicle (4 plus 5), management basis", "", "", ""],
        ["7. Gross profit for the month on the IFRS basis (as it will appear in the statements)", "", "", ""],
        ["8. Gross profit per vehicle, IFRS basis (7 divided by 1), and the items making up the difference from line 6", "", "", ""],
        ["9. Total revenue in the month", "", "", ""],
        ["10. Gross margin (7 divided by 9), percent", "", "", ""],
        ["11. Fixed operating costs in the month (for the arithmetic line, if Lawson keeps it)", "", "", ""],
    ], (W(3.1), W(1.1), W(1.1), W(1.5)))'''
assert old_rows in s; s = s.replace(old_rows, new_rows)
s = s.replace('H.para("Terence: please complete one copy per period from the ledger, using the definitions below exactly, and return it to Matthew with the working file. The same definitions apply every period; if a definition needs to change, say so once and we change it everywhere before it is used. First sheet due Monday 26 October for the most recent closed month and for the most recent closed fiscal quarter, so the cadence can be chosen.", size=10.5)',
              'H.para("Terence: please complete one copy per month from the ledger, using the definitions in the release program notes and on the Operating metrics page exactly, and return it to Matthew with the working file. The same definitions apply every month; if a definition needs to change, say so once before the October update and we change it everywhere before it is used. First sheet: October 2026 with September beside it, due in the first two business days of November; a trial sheet for September by Monday 26 October would let the site and the release be checked against real figures.", size=10.5)')
s = s.replace('["Funded deals since 2021", "more than 1,500 (public record says 1,250+)", ""],', '["Funded deals since 2021", "more than 1,250 (6 October release); give the new cumulative count when it can be released", ""],')
s = s.replace('["FY2024 revenue and gross margin", "$5.45M and 11.2% (audited comparatives); the 6 October release said about $5.8M", ""],', '["FY2024 revenue and gross profit", "$5,454,893 and $610,787, 11.2% (audited comparatives); the 6 October release rounded to $5.8M", ""],')
# document 00 row and gate wording
s = s.replace('["04", "News release template", "Matthew, Shushu, Terence, Garrett", "The standard release: lead paragraph, news, operating update section with defined metrics, boilerplate, cautionary notes, s8.6 statement. Plus 04a, the one-page fill-in sheet for Terence."],',
              '["04", "Operating update on the site", "Matthew, Terence, CQ, Has", "Companion to the release program rebuilt the same day (Press Releases, 02 Scheduled, notes 00): how the monthly block appears on the site, how a release becomes a page, who does what each month. Plus 04a, the fill-in sheet for Terence."],')
s = s.replace('H.numbered("The funded-deal count matches the public record.", "The site says \'more than 1,500 funded deals\'. The last release said 1,250+. Either the 27 October release states the 1,500 figure in its operating update, or the site reverts to \'more than 1,250\' before go-live. One find-and-replace in content.py.")',
              'H.numbered("The funded-deal count stays on the public record.", "The site says \'more than 1,250 funded deals\', as the 6 October release did. When Terence gives a new cumulative count and it is released, one find-and-replace in content.py updates every page.")')
s = s.replace('H.bullet("Operating metrics ship as placeholders.", "Vehicles funded, average vehicle price, gross profit per vehicle and gross margin per vehicle appear on the home page, the Operating metrics page and in the release template as bracketed placeholders until Terence confirms the first period from the ledger (sheet 04a). Nothing unverified goes public.")',
              'H.bullet("Operating metrics ship as placeholders, monthly, on the release program\'s definitions.", "Vehicles funded and delivered, average selling price, deal gross profit per vehicle (management basis, split) beside gross profit per vehicle on the IFRS basis, and gross margin appear on the home page and the Operating metrics page as bracketed placeholders until Terence confirms October 2026 from the ledger (sheet 04a). The definitions are the ones in the release program notes of the same day; nothing unverified goes public.")')
s = s.replace('["Fri 23 Oct", "Terence", "Sheet 04a, document 04, and the Stock and Financials pages (PDF of document 06 sections)", "Numbers back by Mon 26 Oct"],',
              '["Fri 23 Oct", "Terence", "Sheet 04a, document 04, and the Stock and Financials pages (PDF of document 06 sections)", "Capitalization lines back by Mon 26 Oct; September trial sheet if possible; October in the first two days of November"],')
s = s.replace('H.numbered("Garrett reads three pages.", "Why OCAL (the plan table and market table), Operating metrics (the definitions and non-IFRS note) and the release template. The rest of the site restates the filed record.")',
              'H.numbered("Garrett reads three pages.", "Why OCAL (the plan table and market table), Operating metrics (the definitions and non-IFRS note) and the FAQ break-even answer. The rest of the site restates the filed record.")')
open(p, "w", encoding="utf-8").write(s)
print("build files patched")
