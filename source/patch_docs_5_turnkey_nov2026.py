# -*- coding: utf-8 -*-
"""
patch_docs_5_turnkey_nov2026.py (4 November 2026): build_docs.py for the turnkey rebuild.
  - stamp 2026-11-04; no Terence or Garrett gates; the 04a fill-in sheet is no longer generated (archived);
  - go-live steps, schedule, send list and the two go-live strings replace the placeholder sections;
  - wording guide: Garrett Lee's 31 October lines (never 'exclusive', NI 52-112 definition, rates with periods,
    no fixed-cost figure, no valuation line, nothing on who sells), the 3 November About OCAL boilerplate;
  - scorecard rescored for the 4 November state.
Backup: build_docs_2026-11-04 (pre turnkey rebuild).py.bak
"""
import io, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(HERE, "build_docs.py")
src = io.open(PATH, encoding="utf-8").read()
N = 0
def rep(old, new, count=1):
    global src, N
    c = src.count(old)
    if c != count:
        print("REPLACE FAILED (%d found, %d expected): %s" % (c, count, old[:100])); sys.exit(1)
    src = src.replace(old, new); N += 1
def span(start, end, new):
    global src, N
    a = src.find(start); assert a >= 0, start[:80]
    b = src.find(end, a + len(start)); assert b >= 0, end[:80]
    src = src[:a] + new + src[b:]; N += 1

rep('STAMP = "2026-10-23"', 'STAMP = "2026-11-04"')
rep("October 23, 2026  ·  ", "November 4, 2026  ·  ", count=10)
rep('Every figure on the site traces to a filing or a release; placeholders in double brackets must be cleared before go-live.',
    'Every figure on the site traces to a filing or a release. There are no placeholders; the two go-live strings are in document 01, section 9.')

