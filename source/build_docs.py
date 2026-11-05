# -*- coding: utf-8 -*-
"""
Build the handoff documents for the OCAL investor site package (house style, python-docx, PDFs via Word COM).

    python -X utf8 build_docs.py           -> writes the nine .docx files one folder up, then exports PDFs
    python -X utf8 build_docs.py --nopdf   -> docx only

Reads content.py (the site copy) so the review deck and the handoff tables never drift from the site.
"""
import os, sys, re, datetime
sys.path.insert(0, r"C:\Users\matth\OneDrive\Claude Code\scripts")
from docx.shared import Inches
import ocal_ir_helpers as H
import content as C

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.normpath(os.path.join(HERE, ".."))
STAMP = "2026-11-04"
FOOT = "INTERNAL WORKING DOCUMENT FOR OCAL'S WEB AND IR TEAM  |  NOT FOR PUBLICATION"
W = Inches

def clean(t):
    t = re.sub(r"</?em>", "", t)
    t = re.sub(r"\*\*(.+?)\*\*", r"\1", t)
    t = re.sub(r"\[([^\]]+?)\]\(([^)]+?)\)", r"\1", t)
    return t

def placeholders():
    p = os.path.join(HERE, "PLACEHOLDERS.txt")
    rows = []
    if os.path.exists(p):
        for line in open(p, encoding="utf-8").read().splitlines()[2:]:
            if line.strip():
                slug, txt = line[:32].strip(), line[32:].strip()
                rows.append([slug, txt.replace("&#x27;", "'")])
    return rows

def closing(kick="QUESTIONS ON THIS PACKAGE"):
    H.closing_band(kick, "Matthew Friesen, Executive Chairman and Director",
                   ["matthew@ocal.ca  ·  604-240-7818  ·  OCAL Financial Inc., Vancouver", "Shushu Feng, Signal Capital Advisors, reviews investor-facing wording"],
                   "Internal working document for OCAL's web and investor relations team. Not for publication. Every figure on the site traces to a filing or a release. There are no placeholders; the two go-live strings are in document 01, section 9.")

def save(name, pdf=True):
    path = os.path.join(OUT, name)
    H.finish(path)
    return path

PAGE_SPECS = [(p["slug"], p["title"], p["description"]) for p in C.PAGES]

# =====================================================================================================
# 00 READ ME FIRST
# =====================================================================================================
def doc_00():
    H.new_doc("INVESTOR SITE PACKAGE  ·  READ ME FIRST", FOOT)
    H.band("Read me first", "November 4, 2026  ·  investors.ocal.ca  ·  for CQ (EasyPear) and Has")
    H.kicker("What is in this folder, what was decided, and what happens next")
    H.para("A complete, turnkey investor website for OCAL Financial (TSXV: OCAL): eighteen finished HTML pages, every word of copy, structured data, sitemaps, the 3 November 2026 news release as the per-release page pattern, and the handoff documents CQ and Has need to put it live at investors.ocal.ca. Built on 23 October 2026 from a review of 33 investor sites and an audit of OCAL's public record; rebuilt on 4 November 2026 on Matthew's instruction with every placeholder cleared, the audited figures only, and counsel's 31 October wording applied throughout. Nothing on the site waits on anyone: CQ deploys it, Has connects the email list, Matthew reads it once.", size=10.5)
    H.stat_cards([("18", "pages built", "working HTML in the site folder, opens from disk"), ("0", "placeholders", "the build prints the count; two go-live strings in document 01, section 9"), ("33", "investor sites reviewed", "four research files in the research folder"), ("Now", "ready to deploy", "DNS, redirects and the email list are the only steps")])
    H.h("The documents")
    H.table(["#", "Document", "For", "What it is"], [
        ["00", "Read me first", "Everyone", "This index, the decisions, the go-live gates, what to send."],
        ["01", "Master handoff for CQ", "CQ, copy Has", "Domain and DNS, hosting, how to deploy the static site or port it into the CMS, per-page title and description table, widgets, redirects from ocalfinancial.ca, sitemaps, Search Console, analytics events, release-page workflow, acceptance checklist, every placeholder."],
        ["02", "Handoff for Has", "Has, copy CQ", "Email list set-up, welcome email, data-vendor profile corrections with the approved description, LinkedIn and Crunchbase, measurement dashboard, monthly maintenance rhythm, release-day checklist."],
        ["03", "Wording guide", "Everyone who writes", "Lines that hold, wording that goes and what replaces it, metric definitions, the forward-looking legend and non-IFRS note, title-tag patterns, voice rules."],
        ["04", "Operating update on the site", "Matthew, Terence, CQ, Has", "Companion to the release program (Press Releases, 02 Scheduled, notes 00): how the monthly results block appears on the site, how a release becomes a page, who does what each month."],
        ["05", "SEO and search plan", "CQ and Has", "The queries to own and who ranks today, the five moves that matter, technical patterns, structured data, indexing, AI answer engines, vendor fix order, newswire distribution."],
        ["06", "All page copy (review deck)", "Matthew, Mehdi, Shushu", "Every page's copy in reading order for review and markup. Generated from the same source as the site."],
        ["07", "Research synthesis", "Everyone", "What we took from which site, what we deliberately did not copy, and where each idea landed on the new site."],
        ["08", "Self-review and scorecard", "Matthew", "The site scored against the 12 October 14-element checklist (the old page scored 38 of 100) as delivered and at go-live, against the ideas lists in the three research files, and an honest view of how it will rank in search and why."],
        ["site folder", "The website", "CQ", "index.html and one folder per page; assets; sitemap.xml, news-sitemap.xml, feed.xml, robots.txt, llms.txt, 404.html, site.webmanifest."],
        ["source folder", "Generators", "CQ, future sessions", "content.py (all copy), build_site.py (HTML), build_docs.py (these documents), PLACEHOLDERS.txt. Change the copy in content.py and rebuild; never hand-edit the HTML."],
        ["research folder", "Research", "Reference", "A: Canadian fintech, auto and TSXV sites. B: US auto retail and marketplaces. C: best-in-class sites and the SEO plan. D: OCAL public record audit (site, TMX, SEDAR+, releases, vendors, search)."],
    ], (W(0.5), W(1.7), W(1.2), W(3.4)))
    H.h("Decisions (Matthew, 23 October and 4 November 2026)")
    H.bullet("Separate domain.", "The investor site lives at investors.ocal.ca, not inside ocalfinancial.ca. The consumer site keeps its Investors menu item, pointing to the new domain, and every old investor URL on ocalfinancial.ca is redirected one to one (document 01, section 5). Trade-off accepted: a new domain starts with no search authority, so the redirects, the links from every news release and the consumer site footer, and the entity work in document 05 carry the ranking.")
    H.bullet("Turnkey, 4 November 2026.", "No gate sits with Terence or Garrett. Every figure on the site is from the audited FY2025 and FY2024 statements, the Filing Statement, the exchange record or an issued release; the monthly operating metrics start with the 10 November 2026 results release and are added to the site the day each release is issued, exactly as released. The two things only the team can supply, the email list's form action and a captured SEDAR+ profile link, are single strings in content.py.")
    H.bullet("No forecast, no plan table, no per-vehicle dollar figures (30 October 2026).", "The FY2027 to FY2030 plan table and the per-vehicle economics were removed on 30 October 2026 under the investor narrative rules: the site carries the audited FY2025 and FY2024 figures, the roadmap with the status of each market, the metric definitions and the audited operating-leverage lines only (revenue up 18.8 percent, gross profit up 32.7 percent, operating expenses down 9.8 percent, operating loss halved). No fixed-cost dollar figure, no financing terms or amounts, and no statement about who has been selling the stock, anywhere (counsel, 31 October; the 30 October evening review).")
    H.bullet("Free widgets.", "TradingView chart for TSXV:OCAL (delayed), links to TMX Money and Frankfurt, Brevo free tier for the alert list; until Has pastes its form action into content.py the Subscribe button sends an email request to investors@ocal.ca, so the block works from day one. No monthly cost.")
    H.h("Facts the audit changed")
    H.para("The public-record audit (research file D) corrected several figures that earlier internal documents carried. The site now uses: 23,638,104 shares in escrow (TSXV bulletin and TMX Money); warrants 11,029,501 plus 39,760 finder warrants; options 600,000 plus 100,000 pending for the IR firm; about 48.3 million fully diluted; the July 2026 financing as 6,029,500 units for $1,507,375; the market maker (Integral Wealth Securities) and the IR firm (Signal Capital Advisors) named exactly as released; and a plain answer to the inventory and floorplan balances that appear in the interim statements ($86,300 and $222,033 at 31 May 2026), which the old page contradicted with 'no inventory'. No news release yet covers the lead supplier, so the site says only that lead generation, the CRM and the AI sales agents run on one platform; when release 10 is issued (scheduled 17 November 2026), one sentence is added in the release's words.")
    H.h("Go-live steps (three, none of them a figure)")
    H.numbered("CQ: domain, deploy, redirects.", "DNS for investors.ocal.ca, the site folder as-is, the 301 redirects from ocalfinancial.ca and the consumer-site Investors link live at the same moment (document 01).", restart=True)
    H.numbered("Has: the email list.", "Create the Brevo list with double opt-in, paste the form action URL into SITE['form_action'] in content.py and rebuild; add the GA4 snippet (document 02).")
    H.numbered("Matthew: one read.", "Document 06 is every word on the site in reading order. Shushu may read it too; edits go into content.py, then rebuild.")
    H.h("What to send, and when")
    H.table(["When", "To", "What", "How"], [
        ["Now", "CQ (EasyPear), copy Has", "Documents 00, 01, 03, 05 and the site, source and research folders (zip)", "Email draft for Matthew to send"],
        ["Now", "Has, copy CQ", "Documents 00, 02, 03, 05", "Same email thread"],
        ["When the staging link exists", "Shushu", "Document 06 and the staging URL", "For her read; edits via content.py"],
        ["At go-live", "Mehdi, board", "The live link and document 00", "For information; Matthew approves go-live"],
    ], (W(0.9), W(1.5), W(2.6), W(1.8)))
    H.h("Not in this package, on purpose")
    H.para("Anything not yet released: the OTC quotation and DTC eligibility (release 16, 22 December), the lead supplier transaction and Hasneen Jalil's appointment (release 10, 17 November), the United States beyond the roadmap line; any cash figure between reporting dates; any FY2026 figure before the audited statements are filed; share-trading analysis; financing terms. The consumer site is not touched beyond the Investors link and the redirects.")
    closing()
    return save("%s 00 READ ME FIRST - investor site package index, decisions and go-live gates.docx" % STAMP)

