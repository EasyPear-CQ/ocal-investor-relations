# Best-in-class IR sites and the SEO plan for the OCAL investor site

Prepared 23 Oct 2026 for CQ and Has (investor site build). Author: Claude Code, working for Matthew Friesen. Every site and page below was visited on 23 Oct 2026 unless the entry says otherwise. This file is research only: nothing was sent, submitted, claimed or changed anywhere.

## 0. Read this first

### How the research was done, and its limits

- Sites were read with WebFetch, raw HTML (curl) and, where bot walls blocked those (Affirm, SoFi, Docebo), a real Chrome session. Vendor names are taken from script URLs and file names in the HTML where possible; a vendor named "inferred" was not stated on the page.
- Rendered colour, animation and true phone layout could not be observed on most sites and are marked "not verified". Fonts and hex values come from CSS and computed styles, not from screenshots.
- The "who ranks today" table in Part 2a comes from the WebSearch tool (a US search index), not from a live Google.ca results page. Treat positions as a proxy and have CQ repeat the check in a logged-out browser on google.ca before launch and again 30 days after (Part 2a has the checklist).
- Claims about search engines are tied to a source URL. Where no primary source exists (for example, how ChatGPT and Perplexity choose company facts) the text says so plainly and gives first-principles advice, not a claim of proof.
- Content rules applied to everything proposed here: OCAL role only for people (no outside roles); never "zero inventory" alone, use "zero standing inventory"; no "broker"; no "Canada's first"; no "digital inventory of 3,000+ vehicles" in titles, descriptions or schema until the CIRO query of 29 Sep is closed (see the vendor-text notes in Part 2d); FY2025 revenue $6.48M audited if a revenue figure is used at all.

### The ten design ideas worth copying (ranked)