# ---------------------------------------------------------------- 00
rep('''H.para("A complete investor website for OCAL Financial (TSXV: OCAL), built from the ground up on 23 October 2026: eighteen finished HTML pages, every word of copy, structured data, sitemaps, a news release template with the standing operating update section Shushu asked for on the 23 October Signal call, and the handoff documents CQ and Has need to put it live at investors.ocal.ca. The design and content decisions follow a review of 33 investor sites (Canadian fintech and auto, US auto retail and marketplaces, award winners) and an audit of OCAL's own public record on the same day.", size=10.5)''',
'''H.para("A complete, turnkey investor website for OCAL Financial (TSXV: OCAL): eighteen finished HTML pages, every word of copy, structured data, sitemaps, the 3 November 2026 news release as the per-release page pattern, and the handoff documents CQ and Has need to put it live at investors.ocal.ca. Built on 23 October 2026 from a review of 33 investor sites and an audit of OCAL's public record; rebuilt on 4 November 2026 on Matthew's instruction with every placeholder cleared, the audited figures only, and counsel's 31 October wording applied throughout. Nothing on the site waits on anyone: CQ deploys it, Has connects the email list, Matthew reads it once.", size=10.5)''')
rep('''H.stat_cards([("18", "pages built", "working HTML in the site folder, opens from disk"), ("52", "placeholders to clear", "every one listed in document 01, section 9"), ("33", "investor sites reviewed", "four research files in the research folder"), ("Mon 26 Oct", "Shushu's date", "staging link to Signal; live by Wed 28 Oct")])''',
'''H.stat_cards([("18", "pages built", "working HTML in the site folder, opens from disk"), ("0", "placeholders", "the build prints the count; two go-live strings in document 01, section 9"), ("33", "investor sites reviewed", "four research files in the research folder"), ("Now", "ready to deploy", "DNS, redirects and the email list are the only steps")])''')
rep('''"Companion to the release program rebuilt the same day (Press Releases, 02 Scheduled, notes 00): how the monthly block appears on the site, how a release becomes a page, who does what each month. Plus 04a, the fill-in sheet for Terence."''',
'''"Companion to the release program (Press Releases, 02 Scheduled, notes 00): how the monthly results block appears on the site, how a release becomes a page, who does what each month."''')
rep('''H.h("Decisions taken on 23 October 2026 (Matthew)")''', '''H.h("Decisions (Matthew, 23 October and 4 November 2026)")''')
rep('''H.bullet("Operating metrics ship as placeholders, monthly, on the release program's definitions.", "Vehicles funded and delivered, average selling price, deal gross profit per vehicle (management basis, split) beside gross profit per vehicle on the IFRS basis, and gross margin appear on the home page and the Operating metrics page as bracketed placeholders until Terence confirms October 2026 from the ledger (sheet 04a). The definitions are the ones in the release program notes of the same day; nothing unverified goes public.")''',
'''H.bullet("Turnkey, 4 November 2026.", "No gate sits with Terence or Garrett. Every figure on the site is from the audited FY2025 and FY2024 statements, the Filing Statement, the exchange record or an issued release; the monthly operating metrics start with the 10 November 2026 results release and are added to the site the day each release is issued, exactly as released. The two things only the team can supply, the email list's form action and a captured SEDAR+ profile link, are single strings in content.py.")''')
rep('''the site carries the audited FY2025 and FY2024 figures, the roadmap with the status of each market, the operating metrics placeholders and the fixed-cost line only. Financing terms and amounts are not on the site anywhere.")''',
'''the site carries the audited FY2025 and FY2024 figures, the roadmap with the status of each market, the metric definitions and the audited operating-leverage lines only (revenue up 18.8 percent, gross profit up 32.7 percent, operating expenses down 9.8 percent, operating loss halved). No fixed-cost dollar figure, no financing terms or amounts, and no statement about who has been selling the stock, anywhere (counsel, 31 October; the 30 October evening review).")''')
rep('''Brevo or Mailchimp free tier for the alert list. No monthly cost.")''',
'''Brevo free tier for the alert list; until Has pastes its form action into content.py the Subscribe button sends an email request to investors@ocal.ca, so the block works from day one. No monthly cost.")''')
rep('''No news release announces the acquisition of the lead supplier, so the site says lead generation was brought in-house and names no transaction; if a release is issued before go-live, one sentence is added (document 01, section 9).")''',
'''No news release yet covers the lead supplier, so the site says only that lead generation, the CRM and the AI sales agents run on one platform; when release 10 is issued (scheduled 17 November 2026), one sentence is added in the release's words.")''')
span('''    H.h("Go-live gates (nothing goes live until all six are cleared)")''', '''    H.h("What to send, and when")''',
'''    H.h("Go-live steps (three, none of them a figure)")
    H.numbered("CQ: domain, deploy, redirects.", "DNS for investors.ocal.ca, the site folder as-is, the 301 redirects from ocalfinancial.ca and the consumer-site Investors link live at the same moment (document 01).", restart=True)
    H.numbered("Has: the email list.", "Create the Brevo list with double opt-in, paste the form action URL into SITE['form_action'] in content.py and rebuild; add the GA4 snippet (document 02).")
    H.numbered("Matthew: one read.", "Document 06 is every word on the site in reading order. Shushu may read it too; edits go into content.py, then rebuild.")
''')
span('''    H.table(["When", "To", "What", "How"], [
        ["Fri 23 Oct", "CQ (EasyPear), copy Has",''', '''    ], (W(0.9), W(1.5), W(2.6), W(1.8)))
    H.h("Not in this package, on purpose")''',
'''    H.table(["When", "To", "What", "How"], [
        ["Now", "CQ (EasyPear), copy Has", "Documents 00, 01, 03, 05 and the site, source and research folders (zip)", "Email draft for Matthew to send"],
        ["Now", "Has, copy CQ", "Documents 00, 02, 03, 05", "Same email thread"],
        ["When the staging link exists", "Shushu", "Document 06 and the staging URL", "For her read; edits via content.py"],
        ["At go-live", "Mehdi, board", "The live link and document 00", "For information; Matthew approves go-live"],
''')
rep('''H.para("The US board plan and the US OTC plan beyond the public line ('an OTCQB quotation and DTC eligibility application is in progress'); any cash figure between reporting dates; any FY2026 figure before the audited statements are filed; share-trading analysis; financing terms; Shushu's September deck figures (her deck goes out as she wrote it, by Matthew's 13 September decision). The consumer site is not touched beyond the Investors link and the redirects.")''',
'''H.para("Anything not yet released: the OTC quotation and DTC eligibility (release 16, 22 December), the lead supplier transaction and Hasneen Jalil's appointment (release 10, 17 November), the United States beyond the roadmap line; any cash figure between reporting dates; any FY2026 figure before the audited statements are filed; share-trading analysis; financing terms. The consumer site is not touched beyond the Investors link and the redirects.")''')