# =====================================================================================================
# 01 CQ HANDOFF
# =====================================================================================================
def doc_01():
    H.new_doc("INVESTOR SITE  ·  MASTER HANDOFF FOR CQ", FOOT)
    H.band("Master handoff for CQ", "November 4, 2026  ·  investors.ocal.ca  ·  for CQ (EasyPear), copy Has")
    H.kicker("Domain, hosting, build, redirects, search, analytics, release workflow, acceptance")
    H.para("The site is finished HTML. Your job is to put it on investors.ocal.ca, wire the three things that need an account (the email form, analytics, Search Console), redirect the old investor pages, and run the release workflow from then on. Nothing in the copy is yours to change; wording changes go to Matthew and are made in content.py, then rebuilt. Where the HTML has to be adapted to your stack, keep the structure, the title tags, the meta descriptions, the JSON-LD and the URLs exactly as built.", size=10.5)
    H.h("1. Domain and DNS")
    H.table(["Item", "Setting"], [
        ["Host name", "investors.ocal.ca (ocal.ca is OCAL's; investors@ocal.ca already runs on it). Matthew confirms registrar access."],
        ["Record", "CNAME investors to the host you deploy on (Cloudflare Pages, Netlify, or the current ocalfinancial.ca host). HTTPS mandatory; HTTP to HTTPS 301."],
        ["Apex", "ocal.ca itself: leave as is. If it has no website, a 301 from https://ocal.ca/ to https://investors.ocal.ca/ is welcome but not required."],
        ["www", "www.investors.ocal.ca is not used; do not create it."],
        ["Email", "No change. The site links mailto:investors@ocal.ca; that mailbox forwards to Matthew and Shushu (Has confirms the rule)."],
    ], (W(1.3), W(5.5)))
    H.h("2. Hosting and deployment")
    H.bullet("Recommended: static hosting.", "Cloudflare Pages (free) or the existing Cloudflare account in front of a static bucket. Upload the site folder as-is: index.html at the root, one folder per page with its own index.html, assets, sitemap.xml, news-sitemap.xml, feed.xml, robots.txt, llms.txt, 404.html, site.webmanifest. Set 404.html as the not-found page so unknown URLs return a real 404 status (the current site returns 200 for unknown URLs, which search engines treat as a soft 404).")
    H.bullet("Alternative: port into the CMS.", "If you prefer the investor pages inside your content system, create one page per URL with the same slug, paste the body of each page's main element, keep the title tag, meta description, canonical and JSON-LD from each file's head, and load assets/css/style.css unchanged. Do not let the consumer site's header, footer, lead-gen scripts or chat widgets onto investor pages (TMX guidance: keep investor and consumer content apart).")
    H.bullet("Trailing slashes.", "Every URL ends with a slash (/stock/). Redirect the slashless form with a 301. No query strings for content.")
    H.bullet("Caching.", "Cache HTML at the edge for anonymous visitors and purge on every publish. The investor home must weigh under about 1.5 MB on first load; today it is well under that.")
    H.bullet("Fonts and third parties.", "Poppins loads from Google Fonts with preconnect; you may self-host it instead. The only other third parties are TradingView (two script embeds) and the email form's endpoint. No tag manager, no pixels, no chat widget on this domain.")
    H.h("2a. Design: it matches ocalfinancial.ca")
    H.para("The investor site uses the live consumer site's design tokens, read from ocalfinancial.ca on 23 October 2026: Poppins body at 16px in #263340 on #FAFAFA; Outfit for headings, navigation, buttons and labels; Playfair Display italic for the accent word in hero headlines; navy #001240 panels and headings; green #017333 pill buttons (999px radius, 12px by 22px padding, 14px, weight 600); lime and mint accents for kickers; a white sticky header at 68px with the navy logo and a green pill; the dark #101510 footer at 72 percent white; 12px to 24px radii; the navy step cards with a small-caps step label. If the consumer site's tokens change, change them once in assets/css/style.css (the :root block) and the whole investor site follows. Fonts load from Google Fonts; self-host them if the consumer site does.")
    H.h("3. The pages: URL, title tag, meta description")
    H.para("These are built into each file. Keep them exactly; they carry the brand string 'TSXV: OCAL' that the SEO plan (document 05) depends on.")
    H.table(["URL", "Title tag", "Meta description"], [[s, t, dsc] for s, t, dsc in PAGE_SPECS], (W(1.3), W(2.3), W(3.2)), size=7.5)
    H.h("4. Widgets and accounts")
    H.table(["Widget", "Where", "What you do"], [
        ["TradingView mini overview", "Home, below the hero", "Already embedded (symbol TSXV:OCAL, 3-month range). No account needed. The fallback text under it links to TMX Money and Frankfurt; keep it, because a dead quote box is worse than none."],
        ["TradingView advanced chart", "Stock page", "Already embedded, daily candles, 6-month default, symbol locked. Fixed height of 520 px to prevent layout shift."],
        ["Email alert form", "Home, Stock, Financials, Operating metrics, Events, Contact, Subscribe", "Has creates the Brevo list with double opt-in and gives you the form action URL; paste it into SITE['form_action'] in content.py and rebuild (one string, seven blocks). Field name EMAIL. Until then the button opens an email to investors@ocal.ca with the visitor's address, so the block already works."],
        ["Investor call booking", "Home, Why OCAL, Leadership, Contact", "The buttons open an email to investors@ocal.ca with the subject 'Book a 30-minute investor call'. If Matthew later supplies a calendar link, it is one string (SITE['booking_link']) and a rebuild."],
        ["Hero photograph", "Home page", "assets/img/hero.jpg is a placeholder frame from an internal slide, heavily overlaid. Replace it with the consumer site's night-time car photograph or another OCAL-owned photograph with no text in it, 1920 px wide, under 250 KB, and keep the overlay; the headline must stay readable at every width."],
        ["Analytics", "Every page", "GA4 property for investors.ocal.ca (Has owns it). Add the gtag snippet to the head in the build template or via Cloudflare Zaraz. Events to configure: subscribe_submit, fact_sheet_print, deck_download, release_read (per-release page view), call_booked (outbound click to the booking link), quote_widget_click (TradingView iframe interaction is not trackable; track the TMX Money link instead)."],
        ["Search Console and Bing", "Domain level", "Verify investors.ocal.ca by DNS TXT in Google Search Console and Bing Webmaster Tools; submit sitemap.xml and news-sitemap.xml to both; add IndexNow (key file at the root, one POST per publish). Screenshots of both verifications to Matthew."],
    ], (W(1.4), W(1.5), W(3.9)))
    H.h("5. Redirects from ocalfinancial.ca")
    H.para("Every investor URL on the consumer site redirects one to one with a 301 the moment the new domain is live. Keep them for at least a year. The old release pages move to the new per-release pattern; until each release has its own page on the new site, redirect it to /news/.")
    H.table(["From (ocalfinancial.ca)", "To (investors.ocal.ca)"], [
        ["/investor-relations", "/"],
        ["/investor-relations/ and /investors and /investors/", "/"],
        ["/investor-relations/press-release/<slug> (19 pages)", "/news/<YYYY-MM-DD-slug>/ once built; /news/ meanwhile"],
        ["/investor-relations/press-release/press-release-ceo and press-release-director (the 18 March 2026 letters)", "/presentations/ (the letters are withdrawn; they still call OCAL a brokerage)"],
        ["Corporate presentation and fact sheet PDFs linked from the old page", "/presentations/ (the August fact sheet and any deck showing $6.88M are withdrawn; see document 03)"],
        ["/llms.txt on ocalfinancial.ca", "Rewrite it (document 03, section 4) so it no longer says 'auto finance broker' or 'One Click Auto Loan'. The new site has its own llms.txt."],
    ], (W(3.4), W(3.4)))
    H.para("On the consumer site: the Investors item in the main navigation and the footer link point to https://investors.ocal.ca/ with the anchor text 'Investors (TSXV: OCAL)'. Add the same link to the consumer footer's legal line. Remove the old investor page from the consumer sitemap after the redirect is live.")
    H.h("6. Release-page workflow (every news release, from the first one after go-live)")
    H.numbered("Wait for the wire.", "The release page goes live only after Newsfile has distributed it (TSXV Policy 3.3, CIRO). Shushu or Matthew sends you the final text and the Newsfile URL.", restart=True)
    H.numbered("Create the page.", "Add the release to content.py NEWS (date, headline, path, category) and add a page entry using the 3 November 2026 page (/news/2026-11-03-repossession-rate-and-agm/) as the pattern: kicker with date and dateline, headline as H1, sub-headline, body paragraphs as issued, quotes, operating performance section, About OCAL, investor contact, cautionary notes, s8.6 statement. The description is the release's first sentence, 140 to 155 characters, never the dateline.")
    H.numbered("Rebuild and publish.", "Run build_site.py; the news list, RSS feed, sitemap and news sitemap update themselves. Deploy. The new URL is permanent.")
    H.numbered("Tell the engines.", "IndexNow POST for the new URL; Search Console URL inspection and Request indexing for the new URL and the news index.")
    H.numbered("Tell the list.", "Has sends the release to the email list within the hour, linking to the new page and to SEDAR+.")
    H.numbered("Operating metrics.", "If the release is a monthly results release, its figures go into the Operating metrics history (content.py, same rebuild), exactly as released.")
    H.h("7. Schedule")
    H.table(["Day", "Milestone"], [
        ["Day 1", "Package received. DNS record requested from Matthew. Staging URL created from the site folder as delivered."],
        ["Day 2", "Staging URL to Matthew and Shushu. Email form wired if Has has the list ready; otherwise the email-request fallback stays."],
        ["Day 3", "Matthew's and Shushu's edits applied (via content.py), rebuild, placeholder count zero (it is zero today)."],
        ["Go-live", "DNS, HTTPS, redirects, consumer-site links, sitemaps submitted, IndexNow key in place. Acceptance checklist signed off. The 10 November 2026 results release is the first under the new workflow if the site is live by then."],
        ["Within 7 days", "Core Web Vitals check (PageSpeed Insights, mobile and desktop), Search Console coverage report clean, GA4 events firing, first weekly search-rank snapshot (document 05, section 2)."],
    ], (W(1.1), W(5.7)))
    H.h("8. Acceptance checklist (CQ signs each line, Matthew approves)")
    for line in [
        "All 18 URLs return 200 with the built title, description, canonical and JSON-LD; an unknown URL returns 404 with the 404 page.",
        "Every link on every page resolves; no # anywhere.",
        "TradingView widgets load and show TSXV:OCAL; fallback text visible beneath.",
        "Email form submits to the live list; a test subscription receives the double opt-in and the welcome email with the fact sheet attached or linked.",
        "Booking links open the calendar; mailto links open with the right address and subject.",
        "All ocalfinancial.ca investor URLs redirect with 301 to the mapped targets; the consumer Investors link points to the new domain.",
        "sitemap.xml, news-sitemap.xml, feed.xml and robots.txt are reachable and submitted; IndexNow key file present.",
        "Rich results test passes on the home (Corporation, WebSite, BreadcrumbList), FAQ (FAQPage) and the sample release (NewsArticle).",
        "Mobile: no horizontal scroll at 375 px; menu opens and closes; tables scroll inside their frame; KPI tiles stack.",
        "Print: /fact-sheet/ prints to one page from the browser with header, footer and buttons hidden.",
        "Lighthouse or PageSpeed: performance 90+, accessibility 95+, SEO 100 on the home and the stock page (mobile).",
        "No consumer scripts, chat widgets or lead-gen pixels on the investor domain.",
        "Placeholder count zero (python build_site.py prints it) and no yellow highlights anywhere.",
    ]:
        H.bullet("", line)
    H.h("9. The two go-live strings (there are no placeholders)")
    H.para("The build prints 'placeholders: 0'. Two values are swapped in content.py when the team has them, then rebuild: SITE['form_action'] (the Brevo form action URL from Has; empty today, which renders the email-request fallback) and, optionally, SITE['sedar_profile'] and the FILINGS links (today they open the SEDAR+ search page, where the issuer profile is found by searching 'OCAL Financial Inc.'; SEDAR+ refuses automated access, so a person captures the profile URL from a browser and pastes it).")
    closing()
    return save("%s 01 Investor site - master handoff for CQ (domain, build, SEO, go-live).docx" % STAMP)