1. **A two to six number "at a glance" strip with a definition line and an as-of date under each number.** Affirm uses two numbers, Shopify three, Happen four, Calian six, Lightspeed a dated grid. The definition and date are what make it credible, not the size of the number. For OCAL: units funded (trailing twelve months), average sale price, gross profit per vehicle, gross margin, median days lead to funding, FY2025 audited revenue $6.48M. Every figure footnoted to a filing or a release, historical only.
2. **A "Latest results" card that holds every document for the period in one place** (release, MD&A, financial statements, presentation, webcast, supplemental), plus a Download All ZIP (Shopify) and a per-quarter three-document card (Constellation). For OCAL, one card per period, file names in house style.
3. **A document matrix: type by year by quarter** (Calian's filings page, Constellation's 2007 to 2026 selector). Investors find a 2026 Q3 MD&A in two clicks. Add a SEDAR+ link beside it because TMX best practice asks for one.
4. **A sticky quote bar on every IR page** (SoFi) showing price, change and "delayed 15 minutes" with a timestamp. If the feed fails, fall back to a "view on TMX Money" link and never show a zero-filled quote (Shift's dead "--" widget is the warning).
5. **A dated update feed on the IR home** (Lemonade), mixing releases, results snapshots and event dates in order, with a short "Snapshot" bullet list for each quarter. For a company with few releases this makes the home look alive and gives search engines fresh text.
6. **A permanent Chairman or CEO letter page and a topic-titled Shareholder Q&A archive** (Lemonade's Founders' Letter, Constellation's President's Letters and Q&A). Cheap to run, and it is the page long-term holders bookmark.
7. **A real investor FAQ, 25 to 35 questions, in groups** (OCAL already has about 35). IR Magazine research puts an FAQ on only about 40 percent of IR sites, so it is a differentiator for a microcap. Add the transfer agent, auditor, fiscal year end, CUSIP and ISIN, dividends, DRIP, listings (TSXV and Frankfurt), how to buy, and how to get alerts (Shopify, Lightspeed, Lemonade all do these).
8. **Email alerts by content type with double opt-in** (Lightspeed, Docebo, Equisolve). Red Robin's alert form (an Equisolve client) also asks "individual, analyst, broker, portfolio manager, banker, media", so the list segments itself. Send only after wire dissemination (TSX electronic communications guidelines, Part 1 vendor section).
9. **A governance page with a committee matrix and a board skills matrix** (Lemonade, Docebo), plus a documents list (charters, code of conduct, whistleblower policy, insider trading policy). OCAL's governance is a strength after the 1 Oct board; show it.
10. **Native structured data and per-page metadata** (Happen's FAQPage and Corporation JSON-LD, Shopify's unique meta descriptions and investor sitemap). Most IR sites reviewed have none; this is where OCAL can beat them cheaply (Part 2b and 2c).

### Do not copy

- Script-only content that renders "Loading..." to crawlers (Lightspeed, Lemonade filings, Calian stock page).
- A hero that contradicts the company's current state (Shift archived; Vroom's legacy tagline).
- An FAQ that stops at transfer agent facts, or no forward-looking notice on the home page (Red Robin).
- Blank meta descriptions and one site-wide description (Lightspeed, Lulu's).
- Promotional consumer content mixed with investor content under the consumer header and footer. TMX best practice says keep them apart; OCAL's current investor page sits inside the consumer site.

### Proposed IR navigation for OCAL (synthesis, in this order)

Overview (Why invest) | Stock and Listings | News | Financials and Filings | Presentations and Events | Governance | Management | Letters and Q&A | FAQ | Email Alerts | Contact. Footer: SEDAR+ link, forward-looking information notice, privacy, link back to ocalfinancial.ca. Home modules top to bottom: one-line equity story and TSXV: OCAL, quote card, at-a-glance strip, latest results card, news feed, next event, alert box, Chairman and CEO line. Mobile: quote bar collapses to price and change; the at-a-glance strip becomes a two-column grid.

Design system notes pulled from the sites: one grotesque sans (Inter or Lato class) with a single accent colour; light background for dense financial pages and a dark hero only on the home (Shopify, Affirm); 15 to 25 percent of the page given to white space; tables with year filters and sticky headers; never more than two typefaces (OCAL already self-hosts Poppins, Outfit and Inter; use two of them in the IR section).

### The five SEO moves that matter most

1. **Make the investor section real HTML.** The raw HTML of the hub page https://ocalfinancial.ca/investor-relations holds about 1,300 characters of generic text, while the page a visitor sees holds a 35-question FAQ, a corporate table and a release archive (observed 23 Oct 2026 by comparing curl output with the rendered page read in a browser). Individual release pages are pre-rendered properly (about 9,600 characters on the Frankfurt release), so the gap is the hub and any page built the same way. Non-Google crawlers and many AI crawlers may not run JavaScript (an inference, not proven here). Server-render or statically generate /investors/ and every release. Also fix the soft 404 (a made-up URL returns HTTP 200 with a consumer-page title) and the per-release meta description, which today is only the dateline.
2. **Fix the data vendors at the source, starting with S&P Capital IQ.** Yahoo Finance and Simply Wall St both state that their profiles come from S&P Global Market Intelligence, and the powersports, RV and healthcare description appears word for word on Yahoo, Simply Wall St, Investing.com, Stockhouse and Weiss (Part 2d). One correction there repairs most of the web. Then TMX Money, Newsfile's company page, Stockhouse, Morningstar check.
3. **Build the entity layer.** One Corporation JSON-LD block on the investor home (tickerSymbol "XTSX OCAL", LEI via iso6523Code, sameAs to TMX Money, Frankfurt, Yahoo, LinkedIn, GLEIF, Wikidata), a Wikidata item, matching Crunchbase and LinkedIn text, and a /investors/facts/ page that states the same facts as the schema. Resolve the LEI address (West Georgia on GLEIF, Dunsmuir everywhere else) and the lapsed BVI entity with the identical legal name (Part 2d).
4. **Own the exact brand string and push it into every release.** "OCAL Financial (TSXV: OCAL)" in the title tag, H1 and boilerplate; every wire release ends with the investor URL (https://ocalfinancial.ca/investors/) so wires, Yahoo and Stockhouse link back to the page you want to rank. The OCAL site does not appear in the top results for any of the nine OCAL brand queries tested; the winners are Yahoo, Investing.com, Newsfile, Stockwatch and auto-written pages.
5. **Make discovery fast and honest.** XML sitemap with accurate lastmod plus a separate news sitemap, a server-rendered "latest news" block on the IR home (Googlebot finds new releases from a page it already visits often), Search Console and Bing Webmaster Tools verified, IndexNow for Bing and Yandex. Do not use the Google Indexing API for releases (it is limited to JobPosting and livestream pages, 200 requests a day by default). Google News and Yahoo placement comes from the wire, not from the company site (Part 2c and 2e).


# Part 1. Best-in-class IR sites reviewed

## Part 1 sites 1 to 4

Method note: raw HTML fetched with curl on 23 Oct 2026 and grepped for vendor strings, plus page text reads. Anything a static fetch cannot show (rendered colour, animation, true mobile layout) is marked "not verified".

### 1. Shopify

**URL:** https://www.shopify.com/investors (investors.shopify.com 301s here). **Visited 23 Oct 2026.** Subpages read: stock-information, quarterly-results, sec-filings, investor-faqs, email-alerts, board-of-directors, press-releases, events.

**What makes it good:** It is a native page set inside the corporate site, so brand, header and footer come from the main Shopify system, not a vendor skin. One screen answers "why invest, latest quarter, news, events, subscribe". Weakness: the email-alerts page has no form in the HTML read, only a hand-off to a vendor-hosted page.

**IR navigation (second-level bar, in order):** Overview; Podcasts; Financials (Financial Reports, Quarterly Results, SEC Filings, Annual Reports); News & Events (Press Releases, Events); Governance (Governance Documents, Board of Directors, Committee Composition); Resources (Stock Quote & Chart, Investment Calculator, Investor FAQs, Email Alerts).

**Hero:** small "Investor Relations" eyebrow, one-line mission headline, one dense paragraph, then a latest-podcast card with date and a Listen Now button.

**KPI strip:** three big numbers under "Why invest": merchants in 175+ countries, cumulative GMV of $1.6T, and US ecommerce share above 14%, each with numbered footnotes defining the measure and source. A themed list of about nine proof points sits beside it.

**Stock widget:** quote table (price, change, volume, intraday and 52-week range, open, previous close) for both NASDAQ:SHOP and TSX:SHOP, server-rendered. The chart is an image or iframe from api.nasdaqomx.wallst.com (Nasdaq / Wall St. on Demand), found in the stock page HTML. Quote feed vendor not verified. Email alerts and PDFs link to shopifyinvestors.gcs-web.com, which is the Q4 platform domain, so Q4 appears to be the content back end behind a custom front end (inference).

**Filings:** the SEC Filings page has a Group dropdown (3,4,5, annual, current, quarterly, registration, other), a year filter 2014 to 2026, and a table with date, form, description and HTML/PDF/RTF/XLS links. Canadian filings are routed to SEDAR+ by a note. Quarterly Results has a year selector 2015 to 2026 and per-quarter links: press release, 10-Q, supplemental, investor presentation, webcast, plus Download All (ZIP).

**News:** home shows the three latest releases and three events (with Webcast tags); "View all" goes to full lists.

**Subscribe:** persistent "Stay informed" band on home; the form itself is on a Q4-hosted page.

**Governance:** three pages: documents, directors (short bios, outside boards listed), committee composition.

**FAQ:** flat page, about 15 questions: exchanges and ticker, IPO date, HQ, fiscal year end, auditor, dividends (never), stock split, DRIP (none), transfer agent with postal, phone and email.

**Design:** large Shopify-Inter type, near-black teal panels with a bright green accent (#36F4A4 is the most frequent hex), generous white space, card layouts. CSS breakpoints at 1200, 900, 768, 640 and 600 px; viewport meta set. Mobile appearance not verified.

**SEO:** title pattern "Page Name - Shopify" (home: "Shopify Investor Relations: ..." plus tagline); every subpage has a unique meta description; canonical present; Open Graph present; no JSON-LD found; flat clean URLs /investors/{page}; a dedicated investors sitemap.xml with lastmod dates.

**OCAL should copy:**
- Dual-listing quote card (TSXV plus OTC) once the OTC symbol exists.
- Footnoted KPI strip of three numbers with a definition line each.
- "Latest earnings" row: release, webcast, presentation, supplemental, all on one card.
- FAQ answers for transfer agent, auditor, fiscal year, dividends, DRIP.
- A Download All ZIP per quarter.
- Unique meta description per IR page and an IR sitemap with lastmod.

### 2. Lightspeed Commerce

**URL:** https://investors.lightspeedhq.com/ (redirects to /English/overview/about-us/default.aspx). **Visited 23 Oct 2026.** Subpages read: Why invest, Stock info, Financial reports, Executive management, Investor FAQ, Email alerts, Newsroom, Governance documents.

**What makes it good:** a complete, conventional institutional site: every item an analyst expects is one click from a mega menu, with a French switch. Bad: dated Q4 Studio template, no meta descriptions, content loads by script ("Loading..."), so crawlers see little.

**IR navigation (in order):** Overview (About us, Why invest); Financials (Financial reports, SEC filings, SEDAR filings); Events and Presentations (Upcoming events, Product events, All events); Stock Info (Stock info, Analyst coverage); Management (Executive management, Board of directors, Committees, Governance documents); Newsroom; Sustainability; Resources (Email alerts, Investor FAQ, Contact us).

**Hero:** community-focused headline, NYSE and TSX tickers shown directly beneath, a video link, then News, Events and Reports feeds.

**KPI presentation:** Why invest has a "by the numbers" grid: LTM revenue, countries, organic growth, payments penetration, LTM GTV, ARPU per location, recurring revenue share, quarterly GPV, with a retail and hospitality mix donut and a note that figures are US dollars as of a stated date. Strongest dated KPI board of the four.

**Stock widget:** Q4 Inc. Confirmed in raw HTML: widgets.q4app.com scripts (q4.stockQuote, q4.chart, q4.historical-range, Highstock). NYSE and TSX quotes plus a historical range tool; analyst coverage on its own page.

**Filings:** Financial reports page with annual reports, a financial summary table and a quarterly archive; separate SEC and SEDAR pages. A hard-copy request link is offered.

**News:** year select plus category filter (All, Corporate, Earnings), featured article and recent list, English/French toggle.

**Subscribe:** dedicated page, email plus checkboxes: news, events, quarterly, annual, SEC filings, end of day quote; activation email (double opt-in); unsubscribe tab; explicit promise not to share data.

**Governance:** executive page with full bios (q4.person widget), directors, committees, documents list.

**FAQ:** accordion in Stock and Financial groups: how to invest, IPO dates and price, dividends, DRIP, CUSIP, fiscal year end, reporting currency, how to hear calls.

**Design:** Lato (Google Fonts), white pages, blue link colour (#005fcc), assets from assets.web.q4inc.com; a respond.js shim shows an older responsive method. Mobile not verified.

**SEO:** title pattern "Lightspeed - Section - Page"; no meta description, canonical or JSON-LD on any page checked; URLs are deep .aspx paths with a language folder.

**OCAL should copy:**
- Dated "by the numbers" grid with currency and as-of note.
- Alert checkboxes by content type, end-of-day quote option and double opt-in.
- CUSIP and IPO facts in the FAQ.
- Analyst coverage page (when coverage exists).
- Newsroom category filter.
- Avoid: blank meta descriptions and script-only content.

### 3. Constellation Software

**URL:** https://www.csisoftware.com/investor-relations/ (home https://www.csisoftware.com/). **Visited 23 Oct 2026.** Subpages read: Leadership Team, Latest News, President's Letters, Shareholder Q&A.

**What makes it good:** radically minimal and credible: no promotional chrome, no stock widget, no alerts; trust comes from 20 years of reports and candid letters. Bad: no quote, no calendar, no FAQ, no subscribe, so a new investor cannot self-serve basics.

**Navigation (header, in order):** About Us (Leadership Team, ESG); Being Acquired; Operating Groups; Investor Relations; News. Footer repeats these plus Privacy, Cookie Preferences, Contact. IR is a single page, not a section.

**Hero (home):** acquirer positioning headline, three "philosophy" cards (autonomy, talent, resilience), animated counters (years, acquisitions, countries, employees, customers, shown as 0 in static HTML). Home also embeds the Earnings Reports block and four latest news items.

**KPI presentation:** corporate counters only; financial numbers live in the Shareholder Report PDFs, not on the site.

**Stock widget:** none found (no quote, vendor or widget strings in raw HTML; TSX: CSU appears only as text). Site is WordPress with GeneratePress Pro and GenerateBlocks, built by Blue Flamingo.

**Filings:** year selector 2007 to 2026 above a card per quarter with three PDFs: MD&A, Shareholders Report, Financial Statements. AGM block with recording, user guide, proxy form, circular and notice. Statutory filings (prospectus, AIF) is a category on a generic document listing (/generic-document/?category=...).

**News:** list with Select Year (2008 to 2026) and filter by General, Regulatory and Transaction announcements; newest item 21 Oct 2026.

**Subscribe:** none. Only the WordPress RSS feed (/feed/) exists.

**Governance:** Leadership Team page (management and board), a corporate documents category, an ESG page. Not in the IR page itself beyond the documents tile.

**Investor FAQ:** replaced by a Shareholder Q&A archive with dated entries named by topic, and annual President's Letters. The letters list as served shows gaps (not verified whether more load dynamically).

**Design:** Plus Jakarta Sans and Google Sans files hosted locally; light, text first; breakpoints at 1250, 1024, 767 and 500 px. Colours not verified.

**SEO:** keyword titles ("... Investor Relations & Financial Reports"), unique descriptions on home, IR, news and leadership; generic document pages have none; Organization JSON-LD on home, but a LocalBusiness block has a malformed "www.www" URL and a different address from the footer; sitemap index (post, page, corporate-material); /wp-json left open.

**OCAL should copy:**
- A Chairman's letter archive and dated shareholder Q&A, titled by topic.
- Per-quarter three-document cards (MD&A, report, statements).
- Year selector on every archive.
- Announcement filter: General, Regulatory, Transaction.
- Do not copy the absence of a quote, alerts and FAQ.

### 4. Lemonade

**URL:** https://www.lemonade.com/investor (investor.lemonade.com 301s here; an old Q4 path investor.lemonade.com/home/default.aspx is still referenced in the HTML). **Visited 23 Oct 2026.** Subpages read: stock-information, quarterly-results, faq, governance, filings, news, events, founders-letter.

**What makes it good:** reads like a product: one running "updates" feed on home mixes earnings snapshots, call registrations, social posts, board news and milestones in date order. Quarterly snapshot posts give bullet KPIs. Bad: filings and news pages render "Loading..." client-side, so little static content.

**IR navigation (in order):** Feed; Quarterly Results; News; Events; Stock Info; Filings; Governance; Founders' Letter; FAQs. Product links (Renters, Homeowners, Car, Pet, Life, Giveback) sit in the top bar above it.

**Hero:** a welcome line, an AI insurer summary, three buttons: Investor Presentation, Finance Dashboard, latest earnings call.

**KPI presentation:** each quarter's "snapshot" post lists in-force premium and growth, revenue, gross profit, customers, adjusted free cash flow, loss ratio, then a "looking forward" guidance block. The Quarterly Results page is a year grid with Shareholder letter, Earnings call, 10-Q or 10-K per quarter.

**Stock widget:** quote numbers are baked in at build time (Next.js static data with a lastUpdated stamp and a "delayed 20 minutes" note); the chart is a TradingView widget iframe (confirmed in HTML). Quote data source not verified. Events use events.q4inc.com registration links. Analyst coverage table on the same page.

**Filings:** short; Annual Report and Proxy links plus a dynamically loaded list.

**News:** news page plus the home feed; events page with Upcoming and Past, earnings calls at 8:00 AM ET.

**Subscribe:** footer form "Subscribe to Lemonade Updates" on every IR page, email only.

**Governance:** one page: executive management, board with outside roles, committee matrix (chair and member marks), six governance documents.

**FAQ:** about 15 items: exchange, HQ, incorporation, fiscal year, DSPP, CUSIP, dividends, transfer agent with contacts, counsel, auditor, headcount (dated), where to find reports.

**Design:** Lato body with Merriweather serif accent, light grey (#F4F4F4) panels on white, brand-led; breakpoints at 1025, 767 and 355 px. Mobile not verified.

**SEO:** title "Lemonade Inc. - Page"; unique meta descriptions on all eight pages; canonical and Open Graph; only BreadcrumbList JSON-LD; investor URLs not listed in the main sitemap.xml; clean /investor/{page} paths.

**OCAL should copy:**
- Home feed with dated "Snapshot" posts: five KPI bullets, guidance, link to the letter.
- Founders' Letter page as a permanent landing page.
- Footer subscribe on every page.
- Committee matrix on governance.
- "Pricing delayed" note with timestamp.
- Event cards that link straight to registration.

## Part 1 sites 5 to 8

Method note: curl and WebFetch were blocked on Affirm (Akamai 403) and intermittently on SoFi and Docebo (Cloudflare challenge). All three were reviewed in a real Chrome session (page text, computed styles, DOM and script URLs). Mobile behaviour was not tested on any site ("not verified"). Visited 23 Oct 2026 for every site.

### 5. Affirm

**URL:** https://investors.affirm.com/ (subpages visited: /stock-information/stock-quote-chart, /financial-information/quarterly-results, /investor-resources/investor-faqs, /investor-resources/email-alerts, /corporate-governance/management, /news-events/newsroom). **Visited:** 23 Oct 2026.

**What makes it good:** Brand-led and calm. One dark page, two huge numbers, and a clear path to the latest earnings and annual report. It treats the IR site as an extension of the consumer brand rather than a filings dump. Weak spots: the quote page is thin, and the home has no price ticker.

**IR navigation (in order):** Home; News & Events (Events and Presentations, Newsroom); Stock Information (Stock Quote & Chart); Corporate Governance (Management, Board of Directors, Committee Composition, Documents & Charters, Fact Sheet, Affirm Cares, Corporate Impact Reports); Financial Information (SEC Filings, Annual Reports, Quarterly Results, IRS Form 8937, EU country-by-country reporting); Investor Resources (Fact Sheet, Financial Safeguards One-Pager, Investor FAQs, Email Alerts, Contact IR).

**Hero:** Full-bleed dark navy page (body about #13131F, white text), H1 at 80px, short mission paragraph, then a "by the numbers" block.

**KPI presentation:** Two animated counters only (active consumers, gross merchandise volume), each with a one-line definition and a footnote stating the LTM basis and the quarter-end date. Definitions beside the numbers are the credibility device.

**Stock widget:** Platform is Nasdaq IR Insight. Evidence: Drupal markup, module path /profiles/nasdaqir/, "sites/g/files" asset paths. The quote table (price, change, volume, day and 52-week range) is footed "Minimum 15 minutes delayed. Source: LSEG".

**Filings:** Quarterly results are grouped by quarter, each with an earnings call, supplement, shareholder letter, release, 10-Q or 10-K, transcript and historical financials, with a "Show all" control. Annual reports appear as PDF tiles on the home.

**News:** Newsroom with a featured article, image cards and accordions. Home shows the three latest with dates in "October 5, 2026" format.

**Subscribe:** Email Alerts form with ten checkboxes: Quote, SEC Filing, Event, News, Investor News, Product News, Partnership News, Explainers & Perspectives, Consumer & Merchant Insights, and a Weekly Summary Email, plus an unsubscribe-all form.

**Governance:** Management and board pages are bios with names and titles; committee composition and documents are separate pages.

**FAQ:** Long FAQ page with numbered questions grouped by topic (about 28 accordion items) and a "Show All" toggle.

**Design notes:** Fonts AxiformaForAffirm with Calibre fallback; generous whitespace, very large type, light density. Mobile not verified.

**SEO:** Title "Investor relations | Affirm Holdings, Inc." with subpages as "Stock information | ...", "Quarterly results | ..." (sentence case, pipe separator). Home has a meta description and canonical; subpages showed none. Open Graph is present, but og:url points to /investor-relations while the canonical is the root (minor inconsistency). JSON-LD @graph with Organization, WebPage, WebSite. URLs are clean and extensionless.

**OCAL should copy:**
1. A two-to-four number "by the numbers" block with a one-line definition under each and a dated footnote.
2. Sentence-case title pattern "Page | Company" plus Organization, WebPage and WebSite JSON-LD.
3. Alert checkboxes split into investor news versus product news, plus a weekly digest option.
4. A one-page fact sheet linked from both the nav and the home hero.
5. FAQ grouped by theme with a Show All toggle.

### 6. SoFi

**URL:** https://investors.sofi.com/ (redirects to /overview/default.aspx; subpages: /stock-information/, /financials/quarterly-results/, /resources/investor-faqs/, /governance/committee-composition/, /news/Press-Releases/). **Visited:** 23 Oct 2026.

**What makes it good:** Utility first. A live price bar sits on every page, and the quarterly results page opens with the full press release, so an analyst gets the headline numbers without opening a PDF. Weaknesses: no KPI block on the home, and leadership bios live on the corporate site.

**IR navigation (in order):** Overview; News (Press Releases, Blogs); Events & Presentations; Stock Information (Stock Quote, Stock Chart, Analyst Coverage, Annual Meeting & Proxy Statement); Financials (Quarterly Results, SEC Filings, Forms 8937); Corporate Responsibility (Governance Documents, Leadership, Committee Composition, Corporate Responsibility Report); Resources (Investor FAQs, Investor Email Alerts, Investor Contacts, Feedback Form).

**Hero:** Latest press release headline as a banner, then a short corporate overview (mission, founded 2011). No image-led hero copy beyond that.

**KPI presentation:** None on the home. KPIs appear as the bullet list at the top of each quarterly press release (members, products, originations, guidance).

**Stock widget:** Q4 Inc. Evidence: footer "Powered By Q4 Inc." with a version string, scripts from s27.q4cdn.com and widgets.q4app.com, evergreen.q4Api modules, Highcharts. Sticky ticker bar on every page. The stock page has a quote table, a Highcharts chart (1m, 3m, 6m, YTD, 1y, All, date pickers, news-release flags) and a historical price table.

**Filings:** Quarterly results use tabs by quarter (Q2 2026, Q1 2026, Q4 2025 and so on) that render the whole release in-page. The home shows one block with presentation, release, webcast, transcript and 10-Q.

**News:** Home shows three items with MM/DD/YYYY dates and "View all". Press Releases and Blogs are separate lists.

**Subscribe:** Home footer form: News, Events & Presentations, Quarterly Reports, Annual Reports, SEC Filings, End of Day Stock Quote, plus Unsubscribe.

**Governance:** Committee composition is a matrix of directors against four committees with Chair and Member labels. Leadership links out to sofi.com.

**FAQ:** About 15 accordion questions with a Display All control, including warrant FAQs and a quiet-period policy.

**Design notes:** Fonts larsseit and TTNorms. H1 about 60px, H2 48px, deep purple headings (about #201747), cyan links (about #00A9CE), grey body (#53565A), 16px. Mobile not verified.

**SEO:** Titles follow "Company (TICKER) - Section - Page". No meta description, canonical, Open Graph or JSON-LD observed. URLs use the Q4 pattern ending in /default.aspx.

**OCAL should copy:**
1. A sticky one-line quote bar on every page.
2. A chart with 1m, 3m, 6m, YTD, 1y and All buttons and news-release markers.
3. A results page led by 5 to 7 bullet KPIs, with the release rendered in-page.
4. A committee matrix table.
5. "End of Day Stock Quote" as an alert type.

### 7. Docebo

**URL:** https://investors.docebo.com/ (301 to https://www.docebo.inc/home/default.aspx; subpages: /why-invest/, /news/, /stock-information/stock-quote/, /financials/financial-reports/, /governance/executive-management/, /resources/investor-emails-alerts/). **Visited:** 23 Oct 2026.

**What makes it good:** A TSX and Nasdaq dual-listed company showing both quotes at once, a clean modular home, and a double opt-in alert system. Weaknesses: Why Invest is two paragraphs with no numbers, and there is no FAQ in the nav. Docebo was also a 2025 Canada nominee for best overall IR (small cap) in the awards list cited under 8a.

**IR navigation (in order):** Home; Why Invest; News; ESG; Events and Presentations (Events Calendar, Presentations); Stock Information (Stock Quote, Stock Chart, Historical Stock Quote, Analyst Coverage); Financials (Financial Reports, SEC Filings, Sedar Filings); Governance (Executive Management, Board of Directors, Committee Composition, Board Skills Matrix, Governance Documents); Resources (Information Request Form, Investor Emails Alerts, Investor Contacts).

**Hero:** White 60px H1 over a banner, a TSX and Nasdaq price strip, then a corporate profile paragraph with "Read more" to Why Invest.

**KPI presentation:** None observed in the page text, although counter-animation scripts (jquery.counterup, waypoints) are loaded, so a KPI block may have been used before or be hidden.

**Stock widget:** Q4 Inc. Evidence: "Powered by Q4 Inc." in the footer, the widgets.q4app.com/widgets/q4.stockQuote script, s24.q4cdn.com assets, and a Content-Security-Policy listing Q4 hosts and Highcharts. Separate TSX and Nasdaq quote blocks with a 20-minute delay note.

**Filings:** Financial reports are an accordion with a "Select Year" dropdown. Each quarter offers financial statements, MD&A, release, webcast and presentation. A note states the fiscal year end, USD, and unaudited status. SEDAR and SEC links are separate pages.

**News:** Year dropdown (2019 to 2026) with a count line, date, headline and "Read More", MM/DD/YYYY dates. Home shows the three latest.

**Subscribe:** Email plus three alert types (News, Events and Presentations, End of Day Stock Quote), CAPTCHA, an activation email, a no-third-party-sharing statement, and a separate unsubscribe form.

**Governance:** Executive management as name, title and bio blocks; a board skills matrix has its own nav entry (page content not verified).

**FAQ:** None; an Information Request Form replaces it. A named IR contact (VP Investor Relations) and a separate M&A mailbox appear on every page.

**Design notes:** Figtree for text, Special Gothic Expanded One for headings, IBM Plex Mono for numerals. Navy headings (about #002B80), violet accent (about #7E2EE9), 36px H2. Mobile not verified.

**SEO:** Titles "Docebo Inc. - Page". No meta description, canonical or JSON-LD observed. Cross-domain 301 from investors.docebo.com to docebo.inc.

**OCAL should copy:**
1. Dual quote blocks if OCAL later lists on an OTC or US venue.
2. A Board Skills Matrix page.
3. Double opt-in alerts with a clear privacy line.
4. A named IR contact plus a separate partnerships mailbox on every page.
5. A "figures in CAD, unaudited" note above the reports.

### 8a. Calian Group (award winner: Best IR website, Canada 2025)

**Award source:** https://www.ir-impact.com/event/ir-impact-awards-canada-2025/ (event held 3 Apr 2025, Fairmont Royal York, Toronto; winner list PDF https://www.ir-impact.com/wp-content/uploads/2025/04/Canada-Awards-25-List-of-winners-and-nominees.pdf). The awards now run under the "IR Impact" name at ir-impact.com; earlier years were branded IR Magazine Awards. Nominees were AtkinsRealis, Cenovus Energy, D2L, Fortuna Mining and Roots. Calian also won Best IR officer (small cap).

**URL:** https://investors.calian.com/ (subpages: /financial-information/, /press-releases/, /events-presentations/, /stock/, /governance/). **Visited:** 23 Oct 2026.

**What makes it good:** A TSX small cap with a purpose-built site: a six-metric "at a glance" strip, an investor kit with file sizes, nine investment considerations and a named IR director with credentials. Weaknesses: heavy client-side rendering; the /stock/ page rendered blank in my Chrome session, and several lists showed "Loading".

**IR navigation (in order):** Investors; Financials; News; Events & Presentations; Shares; Governance; More; EN/FR toggle; link back to the corporate site.

**Hero:** Short mission statement, a featured news item, a CEO video interview prompt, then the latest earnings block (financial statement, MD&A, call presentation).

**KPI presentation:** "At a glance" shows six numbers (revenue, gross margin, adjusted EBITDA, workforce, new contract signings, backlog), then three charts: revenue, gross profit and margin, adjusted EBITDA and margin. Four growth pillars follow.

**Stock widget:** Custom, not a vendor module. The compiled front.js calls a function named queryAlphaAdvantageStockChart with symbol TSX:CGY, so the data source is probably Alpha Vantage (inferred from the function name) behind a first-party API. Labels: delayed pricing, today's change, volume, 52-week range; daily, weekly and monthly series. No vendor script strings were present in the HTML.

**Filings:** A matrix: document type rows (press release, financial statements, MD&A, call presentation, call audio, call transcript) against year, with Q1 to Q4 chips. This is the best filings layout seen in this batch.

**News:** A featured release plus filters (search, industry, year), with a disclaimer that releases may be superseded.

**Subscribe:** "Subscribe to IR distribution list" button (modal form; a Gravity Forms script is present, so likely Gravity Forms, inferred).

**Governance:** Mandates and policies as PDF lists in five sections (board mandates, governance, environmental, social, organizational documents); board member cards load dynamically (content not verified).

**FAQ:** 18 numbered questions on the stock page (fiscal year, CUSIP, dividends, DRIP, transfer agent).

**Design notes:** Plus Jakarta Sans, white background, dark grey text, 16px, light density, bilingual EN and FR.

**SEO:** WordPress with Yoast. Titles "Calian Group Investor Relations - Home", "Calian Group Stock Price & Shares - Investor Relations" (descriptive, keyword-led), but news and financial pages use a generic "Page - Investor Relations" form. Home and stock have meta descriptions; Open Graph present; JSON-LD has WebPage, BreadcrumbList, WebSite with SearchAction, and Organization.

**OCAL should copy:**
1. The "at a glance" six-number strip with three trend charts.
2. The document-by-year-by-quarter matrix.
3. An investor kit block with file sizes and "Download All".
4. A list of key investment considerations.
5. A keyword-led stock page title and description.

### 8b. Happen Bank, formerly LendingClub (award winner: Best overall IR, small cap, US 2025)

**Award source:** https://www.ir-impact.com/wp-content/uploads/2025/03/US-Awards-25-List-of-nominees-and-winners-v2.pdf (US awards 26 Mar 2025, New York; event page https://www.ir-impact.com/event/ir-impact-awards-us-2025/). This is an overall IR award, not the website category (that went to United Therapeutics, a large cap, not reviewed).

**URL:** https://ir.lendingclub.com/ redirects to https://ir.happen.com/overview/default.aspx (subpages: /stock-info/stock-quote/, /financials/quarterly-results/, /resources/investor-faqs/, /resources/investor-email-alerts/). **Visited:** 23 Oct 2026. The company's Q2 2026 release states it rebranded from LendingClub (Nasdaq: HAPN).

**What makes it good:** A fresh Q4 build with structured data, a four-KPI "Why Invest" block and a sticky quote bar. Weakness: the site looked mid-migration (default link colours in places, Leadership still linking to lendingclub.com).

**IR navigation (in order):** Overview; News & Events (News Releases, Events & Presentations); Stock Info (Stock Quote, Analyst Coverage); Financials (Quarterly Results, SEC Filings); Governance (Governance Documents, Leadership, Committee Composition); Resources (Investor FAQs, Investor Email Alerts, Investor Contacts).

**Hero:** White 80px H1 in Rethink Sans over a banner, then a short positioning paragraph aimed at a defined customer segment.

**KPI presentation:** "Why Invest" with four counters: 5M+ members, $100B+ lifetime originations, a 4.7-star Trustpilot rating, and more than 90% of loans fully automated. It mixes scale, trust and efficiency.

**Stock widget:** Q4 Inc. Evidence: q4cdn and q4app assets, and JSON-LD naming Q4 Inc as sdPublisher. Sticky ticker bar; quote table; historical lookup by day, month and year selects.

**Filings:** Quarterly Results uses tabs (Q2 2026, Q1 2026, Q4 2025, Q3 2025) showing the release headline and sub-headline in-page, with year selects.

**News and events:** The latest event is shown as a card with Webcast, Presentation, Release and a "Meet" link in one row.

**Subscribe:** Standard Q4 double opt-in with a privacy line.

**Governance:** Governance documents and committee composition pages; leadership is off-site.

**FAQ:** About 15 questions, marked up as FAQPage JSON-LD (Question and Answer).

**Design notes:** Rethink Sans, 80px H1, 36px H2, dark grey headings, 18px body. Mobile not verified.

**SEO:** Titles "Happen Bank, National Association - Stock Info - Stock Quote". No meta description observed on the home or stock page. JSON-LD: Corporation with an @id, plus FAQPage on the FAQ page.

**OCAL should copy:**
1. A four-KPI Why Invest strip mixing scale, trust and efficiency.
2. FAQPage JSON-LD on the investor FAQ.
3. Corporation JSON-LD with a stable @id.
4. A one-row event card: webcast, deck, release.
5. A historical price lookup.

## Part 1 sites 9 and 10

Method note: all sites visited 23 Oct 2026, read through the built-in browser, curl and Exa fetch. Vendor showcases used: Notified design portfolio (https://media.corporate-ir.net/media_files/IROL/25/254722/webdesign/themes/2022/library/portfolio.html) and the Equisolve IR websites page (https://www.equisolve.com/ir-websites). Both customers chosen are US Nasdaq small caps, not TSX or TSXV. Theratechnologies (TSX, also in Notified's portfolio) blocked automated access (HTTP 403), so it was not reviewed. Market caps were not verified; "small cap" is inferred from share prices and vendor labels.

### 9a. Notified customer: Lulu's Fashion Lounge Holdings (Nasdaq: LVLU), online women's fashion retailer

- **URL:** https://investors.lulus.com/ (plus /stock-information/stock-quote-chart, /financial-information/sec-filings, /ir-resources/investor-faqs, /governance/documents, /ir-resources/email-alerts, /ir-resources/contact-ir). **Visited 23 Oct 2026.**
- **Why it is good:** a clean, complete minimum viable IR site on Notified's platform. Every standard section exists and nothing is stale (Q2 2026 results and a 1 Oct 2026 Form 4 are posted). A brand-led hero gives it personality. It is an online-only retailer, so the fit with OCAL's digital model is close.
- **IR nav (in order):** Overview; News & Events (Press Releases, Events & Presentations); Governance (Governance Documents, Management Team, Board of Directors, Committee Composition); Financials (SEC Filings, Quarterly Results, Annual Reports); Stock Information (Stock Quote & Chart); Resources (Investor FAQs, Email Alerts, Contact IR). Top bar only; footer is minimal.
- **Hero:** full-width photo mosaic with the words "Investor Relations", then an About Us block with a short company description and a brand video. No equity-story headline and no ticker in the hero.
- **KPI / at a glance:** none. Home shows management cards, a quarterly results block (release, call, 10-Q per quarter), latest news and events, and "Featured Pages". No stock snapshot on the home page.
- **Stock widget:** Notified platform (ndq and corporate-ir.net markers in the HTML). The quote page footer states a minimum 15 minute delay, source LSEG. Quote values load by script.
- **Filings:** table with year filter and group filters (annual, current, proxy, quarterly, registration, Group 3/4/5), with date, form, description and HTML, PDF and RTF links.
- **News:** year-filtered list with dateline and teaser.
- **Subscribe:** form with alert types (end of day quote, SEC filings, events, news, weekly summary).
- **Governance:** documents page (code of conduct, guidelines, clawback policy, committee charters), plus separate board, management and committee pages.
- **FAQ:** about ten plain facts: HQ, auditor, IPO date, ticker, exchange and similar. Contact IR is one named mailbox, no phone.
- **Design:** Proxima Nova body with Termina bold headings; white page with blush pink panels; photographic. Responsive grid. Density low to medium.
- **SEO:** title pattern "Page | Company legal name"; one site-wide meta description; canonical with trailing slash; flat two-level URLs; JSON-LD is a minimal Organization plus WebPage graph.
- **OCAL should copy:** the six-group nav and the same page set; filing table filters; alert categories including a weekly summary; a results block per period; a governance documents page.
- **OCAL should avoid:** no KPI strip and no ticker on the home page; a quote page that is blank when the script fails.

### 9b. Equisolve customer: Red Robin Gourmet Burgers (Nasdaq: RRGB), restaurant chain

- **URL:** https://ir.redrobin.com/ (plus /stock-data/quote, /sec-filings/all-sec-filings, /about/faq, /governance/board-of-directors, /news-events/email-alerts). **Visited 23 Oct 2026.**
- **Why it is good:** the most information-dense small-cap template found. One scroll answers the usual investor questions: latest news, next event, latest quarter with every document format, latest 10-K, alerts, stock snapshot and a numbers strip. Equisolve lists it as a showcase client.
- **IR nav (in order):** Overview; News & Events (Press Releases, IR Calendar, Presentations, Email Alerts); About (Executive Team, Contacts, Information Request, FAQ); Corporate Responsibility; Governance (Board, Committees, Documents); Financial Info (Results, Income Statement, Balance Sheet, Cash Flow, Proxy); Stock Data (Quote, Charts, Historical, Analyst Coverage); SEC Filings. A link back to the consumer site sits at the top.
- **Hero:** no image hero; the page opens on news and events modules, then a one-paragraph company story.
- **KPI / at a glance:** a strip with restaurant count, franchise count and team members, each dated and sourced to the 10-K. A good model for dated, sourced facts.
- **Stock widget:** QuoteMedia (qmodLoader.js in the HTML; footer credits QuoteMedia and states a 15 minute delay). Home snapshot shows price, change, volume, day and 52-week range with a timestamp.
- **Filings:** home block plus a full SEC filings table with form-type and year filters; PDF, HTML, XBRL and ZIP per filing; RSS feed.
- **News:** latest four on home, full archive page, RSS.
- **Subscribe:** form with a contact-type selector (individual, analyst, broker, portfolio manager, banker, media), so the list segments itself.
- **Governance:** board bios, committees, documents.
- **FAQ:** ten transfer-agent-level questions (listing date, direct purchase, exchange, dividend, CUSIP, auditor, contact). Contacts page plus an Information Request form.
- **Design:** Typekit fonts (tablet-gothic-narrow, alkaline, tenso, roboto); charcoal text on cream and light grey; stockpr theme CSS (Equisolve link inferred from its showcase list and the file names, not stated on the page). Viewport meta present; mobile rendering not tested.
- **SEO:** title pattern "Page :: Company (TICKER)"; home meta description is company boilerplate; per-page canonical; flat section URLs; JSON-LD Corporation with PostalAddress only. No safe-harbour text found on the home page.
- **OCAL should copy:** the sourced and dated at-a-glance strip; home modules (next event, latest quarter, alerts); the self-segmenting alert form; RSS; an information request form; a separate Financial Info tab.
- **OCAL should avoid:** an FAQ that stops at transfer agent facts; no forward-looking notice on home.

### 10. Cautionary example: Shift Technologies (archived) and Vroom (current)

- **URLs:** https://web.archive.org/web/20240216191409/https://investors.shift.com/ (snapshot of 16 Feb 2024); https://ir.vroom.com/ (live, also the 3 Jan 2026 archive). **Visited 23 Oct 2026.** Live investors.shift.com was not reachable (connection failure by curl). ir.vroom.com returned Access Denied (403) to curl but loaded in the browser.
- **Vroom is not a poor site.** Its IR home is live and current (Q2 2026 results of 4 Aug 2026, quote, 10-Q, FAQ, alerts, RSS). It uses the same Notified template as Lulus. Weak points only: the hero keeps a legacy consumer tagline after ecommerce was wound down in January 2024, with the real story only in a paragraph below, and no KPIs on home. Lesson: after a business pivot, rewrite the hero first.
- **Shift is the cautionary case.** Four months after the October 2023 Chapter 11 filing, the IR home showed:
  1. A bankruptcy notice sitting above an unchanged company profile that still described a consumer-centric omnichannel retailer with a "fun, fair" mission. The two contradict each other.
  2. A dead stock widget: ticker "--", blank price, volume 0, because trading had been suspended on 19 Oct 2023.
  3. Stale modules: latest news dated 6 Oct 2023, latest earnings report Q2 2023, and a "more events coming soon" placeholder.
  4. Full nav (analyst coverage, investment calculator, annual meeting) still listing sections with no live content.
  5. A claims-agent contact for creditors but no IR person.
- **Lessons for OCAL:** keep hero and profile in step with reality; hide any module with no data; date every block; never show a zero-filled quote; if a widget fails, fall back to a "view on TMX Money" link.

### OCAL today (observed)

- **URLs:** https://ocalfinancial.ca/ (consumer financing home, titled for used car financing in BC and Alberta) and https://ocalfinancial.ca/investor-relations (the IR page). **Visited 23 Oct 2026.** https://ocalfinancial.ca/investors shows a "Page not found" screen (client-side 404 served with HTTP 200, so a soft 404).
- **Platform:** React single page app with prerendered copy for crawlers. Fonts Poppins, Outfit and Inter. The sitemap lists 286 URLs, including /investor-relations and 19 /investor-relations/press-release/slug pages (earliest July 2026, latest 13 Oct 2026).
- **IR page, present:** one long scrolling page with no IR sub-navigation (header is the consumer nav; "Investor relations" is in the footer only). Contents: TSXV: OCAL badge, hero tagline and summary, four buttons (corporate presentation, investor fact sheet, press releases, management), a "Track OCAL" block linking out to TradingView and TMX Money (external links, no embedded live quote), why-invest narrative and highlights, a CEO video (YouTube embeds), a corporate information table (legal name, CUSIP, ISIN, transfer agent, auditors, counsel, corporate secretary, licensing, filing statement date, contact), leadership list, paginated press releases (four per page, five pages), three Ronin items under "Related filings" (two TheNewsWire links, one PDF), team cards including the IR manager, a long investor story, IR email and phone, an FAQ of about 35 questions in four groups (About OCAL, Listing and capital markets, Risk and governance, Technology and platform), and a forward-looking information notice.
- **Missing versus best practice:** a live quote and chart on the site; a SEDAR+ link and a filings page (no financial statements, MD&A or annual filings listed); an email alert form (the FAQ asks how investors get updates; no form found); an events calendar; governance documents and committee charters; board bios; a KPI strip; IR-specific JSON-LD (only the site-wide FinancialService schema; press release pages add a BreadcrumbList); unique meta descriptions per release (the one checked shows only the dateline); a dedicated IR menu and URL tree. TMX guidance also suggests keeping promotional content apart from IR content; here the IR page sits inside the consumer site with consumer header and footer.
- **Present and strong:** named transfer agent, auditors and counsel; ISIN and CUSIP; FAQ depth; a press release archive with per-release URLs and canonicals; fact sheet and presentation downloads; IR email and phone; forward-looking notice.

### What vendors say a small-cap IR site must have

- **TMX Group, Website Best Practices (https://www.tsx.com/en/resource/2678/):** filings with a SEDAR link; governance (AGM materials, board); investor deck and fact sheet; share data with quote; FAQ that goes beyond transfer agent facts; named IR contact with name, email and phone (avoid forms); news releases; events list; analyst names but not their reports; a "Why Invest" front and centre; sales content kept separate from IR; mobile and SEO optimised; nothing incomplete, incorrect or out of date.
- **TSX Electronic Communications Guidelines (https://www.tsx.com/en/resource/3122 and https://www.tsx.com/ebooks/en/electronic-communications/5/):** website posting does not replace a news release; post releases and SEDAR+ filings promptly; date documents; archive rather than delete; correct misleading content; log postings; email lists send only after wire dissemination; disclaimer when linking out.
- **CSA NP 51-201 s6.12 (https://www.osc.ca/en/securities-law/instruments-rules-policies/5/51-201/national-policy-np-51-201-disclosure-standards):** accurate site, date material items, archive outdated ones.
- **ICR checklist (https://info.icrinc.com/hubfs/Checklists/ICR%20Checklist%2012%20Elements%20Your%20Investor%20Relations%20Website%20Must%20Include.pdf):** twelve elements: story, strategy, management, board, filings links, governance, press room and financials, events and webcasts, FAQ, analyst coverage, stock information, a detailed named contact.
- **Q4 best-practice guide (https://www.q4inc.com/hubfs/Q4Inc_October2025/pdfs/IR-Website-Best-Practice-Reccomendations-Guide.pdf):** pull releases automatically from the wire; show the latest presentation in-page; financials in HTML and PDF with a summary table; a resources area with FAQ, alert subscription and contacts; responsive design.
- **Notified (https://www.notified.com/IR/ir-websites):** stock data, filings, email alerts, IR calendar, video, releases, results, AGM content, a governance library, visitor analytics, and now AI search visibility.
- **IR Magazine research (https://www.ir-impact.com/wp-content/uploads/2026/03/IR-2022-IR-magazine-research-report-ir-websites.pdf):** releases on over 90 percent of sites; events schedule on about 80 percent; named IR contact, alerts and ESG on over 75 percent; FAQ on about 40 percent, so an FAQ is a differentiator for a microcap.
- **BNY IR website guidance (https://www.bny.com/assets/corporate/documents/pdf/solutions/the-ir-website-5-best-practice-considerations.pdf):** searchable release archive of at least three years, named IR contacts, transfer agent details for retail investors, easy-to-find regulatory links.

# Part 2. SEO plan for a microcap investor site

## Part 2a. The query set to own, who ranks today, and what it takes

**Method and caveat.** Searched on 23 Oct 2026 with the WebSearch tool (US index, standard mode). The tool returns about 9 to 10 results per query in its own order, which is not identical to Google's. ocalfinancial.ca did not appear in any of the nine OCAL brand-query result sets below, which is itself the finding. Repeat the check on google.ca in a logged-out window and record positions in the tracker at the end of this part.

Name collisions to design around: "OCAL" alone also returns UCAL (an Indian stock), Ocean Capital Acquisition (OCAC), and "OC Financial" filings. Always pair the ticker with "Financial" and "TSXV".

### Brand and ticker queries

| Query | Top 3 results seen 23 Oct 2026 | Where OCAL's site stands | What OCAL needs to outrank or join them |
|---|---|---|---|
| OCAL stock | 1) https://www.investing.com/equities/ronin-ventures ; 2) https://finance.yahoo.com/quote/OCAL.V/ ; 3) https://wealthawesome.com/whats-going-on-with-ocal-financial-inc-stock-tuesday-10132026-wgo | Absent | Do not aim for position 1. Quote pages from Yahoo and Investing.com will hold it. Aim to be on page one with sitelinks and to own the Google Finance card by fixing the upstream profile (Part 2d). Investing.com's URL slug is still "ronin-ventures", a stale-name signal to correct. |
| OCAL Financial | 1) https://www.newsfilecorp.com/release/306175/... (lang=fr) ; 2) https://www.newsfilecorp.com/company/12553/OCAL-Financial ; 3) https://www.webull.com/news/15265548337177600 | Absent | Realistic target: position 1 to 3. Needs a crawlable investors home titled "OCAL Financial (TSXV: OCAL) Investor Relations", an Organization or Corporation block, sameAs links, and inbound links from the Newsfile company page, TMX Money, Yahoo (website field), LinkedIn and every release boilerplate. |
| OCAL Financial stock | 1) https://www.investing.com/equities/ronin-ventures ; 2) https://weissratings.com/en/stock/ocal-v-tsx/profile ; 3) https://finance.yahoo.com/quote/OCAL.V/ | Absent | Same as "OCAL stock". Add a /investors/stock/ page with a server-rendered quote table (price, volume, 52-week range, shares outstanding as of a date) and the exact phrase "OCAL Financial stock". |
| OCAL Financial stock TSXV | 1) https://www.newsfilecorp.com/release/306175/... ; 2) https://www.newsfilecorp.com/release/305866/... ; 3) https://www.newsfilecorp.com/release/307230/... | Absent | Newsfile pages outrank because they are wire copy with the ticker in the header. Match with an on-site copy of each release carrying the ticker in the H1 and title, published within minutes, plus a canonical to itself and a link back from the wire release body to the on-site URL. |
| OCAL TSXV | 1) https://wwww.stockwatch.com/News/Item/Z-C!RVC-3785211/C/RVC (14 Feb 2026) ; 2) https://wwww.stockwatch.com/News/Item/Z-C!RVC-3842323/C/RVC (18 Jul 2026) ; 3) https://www.miningstockeducation.com/2026/02/1301756-b-c-ltd-dba-ocal-financial-and-ronin-ventures-corp-enter-into-letter-of-intent-to-complete-qualifying-transaction-and-listing-on-the-tsx-venture-exchange/ | Absent | Top results are Stockwatch bulletin items about the Ronin to OCAL transaction. Win by having a "Listings and identifiers" page (TSXV OCAL, FSE JC3, ISIN, CUSIP, WKN, transfer agent, date trading began) that states "TSXV: OCAL" and the 21 Jul 2026 listing date. |
| TSXV:OCAL | 1) https://wwww.stockwatch.com/News/Item/Z-C!RVC-3842323/C/RVC?fmt=orig ; 2) https://wwww.stockwatch.com/News/Item/Z-C!RVC-3842323/C/RVC ; 3) https://wwww.stockwatch.com/News/Item/Z-C!RVC-3785211/C/RVC | Absent | Colon-form queries match Stockwatch's bulletin text. Use the colon form "TSXV: OCAL" (with a space, the TMX style) in titles and H1s and "TSXV:OCAL" once in body copy and the alt text of the quote chart. |
| OCAL Financial investor relations | 1) https://www.newsfilecorp.com/release/305866/... ; 2) https://www.newsfilecorp.com/release/307230/... ; 3) https://www.newsfilecorp.com/release/306175/... | Absent (the existing page https://ocalfinancial.ca/investor-relations is titled only "Investor Relations \| OCAL Financial") | This is the query OCAL should win outright. Title "OCAL Financial (TSXV: OCAL) Investor Relations", H1 "Investor Relations", a server-rendered page, internal links from every consumer page footer, and Search Console sitelinks over time. Highest-confidence win in the set. |
| OCAL share price | 1) https://www.5paisa.com/hindi/stocks/ucal-share-price (UCAL, wrong company) ; 2) https://wealthawesome.com/whats-going-on-with-ocal-financial-inc-stock-tuesday-10062026-wgo ; 3) https://www.zerodha.com/markets/stocks/NSE/UCAL/ (wrong company) | Absent | Largely a quote-card query. The tool returned wrong-company results, which Google disambiguates better with the "OCAL Financial" name. Provide "OCAL share price" as H2 text on /investors/stock/ with a dated price and the 15 minute delay note. |
| OCAL Financial news | 1) https://www.newsfilecorp.com/company/12553/OCAL-Financial ; 2) https://www.newsfilecorp.com/release/306175/... ; 3) https://kalkinemedia.com/ca/news/announcements/ocal-financial-inc-finalizes-qualifying-transaction-begins-trading-on-tsx-venture-exchange-as-ai-driven-remote-auto-dealership | Absent (the site has 19 release URLs in its sitemap) | Realistic target: top 3 with /investors/news/ as an indexable archive page with 25 words of lede per release, the ticker in each headline and a server-rendered list. Syndicators (Kalkine, Finanznachrichten, Webull) copy wire text; unique on-site context helps (Part 2c). |
| JC3 Frankfurt | 1) https://www.travelocity.com/Frankfurt-Hotels-JCBLUE-GUESTHOUSE.h74585135.Hotel-Information ; 2) https://za.hotels.com/es/ho2387724320/jc-blue-guesthouse-frankfurt-alemania ; 3) https://www.lastminute.de/hotel/deutschland/frankfurt-am-main/jcblue-guesthouse-hostel_hid-10994192 | Absent, and no OCAL result at all | Query has hostel intent. Target a better phrase: "OCAL Financial Frankfurt JC3" and "JC3 WKN A42K21" and "CA67449X1050". Put the Frankfurt symbol, WKN, ISIN and the 25 Aug 2026 release link on the Listings page and in the Corporation schema. Börse Frankfurt's own page will outrank; the goal is to appear second. |

### Category queries

| Query | Top 3 results seen 23 Oct 2026 | What it means for OCAL | What OCAL needs |
|---|---|---|---|
| asset-light car dealer stock | 1) https://www.sec.gov/Archives/edgar/data/1683606/000114036125015797/ny20037100x5_ars.pdf (Cars.com annual report) ; 2) https://tipranks.com/news/article/is-carlotz-stock-a-buy-right-now-this-is-what-you-need-to-know ; 3) https://thedailyguardian.com/india/carzbazzar-crosses-1000-cars-stocked-in-just-six-months-valuation-reaches-rs-150-crore-759602/amp/ | An open field: the results are tangential (a marketplace, a defunct consignment model, an Indian startup). No listed Canadian "asset-light car dealer" page exists. | A single explainer page, "What is an asset-light online car dealer? OCAL Financial (TSXV: OCAL)", 800 to 1,200 words, with a definition, how the model works (approval first, vehicle sourced after approval), "zero standing inventory", the contrast with a stocked lot, and a link to the FAQ. Reviewed for CIRO and promotion rules before publishing. Winnable in weeks. |
| online car dealership stock Canada | 1) https://www.marketbeat.com/instant-alerts/autocanada-tseacq-price-target-lowered-to-c1500-at-cibc-2024-11-15 ; 2) https://www.marketbeat.com/instant-alerts/autocanada-tseacq-given-new-c2200-price-target-at-canaccord-genuity-group-2025-03-20 ; 3) https://www.marketbeat.com/stocks/OTCMKTS/AOCIF/competitors-and-alternatives/news/news/news/chart/chart | AutoCanada (TSX: ACQ) owns the intent. No pure online Canadian dealer is listed (the search found Canada Drives in creditor protection and Clutch privately held, per https://apa.ca/en/?p=10444, date unclear). | An explainer "Publicly traded online car dealers in Canada" would have to be factual, balanced and compliance-reviewed (comparative claims need care). Title the OCAL page "Online car dealership in Canada: how OCAL Financial (TSXV: OCAL) works". Medium difficulty; the long tail is open. |
| TSXV fintech auto finance stock | 1) https://simplywall.st/stocks/ca/materials/tsxv-ctg/centenario-gold-shares/news/tsx-penny-stock-picks-automotive-finco-and-2-other-promising ; 2) https://ycharts.com/companies/AFCC.H.V ; 3) https://tsx.com/news/new-company-listings?id=1509 | Competitors named: Automotive Finco (AFCC.H), Axis Auto Finance (sold its business, delisted from TSXV in 2022 to TSX per https://newswire.ca/news-releases/axis-auto-finance-changes-its-trading-symbol-to-axis-610505645.html), Rifco (RFC). OCAL is the only live TSXV online auto-finance-plus-dealership name found. | Long-tail page with "TSXV" and "auto finance" in the title and a clear statement of what OCAL is and is not (it does not hold consumer loans or take credit-default risk, per its own release). Medium difficulty; achievable in 1 to 3 months once the site is crawlable. |
| used car financing company TSXV | 1) https://tsx.com/news/new-company-listings?id=1509 ; 2) https://newswire.ca/news-releases/axis-auto-finance-changes-its-trading-symbol-to-axis-610505645.html ; 3) https://www.theglobeandmail.com/investing/markets/stocks/AXIS-T | Same pool as above, mostly stale (Axis). | Same page plus an exact-match H2 "Used car financing company on the TSX Venture Exchange". Easy to medium. |
| Canadian Carvana stock | 1) https://www.marketbeat.com/instant-alerts/filing-national-bank-of-canada-fi-lowers-position-in-carvana-co-cvna-2025-08-18 ; 2) https://www.marketbeat.com/instant-alerts/carvana-nysecvna-given-new-46000-price-target-at-royal-bank-of-canada-2025-07-31 ; 3) https://fool.ca/company/nyse-cvna-carvana/343497 | Carvana (NYSE: CVNA) and Canadian-bank analyst notes dominate; the query is about Carvana, not a Canadian equivalent. | Do not chase this head term. If a comparison page is wanted ("OCAL and Carvana: a different model"), it needs Lawson or CIRO clearance and no "the Canadian Carvana" claim. Low priority, higher compliance risk. |

### Extra queries worth owning (add to the tracker)

"OCAL Financial Inc", "OCAL Financial press release", "OCAL Financial annual report", "OCAL Financial SEDAR", "OCAL Financial CEO Mehdi Moghareh" (note vendors spell it "Medhi"), "Ronin Ventures OCAL" (former name, still used by Investing.com), "OCAL Financial Frankfurt", and, once the OTC symbol is assigned, "OCAL Financial OTCQB". Do not publish any OTC symbol before it is confirmed.

### Tracker to run now and at 30, 60 and 90 days

For each query: logged-out google.ca position of ocalfinancial.ca, which URL ranks, whether a Finance card or knowledge panel shows, and the top 3 competitors. Add Search Console Performance data (queries, impressions, average position) once the property has 28 days of data. Verify that Search Console and Bing Webmaster Tools are set up: the site already carries a google-site-verification tag.

## Part 2b. Structured data

### What each type is for, and what Google says

- **Organization or Corporation** (home of the investor section): Google says Organization markup helps it disambiguate the company and can influence the logo and knowledge panel; no property is required, add every recommended one (source: https://developers.google.com/search/docs/appearance/structured-data/organization). Use the most specific subtype; schema.org defines `Corporation` with `tickerSymbol` (source: https://schema.org/Corporation).
- **tickerSymbol format.** schema.org says the exchange and instrument are "separated by a space character", and recommends ISO 10383 Market Identifier Codes for the exchange. TSX Venture Exchange is MIC `XTSX`, Frankfurt is `XFRA`. So the schema value is `XTSX OCAL` and `XFRA JC3` (not "TSXV:OCAL"). Put the human form "TSXV: OCAL" in `alternateName` and visible text. Google documents no rich result for tickerSymbol, so its value is entity disambiguation for crawlers and AI systems, not a search feature (inference from the absence of any Google documentation).
- **Identifiers.** Google encourages `iso6523Code` over `leiCode`, with ICD prefix 0199 for an LEI, written `0199:<LEI>` (same Google source). OCAL's LEI is 984500E70698C2C2AC97 per GLEIF (see Part 2d, finding 5, and fix the registered address first).
- **NewsArticle** (each release): Google says Article markup is optional and there is "no markup requirement to be eligible for Google News features like Top stories"; recommended properties are headline, image, datePublished, dateModified, author (source: https://developers.google.com/search/docs/appearance/structured-data/article). Still worth adding for date accuracy and for non-Google parsers.
- **FAQPage.** Google's changelog states the FAQ rich result stopped appearing in Google Search on 7 May 2026 and that its FAQ documentation was removed on 15 June 2026; it had been limited to well-known authoritative government and health sites since September 2023 (source: https://developers.google.com/search/docs/appearance/structured-data/faqpage). So the FAQ markup will not produce a rich result for OCAL. It is still harmless, mirrors visible text, and may help other parsers; keep it but do not spend time on it, and make sure the visible FAQ is crawlable HTML. Happen Bank's investor site carries FAQPage (Part 1, 8b).
- **BreadcrumbList.** Cheap, helps URL display in results. Lemonade ships it.
- **Event** (webcasts, AGM, conference presentations): Google's Event documentation requires `name`, `startDate` and `location`, and states events must take place in a physical location and virtual-only experiences are not supported (source: https://developers.google.com/search/docs/appearance/structured-data/event). So expect no rich result for an online-only earnings call; use it for in-person events (AGM, Cantech-style conferences) and consider `BroadcastEvent` inside a `VideoObject` only if a livestream is embedded. Include `eventAttendanceMode` for non-Google consumers.
- **Person** (executives and directors): name, jobTitle, worksFor (by @id), image, sameAs. OCAL role only. Add a person only with the individual's approval and approved bio.
- **Dataset or DataFeed for KPI tables:** Google's Dataset markup requires `name` and a `description` of 50 to 5,000 characters, targets Dataset Search, and describes metadata, not values (source: https://developers.google.com/search/docs/appearance/structured-data/dataset). Only worth doing if OCAL publishes a downloadable CSV of the quarterly operating update (units, average price, gross profit per vehicle, margin). Low priority; a plain HTML table plus the CSV link does more for readers.
- **WebSite with SearchAction:** drop it from IR pages. Google retired the sitelinks search box from 21 Nov 2024 (reported by Search Engine Land, https://searchengineland.com/google-search-to-drop-sitelinks-search-box-447682). The existing site-wide block points its search at /inventory, which is irrelevant to investors. Keep WebSite only for the site name.
- **Matching rule.** Google says structured data must match the visible page text (https://developers.google.com/search/docs/appearance/ai-features). Take every value from the approved boilerplate and the Listings page, and update schema in the same deploy as the text.

### Existing OCAL markup (observed 23 Oct 2026)

The site-wide block is a `FinancialService` named "OCAL Financial" with address, `telephone` +1-877-495-2012 (consumer line), `email` general@ocal.ca, `priceRange` "$$", and `sameAs` to LinkedIn, Facebook, TMX Money and Börse Frankfurt (CA67449X1050). A `WebSite` block follows. Release pages add a BreadcrumbList. Problems for the investor use: wrong type for a listed issuer (`FinancialService` is a LocalBusiness-style type; `Corporation` is right on the investor home), no legalName, no ticker, no LEI, the consumer phone number, and a stale-sounding description. Leave the consumer block on consumer pages; put the Corporation block on /investors/ and /investors/facts/ only, with the same @id root so the graph stays one entity (use `https://ocalfinancial.ca/#corporation`, and set the consumer block's `parentOrganization` or `@id` reference to it, or retire the duplicate; CQ to decide).

### Copy-ready JSON-LD: Corporation (investor home and facts page)

Verified facts used: legal name, tickers, address, site, phone from Matthew's brief; ISIN CA67449X1050 and CUSIP 67449X105 from OCAL's own investor page; LEI and WKN from Part 2d (GLEIF and Börse Frankfurt references). Two items need a human check before launch and are flagged after the block: the investors@ocal.ca mailbox (OCAL's own releases and site list general@ocal.ca) and the registered address on the LEI record.

```json
{
  "@context": "https://schema.org",
  "@type": "Corporation",
  "@id": "https://ocalfinancial.ca/#corporation",
  "name": "OCAL Financial",
  "legalName": "OCAL Financial Inc.",
  "alternateName": ["OCAL", "OCAL Financial Inc.", "TSXV: OCAL", "Ronin Ventures Corp. (former name)"],
  "url": "https://ocalfinancial.ca/investors/",
  "mainEntityOfPage": "https://ocalfinancial.ca/investors/",
  "logo": {
    "@type": "ImageObject",
    "url": "https://ocalfinancial.ca/ocal-logo.png",
    "width": 512,
    "height": 512
  },
  "description": "OCAL Financial Inc. is a Vancouver-based virtual automotive dealership and vehicle-finance platform, licensed in British Columbia and Alberta. It sources each vehicle after a customer is approved and earns revenue from vehicle sales and related finance and protection products. It does not hold consumer loans or take credit-default risk.",
  "tickerSymbol": ["XTSX OCAL", "XFRA JC3"],
  "isicV4": "4510",
  "naics": "441120",
  "iso6523Code": "0199:984500E70698C2C2AC97",
  "leiCode": "984500E70698C2C2AC97",
  "identifier": [
    { "@type": "PropertyValue", "propertyID": "ISIN", "value": "CA67449X1050" },
    { "@type": "PropertyValue", "propertyID": "CUSIP", "value": "67449X105" },
    { "@type": "PropertyValue", "propertyID": "WKN", "value": "A42K21" },
    { "@type": "PropertyValue", "propertyID": "TSXV symbol", "value": "OCAL" },
    { "@type": "PropertyValue", "propertyID": "Frankfurt symbol", "value": "JC3" }
  ],
  "foundingDate": "2021",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Suite 500, 885 Dunsmuir Street",
    "addressLocality": "Vancouver",
    "addressRegion": "BC",
    "postalCode": "V6C 1N5",
    "addressCountry": "CA"
  },
  "areaServed": [
    { "@type": "AdministrativeArea", "name": "British Columbia" },
    { "@type": "AdministrativeArea", "name": "Alberta" }
  ],
  "contactPoint": [
    {
      "@type": "ContactPoint",
      "contactType": "investor relations",
      "email": "investors@ocal.ca",
      "telephone": "+1-604-687-7765",
      "areaServed": "CA",
      "availableLanguage": ["English"]
    }
  ],
  "sameAs": [
    "https://money.tmx.com/en/quote/OCAL",
    "https://www.boerse-frankfurt.de/equity/CA67449X1050",
    "https://finance.yahoo.com/quote/OCAL.V/",
    "https://www.newsfilecorp.com/company/12553/OCAL-Financial",
    "https://ca.linkedin.com/company/ocalfinancial",
    "https://www.facebook.com/OCALFinancial/",
    "https://search.gleif.org/#/record/984500E70698C2C2AC97",
    "https://www.wikidata.org/wiki/REPLACE_WITH_QID_AFTER_CREATION",
    "https://www.crunchbase.com/organization/REPLACE_WITH_CLAIMED_SLUG"
  ],
  "member": {
    "@type": "OrganizationRole",
    "roleName": "Listed issuer",
    "member": {
      "@type": "Organization",
      "name": "TSX Venture Exchange",
      "url": "https://www.tsx.com/"
    }
  }
}
```

Notes on the block:

- Remove the two REPLACE lines (Wikidata, Crunchbase) until those pages exist; broken sameAs links hurt more than they help.
- `tickerSymbol` as an array is valid (any schema.org property may repeat). The values follow schema.org's MIC guidance. If CQ wants a single value, keep "XTSX OCAL".
- `isicV4` 4510 (sale of motor vehicles) and `naics` 441120 (used car dealers) are my classification suggestion and assume the Part 2d decision to classify OCAL as automotive retail first and consumer finance second. Delete both if Matthew wants no classification stated. They must agree with the S&P and Morningstar sector labels.
- The `member` block is optional decoration; delete if CQ prefers a shorter graph. Do not add "digital inventory", "five channels" or "Canada's first" to `description`.
- `foundingDate` is the year only because the exact incorporation date (23 Apr 2021 per Part 2d) belongs to the predecessor entity, 1301756 B.C. Ltd.; confirm against the filing statement before using a full date.
- Phone: Matthew's investor line (604) 687-7765 is used here; the site-wide schema's 1-877-495-2012 is the consumer line and should stay out of the investor block.
- Google's logo rule: at least 112 by 112 pixels, crawlable, readable on white (Google Organization docs, above). Confirm ocal-logo.png meets it.

### Copy-ready examples for the other types

NewsArticle (real release, template for the pattern; replace values per release):

```json
{
  "@context": "https://schema.org",
  "@type": "NewsArticle",
  "@id": "https://ocalfinancial.ca/investors/news/2026-08-25-common-shares-trading-frankfurt-jc3/#article",
  "mainEntityOfPage": "https://ocalfinancial.ca/investors/news/2026-08-25-common-shares-trading-frankfurt-jc3/",
  "headline": "Common Shares Now Trading on the Frankfurt Stock Exchange",
  "datePublished": "2026-08-25T07:00:00-07:00",
  "dateModified": "2026-08-25T07:00:00-07:00",
  "dateline": "VANCOUVER, B.C.",
  "inLanguage": "en-CA",
  "articleSection": "Press release",
  "image": ["https://ocalfinancial.ca/images/investors/og-ocal-tsxv-1200x630.png"],
  "author": { "@type": "Organization", "name": "OCAL Financial Inc.", "@id": "https://ocalfinancial.ca/#corporation" },
  "publisher": { "@type": "Organization", "name": "OCAL Financial Inc.", "@id": "https://ocalfinancial.ca/#corporation" },
  "about": { "@id": "https://ocalfinancial.ca/#corporation" },
  "keywords": "OCAL Financial, TSXV: OCAL, FSE: JC3, Frankfurt Stock Exchange",
  "isBasedOn": "https://www.newsfilecorp.com/release/REPLACE_WITH_NEWSFILE_ID/"
}
```

(The publication time 07:00 Pacific is a placeholder: use the actual wire time. The headline and date are from the live release page https://ocalfinancial.ca/investor-relations/press-release/ocal-frankfurt-stock-exchange-listing-august-2026 .)

BreadcrumbList:

```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    { "@type": "ListItem", "position": 1, "name": "OCAL Financial", "item": "https://ocalfinancial.ca/" },
    { "@type": "ListItem", "position": 2, "name": "Investors", "item": "https://ocalfinancial.ca/investors/" },
    { "@type": "ListItem", "position": 3, "name": "News", "item": "https://ocalfinancial.ca/investors/news/" },
    { "@type": "ListItem", "position": 4, "name": "Common Shares Now Trading on the Frankfurt Stock Exchange" }
  ]
}
```

FAQPage (two verified answers; mirror the visible FAQ exactly):

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Where do OCAL Financial shares trade?",
      "acceptedAnswer": { "@type": "Answer", "text": "OCAL Financial Inc. common shares trade on the TSX Venture Exchange under the symbol OCAL (TSXV: OCAL) and on the Frankfurt Stock Exchange under the symbol JC3." }
    },
    {
      "@type": "Question",
      "name": "When did OCAL Financial begin trading on the TSX Venture Exchange?",
      "acceptedAnswer": { "@type": "Answer", "text": "OCAL Financial Inc. began trading on the TSX Venture Exchange on July 21, 2026, after completing its qualifying transaction with Ronin Ventures Corp." }
    }
  ]
}
```

Event (in-person or webcast; template):

```json
{
  "@context": "https://schema.org",
  "@type": "Event",
  "name": "OCAL Financial Annual General Meeting 2026",
  "startDate": "2026-12-10T10:00:00-08:00",
  "eventStatus": "https://schema.org/EventScheduled",
  "eventAttendanceMode": "https://schema.org/MixedEventAttendanceMode",
  "location": [
    { "@type": "Place", "name": "REPLACE_VENUE", "address": { "@type": "PostalAddress", "addressLocality": "Vancouver", "addressRegion": "BC", "addressCountry": "CA" } },
    { "@type": "VirtualLocation", "url": "https://ocalfinancial.ca/investors/events/REPLACE/" }
  ],
  "organizer": { "@type": "Organization", "name": "OCAL Financial Inc.", "url": "https://ocalfinancial.ca/investors/" },
  "description": "REPLACE with the approved notice wording."
}
```

(The 10 Dec 2026 date is from the 1 Oct board record; the start time, venue and format are placeholders. Do not publish until the notice of meeting is issued.)

Person (executive; OCAL role only):

```json
{
  "@context": "https://schema.org",
  "@type": "Person",
  "@id": "https://ocalfinancial.ca/investors/management/#mehdi-moghareh",
  "name": "Mehdi Moghareh",
  "jobTitle": "Chief Executive Officer and Director",
  "worksFor": { "@id": "https://ocalfinancial.ca/#corporation" },
  "image": "https://ocalfinancial.ca/images/investors/mehdi-moghareh.jpg",
  "url": "https://ocalfinancial.ca/investors/management/"
}
```

Use the same pattern for Matthew Friesen with `jobTitle` "Executive Chairman and Director" (never "CEO"), and add `sameAs` for LinkedIn only with each person's approval.

Dataset (only if a CSV of the operating update is published):

```json
{
  "@context": "https://schema.org",
  "@type": "Dataset",
  "name": "OCAL Financial quarterly operating update (historical)",
  "description": "Historical quarterly operating metrics published in OCAL Financial press releases: vehicles funded, average sale price, gross profit per vehicle and gross margin, with the filing or release each figure comes from.",
  "creator": { "@id": "https://ocalfinancial.ca/#corporation" },
  "license": "https://ocalfinancial.ca/investors/terms/",
  "isAccessibleForFree": true,
  "distribution": {
    "@type": "DataDownload",
    "encodingFormat": "text/csv",
    "contentUrl": "https://ocalfinancial.ca/investors/downloads/ocal-operating-update.csv"
  }
}
```

## Part 2c. Technical SEO

### Title tag and meta description patterns by page type

Google rewrites many titles, but a consistent pattern with the brand string first or last gets rewritten less. Keep titles to about 60 characters and descriptions to 140 to 155. The ticker form is "TSXV: OCAL" with a space.

| Page type | URL | Title pattern | Meta description pattern |
|---|---|---|---|
| IR home | /investors/ | OCAL Financial (TSXV: OCAL) Investor Relations | Investor information for OCAL Financial (TSXV: OCAL, FSE: JC3): stock quote, news, filings, presentations, governance and email alerts. |
| Stock and listings | /investors/stock/ | OCAL Stock Quote and Chart (TSXV: OCAL, FSE: JC3) | OCAL Financial share price, 52-week range, volume and listings on the TSX Venture Exchange and Frankfurt (JC3). Delayed 15 minutes. |
| News index | /investors/news/ | OCAL Financial News and Press Releases (TSXV: OCAL) | All OCAL Financial press releases, newest first, from the TSXV listing on 21 July 2026 to today. |
| Release | /investors/news/2026-10-22-slug/ | {Headline, up to 55 characters} \| OCAL Financial (TSXV: OCAL) | The release's first sentence (the lede after the dateline), 140 to 155 characters, no dateline. Today's pages use only the dateline as the description. |
| Financials and filings | /investors/financials/ | OCAL Financial Reports, MD&A and SEDAR+ Filings | Annual and interim financial statements, MD&A and filings for OCAL Financial Inc., with a link to its SEDAR+ profile. |
| Presentations | /investors/presentations/ | OCAL Financial Investor Presentation and Fact Sheet | Current corporate presentation, investor fact sheet and past presentations for OCAL Financial (TSXV: OCAL). |
| Events | /investors/events/ | OCAL Financial Events, Webcasts and AGM | Upcoming and past investor events, conference presentations and the annual general meeting of OCAL Financial. |
| Governance | /investors/governance/ | OCAL Financial Governance: Board, Committees, Policies | Directors, committee composition and governance documents of OCAL Financial Inc. |
| Management | /investors/management/ | OCAL Financial Management Team and Board | Biographies of the officers and directors of OCAL Financial Inc. |
| Letters and Q&A | /investors/letters/ | OCAL Financial Letters to Shareholders | Letters from the Chairman and CEO and answers to shareholder questions. |
| FAQ | /investors/faq/ | OCAL Financial Investor FAQ: Shares, Listings, Transfer Agent | Answers on OCAL Financial shares, symbols, transfer agent, auditor, fiscal year end and how to get alerts. |
| Alerts | /investors/alerts/ | Email Alerts \| OCAL Financial Investor Relations | Subscribe to OCAL Financial news, filings and event alerts. Sent after each release is disseminated. |
| Contact | /investors/contact/ | Contact Investor Relations \| OCAL Financial | Investor relations contact for OCAL Financial: email and phone, with head office address in Vancouver. |
| Facts | /investors/facts/ | OCAL Financial Facts: Symbols, Address, Officers, Auditor | Reference facts for OCAL Financial Inc.: legal name, TSXV and Frankfurt symbols, ISIN, head office, officers, transfer agent, auditor. Updated 23 Oct 2026. |

### URL structure

- One root, /investors/, flat second level, per-release pages at /investors/news/YYYY-MM-DD-short-slug/. Lowercase, hyphens, no query strings for content, no trailing-slash mix (pick the trailing slash and 301 the other).
- Today the section lives at /investor-relations and /investor-relations/press-release/<slug> (19 release URLs in the sitemap). If CQ moves to /investors/, 301 each old URL one to one (Cloudflare bulk redirects work, since the site sits behind Cloudflare), update the sitemap, canonicals and the Newsfile company page link, and keep the old URLs redirecting for at least a year. If moving is a risk to the Monday deadline, keep /investor-relations/ as the root, add /investors/ as a 301 to it, and use the same patterns underneath. The brand-query ranking benefit comes from the title, content and links, not from the path word.
- Return real 404 status for unknown URLs. https://ocalfinancial.ca/investors currently returns a client-rendered "Page not found" with HTTP 200, and an unknown release path returned a consumer-page title with HTTP 200 (soft 404s, observed 23 Oct 2026).
- Filings and PDFs: descriptive file names (2026-08-31-ocal-financial-annual-mdna.pdf), PDF title metadata set, a page for each period that links the PDFs, not a bare file list.

### Canonical, hreflang, robots

- Canonical: absolute, self-referencing, https, on every IR page; the site's template comment says no sitewide canonical, which is right. The existing investor page and its release pages already carry canonicals (verified).
- Wire copy: Newsfile, Stockhouse and others will republish OCAL's text. Keep a self-referencing canonical on the OCAL page and publish it as early as the wire does. Google's duplicate handling picks a version; the home-field advantages are the on-site context (links to the quote, filings, related releases) and the internal links. Do not use cross-domain canonicals to the wire.
- hreflang: not needed while the investor section is English only. If a French section is added (Newsfile already serves releases with ?lang=fr), Google needs each version to list itself and all others, reciprocal tags, an x-default, valid ISO codes such as en-CA and fr-CA, and the tags in HTML, headers or the sitemap, not all three (source: https://developers.google.com/search/docs/specialty/international/localized-versions). Do not machine-translate disclosure documents.
- robots.txt (observed): allows all, blocks /admin, /dashboard, /auth, /paid-leads, lists the sitemap. Fine. Do not block /investors/downloads/. Decide on AI crawlers below.

### Sitemaps

- Current: one sitemap.xml of 286 URLs with changefreq and priority and no lastmod (observed). Change to a sitemap index with /sitemap-investors.xml (all IR URLs with true lastmod, updated only when content changes) and /sitemap-news.xml.
- News sitemap: per Google, include only articles published within the last two days, up to 1,000 `news:news` entries, with publication name matching the name in Google News, language, publication_date (first publication) and title that matches the page (source: https://developers.google.com/search/docs/crawling-indexing/sitemaps/news-sitemap). With one or two releases a week the file will often hold zero to three URLs; that is fine. Note the caveat in the next section: a news sitemap tells Google about articles but does not make OCAL a Google News publisher.
- Reference both in robots.txt and submit in Search Console and Bing Webmaster Tools.

### Speed and Core Web Vitals

- Targets at the 75th percentile, mobile and desktop: LCP 2.5 s or less, INP 200 ms or less, CLS 0.1 or less (source: https://web.dev/articles/vitals). Check with the Search Console Core Web Vitals report once there is field data, and PageSpeed Insights now.
- Server-render the page body and the first quote table so LCP is text, not a script-injected block. Load the third-party chart lazily in a fixed-height box (prevents CLS) and use a static "as of" table as the fallback. Self-host fonts (the site already does), preload the one hero font file, use two typefaces at most, serve images as AVIF or WebP with width and height attributes, and lazy-load below the fold.
- Cache HTML at Cloudflare for anonymous visitors, with purge on publish; keep the IR section free of consumer lead-gen scripts (tag managers, pixels) where possible, since each adds to INP.
- The IR home should weigh under about 1.5 MB on first load. (A working budget, not a Google rule.)

### Image alt text

Describe the content and include the brand and ticker where they add meaning; no stuffing. Patterns:

- Logo: "OCAL Financial logo".
- Quote chart: "OCAL Financial (TSXV: OCAL) share price chart, 12 months to 23 October 2026".
- KPI graphic: "Chart: OCAL vehicles funded by quarter, FY2026".
- Executive photo: "Mehdi Moghareh, Chief Executive Officer of OCAL Financial".
- Presentation thumbnail: "OCAL Financial corporate presentation, October 2026, cover slide".
- Decorative images: empty alt (alt="").

### Getting a Google Finance panel and a knowledge panel for a TSXV ticker

- **Google Finance.** There is no application. Google says end-of-day prices come from Morningstar and corporate actions and company metadata from Refinitiv, and that it does not verify the data; TSXV appears in its exchange table with a 15 minute delay (source: https://www.google.com/intl/en/googlefinance/disclaimer/ and https://www.google.ca/googlefinance/disclaimer). So the route is: be correct in Morningstar and LSEG/Refinitiv (Part 2d), have a Yahoo/Morningstar page with the right description, and use the feedback link on the Google Finance page for corrections (route confirmed in Part 2d). Finance cards usually appear in a ticker search once the instrument is in the feeds.
- **Knowledge panel.** Google says it does not manually create or delete panels and cannot write custom descriptions; descriptions generally must change at the original source; an organization verifies identity and then uses "Suggest edits" on its panel, and verified feedback is typically reviewed within a few days (source: https://support.google.com/knowledgepanel/answer/7534842). A panel needs an entity in the Knowledge Graph, which is fed by sources such as Wikipedia, Wikidata and other authoritative pages. OCAL has no Wikipedia article and one is not recommended (Part 2d). A Wikidata item (notability allows an item that refers to a clearly identifiable entity with serious, publicly available references, per https://www.wikidata.org/wiki/Wikidata:Notability) plus consistent sameAs links is the realistic route. A panel for a microcap is not guaranteed; the measurable goal is the brand SERP: investors page, TMX Money, Yahoo, LinkedIn, Newsfile and the Finance card, all with the same description.

### Getting per-release pages indexed within hours: what works, what does not

| Method | Verdict | Evidence |
|---|---|---|
| XML sitemap with accurate lastmod | Do it. Necessary, not fast on its own. | Google: sitemaps help it discover new URLs; recrawl takes days to weeks and a request does not guarantee inclusion (https://developers.google.com/search/docs/crawling-indexing/ask-google-to-recrawl). |
| Search Console URL Inspection "Request indexing" | Use for each release, a handful a month. | Same Google page: for a few URLs; there is a quota but the limit is not published; repeated requests for one URL do not speed it up. |
| Server-rendered "latest news" block on the IR home and on the consumer home footer | Do it. Strongest practical lever: Googlebot revisits the homepage often and follows links to new releases. | Inference from Google's link-based discovery; not a documented guarantee. |
| News sitemap | Do it, cheap. | Format and limits from https://developers.google.com/search/docs/crawling-indexing/sitemaps/news-sitemap. |
| IndexNow | Do it for Bing, Yandex, Naver, Seznam, Yep; Google does not participate. One POST per publish, key file at the root, up to 10,000 URLs per request (https://www.indexnow.org/documentation). | Third-party summaries dated April 2026 state Google does not support IndexNow (https://blckalpaca.at/en/knowledge-base/seo-geo/technical-seo/indexnow-35-billion-urls-daily-without-google); no Google primary statement found. Bing matters because Microsoft Copilot and other products draw on its index (general industry understanding, not verified here). |
| Google Indexing API | Do not use for releases. | Google: usable only for pages with JobPosting, or BroadcastEvent embedded in a VideoObject; default quota 200 publish requests a day per project; abuse can lead to revoked access (https://developers.google.com/search/apis/indexing-api/v3/quickstart and https://developers.google.com/search/apis/indexing-api/v3/quota-pricing). A livestreamed webcast page could qualify; a press release does not. |
| Google Publisher Center and Google News | Not a route for a company site. | Google says publishers no longer need to apply; policy-compliant publishers are eligible for consideration, and Publisher Center membership does not decide eligibility or guarantee visibility (reported by the search tool from Google's help pages, e.g. https://support.google.com/news/publisher/answer/4203?hl=en-GB ; the page's own text was not retrieved, so verify). Reports that Google stopped accepting new publications in Publisher Center are from a third party (https://userp.io/news/google-news-removes-manual-publication-option) and need verification. Google News is aimed at news publishers; a company's own newsroom page is unlikely to qualify. |
| Wire distribution (Newsfile) | The real route to Yahoo Finance and wire-fed sites. See Part 2e. | Part 2e. |

Realistic expectation: a release page on a site of OCAL's authority is usually crawled within hours to a few days with sitemap, internal links and URL Inspection; "indexed within an hour" is not guaranteed by any documented method for Google. Bing and Yandex via IndexNow are typically faster (not documented with numbers). Wire pages are indexed fastest because the wires have high crawl priority, which is why they currently outrank OCAL for its own news.

### How AI answer engines pick up company facts

- **Google AI Overviews and AI Mode.** Google's own guidance: pages must be indexed and snippet-eligible, "no additional technical requirements", no special markup or AI text file is needed, structured data should match visible text, keep important content in text form, and crawling must be allowed (source: https://developers.google.com/search/docs/appearance/ai-features). They use query fan-out, so several related pages from one site can be cited for one question. Implication: the Facts page, the Listings page, the FAQ and the About page all need to be real, crawlable HTML.
- **ChatGPT search and Perplexity.** No primary-source or empirical study was found on how they weigh Wikidata, Crunchbase or LinkedIn; the search turned up only vendor blogs, which are not evidence. The reasonable, low-risk steps follow from how retrieval systems work in general: they cite pages they can fetch, so serve static HTML; they prefer pages that state facts plainly and consistently across sources, so keep the entity data identical everywhere; and they surface third-party profiles, so correct those profiles. This is advice from first principles, not proven ranking science.
- **Concrete steps.**
  1. A /investors/facts/ page: definition list of legal name, former name, tickers (TSXV: OCAL; FSE: JC3), ISIN, CUSIP, WKN, head office, phone, IR email, fiscal year end (31 August), officers and directors by OCAL role, transfer agent, auditor, counsel, listing date, "last updated" date. One page, no marketing language, same text as the schema description.
  2. The same one-paragraph description everywhere (Pack S in Part 2d for short fields, Pack L for 500 characters), including Wikidata, Crunchbase and LinkedIn "About".
  3. Wikidata item with the properties listed in Part 2d (instance of business, stock exchange, ticker, official website, LEI, headquarters, inception, ISIN) and a COI disclosure on the talk page; Crunchbase claimed and corrected; LinkedIn page text matched.
  4. Bloomberg and LSEG/Refinitiv profile corrections through the routes in Part 2d (the Bloomberg route is confirmed; LSEG and FactSet public issuer routes were not found).
  5. robots.txt: keep Googlebot and Bingbot allowed. Allow search-grounding crawlers such as OAI-SearchBot and PerplexityBot unless Matthew wants otherwise (the current robots.txt allows everything). Training-only crawlers (GPTBot, Google-Extended, which Google documents as the control for AI training and grounding in other Google systems) are a policy choice for Matthew; for an issuer wanting to be known, allowing is the default recommendation.
  6. llms.txt is optional; Google says no AI text file is required. Skip unless CQ wants it.
  7. Ask the engines. After launch, test five prompts weekly in ChatGPT, Perplexity, Gemini and Google AI Mode ("What is OCAL Financial?", "What stock exchange is OCAL Financial listed on?", "OCAL Financial Frankfurt symbol", "Who is the CEO of OCAL Financial?", "Is OCAL Financial a car dealer?") and log what each says and which sources it cites. Wrong answers point to the profile that needs fixing.

### Compliance and risk notes for the SEO work

- Anything posted on the website is disclosure: an on-site summary of a release must match the wire text and cannot add material information (TMX electronic communications guidance, cited in Part 1 vendor section). A "why it matters" block should be limited to links and restated facts.
- Release pages go live only after wire dissemination (same guidance).
- Category and comparison pages (asset-light, Carvana, AutoCanada) are promotional content and should go through the same Lawson and CIRO review path as releases (the 29 Sep CIRO query concerned "digital inventory").
- OCAL roles only in every bio, schema block, Wikidata item and vendor profile: no outside roles or prior-company history.
- The consumer site and the IR site share a domain: keep consumer lead-gen scripts and promotional calls to action off investor pages, per TMX best practice.



Method note. Everything below was read from the pages cited. Where a page could not be read (JavaScript pages, HTTP errors) or a route could not be confirmed on an official page, the cell says "not verified". No email, form or account action was taken anywhere. Prices marked "estimate" come from third-party articles, not from the vendor.

## Part 2d. Data vendor hygiene

### Headline findings (read these first)

1. **One upstream source drives most of the stale text.** Yahoo's own data-provider page says global company profiles on Yahoo Finance come from S&P Global Market Intelligence (S&P Capital IQ). Simply Wall St says all its data comes from S&P Global Market Intelligence. The Yahoo, Simply Wall St, Investing.com, Stockhouse, stockanalysis.com and Weiss descriptions are the same sentence ("through its finance platform, offers vehicle financing solutions ... auto, power sports, recreational vehicles, personal loans, auto repair, and healthcare financing"). Fixing the Capital IQ record is the single highest-value action. (Only Yahoo and Simply Wall St documented their S&P link; for Investing.com, Stockhouse and Weiss the source is not stated, and the identical wording is the evidence.)
2. **The powersports, RV and healthcare wording is OCAL's own pre-listing text, not generic Ronin text.** It matches the 13 Feb 2026 LOI release, the Newsfile company page for OCAL, and a Tracxn profile last updated 14 Feb 2026 (inference: vendors scraped OCAL's pre-redesign website and LOI material; the website was redesigned on 3 Sep 2026 per Stockwatch's headline list). Other stale items do come from the Ronin shell: S&P Capital IQ reported a "full year ended February 28, 2026" result under the OCAL name (Ronin's old fiscal year; OCAL's year end is 31 August), and CNBC lists "Anthony Zelen" as CEO, CFO, Corporate Secretary and Director (not an OCAL officer on ocalfinancial.ca; presumably a legacy Ronin officer, not verified).
3. **The Feb 2026 LOI text called OCAL a "virtual brokerage".** Related LOI wording is still live on Newsfile's OCAL company page ("fully virtual, AI-native licensed automotive finance platform ... prime to deep subprime"), MarketScreener and CNBC, and the Newsfile page also says "Canada's first". Newsfile's company page is controlled by OCAL through its Newsfile account, so it can be corrected without any third party (route: Newsfile account manager; a self-serve form is not verified).
4. **Name error.** Yahoo, Simply Wall St and stockanalysis.com spell the CEO "Medhi Moghareh" (correct: Mehdi). Same upstream (S&P).
5. **A lapsed BVI entity has the identical legal name "OCAL FINANCIAL INC."** in the GLEIF register (LEI 875500SZTUW4O1V6TQ62, status LAPSED). OCAL's own LEI is 984500E70698C2C2AC97 (status ISSUED, renews 2027-07-31), but its registered legal address on GLEIF is 1600 - 925 West Georgia Street, Vancouver, not 500 - 885 Dunsmuir Street. Confirm which address is intended and update through the LEI issuer. Wikidata, Crunchbase and vendors that match on name could confuse the two entities.
6. **Morningstar is already close to right** (see table), so the Yahoo problem is S&P, not Morningstar.
7. **Yahoo shows an estimated earnings date of "Oct 27, 2026"**, which is not an OCAL-announced date I could find. OCAL's year ended 31 Aug 2026, and a venture issuer has 120 days (to about 29 Dec 2026) per OCAL's own investor page. Which vendor owns that field: not verified.

### Proposed profile text (the "pack" referred to in the table)

Built from the 22 Oct 2026 "About OCAL" paragraph (the latest wording that went through the Newsfile and CIRO route). Matthew to approve before anything is sent anywhere.

- **Pack L (484 characters, fits Stockhouse's 500 limit):** "OCAL Financial Inc. is a Vancouver-based, asset-light, AI-native virtual automotive dealership and vehicle-finance platform. Operating remotely and licensed in British Columbia and Alberta, OCAL takes customers from application to lender approval, vehicle matching, digital contracting and delivery. It sources each vehicle only after approval, through OPENLANE Canada, and earns revenue from vehicle sales and related finance and protection products. It does not hold consumer loans."
- **Pack S (338 characters):** "OCAL Financial Inc. is a Vancouver-based virtual automotive dealership and vehicle-finance platform, licensed in British Columbia and Alberta. It sources each vehicle after a customer is approved and earns revenue from vehicle sales and related finance and protection products. It does not hold consumer loans or take credit-default risk."
- **Pack 1 (101 characters):** "Virtual automotive dealership and vehicle-finance platform, licensed in British Columbia and Alberta."
- **Pack F (facts):** Legal name OCAL Financial Inc. (formerly Ronin Ventures Corp.). TSXV: OCAL; Frankfurt: JC3 (WKN A42K21). ISIN CA67449X1050; CUSIP 67449X105; LEI 984500E70698C2C2AC97. Head office Suite 500, 885 Dunsmuir Street, Vancouver, BC V6C 1N5; phone (604) 687-7765; website https://ocalfinancial.ca; investor contact investors@ocal.ca. Operating business incorporated 23 Apr 2021; began trading as OCAL 21 Jul 2026; fiscal year end 31 August. Officers: Mehdi Moghareh (CEO and Director), Matthew Friesen (Executive Chairman and Director), Terence Lee (CFO and Corporate Secretary); directors Michael Stier and Robert Birmingham. Transfer agent Endeavor Trust Company; auditor DMCL LLP; counsel Lawson Lundell LLP. Sources: ocalfinancial.ca/investor-relations, Newsfile releases 305866 and 306175, the Feb 2026 LOI release, and Yahoo for the address and phone as currently shown.
- **Wording choices to confirm.** (a) I used "OPENLANE Canada" only in the form the 22 Oct release used it ("exclusive auction and sourcing channel" is in that release; I left that phrase out of the packs). I left out "digital inventory of 3,000+ vehicles" and "five channels" because your notes record that CIRO queried "digital inventory" on 29 Sep and that the five-channel pitch conflicts with the "exclusive" wording. Add the "zero standing inventory" line only if you want it in vendor text (use that phrase, never "zero inventory" alone). (b) No "broker", no "Canada's first", no revenue figure (FY2025 revenue of $6.48M audited already shows in Yahoo financials; not needed in a description). (c) Biographies for Crunchbase, Wikidata or vendors: OCAL role only, no outside roles. (d) One cross-check outside the vendors: your Sept notes say the AMVIC register still shows the old entity name for B2036050, which sits uneasily with "licensed" in every boilerplate; not a vendor issue, flagged once.
- **Industry classification (recommendation, your call).** Vendors currently show Credit Services (Yahoo), Banking Services (Investing.com), Consumer Lending (MarketScreener), Financial Conglomerates (TradingView), Consumer Finance (Simply Wall St). The release says vehicle sales are the largest revenue source and OCAL arranges rather than lends. Recommended ask: primary "Automotive Retail" (online vehicle retail), secondary "Consumer Finance". This changes the peer set vendors show (today Investing.com lists GRMI, AMT, 6623, NWAU and SPST as peers).

### Vendor table

| Vendor | Where profile comes from | How to correct (URL or route) | Turnaround | What OCAL should have it say | Status observed 23 Oct 2026 |
| --- | --- | --- | --- | --- | --- |
| TMX Money (money.tmx.com) and TSXV Issuer Services | TMX says TSX and TSXV do not supply TMX Money data; it is sourced from third parties including Barchart, Cision, Morningstar, QuoteMedia, SEDAR, SEDI and TipRanks. QuoteMedia supplies profile fields such as business description, address, website and sector. | TMX FAQ for Listed Issuers has dedicated articles "How Can Companies Update / Correct Their Company Description?" and "...Industry and/or Sector Classifications?" (titles confirmed on the FAQ index; article text could not be retrieved). Sister articles give the route: TSX/TSXV Company Services at issuer.services@tmx.com, who relay requests to providers but cannot guarantee changes; QuoteMedia at support@quotemedia.com for website changes. TMX LINX issuer portal (Principal Contact) controls uploaded Investor Kit content; tmxadmin@tmx.com if the Principal Contact is unknown. Company Services contact page: tsx.com/en/contact/public-company-reps. | Issuer Services replies in 2 business days; QuoteMedia in 5 business days (both per those sister articles); actual change not guaranteed. | Pack L or S, Pack F, industry per recommendation above. | Quote page loads (price $0.11, 36,667,803 shares, escrow 23,638,104). Profile and description sub-pages are JavaScript and returned no text, so description NOT captured. News tab shows OCAL releases credited to "TMX Newsfile" (latest 22 Oct 7:56 AM EDT). TMX Datalinx issuer-correction route: not verified (its Issue Data security master lists "nature of business" as a field). |
| S&P Capital IQ (S&P Global Market Intelligence) | Collects from public sources including regulators, company websites, exchange sites and news agencies, plus company contacts (per Simply Wall St's description of its S&P feed). Feeds Yahoo Finance profiles, Simply Wall St, and sector and industry data for Google Finance. | Yahoo Help names clientsupport@capitaliq.com for company-info updates. S&P's current contact page lists support.CIQ@spglobal.com (Capital IQ client support) and support.CapIQPro@spglobal.com; the $50 Quality Program is for subscribers only. Whether an issuer who is not a client is served: not verified. Suggested content: a short factual note citing the 22 Oct release, the website About page and the SEDAR+ filing statement. Also ask a broker or IR firm with a Capital IQ seat (Signal Capital, Integral Wealth) to file it. | Yahoo says changes show on Yahoo within up to 14 days of the vendor change. S&P's own turnaround: not documented for non-clients. | Pack L, Pack F, name spelling Mehdi, fiscal year end 31 Aug, industry per recommendation, and remove the Feb 28 Ronin fiscal-year series if it sits under OCAL. | Source of the stale text (see headline finding 1). Earnings item credited to S&P Capital IQ on MarketScreener: "full year ended February 28, 2026" under the OCAL name (Ronin legacy). |
| Refinitiv / LSEG | Company metadata and corporate actions for Google Finance, and Yahoo's footnote "Data provided by Refinitiv" for insider and institution holdings. Business description source for LSEG not confirmed. | No public issuer correction form found. Subscribers use the Refinitiv Content Helpdesk (Workspace Contact Us, my.refinitiv.com). Contributors can use contribute@lseg.com per LSEG's contribute-data page. Route for a non-subscribing issuer: not verified; use a broker or IR firm with Workspace. | Not documented. | Pack S, Pack F, OCAL's LEI. | Not observed (terminal product). Yahoo shows "% held by insiders 61.15%" sourced to Refinitiv, plausible given escrow. |
| FactSet | Overview profile has business description, industry (RBICS), contact fields and Crunchbase categories (per FactSet's profile API schema). | No public issuer route found. FactSet's contact page offers support for existing clients only (support +1.877.322.8738). Route for non-client issuers: not verified; use a broker or IR firm with a FactSet seat. | Not documented. | Pack S, Pack F. | Not observed (terminal product). CNBC's profile text matches the LOI wording and shows the wrong executive; CNBC's data source is not verified, so do not assume FactSet. |
| Morningstar | Morningstar data analysts capture from annual reports and filings; operating data (address, industry classification, business description) is refreshed annually when the annual report arrives, and corporate actions can trigger updates (Nasdaq/Morningstar FAQ). Feeds Yahoo's financial statements and market cap, TMX Money, and Google Finance end-of-day prices. | dataquestions@morningstar.com, +1 312 696-6600 (Morningstar contact page; Europe: dataquestions.uk@morningstar.com). Yahoo Help also names this address for company info. | Annual refresh cycle for descriptions, so the FY2026 annual report (due by about 29 Dec 2026) is the natural trigger. | Pack S. Already close; ask only to add the OCAL TSXV listing and the 31 Aug year end. | Morningstar JC3 page (morningstar.com.au) reads: Canadian financial technology company with a digital platform for vehicle financing, revenue from vehicle sales, financing and warranties, serves BC and Alberta; sector Financial Services, industry Credit Services; Vancouver address correct; fiscal year end shown as 31 August 2027 (a year ahead, check). The OCAL.V Morningstar page was not retrievable. |
| Yahoo Finance | Per Yahoo Help: global company profile, EPS and revenue estimates, analyst data from S&P Global Market Intelligence; financial statements, ratios, market cap and shares outstanding from Morningstar; insider transactions from LSEG; corporate events from Wall Street Horizon (a TMX company). An older Yahoo article (SLN24383) says profile and industry come from Capital IQ and Morningstar. News and press releases come from contributing newswires. | Yahoo does not edit profiles. (1) Fix S&P (above). (2) Yahoo Help SLN24383: Capital IQ clientsupport@capitaliq.com, Morningstar dataquestions@morningstar.com. (3) Data corrections: email finance.support@yahooinc.com with the page URL and the error (Yahoo Help SLN2263). (4) Yahoo Finance Feedback Forum (public, needs a Yahoo account; Yahoo Help sln28397). | Up to 14 days after the upstream change (Yahoo Help). | Pack L from S&P, name spelling, executives, earnings date. | Description is the stale text. Sector Financial Services, industry Credit Services. Executives: Friesen Executive Chairman, "Medhi Moghareh" CEO and Director, Terence Lee CFO and Corporate Secretary. Address 500 - 885 Dunsmuir and phone (604) 687-7765 are correct. Estimated earnings date Oct 27, 2026 shown. OCAL.V was read through an Exa cache (WebFetch got HTTP 503); the profile snapshot's price date is not certain. The press-release list page captured no items (JavaScript), so Yahoo's carriage of OCAL releases is not directly confirmed; see Part 2e. |
| Google Finance | Google's disclaimer: end-of-day prices by Morningstar, corporate actions and company metadata by Refinitiv, intraday possibly ICE, sector and industry from S&P Capital IQ, corporate financials from S&P and Fiscal.ai. TSXV quotes carry a 15 minute delay. Google does not verify the data. Knowledge panels (the larger Search panel) are separate: built from many web sources and partner data, and can be claimed. | Finance page: "Send feedback" at the bottom of google.com/finance (Google help 9924955). Knowledge panel: claim and suggest edits via "Get verified on Google" and "Update your Google knowledge panel" (Google Search help 9163198); non-representatives use the panel's feedback link. | Not documented (third-party guides say days to weeks; estimate). | Same text as the upstream vendors, so fix S&P and Refinitiv first. | Page google.com/finance/quote/OCAL:CVE exists but returned only a shell, so the description is NOT captured. Whether OCAL has a Google knowledge panel: not verified. |
| Stockwatch | Stockwatch builds quote pages and a company-participant database (Infojex); its news is picked up automatically from the newswires and edited by Stockwatch to its style guide. | Technical or data problems: contact form (Help, Contact) or webmaster@stockwatch.com; phone 604.687.1500 or 800.268.6397. A page to add a company URL exists at stockwatch.com/Quote/Url (it refers to the US listing URL). For news only: email a release as PDF or Word to news@stockwatch.com after it is public. Profile text route: not verified. | Not documented. | Pack 1 and website URL (Stockwatch shows little more than the URL). | Quote page header reads "V:OCAL - OCAL Financial Inc." with https://ocalfinancial.ca; no business description on that page. It lists every OCAL release since 13 Aug in Stockwatch's own rewritten headlines, some hours after the wire (the 22 Oct Showroom item is stamped 17:00 ET against a 7:56 AM release; the 6 Oct deal-count item 18:22 ET against 9:42 AM). |
| Stockhouse | Uses multiple external data providers (per its support article). Description box on the quote page; the page is also tied to the Grey Market symbol OCALF. | support@stockhouse.com or ticket form (Stockhouse support article 223422627 and contact page). Needs a company-issued email address, or for an IR firm a reference to a press release. Description limit 500 characters, no hyperlinks, no promotion. They also ask providers to be updated. Advertising and licensing: sales@stockhouse.com. | Browser cache clears 90 minutes after confirmation (their note); processing time not documented. | Pack L (484 characters). | Quote page (symbol=v.ocal) shows "GREY:OCALF" and the stale S&P-style text. Stockhouse carried the 22 Oct release the same minute it was issued (11:56 UTC). |
| Simply Wall St | All data from S&P Global Market Intelligence (support article); pages exist for TSXV:OCAL and DB:JC3. | Cannot be edited at the front end; Simply Wall St asks users to message support with a source document (support.simplywall.st, article "What if I spot an error in the data?"). Real fix is at S&P. | News errors are triaged each business day (Australian time); data errors not documented. | Follows S&P. | Overview truncated to "Through its finance platform, offers vehicle financing solutions"; risk flags "Has not reported any financial data" and "Does not have a meaningful market cap"; AGM 10 Dec 2026 shown; CEO "Medhi Moghareh" on the JC3 page. |
| MarketScreener | Source of the profile text is not stated by MarketScreener. Text matches the Feb 2026 LOI and Newsfile company page. News feed items are credited "Newsfilecorp" or "CI" (S&P Capital IQ). | Official correction route: not verified. A third-party LinkedIn listing shows customers@marketscreener.com; treat as unconfirmed. | Not documented. | Pack L, Pack F. | Business description is the LOI-era text (fintech, "prime to deep subprime", Washington, Arizona, Nevada, powersports, RV, healthcare). Sector Consumer Lending. The page shows a +1 (951) 669-7394 phone number I could not tie to OCAL (not verified). Quote 0.1100 CAD at 20 Oct close. Carried the 22 Oct release at 7:58 AM EDT. |
| Investing.com | Source not stated; text identical to the S&P-style sentence. | Official correction route: not verified. | Not documented. | Follow upstream. | Page at in.investing.com/equities/ronin-ventures (the URL slug still says "ronin-ventures") shows the stale text; industry Banking Services, sector Financial. A reseller (Interaction Partners) says Newsfile's North America circuit reaches Investing.com directly (third-party claim). |
| Bloomberg | Bloomberg's own database. A FIGI exists for the TSXV line (BBG0168H3SL1 per TradingView). Bloomberg.com market data pages are a separate product. | Bloomberg Help Center "How do I update a company profile?" and the Bloomberg Professional support page list "Market Data Update Requests" for company profile updates (form link not captured). Terminal users: HELP HELP, then a profile change request. Issuer without a Terminal: ask a broker or IR firm with a Terminal. | Not documented (one Quora answer says 1 to 6 weeks; unreliable, ignore). | Pack S, Pack F. | Terminal profile not observable. Newsfile says it has direct feeds to Bloomberg Terminal (Newsfile blog, 2021). |
| Wikipedia | Volunteer-written. No article for OCAL Financial or Ronin Ventures (Wikipedia search, 23 Oct: zero hits). | Not recommended yet. Notability for companies (WP:NCORP) needs significant coverage in reliable sources independent of the company; trading data and press releases do not count. If ever: anyone paid or connected must disclose on their user page and the talk page, should not edit the article directly, should use the {{Edit COI}} template or the Edit Request Wizard on the talk page, and should submit new articles through Articles for Creation (WP:COI and the paid-contribution disclosure policy). This includes an IR firm such as Signal Capital. | Volunteer queues, weeks (WikiProject Cooperation page lists backlog sizes; no promise). | Not applicable now. | No article. Do not create one. |
| Wikidata | Volunteer-edited structured data, used by Google knowledge panels and many apps. | Notability is met if the item can be described with serious public references (Wikidata notability policy, criterion 2); a Wikipedia sitelink is not required. Rule: do not create items for promotional purposes (Help:Items). Create via the standard "Create a new Item" page (not fetched). Statements: instance of (P31) business (Q4830453); official name (P1448) "OCAL Financial Inc." with former name Ronin Ventures Corp.; official website (P856) https://ocalfinancial.ca; country (P17) Canada; headquarters location (P159) Vancouver; stock exchange (P414) TSX Venture Exchange with qualifier ticker symbol (P249) "OCAL" and a start date of 2026-07-21, then a second P414 Frankfurt Stock Exchange with P249 "JC3"; ISIN (P946) CA67449X1050; LEI (P1278) 984500E70698C2C2AC97; inception (P571) per the operating business; LinkedIn company ID (P4264) "ocalfinancial"; Crunchbase organization ID (P2088) once claimed. Cite SEDAR+, the TSXV bulletin and GLEIF for each. P249 is still used as a qualifier of P414 (a proposal to change that is open on its talk page). | Immediate on save. | Pack 1 as the item description. | No Wikidata item exists (entity search "OCAL Financial" returned empty). Paid editing disclosure under Wikimedia's Terms of Use applies to Wikimedia projects generally (Wikimedia Foundation notice). |
| Crunchbase | Crowd-sourced plus company claims. Feeds Google Finance's private company data and FactSet's profile category field. | Any registered user can edit; verified employees (log in with a company-domain email, "Manage My Company") control the Overview section; support@crunchbase.com for help (Crunchbase Knowledge Center). | Edits are immediate for verified users; staff review for locked fields not documented. | Pack S, Pack F; people: OCAL roles only. | A profile appears to exist under the old trade name (slug "one-click-auto-loans", seen on a third-party LinkedIn aggregator, not directly fetched). Tracxn (a separate database) still describes a "provider of financing solutions for auto, personal loans, powersports, RVs, and healthcare" as of 14 Feb 2026. |
| LinkedIn company page | OCAL-controlled. | Super admin: Edit page (LinkedIn Help a564346). Verification needs eligibility such as Ads, Jobs or Premium Company Page, plus website domain proof (Help a7174627, a6275638); can take up to 10 days. | Edits immediate. | Pack S in the overview, website, industry, headquarters. | Page exists (linkedin.com/company/ocalfinancial). The visible text is about a virtual dealership and fintech platform, "type: public company", alias "One Click Auto Loans". No stale powersports text. Verification status not verified. |
| Frankfurt / Deutsche Boerse (FSE: JC3) | Deutsche Boerse Open Market (Freiverkehr) master data from the inclusion application. For the Quotation Board, a trading participant who is also a specialist applies, or Deutsche Boerse includes shares without any application (AGB section 10). Prerequisites include an ISIN and an issuer LEI (section 7). The Scale segment needs a Capital Market Partner (the issuer has no access to the E-Listing tool). | Issuer-initiated changes go through whoever applied (participant or Capital Market Partner). Direct contact route at Deutsche Boerse for a Quotation Board issuer: not verified. Identifiers: ISIN CA67449X1050, WKN A42K21, symbol JC3 (OCAL release of 25 Aug 2026). | Not documented. | Pack F identifiers; make sure the LEI address matches. | Börse Frankfurt page could not be fetched. Third parties show JC3: Morningstar (decent text), Yahoo JC3.F, GuruFocus (NAICS 522291, IPO 2026-08-24), CNBC (stale text and wrong executive), Simply Wall St (market cap about 2.2 million euros). The OCAL release calls Frankfurt a "secondary listing"; whether the segment is Quotation Board or Scale: not verified. |
| SEDAR+ profile | The issuer's own filing. NI 13-103 section 4: profile information must be accurate and updated at the earlier of the next filing or 10 days after you know it is inaccurate. CSA help: accuracy of an issuer profile is solely the issuer's responsibility. | Maintain the profile in SEDAR+ through the issuer's Authorized Super User or a filing agent (Newsfile files for many issuers). Report errors to the principal regulator named on the profile (for a BC head office, normally the BCSC; not verified for OCAL). | The 10 day rule is the legal deadline. | Legal name OCAL Financial Inc., Suite 500, 885 Dunsmuir address, industry per the filing statement, fiscal year end 31 August, former name Ronin Ventures Corp. | Public profile not fetched (JavaScript). Check legal name, address, year end (Ronin was 28 Feb) and previous names. S&P and others scrape this, so errors here propagate. |

### Short notes

- **Fix order (suggested, nothing done).** (1) Confirm Pack L and the industry call. (2) Newsfile company page and the website About page, which OCAL controls. (3) Capital IQ, which fixes Yahoo, Simply Wall St and probably Investing.com and Stockhouse. (4) TMX Issuer Services for TMX Money and QuoteMedia. (5) Stockhouse and Morningstar. (6) LinkedIn and Crunchbase. (7) LEI address and SEDAR+ profile hygiene. (8) Wikidata later, with sources, from an account that discloses its connection.
- **Why one boilerplate matters.** S&P collects from company websites and press releases, so a single consistent "About OCAL" paragraph in every release and on the website is how the text sticks. The 22 Oct release already uses newer wording; earlier releases used "OPENLANE auction network and select partners", so vendors may have picked up either.
- **Not found at all.** An official, public, issuer-facing correction form for FactSet, LSEG/Refinitiv, Investing.com, MarketScreener and Deutsche Boerse. For these the practical route is a broker or IR advisor with a seat, or the vendor's sales or support line.
- **Pages I could not read.** TMX Money profile tab, Google Finance, Börse Frankfurt, SEDAR+, Yahoo OCAL.V press-release list, Wealth Awesome stock page, Morningstar OCAL.V page.
- **Wealth Awesome.** Only auto-generated articles for OCAL.V were found (for example "What's Going On With OCAL Financial Inc. Stock Tuesday?", 13 Oct 2026), with a price-range model and bull and bear cases; no company description block was captured. Correction route for Wealth Awesome: not verified.
- **Weiss Ratings** (weissratings.com/en/stock/ocal-v-tsx/profile): reads as the S&P sentence ("vehicle financing solutions" through its finance platform), sector Financials, industry Financial Services; no employee count, market data or founding year.

### Sources (Part 2d)

- https://finance.yahoo.com/quote/OCAL.V/profile/ (via Exa cache; WebFetch returned HTTP 503)
- https://finance.yahoo.com/quote/OCAL.V/
- https://finance.yahoo.com/quote/OCAL.V/financials/
- https://finance.yahoo.com/quote/OCAL.V/press-releases/
- https://finance.yahoo.com/quote/JC3.F/key-statistics/
- https://help.yahoo.com/kb/SLN24383.html
- https://help.yahoo.com/kb/SLN2310.html
- https://help.yahoo.com/kb/SLN2263.html
- https://help.yahoo.com/kb/report-problems-feedback-ideas-yahoo-finance-sln28397.html
- https://weissratings.com/en/stock/ocal-v-tsx/profile
- https://money.tmx.com/en/quote/OCAL
- https://money.tmx.com/en/quote/OCAL/key-data
- https://money.tmx.com/en/quote/OCAL/news
- https://money.tmx.com/en/admin/info
- https://tmxmoneysupport.zendesk.com/hc/en-us/sections/360009595194-FAQ-for-Listed-Issuers
- https://tmxmoneysupport.zendesk.com/hc/en-us/articles/360053563733-Where-Does-TMX-Money-Source-its-Information-and-Data
- https://tmxmoneysupport.zendesk.com/hc/en-us/articles/360052784214-How-Can-Companies-Update-Correct-Their-Shares-Outstanding
- https://tmxmoneysupport.zendesk.com/hc/en-us/articles/360058414753-How-can-Companies-Update-Correct-their-Displayed-Company-Website-Address
- https://tsx.com/en/company-services/building-your-company-profile
- https://tmxpowerstream.quotemedia.com/contentsolutions/company_profiles
- https://www.tmxinfoservices.com/resource/en/91
- https://www.spglobal.com/market-intelligence/en/info/contact-us
- https://www.spglobal.com/market-intelligence/en/solutions/products/quality-program
- https://support.simplywall.st/hc/en-us/articles/8908651462543-Where-do-you-source-financial-data
- https://simplywall.st/stocks/ca/diversified-financials/tsxv-ocal/ocal-financial-shares
- https://simplywall.st/es/stocks/de/diversified-financials/fra-jc3/ocal-financial-shares
- https://www.google.com/googlefinance/disclaimer/
- https://support.google.com/websearch/answer/9924955
- https://support.google.com/knowledgepanel/answer/9163198
- https://www.google.com/finance/quote/OCAL:CVE
- https://www.stockwatch.com/Quote/Detail?V:OCAL
- https://www.stockwatch.com/Help/Contact
- https://www.stockwatch.com/Help/Newsdiss
- https://www.stockwatch.com/Quote/Url
- https://stockhouse.com/companies/quote?symbol=v.ocal
- https://support.stockhouse.com/hc/en-us/articles/223422627-How-to-update-your-company-profile-on-Stockhouse
- https://stockhouse.com/corporate/contact-us
- https://www.marketscreener.com/quote/stock/OCAL-FINANCIAL-INC-212887150/company/
- https://ca.marketscreener.com/news/ronin-ventures-corp-reports-earnings-results-for-the-full-year-ended-february-28-2026-ce7f5cdddb8af120
- https://in.investing.com/equities/ronin-ventures
- https://interactionpartners.ch/north-american-distribution
- https://www.morningstar.com.au/investments/security/fra/JC3/summary
- https://www.morningstar.com/company/global-contacts
- https://www.nasdaq.com/european-market-activity/shares/fact-sheet-faq
- https://www.bloomberg.com/help/question/can-update-company-profile/
- https://professional.bloomberg.com/support/
- https://www.tradingview.com/symbols/TSXV-OCAL/
- https://www.cnbc.com/quotes/OCALF
- https://www.cnbc.com/quotes/JC3-FF
- https://www.gurufocus.com/stock/FRA:JC3/summary
- https://stockanalysis.com/quote/tsxv/OCAL/company/
- https://tracxn.com/d/companies/ocalfinancial/__PX4H4OH0Y5hLuMkHurXEKm-B4YmA9HA8SxcyLS5gNto
- https://www.newsfilecorp.com/company/12553/OCAL-Financial
- https://www.tradingview.com/news/reuters.com,2026-02-14:newsml_Tnw5Tp8SL:0-1301756-b-c-ltd-dba-ocal-financial-and-ronin-ventures-corp-enter-into-letter-of-intent-to-complete-qualifying-transaction-and-listing-on-the-tsx-venture-exchange/
- https://www.lseg.com/en/data-analytics/market-data/contribute-financial-data
- https://www.lseg.com/en/contact-us
- https://www.factset.com/contact-us
- https://raw.githubusercontent.com/api-evangelist/factset/refs/heads/main/openapi/factset-profile-api-openapi.yml
- https://en.wikipedia.org/wiki/Wikipedia:Conflict_of_interest_editing
- https://en.wikipedia.org/wiki/Wikipedia:Paid-contribution_disclosure
- https://en.wikipedia.org/wiki/Wikipedia:Edit_Request_Wizard/Paid
- https://en.wikipedia.org/wiki/Wikipedia:Notability_(organizations_and_companies)
- https://en.wikipedia.org/wiki/Wikipedia:WikiProject_Cooperation
- https://wikimediafoundation.org/news/2014/06/16/change-terms-of-use-requirements-for-disclosure/
- https://www.wikidata.org/wiki/Wikidata:Notability
- https://www.wikidata.org/wiki/Help:Items
- https://www.wikidata.org/wiki/Property:P249
- https://www.wikidata.org/wiki/Property_talk:P249
- https://www.wikidata.org/wiki/Property:P414
- https://www.wikidata.org/wiki/Property:P856
- https://www.wikidata.org/wiki/Property%3AP159
- http://wikidata.org/wiki/Wikidata:WikiProject_Companies/Properties
- https://api.gleif.org/api/v1/lei-records?filter[entity.legalName]=OCAL%20FINANCIAL%20INC.
- https://support.crunchbase.com/hc/en-us/articles/115010477107-Edit-a-Profile-on-Crunchbase
- https://support.crunchbase.com/hc/en-us/articles/360022296433-How-do-I-verify-my-account
- https://linkedin.com/company/ocalfinancial
- https://www.linkedin.com/help/linkedin/answer/a564346
- https://www.linkedin.com/help/linkedin/answer/a7174627
- https://www.linkedin.com/help/linkedin/answer/a6275638
- https://www.cashmarket.deutsche-boerse.com/cash-en/Get-Listed/ipo-line-going-public/ipo-line-going-public
- https://www.cashmarket.deutsche-boerse.com/resource/blob/34046/37401e6cd5311997bfdc3fda44ba9fe6/data/2026_06_12_dbag_agb_freiverkehr_en.pdf
- https://www.tradingview.com/news/tmx_newsfile:d243df961094b:0-ocal-financial-common-shares-now-trading-on-the-frankfurt-stock-exchange/
- https://systems.securities-administrators.ca/onlinehelp/faqs/maintaining-a-profile/
- https://www.bcsc.bc.ca/-/media/PWS/New-Resources/Securities-Law/Instruments-and-Policies/Policy-1/13103-NI-July-25-2025.pdf?dt=20250724184355
- https://ocalfinancial.ca/investor-relations
- https://wealthawesome.com/whats-going-on-with-ocal-financial-inc-stock-tuesday-10132026-wgo

## Part 2e. Distribution

### Distribution table

Price column: "published" means on the vendor's own page; "reseller" means a reseller or issuer-service page; "estimate" means a third-party article. Currency as stated. All prices are single-release planning anchors, not quotes.

| Service | Reach as documented (Yahoo Finance, Google News, Bloomberg, Refinitiv, FactSet, Canadian terminals) | Cost per release | Notes for OCAL |
| --- | --- | --- | --- |
| Newsfile Corp / TMX Newsfile (OCAL's wire) | Yahoo Help lists Newsfile as a contributing newswire. Newsfile says it reaches major broker terminals, financial databases and aggregators and ensures stock exchange compliance; a 2021 Newsfile blog says direct feeds to Thomson Reuters Eikon, Thomson One and Bloomberg Terminal. A reseller page lists Bloomberg, Refinitiv, FactSet, Dow Jones, LexisNexis, Yahoo Finance and Investing.com on its North America circuit (reseller claim). Observed for OCAL on 22 Oct: TMX Money 7:56 AM EDT, Stockhouse and 6ix 7:56, MarketScreener 7:58; TipRanks, StreetInsider, Kalkine, TradingView and Finanznachrichten also carry OCAL Newsfile items. Google News inclusion: not documented, not verified. | Newsfile does not publish prices. I could not open a Newsfile pricing page (the TSXV tier page you mentioned): not found. Estimate "about $300 to $1,200 per release" (The Next Gen Nexus, May 2026, labelled a planning anchor). Reseller: Interaction Partners (Swiss) quotes its Newsfile North America circuit from CHF 425 per release plus CHF 750 a year; that is a reseller price for a different customer type. | OCAL pays for Newsfile directly; ask the account manager for the TSXV rate card and per-release add-ons (images, extra circuits). Newsfile's own site says it also handles SEDAR+ and EDGAR filings. |
| GlobeNewswire (Notified) | Canada National via the Canadian Press wire network (about 700 outlets), Globe and Mail, National Post, Stockwatch and others (GlobeNewswire pages); an older Canadian page lists TSX, Bloomberg, Dow Jones, Thomson Reuters, Yahoo Canada and Stockhouse for IIROC-compliant distribution. US National lists Yahoo Finance, Bloomberg, CNBC, AP. Yahoo Help lists it as a contributing wire. | No public rate card. Reseller FrontFundr: C$750 for a standard Canada release (text and logo), images C$140, video C$170 (date not shown). Estimate US$600 to 1,200 for North America (NewswireJet, Sep 2025). | Strong Canadian newsroom reach (CP wire); more journalist pickup than a finance-only wire. |
| ACCESSWIRE (now ACCESS Newswire) | Yahoo Help lists it. National tier says broker terminals, trading platforms and AP; has a Canadian site (accesswire.ca) with SEDAR filing shown on its Canadian subscriptions; calls itself a top three newswire in Canada (company claim). | Published (ACCESS blog, May 2024): public company National US$775, Premium US$1,095 per release, flat, no word or image fees. Third-party Jan 2026 pay-as-you-go: Budget US$457, National US$853, US Premium US$1,205 (estimate). Apr 2026 article 5-pack list: US$363, US$660, US$1,023 per release (estimate). | Cheapest flat-fee route with a published card. |
| Cision / PR Newswire Canada (CNW) | Yahoo Help lists PR Newswire. CNW appeared in the TSX Company Manual's list of paid distribution news services (2017 OSC notice). Reach: Canadian newsrooms, AP, financial sites. | No public rate card. Estimates only: US$800+ per Canadian release (listicle, Feb 2026); PR Newswire national US$1,300 to 2,600 (Vendr estimate, 2026). Treat as unverified. | Highest cost and the biggest journalist database; no reason to switch for a TSXV microcap unless a media push needs it. |
| Business Wire | Yahoo Finance, Morningstar, AP (Business Wire's own "find your news" page); claims FactSet, Factiva, LexisNexis, Bloomberg and TSX approval for Canada (third-party summary of company claims). | Published: from US$475 for 400 words on a US local circuit; wider circuits, extra words and multimedia cost more (businesswire.com/pricing). Vendr estimate for US national US$1,200 to 2,500. | US-centric; useful if OCAL wants US exposure before a US listing. |
| Stockwatch (dissemination) | Free dissemination of material Canadian public company news; picks releases up from newswires automatically, edits them to its style, posts them to its site and subscribers. For slightly faster pickup, email the public release as PDF or Word to news@stockwatch.com (Stockwatch Help, News Dissemination). | Free for news; paid eblasts (15,000 opted-in users) via sales@stockwatch.com, price not published. | Observed edits and later timestamps (see Part 2d). Not a substitute for a Policy 3.3 newswire. |
| Stockhouse | Carries Newsfile press releases (observed for OCAL, same minute). Offers paid IR products. | Price not published (sales@stockhouse.com). | Free ride on the wire feed; profile text fixable by support ticket. |
| Finanznachrichten | German aggregator; carries OCAL's July Newsfile release (observed URL). Source list and any issuer route: not verified. A 2011 company release says it took news from 412 media sources. | Not applicable (aggregator). | Relevant to the JC3 European audience. |

### Notes

- **Required by rule.** TSXV Policy 3.3 Part 7 says each release must be given to a news dissemination service (or combination) that carries the full text unedited to the national financial press and daily newspapers, to all Participating Organizations and to regulators; the onus is on the issuer and cost is no excuse (Part 7 as read in the Spanish edition of Policy 3.3, and the TSX Guide to Timely Disclosure, same substance). On 21 May 2026 TSXV repealed Appendix 3C, its old list of commercial news disseminators, and told issuers to keep complying with Part 7 (Notice to Issuers), so there is no approved-vendor list any more: pick any wire meeting those three tests. CIRO says news releases with material information must go out over a newswire before they are posted on the company's website or social media, and TSXV releases must be reviewed by CIRO under Policy 3.3 (CIRO timely disclosure page). The TSX guide says to notify market surveillance beforehand via the PR Portal or pr@ciro.ca (your Oct notes list a CIRO West address; not re-verified). Under NI 51-102 s. 7.1 a material change requires immediately issuing and filing a news release (law-firm summaries; the instrument text itself was not fetched).
- **No "submit your release" step at Google.** Google's Publisher Center page says publishers do not need to submit their site to be eligible; Google discovers news content through Search crawling, and a news sitemap only helps its crawler find content faster. Publisher Center is optional (Google News Initiative training). Publishers can self-apply a "Press release" content label there if their site mostly publishes press releases.
- **Can OCAL's own site be a Google News source?** Yes in principle: any crawlable site that meets Google's content and transparency policies (clear dates, information about the publisher, contact details) can appear. A site that only publishes its own releases is a weak news source in practice (my read, not a Google statement). In OCAL's case the company page posts after the wire (CIRO sequencing). OCAL's release pages already exist under ocalfinancial.ca/investor-relations/press-release/. Whether any OCAL page is in Google News: not verified (I cannot query Google News from here).
- **Wires and Google.** Wire releases reach Google surfaces through the wire's own domains and syndication partners. Since May 2023 Google recommends that syndication partners noindex copies, so many partner copies never get indexed; the wire's own page (newsfilecorp.com) is normally the indexed original (reported by SEO practitioners; two independent write-ups agree). Which Newsfile domain Google News treats as a source: not verified.
- **Google News versus Top Stories.** Google News (news.google.com and the app) is a product; Top Stories is a block inside Google Search results, chosen algorithmically for queries Google treats as newsworthy. Appearing in one does not imply the other, and no vendor can buy or guarantee Top Stories. Freshness, prominence and source authority drive ranking (Google "How news works"). For a TSXV microcap with thin independent coverage, a Top Stories box for "OCAL Financial" is possible only when Google sees fresh, authoritative pieces; do not plan around it.
- **Yahoo Finance and wire feeds.** Yes, automatic. Yahoo does not accept releases from companies directly; it takes them from contributing wires (Newsfile, PR Newswire, ACCESSWIRE, Business Wire, GlobeNewswire, NewMediaWire). The release must have the ticker symbol in its header so Yahoo attaches it to the quote page (Yahoo Help SLN24383). Yahoo quote pages show the wire's name beside each item (for example Shopify's list shows GlobeNewswire, Business Wire, PR Newswire, TMX Newsfile and ACCESS Newswire). I could not capture OCAL.V's own press-release list (page is dynamic), so confirm by eye.
- **The "within an hour" claim.** What the evidence supports: on 22 Oct the Newsfile release was on TMX Money at 7:56 AM EDT, Stockhouse and 6ix at 7:56, MarketScreener at 7:58, so finance aggregators carried it within zero to two minutes. What it does not support: Google News tab or Top Stories inside an hour. Google says it cannot guarantee that every article is published or how it ranks. A third-party analysis puts web-search indexing of wire copies at roughly 2 to 8 hours (estimate, skewed to US technology releases). The honest promise is: on Yahoo (given the ticker header), TMX Money, Stockhouse and MarketScreener within minutes; in Google web search typically within hours; Google News and Top Stories not controllable.

### Release-day checklist to get into Google News and Yahoo within an hour

Each line states the evidence. Nothing here is sent or submitted by me.

1. **Pre-file with CIRO before the wire** (TSXV Policy 3.3; CIRO timely disclosure page; TSX guide: PR Portal or pr@ciro.ca). Evidence: CIRO says releases are reviewed and must be disseminated by newswire before website or social posting.
2. **Use a contributing wire, Newsfile** (Yahoo Help SLN24383 lists it). Evidence: the 22 Oct release reached TMX Money, Stockhouse, MarketScreener, 6ix and TipRanks within two minutes.
3. **Ticker in the header exactly as now: "(TSXV: OCAL) (FSE: JC3)".** Evidence: Yahoo Help requires the ticker symbol in the header to attach the release to the quote page; the 22 Oct release carries both.
4. **Release before market open, about 7:30 to 8:30 AM ET.** Evidence: the 22 Oct 7:56 AM release was visible on four aggregators by 7:58 AM; Google says freshness matters in news ranking.
5. **Headline that states a fact, not a claim.** Google's article best practices ask for a clear headline, 2 to 22 words, no date in the title, and the same title in the page title tag and the heading. CIRO may ask for a rewrite if a release is overly promotional.
6. **Same "About OCAL" paragraph in every release** (Pack S, or the 22 Oct paragraph). Evidence: S&P collects from press releases and websites (Simply Wall St's description of its S&P feed); inconsistent boilerplate already produced two versions of the OPENLANE wording.
7. **Post the release on ocalfinancial.ca only after the wire has carried it.** Evidence: CIRO page and the TSX guide, which says any electronic distribution of material information must come after wire dissemination.
8. **Make the company page a clean news article:** one visible date and time under the headline, datePublished in structured data, a self-referencing canonical, no noindex, and an About and contact page (Google's article page best practices and the Google News transparency policy).
9. **Optional: news sitemap and Search Console.** Google says a news sitemap (only articles from the last two days, publication name matching how it shows on Google News) can speed discovery; the URL Inspection tool shows how Google's crawler sees a page (Google Publisher Center help). Publisher Center registration is optional and does not change eligibility.
10. **Email the PDF to news@stockwatch.com once public** if you want Stockwatch to move a little faster (Stockwatch News Dissemination page; the wire pickup happens regardless).
11. **After 15 minutes, verify:** finance.yahoo.com/quote/OCAL.V/press-releases/ (the wire's name appears beside the item), money.tmx.com/en/quote/OCAL/news, the Stockhouse release page, the Stockwatch quote page, MarketScreener news. In Google, search the exact headline in quotes and use the site: operator to test indexing (method from Google's Publisher Center help).
12. **Do not re-release to "fix" a slow Google pickup.** Evidence: Google's guidelines warn against artificially freshening stories, and re-issuing a release is also a Policy 3.3 and CIRO matter.

### Sources (Part 2e)

- https://help.yahoo.com/kb/SLN24383.html
- https://ca.finance.yahoo.com/quote/SHOP/press-releases/
- https://finance.yahoo.com/topic/provider-globenewswire/
- https://www.businesswire.com/help/find-your-news-online
- https://www.businesswire.com/pricing
- https://www.globenewswire.com/pr-distribution-service
- https://www.globenewswire.com/Home/Send-Press-Release/Distribution-Options
- https://www.thecanadianpress.com/pr-publishing-tools/press-release-distribution/
- https://www.globenewswire.com/newswire-press-release-content
- https://entrepreneurs.frontfundr.com/learn/submitting-a-press-release-with-frontfundr
- https://newswirejet.com/globenewswire-pricing/
- https://www.accessnewswire.com/blog/press-release-distribution-cost
- https://signalgenesys.com/accesswire-review/
- https://www.tsnewswire.com/blog/best-press-release-distribution-which-wires-get-cite-by-ai
- https://www.accesswire.ca/
- https://www.newswire.ca/
- https://www.openpr.com/news/4396280/best-press-release-distribution-services-in-canada
- https://www.vendr.com/marketplace/business-wire
- https://mentionagent.ai/blog/business-wire-vs-pr-newswire/
- https://thenextgennexus.com/2026/05/30/pr-newswire-alternatives-compared-2026/
- https://www.newsfilecorp.com/newswire/investor-relations.php
- https://blog.newsfilecorp.com/post/7-ways-newsfile-enhances-your-distribution-service
- https://wireapp.newsfilecorp.com/newswire/
- https://interactionpartners.ch/north-american-distribution
- https://www.newsfilecorp.com/release/307230/OCAL-Financial-Outlines-How-Its-Virtual-FinanceFirst-Model-Differs-From-the-Traditional-Dealership
- https://www.stockwatch.com/Help/Newsdiss
- https://sales.stockwatch.com/EmailAds
- https://stockhouse.com/news/press-releases/2026/10/22/ocal-financial-introduces-ocal-showroom-a-live-virtual-view-of-its-dealership
- https://ca.marketscreener.com/news/ocal-financial-introduces-ocal-showroom-a-live-virtual-view-of-its-dealership-operations-ce785cded88af426
- https://6ix.com/news/ocal-financial-introduces-ocal-showroom-a-live-virtual-view-of-its-dealership-operations
- https://money.tmx.com/en/quote/OCAL/news
- https://www.finanznachrichten.de/nachrichten-2026-07/69106793-ocal-financial-ocal-financial-inc-provides-corporate-overview-following-tsx-venture-exchange-listing-296.htm
- https://www.stockwatch.com/Quote/Detail?V:OCAL
- https://www.tsx.com/en/resource/3509
- https://www.tsx.com/en/resource/3562
- https://www.tsx.com/en/resource/3122
- https://www.tsx.com/en/listings/tsx-and-tsxv-issuer-resources/tsx-venture-exchange-issuer-resources/tsx-venture-exchange-corporate-finance-manual/tsxv-corporate-finance-manual-policies
- https://www.osc.ca/en/industry/market-regulation/marketplaces/exchanges/exempt-exchanges/tsx-venture-exchange-orders-notices/notice-housekeeping-amendments-amendments
- https://www.ciro.ca/markets/trade-surveillance/trading-halts-timely-disclosure
- https://www.mccarthy.ca/en/insights/blogs/canadian-securities-regulatory-monitor/gaining-followers-use-of-social-media-by-canadian-public-companies-while-navigating-canadian-securities-laws
- https://support.google.com/news/publisher-center/answer/9606634?hl=en
- https://support.google.com/news/publisher-center/answer/6204050?hl=en
- https://support.google.com/news/publisher-center/answer/9607104?hl=en
- https://support.google.com/news/publisher-center/answer/9606542?hl=en
- https://developers.google.com/search/docs/crawling-indexing/sitemaps/news-sitemap
- https://newsinitiative.withgoogle.com/resources/trainings/get-started-on-google-news-with-publisher-center/
- https://www.google.com/intl/en_us/search/howsearchworks/how-news-works
- https://www.searchenginejournal.com/google-news-optimization-mistakes/448539/
- https://www.seoforgooglenews.com/p/syndicated-content-seo
- https://www.gsqi.com/marketing-blog/news-syndication-seo-case-study/
- https://signalgenesys.com/press-release-seo-guide/
- https://redpress.net/publish-yahoo-finance-press-release