# ---------------------------------------------------------------- 01
rep('''"Has creates the Brevo or Mailchimp list with double opt-in and gives you the form action URL. Replace the form action placeholder in every subscribe block (one string in content.py, SITE['form_action']; rebuild). Field name EMAIL. Until then the form is inert by design."''',
'''"Has creates the Brevo list with double opt-in and gives you the form action URL; paste it into SITE['form_action'] in content.py and rebuild (one string, seven blocks). Field name EMAIL. Until then the button opens an email to investors@ocal.ca with the visitor's address, so the block already works."''')
rep('''"Matthew supplies a Calendly or Google booking link (SITE['booking_link']). Until then the buttons point to #."''',
'''"The buttons open an email to investors@ocal.ca with the subject 'Book a 30-minute investor call'. If Matthew later supplies a calendar link, it is one string (SITE['booking_link']) and a rebuild."''')
rep('''"Add the release to content.py NEWS (date, headline, path, category) and add a page entry using the 22 October sample (/news/2026-10-22-ocal-showroom/) as the pattern: kicker with date and dateline, headline as H1, sub-headline, body paragraphs, quotes, Operating update section, About OCAL, investor contact, cautionary notes, s8.6 statement.''',
'''"Add the release to content.py NEWS (date, headline, path, category) and add a page entry using the 3 November 2026 page (/news/2026-11-03-repossession-rate-and-agm/) as the pattern: kicker with date and dateline, headline as H1, sub-headline, body paragraphs as issued, quotes, operating performance section, About OCAL, investor contact, cautionary notes, s8.6 statement.''')
rep('''"If the release carries the operating update section, Terence's confirmed figures go into the Operating metrics history table and the home-page block (content.py, same rebuild)."''',
'''"If the release is a monthly results release, its figures go into the Operating metrics history (content.py, same rebuild), exactly as released."''')
span('''    H.table(["Day", "Milestone"], [
        ["Fri 23 Oct", "Package received.''', '''    ], (W(1.1), W(5.7)))
    H.h("8. Acceptance checklist''',
'''    H.table(["Day", "Milestone"], [
        ["Day 1", "Package received. DNS record requested from Matthew. Staging URL created from the site folder as delivered."],
        ["Day 2", "Staging URL to Matthew and Shushu. Email form wired if Has has the list ready; otherwise the email-request fallback stays."],
        ["Day 3", "Matthew's and Shushu's edits applied (via content.py), rebuild, placeholder count zero (it is zero today)."],
        ["Go-live", "DNS, HTTPS, redirects, consumer-site links, sitemaps submitted, IndexNow key in place. Acceptance checklist signed off. The 10 November 2026 results release is the first under the new workflow if the site is live by then."],
        ["Within 7 days", "Core Web Vitals check (PageSpeed Insights, mobile and desktop), Search Console coverage report clean, GA4 events firing, first weekly search-rank snapshot (document 05, section 2)."],
''')
rep('''"Every link on every page resolves (no # left except where a placeholder is still open, and none at go-live).",''',
'''"Every link on every page resolves; no # anywhere.",''')
rep('''    H.h("9. Placeholders at the time of handoff")
    H.para("Generated by the build from the double-bracket markers in the copy. Each one has an owner: Terence (figures), Matthew (links and decisions), Has (email form, analytics), Garrett (governance documents).")
    rows = placeholders()
    H.table(["Page", "Placeholder"], rows, (W(1.6), W(5.2)), size=7.5)''',
'''    H.h("9. The two go-live strings (there are no placeholders)")
    H.para("The build prints 'placeholders: 0'. Two values are swapped in content.py when the team has them, then rebuild: SITE['form_action'] (the Brevo form action URL from Has; empty today, which renders the email-request fallback) and, optionally, SITE['sedar_profile'] and the FILINGS links (today they open the SEDAR+ search page, where the issuer profile is found by searching 'OCAL Financial Inc.'; SEDAR+ refuses automated access, so a person captures the profile URL from a browser and pastes it).")''')