# =====================================================================================================
# 02 HAS HANDOFF
# =====================================================================================================
def doc_02():
    H.new_doc("INVESTOR SITE  ·  HANDOFF FOR HAS", FOOT)
    H.band("Handoff for Has", "November 4, 2026  ·  investors.ocal.ca  ·  for Hasneen Jalil, copy CQ")
    H.kicker("Email list, vendor profiles, measurement, the monthly rhythm")
    H.para("CQ puts the site up. You make it work as a channel: the alert list that turns a visitor into a subscriber, the data-vendor profiles that still describe OCAL as a powersports and healthcare lender, the analytics that tell Matthew what investors read, and the monthly rhythm that keeps every date and number on the site current. Everything here is inside the rules: nothing is sent to the list before the wire has it, no vendor text goes out before Matthew approves it, and nothing promotional is bought.", size=10.5)
    H.h("1. The email alert list (this week)")
    H.table(["Step", "Detail"], [
        ["Tool", "Brevo (free to 300 emails a day) or Mailchimp free tier. One list: 'OCAL investor alerts'. Sender: OCAL Financial Investor Relations <investors@ocal.ca>, reply-to the same. Verify the ocal.ca sending domain (SPF, DKIM) so releases do not land in spam."],
        ["Consent", "Double opt-in, mandatory. Confirmation email text: 'Confirm your OCAL investor alerts. You asked to receive OCAL Financial (TSXV: OCAL) news releases, operating updates and filings by email. Click to confirm. Issued by OCAL Financial Inc., Suite 500, 885 Dunsmuir Street, Vancouver, BC V6C 1N5.' CASL requires the identification and an unsubscribe link in every message."],
        ["Segments (optional fields, never required)", "Investor type: individual, advisor or broker, fund, media, other. Used for reporting only."],
        ["Welcome email", "Subject: 'Welcome to OCAL investor alerts'. Body: three lines on what they will receive, the one-page fact sheet as a PDF attachment and a link to /fact-sheet/, the link to the Why OCAL page, the IR contact. No pitch beyond that."],
        ["Form", "Give CQ the embedded form action URL and the field name (EMAIL). CQ wires it into the seven subscribe blocks in one change."],
        ["Every release", "Within the hour of Newsfile distribution, never before: subject line is the release headline; body is the first two paragraphs, the operating update table if there is one, a link to the release page on investors.ocal.ca and to SEDAR+, the s8.6 statement, the unsubscribe line."],
        ["Every filing", "Audited statements, interims and the circular: one email the day they are filed, with the plain-language summary from the Financials page."],
        ["Targets", "250 confirmed subscribers by 21 January 2027 (90 days), 600 by 21 April 2027. Report the count in the monthly dashboard."],
    ], (W(1.6), W(5.2)))
    H.h("2. Fix the record: data-vendor profiles")
    H.para("Eight of fourteen data vendors still carry OCAL's pre-listing description (auto, powersports, RV, personal loans, auto repair and healthcare financing). The text is identical across Yahoo Finance, Stockhouse, Simply Wall St, StockAnalysis, Weiss, Wealth Awesome, MarketScreener and CNBC, and it comes from one upstream source, S&P Capital IQ. Google Finance shows 13.03 million shares and 'payment service provider'. CNBC lists Ronin's former officer as CEO. Fixing these is cheap and changes what every investor and every AI assistant reads first. Full vendor table with contact routes: research file C, Part 2d.")
    H.h2("The approved description (approved 4 November 2026: the About OCAL boilerplate of the 3 November release)")
    H.card("Standard, about 530 characters (for a 500 limit, drop the last sentence)", "OCAL Financial Inc.", "OCAL Financial Inc. (TSXV: OCAL; FSE: JC3) is a technology-enabled automotive financing and purchasing platform. Built around an approval-first approach, OCAL connects customers with suitable financing before sourcing a vehicle that fits their needs and budget. It holds no standing vehicle inventory, sourcing each vehicle only after approval through OPENLANE Canada, its auction and sourcing channel, and earns revenue from vehicle sales and related finance and protection products. It does not hold consumer loans or assume credit-default risk.")
    H.card("Short, one line", "For fields under 120 characters", "Technology-enabled automotive financing and purchasing platform, licensed in British Columbia and Alberta.")
    H.card("Facts", "The reference block (also at investors.ocal.ca/facts/)", "Legal name OCAL Financial Inc. (formerly Ronin Ventures Corp.). TSXV: OCAL (since 21 July 2026); Frankfurt: JC3, WKN A42K21. ISIN CA67449X1050; CUSIP 67449X105; LEI 984500E70698C2C2AC97. Head office Suite 500, 885 Dunsmuir Street, Vancouver, BC V6C 1N5; (604) 687-7765; investors@ocal.ca; investors.ocal.ca. Fiscal year end 31 August. CEO Mehdi Moghareh; Executive Chairman Matthew Friesen; CFO Terence Lee, CPA; Vice President of Sales Ryan McDonald; independent directors Michael Stier and Robert Birmingham. Auditor DMCL LLP; transfer agent Endeavor Trust Corporation; counsel Lawson Lundell LLP. Industry: automotive retail (online vehicle sales), secondary consumer finance.")
    H.h2("Fix order and routes")
    H.table(["#", "Where", "Route", "What to send"], [
        ["1", "Newsfile company page (OCAL controls it; on 4 November 2026 it still reads 'Canada's first fully virtual, AI-native licensed automotive finance platform')", "Newsfile account manager, via Shushu", "Standard description above; investor URL investors.ocal.ca"],
        ["2", "ocalfinancial.ca About page, llms.txt, JSON-LD", "CQ", "Same description; remove 'broker', 'One Click Auto Loan', 'brokerage'"],
        ["3", "S&P Capital IQ (feeds Yahoo, Simply Wall St, Investing.com, Stockhouse, Weiss, StockAnalysis)", "clientsupport@capitaliq.com or support.CIQ@spglobal.com, citing the 22 October release, the About page and the SEDAR+ Filing Statement; ask Shushu (Signal) or Integral to file it through a Capital IQ seat as well", "Standard description, CEO spelling 'Mehdi', fiscal year end 31 August, remove the Ronin 28 February series, industry classification"],
        ["4", "TMX Money and QuoteMedia", "issuer.services@tmx.com (replies in about 2 business days) and support@quotemedia.com", "Description (TMX Money shows none today), industry, website, listing date"],
        ["5", "Stockhouse", "support@stockhouse.com from an ocal.ca address", "Standard description (500-character limit, no links)"],
        ["6", "Morningstar", "dataquestions@morningstar.com", "Add the TSXV listing and the 31 August year end; their text is otherwise close"],
        ["7", "Google Finance", "'Send feedback' link on google.com/finance/quote/OCAL:CVE after items 3 and 6", "Share count 36,667,803; sector; description"],
        ["8", "Bloomberg, LSEG (Refinitiv), FactSet", "Through a broker or IR firm with a terminal (Shushu, Integral)", "Standard description and facts block"],
        ["9", "LinkedIn company page", "Super admin edit; request page verification", "Standard description in About; add 'TSXV: OCAL' to the tagline; remove the 'One Click Auto Loans' alias once verification allows"],
        ["10", "Crunchbase", "Claim via an ocal.ca login ('Manage My Company')", "Rename from the old trade name; standard description; OCAL roles only for people"],
        ["11", "LEI record (GLEIF)", "No action", "Checked 4 November 2026: status issued, legal address Suite 1600, 925 West Georgia Street (the registered and records office), headquarters Suite 500, 885 Dunsmuir Street. Correct as it stands."],
        ["12", "Wikidata (later, after the above)", "Create an item from an account that discloses its connection to OCAL; cite SEDAR+, the TSXV bulletin and GLEIF", "instance of business; official website; stock exchange TSXV with ticker OCAL and start date 2026-07-21; Frankfurt JC3; ISIN; LEI; headquarters Vancouver; inception 2021"],
        ["13", "Mehdi's LinkedIn profile", "Mehdi", "Title 'Co-Founder and Chief Executive Officer, OCAL Financial (TSXV: OCAL)' and the standard description; the profile still carries the old multi-product text"],
    ], (W(0.3), W(1.9), W(2.5), W(2.1)), size=7.5)
    H.para("Keep a log: vendor, date sent, route, date fixed. Report it in the monthly dashboard. Expect Yahoo to update within about 14 days of the S&P change.")
    H.h("3. Measurement")
    H.table(["Measure", "Source", "Cadence"], [
        ["Visits to investors.ocal.ca, pages per visit, top pages, countries", "GA4", "Monthly, first business day"],
        ["Events: subscribe_submit, deck_download, fact_sheet_print, release_read, call_booked", "GA4", "Monthly"],
        ["Confirmed subscribers, opens and clicks per release email", "Brevo or Mailchimp", "Monthly and after each release"],
        ["Search: impressions, clicks, average position for the brand queries in document 05, section 2", "Search Console", "Weekly for the first 90 days, then monthly"],
        ["Rank snapshot for the twelve tracked queries, logged out, google.ca", "Manual or a rank tracker", "At go-live, then days 30, 60, 90"],
        ["Share volume and price (context only, never a target)", "TMX Money", "Monthly"],
        ["Vendor profile log", "Section 2", "Monthly until all are fixed"],
        ["AI answer check: five prompts in ChatGPT, Perplexity, Gemini and Google AI Mode ('What is OCAL Financial?', 'What exchange is OCAL listed on?', 'OCAL Financial Frankfurt symbol', 'Who is the CEO of OCAL Financial?', 'Is OCAL Financial a car dealer?')", "Manual", "Monthly; a wrong answer points to the profile that still needs fixing"],
    ], (W(3.3), W(1.7), W(1.8)))
    H.h("4. The monthly rhythm (first business day of each month)")
    H.bullet("Dates.", "Events page: move past events down, add the next reporting deadline; Financials page: reporting calendar current; home page 'Updated' month in the footer (SITE['updated'] in content.py; CQ rebuilds).")
    H.bullet("Numbers.", "Stock page 'as at' date and any change in shares outstanding from the last release; Operating metrics history table after each release that carries the section; the 'funded deals' tile when a release updates it.")
    H.bullet("Documents.", "Presentations page: the deck and fact sheet carry a version date; anything superseded comes off the page; the old file is moved, not deleted.")
    H.bullet("Links.", "Run a link check on the domain; fix dead SEDAR+ links (SEDAR+ document links can change).")
    H.bullet("Report.", "One page to Matthew: the measures in section 3, what changed on the site, what is due next month.")
    H.h("5. Release day, in order")
    for i, line in enumerate([
        "Garrett's review and the CIRO pre-file are done (Matthew or Shushu confirms).",
        "Newsfile distributes, before 8:30 am Eastern where possible, with '(TSXV: OCAL) (FSE: JC3)' in the header and the investor URL at the foot.",
        "CQ publishes the release page on investors.ocal.ca and pings IndexNow and Search Console.",
        "You send the list email within the hour, linking to the release page and SEDAR+.",
        "LinkedIn company post from the corporate page: headline, one line, link to the release page (no commentary beyond the release text).",
        "Fifteen minutes later, check: Yahoo Finance press-release tab for OCAL.V, TMX Money news tab, Stockhouse, the release page in Google (search the exact headline in quotes).",
        "Log the release in the operating-metrics history if it carries the section.",
    ], 1):
        H.numbered("", line, restart=(i == 1))
    closing()
    return save("%s 02 Investor site - handoff for Has (email list, vendor profiles, measurement, rhythm).docx" % STAMP)

# =====================================================================================================
# 03 WORDING GUIDE
# =====================================================================================================
def doc_03():
    H.new_doc("INVESTOR SITE  ·  WORDING GUIDE", FOOT)
    H.band("Wording guide", "November 4, 2026  ·  lines that hold on investors.ocal.ca and in every release")
    H.kicker("For everyone who writes anything investors will read")
    H.para("The site, the releases, the deck, the fact sheet and the call script use the same words. This guide is the single list. When a line here changes, it changes in content.py first and everywhere else the same day.", size=10.5)
    H.h("1. Lines that hold")
    for l in C.LINES_THAT_HOLD:
        H.bullet("", l)
    H.h("2. Wording that goes, and what replaces it")
    H.table(["Goes", "Replaced by"], [
        ["'Asset-light automotive brokerage model'; 'broker'; 'brokerage platform'", "'Licensed motor dealer of record on every transaction, with no standing inventory and no loans on the balance sheet.' OCAL is not a broker."],
        ["'Zero inventory'; 'no inventory'", "'Zero standing inventory' or 'no cars on a lot'. A vehicle is on OCAL's books for three to five days between purchase and delivery, which is why the balance sheet shows a small inventory and floorplan balance."],
        ["'A digital inventory of 3,000+ vehicles' on its own; 'five auction supply channels'; 'OPENLANE, our exclusive auction and sourcing channel'", "'More than 3,000 vehicles visible on OPENLANE's Canadian marketplace on a typical day; OCAL owns none of them. OPENLANE is OCAL's auction and sourcing channel.' Never 'exclusive' (Garrett Lee, 31 October 2026)."],
        ["'Revenue comes from financing commissions'", "'Retail vehicle sales are about nine-tenths of revenue; finance, insurance and other income is the rest; the finance and protection layer carries most of the gross profit.'"],
        ["'Multi-trillion-dollar automotive ecosystem'; 'Canada's first'; any superlative", "A sized, sourced line: 'Canadians buy about three million used vehicles a year, more than $100 billion worth.' Superlatives only with a named third-party source on the page."],
        ["'$6.88M' or '$6.84M' FY2025 revenue", "'$6.48 million, audited (year ended 31 August 2025)'. The deck and fact sheet carrying $6.88M come off the site; Shushu's own deck is hers to send."],
        ["'Matthew Friesen, Chairman' or 'CEO'", "'Matthew Friesen, Executive Chairman and Director'. Mehdi Moghareh is Chief Executive Officer."],
        ["'Hasneen Jalil, CTO'; 'founder of Canada Auto Experts'", "'Hasneen Jalil leads technology and the demand engine'. Never CTO, and nothing about Canada Auto Experts or EasyPear until release 10 is issued."],
        ["'We acquired Canada Auto Experts and EasyPear' (with consideration)", "'Lead generation, the CRM and the AI sales agents run on one platform' until release 10 (scheduled 17 November 2026) is issued; then one sentence in the release's words."],
        ["Any share-price or valuation target; 'cheap'; 'undervalued'; 'one year of audited revenue'; 're-rating'", "Nothing. No valuation line of any kind, and no statement about who has been buying or selling the stock."],
        ["Monthly run-rate targets, break-even arithmetic, 'at 30 cars we make $1M', 'fixed costs of about $160,000 a month'", "Historical metrics only, in results releases, reconciled. Everywhere else the audited lines carry operating leverage: revenue up 18.8 percent, gross profit up 32.7 percent, operating expenses down 9.8 percent, 'the cost base is largely fixed'. No targets anywhere."],
        ["'Manitoba licence application filed'; 'licence expected in November'", "'Dealer permit application under way with the regulator; office inside the OPENLANE Winnipeg auction facility arranged; opening targeted for December 2026, when the permit is granted.'"],
        ["A rate without a period ('repossessions under one percent')", "'Fewer than one percent of the vehicle loans arranged from the first funded transaction in 2021 to 30 September 2026 have resulted in repossession (management information, lender reporting)'; the same period for 'about 99 percent funded'. The funded-deal count carries its definition sentence beside its first use on every page (NI 52-112)."],
        ["Cash balance between reporting dates; any FY2026 figure before the audit", "'Cash at each reporting date is in the filed statements.' 'Fiscal 2026 closed 31 August; audited results by 29 December.'"],
        ["'Guaranteed approval', 'approved in minutes', 'lowest rates' (consumer claims)", "Not on the investor site at all. Consumer wording lives on ocalfinancial.ca under its own rules."],
        ["Any named competitor (online retailers, dealer groups, lenders, other issuers) and any comparison to one", "Nothing. Industry statistics with a named source (Presidio-NCM, Cox, J.D. Power, TransUnion, Equifax, Angus Reid, Statistics Canada) carry the argument; other companies are never named or described on the investor site. Matthew's instruction, 23 October 2026."],
        ["Em dashes, en dashes", "Commas, colons, periods, parentheses."],
    ], (W(2.8), W(4.0)))
    H.h("3. The operating metrics, defined once")
    H.table(["Metric", "Definition (the release program's block, 23 October 2026)"], [
        ["Vehicles funded and delivered", "Retail vehicle sale contracts funded by a lender and delivered to the customer in the calendar month. Counted once, in the month the lender funds it."],
        ["Average vehicle selling price", "Vehicle sales revenue in the month divided by vehicles funded and delivered, before taxes and protection products."],
        ["Deal gross profit per vehicle (management basis)", "Gross profit on the vehicle plus finance, insurance and protection product income, per funded vehicle, before inventory write-downs and before the auction, reconditioning and transport costs that IFRS places in cost of sales. Split into vehicle margin and finance, insurance and protection income. Non-IFRS; management information."],
        ["Gross profit per vehicle (IFRS basis)", "Gross profit as reported in the financial statements for the month, divided by vehicles funded and delivered, with the items making up the difference from the deal basis stated beside it. Per-vehicle figures appear once the CFO confirms the vehicle counts from the ledger (30 October 2026)."],
        ["Gross margin", "Gross profit (IFRS basis) as a percentage of total revenue in the month. FY2025 audited: 12.5 percent."],
        ["Period and cadence", "Calendar month; the monthly results release after the month closes; October 2026 first, on 10 November 2026; each figure beside the prior month; monthly figures 'approximately'; once started, the series continues in weak months. No break-even arithmetic anywhere."],
    ], (W(1.6), W(5.2)))
    H.para("Master source: OCAL\\Press Releases\\02 Scheduled\\00 Release program 2026-10-23 - calendar, operating update block and drafting notes (internal).md. Terence settles the exact definitions once before the October update; they then never change, and the site's Operating metrics page is updated to match in the same rebuild.", size=8.5, color=H.MUTED)
    H.para("Non-IFRS note, verbatim, once per release and on the Operating metrics page: " + C.NON_IFRS_NOTE, size=9)
    H.h("4. Standard texts")
    H.h2("Forward-looking legend (site pages that carry plans)")
    H.para(C.FLI_LEGEND, size=9)
    H.h2("About OCAL (release boilerplate and vendor description)")
    H.para("OCAL Financial Inc. (TSXV: OCAL) (FSE: JC3) is a technology-enabled automotive financing and purchasing platform transforming how Canadians finance and purchase vehicles. Built around an approval-first approach, OCAL connects customers with suitable financing options before sourcing a vehicle that meets their needs and budget. Its integrated platform brings together credit assessment and financial guidance, lender matching, vehicle sourcing, digital transactions and home delivery anywhere in the provinces it serves, eliminating the need to visit a traditional dealership. OCAL holds no standing vehicle inventory; it sources each vehicle only after a customer is approved, through OPENLANE Canada, its auction and sourcing channel. OCAL earns revenue from vehicle sales and related finance and protection products, and does not hold consumer loans or assume credit-default risk. Licensed in British Columbia and Alberta, OCAL generated revenue of $6.48 million (audited) in the fiscal year ended August 31, 2025 and has completed more than 1,500 funded vehicle transactions to date. Investor information: investors.ocal.ca. (As issued 3 November 2026; the funded-transaction sentence carries its NI 52-112 definition in the release body.)", size=9)
    H.h2("llms.txt for ocalfinancial.ca (replaces the file that says 'auto finance broker')")
    H.para("OCAL Financial Inc. (TSXV: OCAL) is a licensed motor dealer in British Columbia (VSA D50207) and Alberta (AMVIC B2036050) that sells and finances used vehicles entirely online. Customers get pre-qualified with a soft credit check; the lender makes the final approval; OCAL then sources the vehicle through OPENLANE, its auction and sourcing channel, and delivers it. OCAL holds no standing inventory and no consumer loans. Operating since April 2021. Investor information: https://investors.ocal.ca/. Consumer application: https://ocalfinancial.ca/get-approved/auto.", size=9)
    H.h2("Title-tag pattern")
    H.para("'{Page} | OCAL Financial (TSXV: OCAL)' or the ticker inside the title, under 60 characters. Meta descriptions 140 to 155 characters, naming the ticker and what is on the page. Release pages: '{Headline} | OCAL Financial (TSXV: OCAL)'; description is the first sentence after the dateline.", size=9)
    H.h("5. Voice")
    H.bullet("Advocate, with the facts straight.", "Every OCAL document is written as the company's advocate: accurate facts, constructive framing, risks stated with what is being done about them.")
    H.bullet("Lead with the answer.", "Short sentences, one idea each. Numbers in tables or tiles, not stacked in prose. Concede real trade-offs (thin volume, early stage, going-concern note) before the reader finds them.")
    H.bullet("Sound like the founders.", "'We stock access.' 'Approval first, car second.' 'The failures all owned cars.' Pitches written from the founders sound like the founders; pitches written from decks sound like decks.")
    H.bullet("No filler.", "No 'leverage', 'seamless', 'ecosystem', 'journey', 'cutting-edge', 'game changer', 'in today's'. Canadian spelling. Numbers with a date and a source.")
    H.bullet("Same words everywhere.", "Release, page, deck, script, vendor profile. One set of definitions. One revenue figure. One title for Matthew.")
    closing()
    return save("%s 03 Investor site - wording guide and lines that hold.docx" % STAMP)