# ---------------------------------------------------------------- 02
rep('''H.h2("The approved description (use these words only, once Matthew signs off)")
    H.card("Standard, 484 characters (Stockhouse limit 500)", "OCAL Financial Inc.", "OCAL Financial Inc. is a Vancouver-based, asset-light online automotive dealership and vehicle-finance platform. Operating remotely and licensed in British Columbia and Alberta, OCAL takes customers from application to lender approval, vehicle matching, digital contracting and delivery. It sources each vehicle only after approval, through OPENLANE Canada, its exclusive auction and sourcing channel, and earns revenue from vehicle sales and related finance and protection products. It does not hold consumer loans or take credit-default risk.")
    H.card("Short, one line", "For fields under 120 characters", "Virtual automotive dealership and vehicle-finance platform, licensed in British Columbia and Alberta.")''',
'''H.h2("The approved description (approved 4 November 2026: the About OCAL boilerplate of the 3 November release)")
    H.card("Standard, about 530 characters (for a 500 limit, drop the last sentence)", "OCAL Financial Inc.", "OCAL Financial Inc. (TSXV: OCAL; FSE: JC3) is a technology-enabled automotive financing and purchasing platform. Built around an approval-first approach, OCAL connects customers with suitable financing before sourcing a vehicle that fits their needs and budget. It holds no standing vehicle inventory, sourcing each vehicle only after approval through OPENLANE Canada, its auction and sourcing channel, and earns revenue from vehicle sales and related finance and protection products. It does not hold consumer loans or assume credit-default risk.")
    H.card("Short, one line", "For fields under 120 characters", "Technology-enabled automotive financing and purchasing platform, licensed in British Columbia and Alberta.")''')
rep('''CEO Mehdi Moghareh; Executive Chairman Matthew Friesen; CFO Terence Lee, CPA; independent directors Michael Stier and Robert Birmingham.''',
'''CEO Mehdi Moghareh; Executive Chairman Matthew Friesen; CFO Terence Lee, CPA; Vice President of Sales Ryan McDonald; independent directors Michael Stier and Robert Birmingham.''')
rep('''["1", "Newsfile company page (OCAL controls it)", "Newsfile account manager", "Standard description; investor URL investors.ocal.ca; the boilerplate from document 04"],''',
'''["1", "Newsfile company page (OCAL controls it; on 4 November 2026 it still reads 'Canada's first fully virtual, AI-native licensed automotive finance platform')", "Newsfile account manager, via Shushu", "Standard description above; investor URL investors.ocal.ca"],''')
rep('''["11", "LEI record (GLEIF)", "Through the LEI issuer", "Registered address shows West Georgia Street; confirm with Matthew and align to Dunsmuir if that is the registered office"],''',
'''["11", "LEI record (GLEIF)", "No action", "Checked 4 November 2026: status issued, legal address Suite 1600, 925 West Georgia Street (the registered and records office), headquarters Suite 500, 885 Dunsmuir Street. Correct as it stands."],''')