# =====================================================================================================
# 04 RELEASE TEMPLATE and 04a FILL-IN SHEET
# =====================================================================================================
def doc_04():
    H.new_doc("OPERATING UPDATE  ·  SITE COMPANION TO THE RELEASE PROGRAM", FOOT)
    H.band("Operating update: site companion", "November 4, 2026  ·  how the monthly block appears on investors.ocal.ca")
    H.kicker("The master template lives with the release program; this is the site side of it")
    H.para("The news release structure, the ten-release calendar and the operating update block were rebuilt on 23 October 2026 in the release program (OCAL\\Press Releases\\02 Scheduled, notes file 00; generator build_release_program_oct2026.py). This document does not repeat them. It shows how the block lands on the investor site, how a release becomes a page, and who does what each month so the release, the site and the email carry the same numbers on the same day.", size=10.5)
    H.h("1. Where the block appears on the site")
    H.table(["Place", "What is shown", "Updated"], [
        ["Home page, 'The audited results' section", "The audited FY2025 and FY2024 table today; from the first monthly results release, a line linking to the latest month on the Operating metrics page", "Same day as the release"],
        ["Operating metrics page, 'Monthly history'", "The latest month's table: vehicles funded and delivered, average vehicle selling price, gross profit per vehicle on both bases with the reconciling items, gross margin; prior month beside each", "Same day"],
        ["Operating metrics page, history table", "One row per month, plus the fiscal 2025 audited row, added as each release is issued", "Same day"],
        ["Operating metrics page, 'Definitions, fixed'", "The definitions exactly as settled with Terence and Lawson; the non-IFRS note", "Only if a definition changes, which it should not"],
        ["Release page (/news/YYYY-MM-DD-slug/)", "The release as distributed, including its operating update section and the definitions sentence", "When the wire has carried it"],
        ["Email to the list", "Headline, first two paragraphs, the table, links to the release page and SEDAR+", "Within the hour of the wire"],
    ], (W(2.0), W(3.4), W(1.4)))
    H.h("2. The block as it will read on the site, from the 10 November 2026 release")
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
    H.numbered("Add the release to content.py.", "One line in NEWS (date, headline, path, category) and one page entry on the pattern of the 3 November 2026 page; the description is the first sentence after the dateline.")
    H.numbered("Add the month to the metrics.", "The released figures go into the history table on the Operating metrics page (content.py, same change), exactly as released.")
    H.numbered("Rebuild and deploy.", "build_site.py updates the news list, RSS, sitemap and news sitemap; CQ deploys and pings IndexNow and Search Console.")
    H.numbered("Email and LinkedIn.", "Has sends the list email within the hour; the corporate LinkedIn post carries the headline and the link.")
    H.h("4. Who does what, each month")
    H.table(["Step", "Owner", "When"], [
        ["Pull and confirm the month's figures from the ledger", "Terence", "First two business days after month end"],
        ["Draft the operating update release from the program's content module", "Matthew (Shushu's version merged)", "Day 2 to 3"],
        ["Legal review and CIRO pre-file", "Garrett", "Before distribution"],
        ["Newsfile distribution, before 8:30 am ET", "Shushu", "Release day"],
        ["Release page, home block, history table, sitemap, IndexNow", "CQ", "Release day, after the wire"],
        ["Email to the list, LinkedIn post, fifteen-minute pickup check", "Has", "Release day"],
    ], (W(3.3), W(2.0), W(1.5)))
    closing("OWNER")
    path = save("%s 04 Operating update on the investor site - companion to the release program.docx" % STAMP)

    # 04a (the fill-in sheet for Terence) is no longer generated: superseded 4 November 2026, archived with a why-note.
    return path