# ---------------------------------------------------------------- 03
rep('''["'A digital inventory of 3,000+ vehicles'; 'five auction supply channels'", "'More than 3,000 vehicles visible on OPENLANE's Canadian marketplace on a typical day; OCAL owns none of them. OPENLANE is OCAL's exclusive auction and sourcing channel.'"],''',
'''["'A digital inventory of 3,000+ vehicles' on its own; 'five auction supply channels'; 'OPENLANE, our exclusive auction and sourcing channel'", "'More than 3,000 vehicles visible on OPENLANE's Canadian marketplace on a typical day; OCAL owns none of them. OPENLANE is OCAL's auction and sourcing channel.' Never 'exclusive' (Garrett Lee, 31 October 2026)."],''')
rep('''["'Hasneen Jalil, CTO'", "'Founder of Canada Auto Experts; leads technology and the demand engine'. Never CTO."],''',
'''["'Hasneen Jalil, CTO'; 'founder of Canada Auto Experts'", "'Hasneen Jalil leads technology and the demand engine'. Never CTO, and nothing about Canada Auto Experts or EasyPear until release 10 is issued."],''')
rep('''["'We acquired Canada Auto Experts and EasyPear' (with consideration)", "'Lead generation was brought in-house' until a news release announces the transaction; then one sentence naming it and the performance-vested consideration."],''',
'''["'We acquired Canada Auto Experts and EasyPear' (with consideration)", "'Lead generation, the CRM and the AI sales agents run on one platform' until release 10 (scheduled 17 November 2026) is issued; then one sentence in the release's words."],''')
rep('''["Any share-price or valuation target; 'cheap'; 'undervalued'", "Nothing. State the market value as a multiple of audited revenue only as a fact with the date, and let the reader do the arithmetic."],''',
'''["Any share-price or valuation target; 'cheap'; 'undervalued'; 'one year of audited revenue'; 're-rating'", "Nothing. No valuation line of any kind, and no statement about who has been buying or selling the stock."],''')
rep('''["Monthly run-rate targets, break-even arithmetic, 'at 30 cars we make $1M' in a release", "Historical metrics only in releases. Targets live on the Why OCAL page under the forward-looking legend and in the presentation."],''',
'''["Monthly run-rate targets, break-even arithmetic, 'at 30 cars we make $1M', 'fixed costs of about $160,000 a month'", "Historical metrics only, in results releases, reconciled. Everywhere else the audited lines carry operating leverage: revenue up 18.8 percent, gross profit up 32.7 percent, operating expenses down 9.8 percent, 'the cost base is largely fixed'. No targets anywhere."],
        ["'Manitoba licence application filed'; 'licence expected in November'", "'Dealer permit application under way with the regulator; office inside the OPENLANE Winnipeg auction facility arranged; opening targeted for December 2026, when the permit is granted.'"],
        ["A rate without a period ('repossessions under one percent')", "'Fewer than one percent of the vehicle loans arranged from the first funded transaction in 2021 to 30 September 2026 have resulted in repossession (management information, lender reporting)'; the same period for 'about 99 percent funded'. The funded-deal count carries its definition sentence beside its first use on every page (NI 52-112)."],''')
rep('''"Calendar month; first release after the month closes; October 2026 first; each figure beside the prior month; monthly figures 'approximately'; once started, the series continues in weak months. Break-even appears only as the month's arithmetic ('fixed operating costs were equal to the contribution from about 28 funded vehicles'), never as a target, and only if Lawson keeps it."''',
'''"Calendar month; the monthly results release after the month closes; October 2026 first, on 10 November 2026; each figure beside the prior month; monthly figures 'approximately'; once started, the series continues in weak months. No break-even arithmetic anywhere."''')
rep('''H.para("OCAL Financial Inc. is a Vancouver-based, asset-light online automotive dealership and vehicle-finance platform. Operating remotely and licensed in British Columbia and Alberta, OCAL takes customers from application to lender approval, vehicle matching, digital contracting and delivery. It sources each vehicle only after approval, through OPENLANE Canada, its exclusive auction and sourcing channel, and earns revenue from vehicle sales and related finance and protection products. It does not hold consumer loans or take credit-default risk. OCAL trades on the TSX Venture Exchange as OCAL and on the Frankfurt Stock Exchange as JC3. Investor information: investors.ocal.ca.", size=9)''',
'''H.para("OCAL Financial Inc. (TSXV: OCAL) (FSE: JC3) is a technology-enabled automotive financing and purchasing platform transforming how Canadians finance and purchase vehicles. Built around an approval-first approach, OCAL connects customers with suitable financing options before sourcing a vehicle that meets their needs and budget. Its integrated platform brings together credit assessment and financial guidance, lender matching, vehicle sourcing, digital transactions and home delivery anywhere in the provinces it serves, eliminating the need to visit a traditional dealership. OCAL holds no standing vehicle inventory; it sources each vehicle only after a customer is approved, through OPENLANE Canada, its auction and sourcing channel. OCAL earns revenue from vehicle sales and related finance and protection products, and does not hold consumer loans or assume credit-default risk. Licensed in British Columbia and Alberta, OCAL generated revenue of $6.48 million (audited) in the fiscal year ended August 31, 2025 and has completed more than 1,500 funded vehicle transactions to date. Investor information: investors.ocal.ca. (As issued 3 November 2026; the funded-transaction sentence carries its NI 52-112 definition in the release body.)", size=9)''')
rep('''OCAL then sources the vehicle through OPENLANE, its exclusive auction and sourcing channel, and delivers it.''',
'''OCAL then sources the vehicle through OPENLANE, its auction and sourcing channel, and delivers it.''')

# ---------------------------------------------------------------- 04 (and no 04a)
rep('''It shows how the block lands on the investor site, how a release becomes a page, and what Terence fills in on sheet 04a so the release, the site and the email carry the same numbers on the same day.''',
'''It shows how the block lands on the investor site, how a release becomes a page, and who does what each month so the release, the site and the email carry the same numbers on the same day.''')
rep('''["Home page, 'Operating update' section", "The latest month's table: vehicles funded and delivered, average selling price, deal gross profit per vehicle (split), gross profit per vehicle on the IFRS basis, gross margin; prior month beside each", "Same day as the release"],
        ["Operating metrics page, 'Latest period'", "The same table", "Same day"],
        ["Operating metrics page, 'History'", "One row per month, plus the fiscal 2025 audited row; the chart of vehicles funded per month fills in from the first month", "Same day"],''',
'''["Home page, 'The audited results' section", "The audited FY2025 and FY2024 table today; from the first monthly results release, a line linking to the latest month on the Operating metrics page", "Same day as the release"],
        ["Operating metrics page, 'Monthly history'", "The latest month's table: vehicles funded and delivered, average vehicle selling price, gross profit per vehicle on both bases with the reconciling items, gross margin; prior month beside each", "Same day"],
        ["Operating metrics page, history table", "One row per month, plus the fiscal 2025 audited row, added as each release is issued", "Same day"],''')
rep('''H.h("2. The block as it reads on the site (placeholders until Terence's figures)")''', '''H.h("2. The block as it will read on the site, from the 10 November 2026 release")''')
rep('''"One line in NEWS (date, headline, path, category) and one page entry on the pattern of the 22 October sample page; the description is the first sentence after the dateline."''',
'''"One line in NEWS (date, headline, path, category) and one page entry on the pattern of the 3 November 2026 page; the description is the first sentence after the dateline."''')
rep('''"The confirmed figures go into the home-page block and the history table (content.py, same change)."''',
'''"The released figures go into the history table on the Operating metrics page (content.py, same change), exactly as released."''')
rep('''["Pull and confirm the month's figures on sheet 04a", "Terence", "First two business days after month end"],''',
'''["Pull and confirm the month's figures from the ledger", "Terence", "First two business days after month end"],''')
span('''    # 04a fill-in sheet''', '''    return path''', '''    # 04a (the fill-in sheet for Terence) is no longer generated: superseded 4 November 2026, archived with a why-note.
''')
rep('''    paths.append(os.path.join(OUT, "%s 04a Operating metrics fill-in sheet for Terence.docx" % STAMP))
''', '')

# ---------------------------------------------------------------- 06
rep('''Text in double brackets is a placeholder to be filled or confirmed before go-live. Widgets (chart, forms, lists) are noted in place.''',
'''There are no placeholders; every figure is from the audited statements, the Filing Statement, the exchange record or an issued release. Widgets (chart, forms, lists) are noted in place.''')

# ---------------------------------------------------------------- 08
rep('''The same checklist is applied below to the new site twice: as delivered today, with 54 placeholders still open, and at go-live with every gate cleared. The second column is the one that matters and the first is the honest one.", size=10.5)
    H.stat_cards([("38", "old page, 12 October", "43 of 140 points"), ("71", "new site as delivered", "99 of 140; placeholders open, nothing live"), ("89", "at go-live", "124 of 140 with the six gates cleared"), ("95", "reachable by January", "with the first two monthly updates and the vendor fixes")])''',
'''The same checklist is applied below to the site as rebuilt turnkey on 4 November 2026, with no placeholders, and at go-live once the domain, redirects and email list are live. (The 23 October delivery, with 54 placeholders open, scored 99 of 140.)", size=10.5)
    H.stat_cards([("38", "old page, 12 October", "43 of 140 points"), ("84", "4 November rebuild", "117 of 140; no placeholders, nothing live yet"), ("89", "at go-live", "124 of 140 with DNS, redirects and the email list live"), ("95", "reachable by January", "with the first two monthly results releases and the vendor fixes")])''')