# =====================================================================================================
# 05 SEO AND SEARCH PLAN
# =====================================================================================================
def doc_05():
    H.new_doc("INVESTOR SITE  ·  SEO AND SEARCH PLAN", FOOT)
    H.band("SEO and search plan", "November 4, 2026  ·  investors.ocal.ca  ·  for CQ and Has")
    H.kicker("Rank first for OCAL's own name, show up for the category, be read correctly by data vendors and AI assistants")
    H.para("On 23 October 2026 OCAL's own site did not appear in the top nine results for any of nine brand queries ('OCAL Financial', 'OCAL stock', 'OCAL TSXV', 'OCAL share price' and five more). Newsfile copies, Stockwatch, Yahoo, Investing.com (still under a Ronin URL) and auto-written stock pages hold those positions, and three of the queries are polluted by an Indian company called UCAL. The reasons are fixable: the old investor page served crawlers 1,300 characters of generic text, no page carried the brand string 'TSXV: OCAL' in its title, no structured data named the ticker, and the data vendors describe a different company. The new site fixes the on-site half on day one. This plan covers the rest. Full evidence and sources: research file C, Parts 2a to 2e.", size=10.5)
    H.h("1. The five moves that matter most")
    H.numbered("Real HTML, real titles, real data.", "Every page of the new site is static HTML with a unique title carrying 'TSXV: OCAL', a unique description, a self-referencing canonical, Corporation and WebSite JSON-LD with the ticker, ISIN, CUSIP, LEI and sameAs links, BreadcrumbList on every page, FAQPage on the FAQ, NewsArticle on every release, Event on the events page. The old page had none of this. Done in the build; CQ keeps it intact.", restart=True)
    H.numbered("Fix the data vendors at the source.", "S&P Capital IQ feeds Yahoo, Simply Wall St and probably Investing.com, Stockhouse and Weiss; one correction there repairs most of the web. Then TMX Money (which shows no description at all), the Newsfile company page (OCAL controls it), Morningstar, Google Finance. Document 02, section 2 has the approved text and the routes.")
    H.numbered("Build the entity layer.", "The /facts/ page states the same facts as the schema in plain text; LinkedIn, Crunchbase and later Wikidata carry the same description; the LEI record's address is aligned. This is what Google's knowledge panel and the AI answer engines read.")
    H.numbered("Own the exact brand string and push it into every release.", "'OCAL Financial (TSXV: OCAL)' in every title tag and H1; every news release ends with the investor URL so the wires, Yahoo and Stockhouse link to the page we want to rank; the consumer site links to investors.ocal.ca from its navigation and footer.")
    H.numbered("Fast, honest discovery.", "Sitemap with true lastmod, a Google News sitemap for releases, RSS, IndexNow for Bing, Search Console and Bing Webmaster Tools verified, a server-rendered latest-news block on the home so Googlebot finds new releases from a page it already visits. No Indexing API (not permitted for releases), no tricks.")
    H.h("2. The queries to own, and who holds them today")
    H.table(["Query", "Top results on 23 Oct 2026", "What it takes"], [
        ["OCAL Financial", "Newsfile release copies, Newsfile company page, Webull, Kalkine, Weiss", "Home page title 'OCAL Financial (TSXV: OCAL) Investor Relations'; Corporation schema; links from every release and the consumer site; vendor descriptions fixed"],
        ["OCAL stock", "Investing.com (Ronin URL), Yahoo OCAL.V, UCAL (India), Wealth Awesome", "Stock page title 'OCAL stock | TSXV: OCAL share price...'; live chart; capitalization table; Yahoo and Investing.com profiles corrected"],
        ["OCAL TSXV; TSXV:OCAL", "Stockwatch (Ronin-era items), Mining Stock Education copies of the LOI", "Ticker in every title; TMX Money description; Stockwatch URL field; new releases replace Ronin-era items over time"],
        ["OCAL share price", "Three UCAL pages, Wealth Awesome", "Stock page; TradingView and TMX links; Yahoo profile; time"],
        ["OCAL Financial investor relations", "Newsfile, Yahoo, Stockwatch; the old IR page at position 10", "Home page and site name; redirects from the old URL; Search Console"],
        ["OCAL Financial news; OCAL Financial stock; JC3 Frankfurt", "Wire copies; Yahoo JC3.F", "News index and per-release pages; Frankfurt listing on the Stock page and the facts page"],
        ["Category: asset-light car dealer stock; online car dealership stock Canada; used car financing company TSXV; Canadian Carvana stock; TSXV fintech auto finance stock", "Generic articles, Clutch and Canada Drives coverage, Carvana pages", "Why OCAL and How it works pages carry these phrases naturally; a later explainer page per theme ('What an asset-light car dealer is', 'The Canadian online car dealers compared') written as disclosure-safe editorial through the Lawson and CIRO path"],
    ], (W(1.6), W(2.6), W(2.6)), size=7.5)
    H.para("Tracker: record the top five for each query, logged out on google.ca, at go-live and on days 30, 60 and 90 (document 02, section 3).", size=9)
    H.h("3. Technical pattern (built; CQ maintains)")
    H.table(["Element", "Standard"], [
        ["URLs", "One root, flat second level, per-release pages /news/YYYY-MM-DD-slug/, lowercase, hyphens, trailing slash, no query strings; permanent once published; 301 for every change"],
        ["Titles and descriptions", "Document 01, section 3. Under 60 and 155 characters; ticker in every title; release description is the first sentence after the dateline"],
        ["Canonical", "Absolute, self-referencing, on every page; never cross-domain to the wire"],
        ["Structured data", "One @graph per page: Corporation (@id #org), WebSite, WebPage, BreadcrumbList; plus FAQPage, NewsArticle, Event, Person where the page warrants; must match visible text"],
        ["Sitemaps", "sitemap.xml with lastmod; news-sitemap.xml with releases from the last two days only; feed.xml RSS; all referenced in robots.txt and submitted"],
        ["robots.txt", "Allow all, including search-grounding AI crawlers (OAI-SearchBot, PerplexityBot); training crawlers (GPTBot, Google-Extended) allowed unless Matthew decides otherwise"],
        ["404", "Real 404 status with the built 404 page; no soft 404s"],
        ["Performance", "LCP 2.5 s or less, INP 200 ms or less, CLS 0.1 or less at the 75th percentile on mobile; TradingView loads in fixed-height boxes; images WebP with width and height; two font weights"],
        ["Images", "Alt text describes the content and names OCAL where it adds meaning ('OCAL Financial (TSXV: OCAL) share price chart'); decorative images alt empty"],
        ["Language", "en-CA only; no hreflang until a French section exists; never machine-translate disclosure"],
    ], (W(1.6), W(5.2)))
    H.h("4. Getting a release indexed quickly")
    H.table(["Method", "Verdict"], [
        ["Server-rendered latest-news block on the investor home and a link from the consumer home footer", "Do it. The strongest practical lever: Googlebot revisits the home often and follows the link."],
        ["XML sitemap with accurate lastmod; news sitemap", "Do it. Necessary, not fast on its own."],
        ["Search Console URL inspection, Request indexing", "Do it for each release; a handful a month; repeated requests do not help."],
        ["IndexNow", "Do it. Bing, Yandex and others index within hours; Google does not participate."],
        ["Google Indexing API", "Do not. Permitted only for job postings and live-stream pages; misuse can revoke access."],
        ["Google Publisher Center", "Not a route for a company newsroom."],
        ["The wire (Newsfile)", "The real route to Yahoo Finance, Google News and the aggregators; the 22 October release reached TMX Money, Stockhouse, MarketScreener and TipRanks within two minutes."],
    ], (W(3.0), W(3.8)))
    H.para("Realistic expectation: an OCAL release page is crawled within hours to a few days; Bing within hours via IndexNow; wire pages are indexed first because the wires have crawl priority. The release page wins over time because it is the permanent, linked, structured version.", size=9)
    H.h("5. AI answer engines")
    H.bullet("Google AI Overviews and AI Mode.", "No special markup or file is required; pages must be indexed and snippet-eligible, with important content in text form and structured data matching visible text. The facts page, the FAQ, the Stock page and the How it works page are written as the direct answers.")
    H.bullet("ChatGPT, Perplexity, Gemini.", "They cite pages they can fetch and prefer facts stated plainly and consistently across sources. Static HTML, one description everywhere, corrected third-party profiles. The llms.txt file on the new domain lists the facts and the pages; it is optional but costs nothing.")
    H.bullet("Measure it.", "Five prompts a month in each engine (document 02, section 3); a wrong answer points to the profile that still needs fixing.")
    H.h("6. Distribution")
    H.table(["Channel", "Role", "Note"], [
        ["Newsfile (TMX Newsfile)", "Primary wire; feeds Yahoo Finance, TMX Money, Stockhouse, MarketScreener, Bloomberg terminals, Google News via its partner pages", "Ticker in the header exactly '(TSXV: OCAL) (FSE: JC3)'; before 8:30 am ET where possible; investor URL at the foot; cost per release roughly $300 to $1,200 depending on circuit (third-party estimate; confirm with Newsfile)"],
        ["SEDAR+", "The filing of record", "Same day as the wire"],
        ["investors.ocal.ca", "The permanent, structured copy", "After the wire, never before"],
        ["Email list", "Direct to holders and prospects", "Within the hour; release text only"],
        ["LinkedIn company page", "Amplification", "Headline, one line, link; no commentary"],
        ["Stockwatch", "Fast Canadian pickup", "Optionally email the PDF to news@stockwatch.com once public"],
        ["Paid awareness, newsletters, influencers", "Not until the operating metrics have been published for two periods, and then only labelled 'paid advertisement on behalf of OCAL Financial Inc.' under BC rules and TSXV Policy 3.4", "Board decision; Signal is the IR firm of record"],
    ], (W(1.6), W(2.4), W(2.8)))
    H.h("7. Ninety-day plan")
    H.table(["When", "What", "Owner"], [
        ["Go-live week", "Domain, redirects, sitemaps, Search Console and Bing, IndexNow, GA4; rank snapshot day 0; Newsfile company page and ocalfinancial.ca About and llms.txt corrected", "CQ, Has"],
        ["Weeks 1 to 2", "S&P Capital IQ, TMX Money, Stockhouse, Morningstar corrections sent; LinkedIn and Crunchbase updated; first release under the new workflow", "Has, Shushu"],
        ["Weeks 3 to 4", "Google Finance feedback after upstream fixes; LEI address; rank snapshot day 30; Core Web Vitals field data check", "Has, CQ"],
        ["Weeks 5 to 8", "Wikidata item with sources; first AI-answer check; explainer page themes drafted for Lawson review", "Has, Matthew"],
        ["Weeks 9 to 13", "Rank snapshot day 60 and 90; report to Matthew: brand queries owned, vendor log, subscribers, downloads, calls booked; decide on explainer pages and on allowing or blocking training crawlers", "Has"],
    ], (W(1.2), W(4.3), W(1.3)))
    closing()
    return save("%s 05 Investor site - SEO and search plan.docx" % STAMP)