span('''    H.table(["#", "Element", "Old", "Now", "Go-live", "Why, and what is still missing"], [''', '''    ], (W(0.3), W(1.5), W(0.4), W(0.4), W(0.5), W(3.7)), size=7.5)''',
'''    H.table(["#", "Element", "Old", "4 Nov", "Go-live", "Why, and what is still missing"], [
        ["1", "Stock quote and chart", "3", "8", "9", "Live TradingView chart and mini overview, listings table with ISIN, CUSIP and WKN, TMX and Frankfurt links, text fallback. Missing: market cap and 52-week range as text, and a sticky quote bar on every page if the budget ever allows a feed."],
        ["2", "Share structure", "1", "9", "9", "Full capitalization table with sources, escrow total and release schedule, warrants by strike and expiry, options, fully diluted, the July financing, founder holdings from SEDI, the 8 November 2026 hold expiry. Nothing missing."],
        ["3", "Financial reports", "0", "7", "8", "Two-year audited summary, the interim period, the going-concern answer, the reporting calendar, the pre-audit figure explained. Links open SEDAR+ search rather than the document (SEDAR+ refuses automated access; a captured profile URL is a one-string swap)."],
        ["4", "Presentation and fact sheet", "4", "9", "9", "The October 2026 set (deck, pitch, brief, long form, Q&A) linked and copied into the site, all regenerated 4 November on counsel's wording; a printable fact sheet on the site, dated November 2026."],
        ["5", "Why invest", "4", "9", "9", "Nine numbered sections with a sourced number in each, a market table under the legend, no superlatives, no competitors, no fixed-cost figure. The one-point gap: a quarterly letter from the founders, which belongs on the site after the first results release."],
        ["6", "News and filings", "4", "8", "9", "All twenty releases listed with their own Newsfile links, the 3 November release as the per-release page with the s8.6 statement, RSS and a news sitemap. Missing: per-release pages for the earlier releases (CQ builds them on the pattern over time)."],
        ["7", "Email alerts and subscription", "0", "6", "9", "Subscribe blocks on seven pages with a working email-request fallback and CASL identification. The Brevo list and its form action are Has's one string; the welcome email and the first send follow."],
        ["8", "Events and webcasts", "0", "8", "8", "Calendar with the 10 November results release, the AGM with time, place, record date and business, both filing deadlines, past events, Event schema. Materials and replays exist only once events happen."],
        ["9", "Analyst, market maker and IR disclosure", "2", "9", "9", "No analyst coverage stated plainly with a promise to list any; Integral Wealth and Signal Capital named exactly as released. Nothing missing."],
        ["10", "Governance", "4", "8", "9", "Board with independence and committees, the audit committee charter located in the Filing Statement, AGM particulars from the 3 November release, SEDI founder holdings, disclosure practice. Missing: the circular (when filed) and further policies as the board adopts them."],
        ["11", "FAQ", "7", "9", "9", "Thirty questions, the three hard ones first, every answer dated or sourced and inside counsel's wording, FAQPage schema. The gap: dates refreshed monthly."],
        ["12", "Contact and response", "5", "9", "9", "Named people, a one-business-day promise, the selective-disclosure policy, Endeavor Trust's full contact details, booking by email, a separate path for customers."],
        ["13", "AI and search readability", "2", "9", "9", "Static HTML on every page, Corporation schema with ticker, ISIN, CUSIP and LEI, unique titles carrying 'TSXV: OCAL', a facts page, llms.txt, real 404. The last point depends on data vendors outside the site."],
        ["14", "Consistency with the public record", "3", "9", "9", "Audited figures only, escrow and warrants from the exchange record, 1,500+ with its NI 52-112 definition beside every first use, rates with their periods, OPENLANE never 'exclusive', no fixed-cost figure, no statement about who sells, Matthew's title correct everywhere, nothing unreleased."],
        ["", "Total", "43", "117", "124", "Out of 140: 31 percent, 84 percent, 89 percent"],
''')
rep('''H.bullet("Placeholders.", "Fifty-four. They are the right call (nothing unverified goes public) but the site is not finished until they are zero, and the four that matter most (SEDAR+ links, the form action, the booking link, Terence's October figures) sit with four different people.")''',
'''H.bullet("Placeholders.", "None. The two strings that remain (the form action, a captured SEDAR+ profile link) are the team's to paste; nothing on the site is unverified, and nothing waits on a figure from anyone.")''')
rep('''The page stands on the audited figures, the roadmap and the fixed-cost line.")''',
'''The page stands on the audited figures, the roadmap and the audited operating-leverage lines.")''')

assert "—" not in src and "–" not in src
io.open(PATH, "w", encoding="utf-8", newline="\n").write(src)
print("build_docs.py patched: %d edits" % N)