# =====================================================================================================
# 06 REVIEW DECK (all page copy)
# =====================================================================================================
def doc_06():
    H.new_doc("INVESTOR SITE  ·  ALL PAGE COPY (REVIEW DECK)", "REVIEW COPY  |  EDITS GO INTO content.py, THEN REBUILD  |  NOT FOR PUBLICATION")
    H.band("All page copy", "November 4, 2026  ·  investors.ocal.ca  ·  review copy for Matthew, Mehdi and Shushu")
    H.kicker("Every word on every page, in reading order")
    H.para("Mark up anything you want changed; the change is made once in the source and every page and document rebuilds from it. There are no placeholders; every figure is from the audited statements, the Filing Statement, the exchange record or an issued release. Widgets (chart, forms, lists) are noted in place.", size=10.5)
    for pg in C.PAGES:
        H.h(clean(pg["hero"]["h1"]) + "   (" + pg["slug"] + ")", before=18)
        H.para("Title tag: " + pg["title"], size=8.5, color=H.MUTED, after=0)
        H.para("Meta description: " + pg["description"], size=8.5, color=H.MUTED, after=6)
        H.kicker(pg["hero"]["kicker"])
        H.para(clean(pg["hero"]["sub"]), size=10.5, color=H.DARK)
        if pg["hero"].get("ctas"):
            H.para("Buttons: " + "  |  ".join(l for l, _, _ in pg["hero"]["ctas"]), size=8.5, color=H.MUTED)
        for b in pg["blocks"]:
            t = b[0]
            if t == "kicker": H.kicker(b[1])
            elif t == "h2": H.h2(clean(b[1]), before=10)
            elif t == "h3": H.para(clean(b[1]), bold=True, color=H.NAVY, before=6)
            elif t in ("p", "lead"): H.para(clean(b[1]))
            elif t == "note": H.para(clean(b[1]), size=8, color=H.MUTED)
            elif t == "kpis":
                cards = [(clean(f), clean(l), clean(c)) for f, l, c in b[1]]
                for i in range(0, len(cards), 4):
                    H.stat_cards(cards[i:i + 4])
            elif t == "bullets":
                for l, bd in b[1]: H.bullet(clean(l), clean(bd))
            elif t == "table":
                n = len(b[1]); widths = [W(6.8 / n)] * n
                H.table([clean(x) for x in b[1]], [[clean(str(c)) for c in r] for r in b[2]], widths, size=7.5)
                if b[3]: H.para(clean(b[3]), size=8, color=H.MUTED)
            elif t == "steps":
                for n_, ti, bd in b[1]: H.numbered(ti, clean(bd), restart=(n_ == "1"))
            elif t == "faq":
                for q, a in b[1]:
                    H.para(clean(q), bold=True, color=H.NAVY, after=1, before=4); H.para(clean(a))
            elif t == "cards":
                for k, ti, bd, href in b[1]: H.card(k, ti, clean(bd))
            elif t == "quote": H.para("\u201c" + clean(b[1]) + "\u201d  " + b[2], italic=True, color=H.DARK)
            elif t == "cta": H.card("Call to action", b[1], clean(b[2]) + "  Buttons: " + ", ".join(l for l, _, _ in b[3]))
            elif t == "widget": H.para("[Widget: " + b[1] + "]", size=8.5, color=H.LIME, bold=True)
    closing("REVIEW OWNER")
    return save("%s 06 Investor site - all page copy (review deck).docx" % STAMP)

# =====================================================================================================
# 07 RESEARCH SYNTHESIS
# =====================================================================================================
def doc_07():
    H.new_doc("INVESTOR SITE  ·  RESEARCH SYNTHESIS", FOOT)
    H.band("What we took from 33 investor sites", "November 4, 2026  ·  research synthesis  ·  four files in the research folder")
    H.kicker("Thirty-three sites, one afternoon, and where each idea landed")
    H.para("Four reviews ran in parallel on 23 October 2026: Canadian fintech, auto and TSXV investor sites (file A, ten sites); US auto retail, auto finance and marketplace peers (file B, ten sites); best-in-class and award-winning IR sites plus the SEO plan (file C, thirteen sites); and OCAL's own public record (file D). Every site was visited the same day; the files record what each does, what to copy and what to avoid, with URLs. This document is the synthesis: the ideas we took, who we took them from, and where they are on the new site.", size=10.5)
    H.h("1. The sites")
    H.table(["Group", "Sites"], [
        ["A. Canadian fintech, auto, TSXV", "goeasy, Propel Holdings, Chesswood (in wind-down), Mogo (now Orion Digital), AutoCanada, Kraken Robotics, VitalHub, WELL Health, E Automotive and Canada Drives and Clutch (how an online auto company describes itself), Quantum Critical Metals (the TSXV microcap pick, about $7M market value)"],
        ["B. US auto retail, finance, marketplaces", "Carvana, CarMax, Credit Acceptance, America's Car-Mart, Upstart, Open Lending, ACV Auctions, OPENLANE, CarGurus, Cars.com"],
        ["C. Best in class and award winners", "Shopify, Lightspeed, Constellation Software, Lemonade, Affirm, SoFi, Docebo, Calian (Best IR website, Canada 2025), Happen Bank (Best overall IR, small cap, US 2025), Lulu's (Notified showcase), Red Robin (Equisolve showcase), Shift and Vroom (what not to do)"],
        ["D. OCAL's public record", "ocalfinancial.ca investor pages, TMX Money, SEDAR+ mirrors, 22 Newsfile distributions, Frankfurt, 14 data-vendor profiles, 16 search queries, media and bullboards"],
    ], (W(1.9), W(4.9)))
    H.h("2. The ideas we took, and where they are")
    H.table(["Idea", "Taken from", "On the new site"], [
        ["Numbers with a definition and an as-of date under each, never a bare figure", "Propel, Calian, Affirm, Shopify, CarGurus", "KPI tiles on Home, Why OCAL, Financials; every table carries a source note and date"],
        ["Per-vehicle economics table with the denominator stated in a footnote, prior-year column, one sentence on what moved", "CarMax (gross profit per unit with % of sales), Carvana (GPU parts add to the total), America's Car-Mart (candour when units fall)", "Operating metrics page, home-page block, release template; definitions fixed once"],
        ["A dedicated, always-current operating-metrics page with history (none of the ten US peers has one)", "Gap in the peer group; Upstart's monthly page with definitions and 'preliminary' flag", "/operating-metrics/ with history table and chart frame"],
        ["Why Invest page with argument blocks and the forward-looking caution the peers omit", "Cars.com (structure), Propel (dated proof), Clutch (four-tile proof strip)", "/why-ocal/: nine numbered sections, market table with legend and assumptions"],
        ["Capitalization table with as-of date: shares, warrants by strike and expiry, options, fully diluted, escrow, insider ownership (no US peer has a standalone one)", "Quantum Critical Metals, Atlas Salt, WELL's share-structure layout", "/stock/ capitalization and escrow tables"],
        ["Live quote and chart from a free widget, with a text fallback so a dead widget never shows", "Plurilock and Quantum (TradingView), SoFi (sticky quote bar), Shift (the dead '--' warning)", "Home mini chart, Stock page advanced chart, fallback links to TMX and Frankfurt"],
        ["One row per period with every document, and a SEDAR+ link on the financials page", "VitalHub, goeasy, Carvana, Calian", "/financials/ documents table and reporting calendar"],
        ["Investor FAQ written from real questions, with FAQPage schema, the hard questions first", "WELL, Credit Acceptance (questions answered in writing), Open Lending and Cars.com (plumbing questions)", "/faq/: three hard answers first, then business, shares, plan"],
        ["Ticker in every title tag; unique meta descriptions; Corporation JSON-LD with tickerSymbol and sameAs", "Kraken, WELL, Quantum, Happen Bank, ACV; most sites reviewed have none", "Every page; schema graph in the build"],
        ["Double opt-in alerts in several places, named IR contact with direct email and phone, no form", "AutoCanada, Propel, goeasy, CarMax", "Subscribe blocks on seven pages; Contact page"],
        ["Governance on one page: committee matrix, documents list, insider ownership, whistleblower line", "AutoCanada, ACV, Lemonade, Docebo", "/governance/"],
        ["Events with dates, materials and the next reporting deadline; AGM materials shelf", "AutoCanada, Propel, Cars.com", "/events/ with Event schema"],
        ["A facts page and a standard description for vendors and AI engines", "Happen Bank's entity work; the vendor audit in file D", "/facts/ and llms.txt; the description pack in documents 02 and 03"],
        ["Dated, versioned documents; superseded versions withdrawn", "Kraken (dated deck), Carvana (dated introduction deck)", "/presentations/"],
        ["A printable one-page fact sheet", "Clutch's proof strip, the OCAL one-pager", "/fact-sheet/ with print styles"],
        ["Founder voice in the copy", "Lemonade's founders' letter, Constellation's president's letters", "Quotes and lines from Mehdi and Matthew across the site; a letter page is the next addition"],
    ], (W(2.6), W(2.1), W(2.1)), size=7.5)
    H.h("3. What we deliberately did not copy")
    H.bullet("Analyst tables and hosted research.", "OCAL has no coverage; an empty or padded list hurts. The site says so plainly and promises to list every analyst when one appears.")
    H.bullet("Enterprise IR platforms, iframes and two-domain stacks.", "They cost real money, split authority and leak other clients' text (seen on AutoCanada and E INC). One domain, static HTML, free widgets.")
    H.bullet("Mega-menus and modules that arrive empty.", "Carvana, CarMax and WELL run 16 to 35 destinations, several blank without JavaScript. OCAL has nine menu items and no page without content.")
    H.bullet("Non-GAAP stacks, guidance ranges and long-term targets.", "Carvana's and OPENLANE's reconciliations and outlooks suit large caps with analysts. OCAL publishes GAAP-based per-vehicle numbers, historical only, and keeps plans on one page under the legend.")
    H.bullet("Superlatives and comparative claims.", "'No. 1', 'largest', 'industry-leading' rest on third-party rankings. Every comparative on the new site is sourced or absent.")
    H.bullet("Named competitors.", "The peer sites and the first draft of this site used named online retailers and dealer groups as the cautionary tale. Matthew's rule of 23 October: no competitor is named or described on the investor site. The argument now rests on industry statistics with a source and on OCAL's own record.")
    H.bullet("Gated decks, contact-form-only IR, consumer promotions on investor pages, and stale 'as of' dates.", "The deck is a plain PDF, the IR contact is a named email, the consumer site is a link, and every number carries a date and an owner.")
    H.h("4. What the audit of OCAL's own record changed")
    H.bullet("Figures.", "Escrow 23,638,104; warrants 11,029,501 plus 39,760 finder warrants; options 600,000 plus 100,000 pending; fully diluted about 48.3 million; the July financing as 6,029,500 units for $1,507,375.")
    H.bullet("Contradictions removed.", "The old page said 'no inventory' and 'revenue from financing commissions'; the interim statements show $86,300 of inventory, a $222,033 floorplan balance and vehicle sales at 89 percent of revenue. The new site explains both in one paragraph each.")
    H.bullet("Wording.", "'Brokerage' still lives in two March 2026 letters, the consumer site's llms.txt and the Newsfile profile; all are listed for correction. The acquisition of the lead supplier has no news release, so the site does not state it.")
    H.bullet("Search.", "OCAL's own pages were absent from the top nine for every brand query; the SEO plan (document 05) starts from that fact.")
    H.h("5. Where to read more")
    H.table(["File", "What is in it"], [
        ["research\\A - Canadian fintech, auto and TSXV investor sites.md", "Ten site profiles, cross-site grid, top 12 ideas, five not to copy, recommended navigation and SEO pattern"],
        ["research\\B - US auto retail, auto finance and marketplace investor sites.md", "Ten site profiles, per-unit metric definitions from Carvana, CarMax and Car-Mart with latest values, the draft OCAL per-unit table, top 12, five not to copy, stale content seen on live peer sites"],
        ["research\\C - Best-in-class IR sites and the SEO plan.md", "Thirteen site profiles, ten design ideas, the full SEO plan: queries and who ranks, structured data with copy-ready JSON-LD, technical patterns, indexing methods with evidence, AI engines, the vendor table with contact routes, newswire distribution and the release-day checklist"],
        ["research\\D - OCAL public record audit.md", "The live investor page verbatim, every claim on it, TMX Money data, SEDAR+ figures, all 22 releases with URLs and which carry numbers, board and officers as publicly stated, share structure, named parties, 14 vendor profiles quoted and flagged, 16 search queries with top results, media coverage, a 24-item conflicts register"],
    ], (W(2.8), W(4.0)), size=8)
    closing()
    return save("%s 07 What we took from 33 investor sites - research synthesis.docx" % STAMP)


# =====================================================================================================
# 08 SELF-REVIEW AND SCORECARD
# =====================================================================================================
def doc_08():
    H.new_doc("INVESTOR SITE  ·  SELF-REVIEW AND SCORECARD", FOOT)
    H.band("Self-review and scorecard", "November 4, 2026  ·  the new site against the 12 October checklist and today's research")
    H.kicker("Scored the same way the old page was scored, by the same hand, with the same scepticism")
    H.para("On 12 October the live investor page scored 43 of 140 on a fourteen-element checklist built from the IR Magazine and Q4 best-investor-website criteria, NIRI and CIRI guidance and the TSX Venture issuer resources, reported as 38 of 100 after rounding for the quality of its FAQ and design. The same checklist is applied below to the site as rebuilt turnkey on 4 November 2026, with no placeholders, and at go-live once the domain, redirects and email list are live. (The 23 October delivery, with 54 placeholders open, scored 99 of 140.)", size=10.5)
    H.stat_cards([("38", "old page, 12 October", "43 of 140 points"), ("84", "4 November rebuild", "117 of 140; no placeholders, nothing live yet"), ("89", "at go-live", "124 of 140 with DNS, redirects and the email list live"), ("95", "reachable by January", "with the first two monthly results releases and the vendor fixes")])
    H.h("1. The fourteen elements")
    H.table(["#", "Element", "Old", "4 Nov", "Go-live", "Why, and what is still missing"], [
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
    H.bullet("Placeholders.", "None. The two strings that remain (the form action, a captured SEDAR+ profile link) are the team's to paste; nothing on the site is unverified, and nothing waits on a figure from anyone.")
    H.bullet("A new domain.", "Matthew's decision, and a clean one, but it costs ranking time. The redirects and the consumer-site links are the mitigation; they must go live at the same moment as the domain.")
    H.bullet("No plan table.", "The FY2027 to FY2030 plan table came off the Why OCAL page on 30 October 2026 under the investor narrative rules (no forecast, no growth-capital amount, no per-vehicle dollar figures). The page stands on the audited figures, the roadmap and the audited operating-leverage lines.")
    H.bullet("Thin history.", "One audited year, one interim period, one release page in the new pattern. The site is built to fill as the record grows; today it shows the shape more than the depth.")
    H.bullet("Nothing is live.", "A score on a staging folder is a forecast. The acceptance checklist in document 01 is where it becomes a fact.")
    closing("REVIEWER")
    return save("%s 08 Investor site - self-review and scorecard (38 to 89).docx" % STAMP)

# =====================================================================================================
def main():
    paths = [doc_00(), doc_01(), doc_02(), doc_03(), doc_04(), doc_05(), doc_06(), doc_07(), doc_08()]
    # dash check
    import docx as _d
    bad = []
    for p in paths:
        doc = _d.Document(p)
        txt = "\n".join(x.text for x in doc.paragraphs) + "\n".join(c.text for t in doc.tables for r in t.rows for c in r.cells)
        if "\u2014" in txt or "\u2013" in txt:
            bad.append(os.path.basename(p))
    print("dash violations:", bad or "none")
    if "--nopdf" not in sys.argv:
        for p in paths:
            try:
                print("pdf", H.export_pdf(p))
            except Exception as e:
                print("PDF failed for", os.path.basename(p), e)

if __name__ == "__main__":
    main()
