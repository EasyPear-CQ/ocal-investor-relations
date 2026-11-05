# Research A: Canadian fintech, auto and TSXV investor sites

Competitive review for the OCAL Financial (TSXV: OCAL) investor website rebuild.
Date visited: 23 Oct 2026 (all ten sites, all pages below). Prepared for CQ and Has.
Method: WebFetch, raw HTML pulls (page source, sitemap, JSON-LD, script hosts), the built-in browser pane for sites that block bots, and Exa for cached extracts. Benchmark checklist used: the TMX "Your Investor Relations Webpage" best-practice page, https://www.tsx.com/en/resource/2678/ (what a TSX and TSXV issuer should show: why invest up front, financials with a SEDAR link, governance documents, share data with a quote, FAQ, named IR contact without a contact form, news, events, latest deck on the landing page, mobile and SEO optimization, no analyst reports hosted, keep sales and IR separate).

## 0. Access log and URL corrections

| Site | URL as given | What happened | Real IR address and how it was read |
|---|---|---|---|
| goeasy | investors.goeasy.com | Does not resolve (ENOTFOUND). goeasy.com returns 403 to scripted fetches. | https://www.goeasy.com/investor-relations/ read through the built-in browser pane. Documents, news and SEDAR feed live on https://goeasy.investorroom.com/ (fetched normally). |
| Propel Holdings | propelholdings.com investors | investors.propelholdings.com does not resolve; /investors returns 404. | IR is inside the main site: https://www.propelholdings.com/why-invest/ and siblings. Fetched normally. Search results also show an older Q4 host, propel2023tf.q4web.com. |
| Chesswood Group | chesswoodgroup.com investors | WebFetch failed (certificate mismatch, Sucuri firewall cert), curl could not connect, browser pane navigation was denied. | Read from Exa cached extracts only: https://www.chesswoodgroup.com/investors/investor-information and https://www.chesswoodgroup.com/investors/reports--filings/financial-reports plus the home page. The company is in CCAA wind-down (see section 3), so the site is a shell. Fields I could not verify are marked "not verifiable". |
| Mogo | investors.mogo.ca | 301 redirect to https://www.orion-digital.com/investor-relations. Mogo Inc. is now Orion Digital Corp. | Fetched normally. |
| AutoCanada | autocan.ca investors | www.autocan.ca/investors returns 403 to scripts. | The real IR site is https://investors.autocan.ca/ (fetched normally). It embeds a Cision InvestorRoom iframe from https://autocan2.investorroom.com/investor-relations. |
| Kraken Robotics | krakenrobotics.com investors | Fine. | https://www.krakenrobotics.com/investors/ |
| VitalHub | vitalhub.com investors | Fine (browser pane refused one repeat navigation; text came from raw HTML and WebFetch). | https://vitalhub.com/investors/ |
| WELL Health | well.company investors | Fine. News lives on a subdomain. | https://well.company/investors/ and https://news-releases.well.company/news-releases/ |
| E Automotive (E INC) | n/a | Delisted from the TSX in 2023 (still a reporting issuer). Site is frozen at Aug 2023. Clutch and Canada Drives also covered, both private. | https://investors.e.inc ; https://www.canadadrives.ca/about-us ; https://www.clutch.ca/about |
| TSXV microcap | n/a | Chosen after search, see section 10. | https://www.quantumcriticalmetals.com/investors |

## Cross-site comparison grid

| Site | IR platform | Quote and chart | KPI tiles on IR | Cap table | FAQ (schema) | Alerts | Named IR contact | JSON-LD |
|---|---|---|---|---|---|---|---|---|
| goeasy | Gatsby shell plus Cision InvestorRoom | QuoteMedia | Yes (financials page) | Only shares out in quote | No | Yes (press releases) | Yes, name, email, phone, plus form | None |
| Propel | WordPress, Yoast, Q4 feed | QuoteMedia | Yes (6 tiles, footnoted) | No (dividend table instead) | No | Yes (double opt-in) | Email only | None found |
| Chesswood | not verifiable | QuoteMedia (2021 footer) | No | No | No | "Sign up for updates" | investorrelations@ email | not verifiable |
| Mogo / Orion | Webflow | QuoteMedia (live strip, TSX and NASDAQ) | Yes (best of group) | Market cap tile only | Yes, page (no schema) | Yes (footer form) | Email, phone | None |
| AutoCanada | WordPress plus Cision InvestorRoom iframe | InvestorRoom iframe | No | No | No | Yes, granular | Email, phone | WebSite, WebPage |
| Kraken | WordPress, Elementor | None (link to TMX Money) | No | No | No | None found | Email (obfuscated) | Breadcrumb, NewsArticle |
| VitalHub | WordPress, Yoast | None (link to TMX Money) | No | No | No | Yes | Form only | Full Yoast graph |
| WELL | WordPress, Elementor, HubSpot | Custom block, rendered empty | No | Block with shares and market cap (empty) | Yes, FAQPage | Yes (HubSpot) | Email | Graph, FAQPage |
| E INC | Duda-type builder | None | No | No | No | None | Outside advisor | None |
| Quantum (TSXV) | React single page app | TradingView widget | No (cap table instead) | Yes, full | Yes, FAQPage | Yes (monthly digest) | CEO name, phone, email | FAQPage, WebSite, Org |

---

## 1. goeasy (TSX: GSY)

- **URLs visited (23 Oct 2026):** https://www.goeasy.com/investor-relations/ ; /why-invest-in-us/ ; /financials-and-filings/ ; /stock-information/ ; /corporate-documents/ ; /contact-us/ ; /board-of-directors/ ; /events/ ; /newsroom/ ; https://goeasy.investorroom.com/ ; /news ; /presentations ; /quarterly-results?cat=49 ; /sedar ; /email-alerts.
- **Platform:** Two layers. Front site is a Gatsby build (webpack-runtime, framework and app bundles) with Contentful assets (assets.ctfassets.net) and an Irwin analytics script (analytics.imirwin.com, which points to the Irwin IR agency). News, results grid, presentations and SEDAR feed sit on goeasy.investorroom.com, an InvestorRoom product (CNW/Cision lineage inferred from CNW-named CSS on the AutoCanada embed of the same product; goeasy does not say).
- **IR menu in order:** top bar ABOUT (About Us, Leadership Team, Board of Directors) | INVESTOR RELATIONS (Investor Relations, Why Invest In Us, Financials & Filings, Events, Stock Information, Corporate Documents, Contact Us) | NEWSROOM | CAREERS | ESG (Overview, ESG Fact Sheet) | PRIVACY. A sticky ticker "TSX: GSY $43.71 -$0.31 (-0.7%)" sits in the header of every page and links to Stock Information.
- **Top of IR home:** headline "We Are Building Canada's Leading Non-Prime Consumer Lending Business", subline "Proudly Serving More than 9.6 Million Canadians", three tiles (Investor Presentation, linking straight to the Q2 2026 earnings PDF; Newsroom; Events), a quote strip stamped "As of October 23, 2026 12:23 PM ET", a Corporate Overview paragraph ($20.0 billion originated to 1.6 million Canadians) and one KPI ($5.00B gross consumer loans receivable). The footnote date on that tile reads 31 Mar 2026 while the financials page reports the same $5.00B at Q2, a small consistency slip.
- **Quote and chart vendor:** QuoteMedia (qmod.quotemedia.com v1.61.1: miniquotes, detailedquotetab, interactivechart, pricehistory, investmentcalculator). Stock page shows chart (1D to 10Y), detailed quote (bid, ask, beta, 52-week range, dividend, yield, ex-date, market cap, shares out), price-history table and an investment calculator with dividend reinvestment.
- **Financials and SEDAR+:** Financials & Filings page shows Q2 highlights as bullets, five KPI tiles ($272M originations, $5.00B portfolio, $390.0M revenue, $15.9M net income, $16.8M adjusted net income) with non-IFRS footnotes, then three cards (MD&A, financial statements, earnings release). The archive on InvestorRoom is a year selector (2011 to 2026) with a Q1 to Q4 grid whose rows are Consolidated Financial Statements, MD&A, Earnings Press Release, Earnings Presentation, Webcast. A separate "SEDAR Filings" page is a Cision-fed feed filtered by calendar year or trailing 12 months and by about 40 filing types, with description, date, format.
- **News releases:** InvestorRoom list (date, headline, Download), month and year pickers, keyword and advanced search, asset-type filters, RSS (news?pagetemplate=rss), per-release URLs of the form YYYY-MM-DD-Headline-Slug with a ?asPDF twin. The goeasy.com Newsroom page is a media-coverage placeholder that rendered almost empty.
- **KPIs and operating metrics:** Tiles on the financials page; deeper metrics (net charge-off rate, originations) only inside the earnings deck, MD&A and release bullets. No standalone KPI page.
- **Share structure:** Only "Total Shares" and "Shares Out" in the QuoteMedia detail (16.03m). No options, warrants or ownership table.
- **Governance and board:** Separate Board of Directors page (11 names with role and an "Independent Director" label each, Executive Chairman first). Corporate Documents page is a flat Download list (articles, by-laws, advance notice, majority voting, insider trading, code of conduct, board mandate, HR, Audit and Governance committee mandates); board position descriptions are pushed to the AIF.
- **FAQ:** None.
- **Alerts:** InvestorRoom form (first, last, email, company, phone) with consent text for new press releases.
- **Events and presentations:** Events page is a widget; presentations archive by year with an Earnings Presentation and Webcast row per quarter.
- **Analyst coverage:** Ten firms with analyst names, plus the standard disclaimer; no phones.
- **IR contact:** Named person (James Obright, SVP Investor Relations and Capital Markets), email and phone shown, plus a four-field form capped at 240 characters.
- **SEO and schema:** IR home title is only "Investor Relations" (no company, no ticker) but it has a real meta description ("Access goeasy investor relations, press releases, and shareholder information including quarterly results, analyst coverage and more."). Subpages had empty descriptions. No JSON-LD. InvestorRoom titles read "goeasy - News" with empty descriptions. Sitemap not readable (bot block).
- **Worth copying:** the sticky header ticker; a direct "latest earnings deck" tile on the IR home; quarter-by-year grid with five artifacts per quarter; SEDAR feed filtered by filing type; the investment calculator (nice but optional).
- **Avoid:** two domains with two designs; generic title tags; consumer app promo ("Download the FREE goeasy Connect app") in the IR footer (TMX says keep sales and IR apart); empty meta descriptions.

## 2. Propel Holdings (TSX: PRL)

- **URLs visited:** https://www.propelholdings.com/ ; /why-invest/ ; /financial-disclosures/ ; /stocks/ ; /news-and-events/ ; /corporate-governance/ ; /our-leadership/ ; release page https://www.propelholdings.com/news/propel-reports-second-quarter-results-and-announces-dividend-increase/ ; sitemap.xml.
- **Platform:** WordPress with Yoast SEO (sitemap index: post-sitemap.xml, page-sitemap.xml, lastmod 8 Oct 2026), custom theme, HubSpot and Cloudflare. News list loads from a Q4 feed (q4web references in the page script; older host propel2023tf.q4web.com seen in search). QuoteMedia quote module (qmod miniquotes). Webcasts hosted on webinar.net. Releases arrive via CNW.
- **IR menu in order:** Home | About Us (Our Platform, Our Mission and Commitment, Our Leadership, Our Markets, Our Operating Brands, For Partners, Propel Bank For Partners) | Investor Relations (Why Invest, Financial & Filings, Stock Information, Corporate Governance) | Careers | News & Events (News, Events, Insights & Coverage). Footer repeats and adds Contact.
- **Top of IR home (Why Invest):** line "Welcome to a new world of financial opportunity powered by AI", three jump cards (News, Financials, Leadership), a ticker line "Stock: PRL | Exchange: TSX | Sector: Finance | Industry: Credit Finance", then six KPI tiles: 43% revenue CAGR since 2019, 76% net income CAGR, 80% adjusted net income CAGR, US$3.2B total originations funded, 27% YTD annualized ROE, 35% annualized adjusted ROE, each with numbered footnotes and a non-IFRS note that points to the MD&A on SEDAR+. A second tile set covers the platform (more than 100,000 applications a day, about 6 seconds to decision, 5,000 data points, 90% auto-decisioned, trailing twelve months to 30 Jun 2026) and a third the market (US$24 trillion lending market, about 90 million underserved, with sourced footnotes). Then a "Latest Financials + Investor Information" row (newest quarter with FS and MD&A PDFs, plus "Investor Presentation (AUGUST 2026)" PDF), three latest news items, and a subscribe block.
- **Quote and chart vendor:** QuoteMedia (data-qmod-tool="miniquotes"). The Stock Information page is analyst table plus dividend history; the chart module loads by script.
- **Financials and SEDAR+:** Financial & Filings leads with FY2025 highlight tiles (US$590M revenue, US$67M adjusted net income), then year tabs 2026 to 2021; each quarter is one row: date, title "Propel Second Quarter 2026 Financial Report", a "Listen" audio link, Financial Statement PDF, MD+A PDF (hosted at cdn.propelholdings.com). SEDAR+ is mentioned in footnotes, not embedded.
- **News releases:** News & Events has three tabs (News, Events, Insights & Coverage). Insights hold the quarterly shareholder letters and CEO media appearances (BNN Bloomberg, podcasts), paginated 1 to 4. Releases are per-page on propelholdings.com/news/slug/ with the dateline and a Highlights block that states operating metrics as bullets (revenue up 26% to US$179.6M, adjusted EBITDA, ROE, loans and advances receivable, combined loan balances, dividend).
- **KPIs and operating metrics:** Yes, as tiles with CAGRs, in releases as record-quarter bullets, and in the shareholder letter. Strong example of a metric set repeated identically in tiles, release bullets and deck.
- **Share structure:** Not shown (no basic or diluted table); dividend history table instead (amount, frequency, declaration, record, payment date, type, back to 2021).
- **Governance and board:** One Corporate Governance page: seven directors with "Read bio" expanders and a Corporate Documents list of ten PDFs (articles, by-laws, majority voting, advance notice, code of ethics, board mandate, chair position description, nomination and compensation committee charter, audit committee charter, modern slavery report). The chair bio notes OPENLANE co-founder status. Defect: two directors carry the label "Chair of the Board".
- **FAQ:** None.
- **Alerts:** "To opt-in for investor email alerts... you will receive an activation email" (double opt-in), but the button goes to /contact/.
- **Events and presentations:** Upcoming and Past Events by year with "Register" links to app.webinar.net for each earnings call and conference fireside chat.
- **Analyst coverage:** Nine firms with analyst names and the endorsement disclaimer.
- **IR contact:** Contact page; releases show IR@propelholdings.com. No named IR person on the IR pages.
- **SEO and schema:** Titles are "Page - Propel Holdings" but built from the page slug ("stocks - Propel Holdings" in lowercase). og:description is auto-pulled page text, so it reads as junk. Release pages are good: "Headline | Propel Holdings" with a meta description from the release lead. No JSON-LD found. Canonical tags are set.
- **Worth copying:** repeating the same KPI set as dated, footnoted tiles; one-row-per-quarter table with Listen audio; "Insights" shelf for shareholder letters; dividend history table (only relevant if OCAL ever pays one); webinar registration links.
- **Avoid:** slug-based titles; typo link /finacial-disclosures/ in the nav; footer typo "Stock Infomration"; no FAQ; subscribe button routed to a generic contact page.

## 3. Chesswood Group (TSX: CHW, now delisted, in CCAA)

- **URLs visited:** home https://www.chesswoodgroup.com ; https://www.chesswoodgroup.com/investors/investor-information ; https://www.chesswoodgroup.com/investors/reports--filings/financial-reports (all through Exa cache, 23 Oct 2026; live fetch blocked, see section 0). Context from search: CCAA proceedings (court file CV-24-00730212-00CL), assets sold, TSX delisting determination, FTI Monitor's Ninth Report dated 18 Jan 2026 seeking a termination order.
- **Platform:** not verifiable. Site map text: About Us, Our Companies, Investors, News, Privacy Policy, Accessibility, Careers, ESG.
- **IR menu:** Investors > Investor Information; Reports & Filings > Financial Reports (other items not verifiable).
- **Top of IR home:** not verifiable. The home page extract is a short statement ("A Specialty Finance Company"), Contact Us, News, a "Sign up for updates" box, Toronto address, support and investorrelations@chesswoodgroup.com emails.
- **Quote vendor:** QuoteMedia (footer on the investor page reads "copyright 2021 QuoteMedia", data delayed 15 minutes), stale.
- **Financial reports:** A plain table with a "Show All Years" selector (2024 back to 2008) and columns Name, Filing Date, Size, Download. Rows cover interim reports, audited statements, annual reports and even 13-502F1 fee forms. Newest item: Q1 2024 interim (8 May 2024). A 16-year archive with file sizes is the useful part.
- **News, KPIs, share structure, governance, FAQ, events, analysts:** not verifiable. The Investor Information page carries a Registrar and Transfer Agent block (TSX Trust), a Lawyers block (McCarthy Tetrault) and an Auditors block (EY).
- **Alerts:** "Sign up for updates" subscribe button on home.
- **IR contact:** investorrelations@chesswoodgroup.com and a phone number on home.
- **SEO and schema:** not verifiable.
- **Worth copying:** the small "Transfer agent, lawyers, auditors" block; filing date and file size beside every download.
- **Avoid:** a site left running after the company stops reporting. The cached pages show no status notice, a 2021 quote footer and nothing after May 2024. If OCAL ever restructures, post a plain status page.

## 4. Mogo, now Orion Digital Corp. (TSX: ORIO, NASDAQ: ORIO)

- **URLs visited:** https://investors.mogo.ca (301) to https://www.orion-digital.com/investor-relations ; /press-release ; /financial-reports ; /events ; /corporate-governance ; /board-of-directors ; /faq ; sitemap.xml ; release pages under /press-release/slug.
- **Platform:** Webflow (generator meta tag), Webflow CMS lists, QuoteMedia live quote, reCAPTCHA forms, Cloudflare. The old investors.mogo.ca address 301s to the new site (good practice).
- **IR menu in order:** Overview | Press Releases | Financial Reports | Events | Governance (Corporate Governance, Board of Directors) | FAQ. Footer: address, phone, investors@oriondigitalcorp.com, inline "Email Alerts" form.
- **Top of IR home:** tagline "Wealth. Payments. Consumer lending.", headline "Building for an AI-Driven Financial System", then a live share price strip with both listings (TSX: ORIO C$0.72, NASDAQ: ORIO US$0.52, "15 min. delay"). Below: "Orion Digital Today" with KPI tiles: about C$37M current market capitalization (dated 9 Sep 2026), C$67M FY2025 revenue, C$8.9M LTM adjusted EBITDA, C$35M cash and investments, over 20% insider ownership, about 8% of shares retired since 2022. Three segment cards each carry one metric (about C$545M client assets, over C$11B processing volume, about C$75M gross loans). A "Q2 demonstrated earnings" block shows C$3.3M adjusted EBITDA (+115% q/q), C$5.1M core operating cash, and FY2026 adjusted EBITDA guidance of C$6.0M to C$7.0M with its issue date (6 Aug 2026). Then three latest releases and numbered non-IFRS and forward-looking footnotes.
- **Quote and chart vendor:** QuoteMedia in the hero strip. No full chart page.
- **Financials and SEDAR+:** One flat chronological list of downloads (Q2 2026 MD&A, statements, AGM proxy and circular, AIF, earlier quarters). A footnote says continuous disclosure is on SEDAR+ and EDGAR.
- **News releases:** Simple list (date, headline, READ MORE), per-release pages at /press-release/slug. Headlines carry the metrics ("Adjusted EBITDA of $3.3 Million, Up 115% Sequentially, and Wealth AUM Growth of 18%").
- **KPIs and operating metrics:** The strongest tile set of the ten: dated, footnoted, mixing market cap, cash, insider ownership and buyback progress.
- **Share structure:** Market cap tile and insider ownership only.
- **Governance and board:** Governance page lists charters (mandate, audit, compensation and nominating), policies (diversity, disclosure and confidentiality, majority voting, code, NASDAQ governance, whistleblower), articles, notice of articles and position descriptions (chair, lead director). Separate Board page with full bios.
- **FAQ:** A real FAQ page (about ten questions): what the company does, fiscal year end, share certificates and transfer agent with phone, how to invest, where filings are, when earnings are announced (45 and 90 day rules, date posted about two weeks ahead), tickers and listings. No FAQ schema.
- **Alerts:** Inline footer form with success and error states.
- **Events and presentations:** Events list with date, time (EST) and MORE INFO; earnings dates and conferences. No deck archive seen.
- **Analyst coverage:** None shown.
- **IR contact:** Address, phone, fax and email; no named person.
- **SEO and schema:** Titles on subpages are bare ("Financial Reports", "FAQ", "Events"); home is "Orion Digital Corp. - Investor Overview" with a good meta description; no canonical, no JSON-LD. Plain sitemap.xml.
- **Worth copying:** market cap and cash tiles with an as-of date; guidance with its issue date; ticker strip in the hero; metric-bearing headlines; the old-domain 301.
- **Avoid:** bare title tags. A developer note in the page source explains that the "as of" date under the live quote was removed on purpose because a fixed date beside a live price looked stale. Keep live data undated and static data dated, never mix them in one tile.

## 5. AutoCanada (TSX: ACQ)

- **URLs visited:** https://investors.autocan.ca/ ; /investor-information/stock-information/ ; /investor-information/investor-documents-filings/ (Exa extract) ; /investor-information/presentation-events/ ; /corporate-governance/board-of-directors/ ; /corporate-governance/committee-information/ ; /releases/ ; /contact/ ; release https://investors.autocan.ca/2026/08/autocanada-reports-second-quarter-2026-results-and-advances-strategic-initiatives/ ; https://autocan2.investorroom.com/investor-relations ; sitemap_index.xml.
- **Platform:** WordPress with Yoast SEO, The Events Calendar plugin (tribe REST API at /wp-json/tribe/events/v1/ and an iCal link /events/?ical=1), Cloudflare, and a Cision InvestorRoom iframe for the stock block. Webcasts on webinar.net.
- **IR menu in order:** Investor Information (Company Overview, Stock Information, Investor Documents & Filings, Notice and Access Meeting Materials/Presentations & Events) | Corporate Governance (Board of Directors, Committee Information, Conduct & Policies; ESG Oversight) | News Releases | Contact Us | Privacy Policy | Terms of Use. "Sign Up for Email Alerts" repeats in the footer of every page.
- **Top of IR home:** Company Overview text ("multi-location automotive dealership group... TSX: ACQ"), an Operations section (61 franchised dealerships in Canada across 23 brands and 8 provinces, nine Illinois dealerships, about 71,000 retail vehicles sold in 2025), a brand filter, and the five latest releases. No tiles, no quote on the home page.
- **Quote and chart vendor:** Inside the InvestorRoom iframe (vendor not stated). The embedded page also exposes a legacy dealer-site menu and a dealer-sales og:description, a leak to avoid.
- **Financials and SEDAR+:** Investor Documents & Filings has quarterly investor presentations by year tabs (2020 to 2026), annual reports (with a candid note that none were published 2007 to 2010), and financial statements plus MD&A in pairs back to 2007. SEDAR+ is a link with an explainer, not embedded.
- **News releases:** /releases/ with year filter (2012 to 2026), category filter, Load More. Per-release pages at /YYYY/MM/slug/ with "Back to all News Releases", dateline "August 12, 2026 | AutoCanada", Highlights bullets, a results table, the webcast URL and a pointer to MD&A on SEDAR+. Schema on releases: WebPage, ImageObject, Person.
- **KPIs and operating metrics:** Only in releases and decks (revenue, gross profit percentage, adjusted EBITDA and margin, leverage ratio 3.62x, liquidity about C$400.7M, outlook bullets).
- **Share structure:** None.
- **Governance and board:** Board page with Board and Executive Leadership tabs and bios. Committee Information has a membership matrix (Audit, Governance and Nominating, HR by director with Chair or Member) and a charter list with document codes (AC-BD, AC-AC and so on). The Contact page adds a third-party whistleblower line plus the Audit Chair email.
- **FAQ:** None.
- **Alerts:** Granular InvestorRoom signup: Presentations and Events, Daily Closing Stock Price, Stock Price End of Week Summary, All SEDAR Filings, News Releases, plus a checkbox per filing type (about 40).
- **Events and presentations:** Presentations & Events page lists upcoming webcasts (AGM, quarterly call with its own URL such as /2026-q2-conference-call/) and Latest Past Events; calendar with iCal export.
- **Analyst coverage:** Seven firms with analyst, phone and email.
- **IR contact:** Dedicated page: ir@autocan.ca, phone, mailing address, head office, transfer agent (Computershare) with phones. No form.
- **SEO and schema:** Title "Page - AutoCanada Investor Relations"; robots index, follow, max-snippet; canonical; JSON-LD graph (WebSite with SearchAction, WebPage, ReadAction); Yoast sitemap index (posts, pages, events). No meta descriptions on the pages read.
- **Worth copying:** committee matrix; per-event webcast pages; iCal feed; granular alert categories including "All SEDAR Filings"; a plain, complete archive; a whistleblower and transfer-agent block on the contact page; "Notice and Access" materials grouped with events.
- **Avoid:** a stock page whose quote is a third-party iframe that leaks a car-sales description; a very text-heavy home with no tiles or quote.

## 6. Kraken Robotics (TSXV: PNG, OTCQB: KRKNF)

- **URLs visited:** https://www.krakenrobotics.com/investors/ ; /investors/financial-reports/ ; /press-releases/ ; /policies-governance/ ; release /news-releases/kraken-robotics-reports-q2-2026-financial-results/ ; sitemap_index.xml.
- **Platform:** WordPress with Elementor, WP Rocket and Site Kit by Google; Cloudflare; a Notified-style press feed on the press page; releases carried by GlobeNewswire. IR is a thin section of the corporate site.
- **IR menu in order:** site header: About Us | Products | Services | Sectors | News (Press Releases, Publications) | Investors (Financial Reports, Corporate Governance) | Careers | Contact. On the IR page: View All Press Releases, Financial Reports, Analyst Coverage, TMX Share Information, Contact Investor Relations.
- **Top of IR home:** headline "Kraken Robotics is transforming subsea intelligence through advanced imaging sensors, software, and integrated systems", hero image linking to the latest release, "Investor Presentation (August 2026)" PDF button, the ten latest releases (date and headline), an Analyst Coverage list and a Contact block. No tiles.
- **Quote and chart vendor:** None embedded; a link to TMX Money (money.tmx.com/en/quote/PNG).
- **Financials and SEDAR+:** /investors/financial-reports/ lists year blocks 2026 back to 2021 with rows "Reporting Period | Description" (for example "June 30, 2026 | Management Discussion and Analysis Q2/2026", the matching Financial Statements, and the Q2 conference call presentation). The SEDAR+ link sits on the governance page.
- **News releases:** Year-grouped list with READ MORE; per-release pages with Previous and Next links; each page has a written title and meta description and NewsArticle JSON-LD.
- **KPIs and operating metrics:** In release bullets (Q2 revenue C$27.3M, adjusted EBITDA C$5.0M, new orders over C$27M, C$355M announced 2026 orders on a combined basis, guidance). Order announcements double as headline KPIs. No tiles.
- **Share structure:** None.
- **Governance and board:** /policies-governance/: committee charters (Nomination and Governance, Compensation, Audit), email communications policy, privacy policy, terms, SEDAR+ link. The board sits on the Corporate Team page.
- **FAQ:** None.
- **Alerts:** None found on the IR pages.
- **Events and presentations:** No events page; webcast dates are announced by release ("Schedules Q2 2026 Financial Results Release and Webcast").
- **Analyst coverage:** Seven firms with analyst names.
- **IR contact:** Email behind Cloudflare obfuscation, plus a #Contact anchor.
- **SEO and schema:** Best title pattern of the group: "Kraken Robotics Investors | TSX-V: PNG, OTCQB: KRKNF Stocks" and "Kraken Robotics Financial Reports | TSX-V: PNG, OTCQB: KRKNF"; meta descriptions name the ticker and the content types ("from 2021 to present"); robots max-snippet; BreadcrumbList on all pages, NewsArticle on releases; Yoast-style sitemap. Inconsistency: the meta text says "TSX: PNG" while the titles say "TSX-V".
- **Worth copying:** ticker and listings in every title tag and meta description; NewsArticle schema; order and contract headlines as KPIs.
- **Avoid:** no alerts, no embedded quote, no FAQ; an IR page that is only five links.

## 7. VitalHub (TSX: VHI, OTCQX: VHIBF)

- **URLs visited:** https://vitalhub.com/investors/ ; /investor-news/ (redirects to /investor-news-archive/) ; /corporate-governance/ ; /acquisitions/ ; release https://vitalhub.com/investor-news/vitalhub-reports-second-quarter-2026-results/ ; sitemap_index.xml.
- **Platform:** WordPress with Yoast (sitemap index includes custom post-type sitemaps such as corporate-governance), custom mega-menu theme, reCAPTCHA, cookie banner (Customize, Reject All, Accept All). Releases via GlobeNewswire and Newsfile. Country selector (Canada, United Kingdom, Australia).
- **IR menu in order:** Our Story | Solutions | Our Portfolio | Who We Serve | Resources | Investors | Contact. Investors submenu: Investors | Acquisitions | Corporate Governance | Investor News.
- **Top of IR home:** "This is VitalHub." summary (over 1,000 clients, over 700 employees, Toronto head office), growth strategy in two prongs (organic and M&A), a "Share Price" link out to TMX Money (no inline quote), seven latest items (3 Jul to 28 Sep 2026) with See all, and an "Investor Presentation" button that opens a gated form (first name, last name, email required).
- **Quote and chart vendor:** TMX Money link only.
- **Financials and SEDAR+:** Earnings section with year tabs (2026 to 2023); each quarter row links the press release, MD&A, earnings call transcript, call audio (YouTube) and financial statements (PDFs in wp-content/uploads). SEDAR+ appears as text.
- **News releases:** /investor-news/ list; per-release pages "Headline - VitalHub Canada" with the release lead as meta description (includes both tickers).
- **KPIs and operating metrics:** None as tiles; client and employee counts in the summary text.
- **Share structure:** None.
- **Governance and board:** The governance page lists documents only (audit charter, code, disclosure policy, by-laws, articles, insider trading, majority voting, whistleblower, board mandate, governance and compensation committee charter). Leadership is on a separate page.
- **FAQ:** None.
- **Alerts:** "Subscribe to Investor Alerts" repeated across the page, reCAPTCHA protected; separate "Keep Informed" general news signup.
- **Events and presentations:** In the Media shelf with about 25 YouTube videos (2018 to May 2026); an Events page exists on the main site.
- **Analyst coverage:** Ten firms listed.
- **IR contact:** One contact form with an "Investor Inquiry" option; no named person, phone or email on the page.
- **SEO and schema:** Title "Investors - VitalHub Canada"; meta description names the ticker and contents; full Yoast JSON-LD graph (WebPage, BreadcrumbList, WebSite plus SearchAction, Organization); canonical set.
- **Worth copying:** the Acquisitions page, a dated reverse-chronological card list (month and year, a paragraph on each target, links to the press release and the resulting solution), which is a proof-of-execution timeline; the quarter row with transcript and audio.
- **Avoid:** gating the deck behind a form; contact form only; mega-menu text drowning the page for crawlers; no quote on the site.

## 8. WELL Health Technologies (TSX: WELL, OTCQX: WHTCF)

- **URLs visited:** https://well.company/investors/ ; /stock-information/ ; /investors-faq/ ; /financials/ ; /news-releases/ (redirects to https://news-releases.well.company/news-releases/) ; /events/ ; /corporate-filings/ (titled Corporate Governance).
- **Platform:** WordPress with Elementor and HubSpot (forms and tracking); news on a WordPress subdomain with an RSS feed (/feed/); GTM; JSON-LD graph on every page.
- **IR menu in order (Investors submenu, 16 items):** Why Invest In WELL | Strategy | A Word From Hamed Shahbazi | Stock Info | Investor FAQ | Financials | News Releases | Events | Corporate Governance | Download Factsheet | Download Investor Deck | WELL Health USA | Sustainability & Impact | WELL Ventures | WELL Health AI | WELL Public Sector Solutions. Top bar: The WELL Team | What is WELL? | Investors | People & Culture | ticker link.
- **Top of IR home:** headline "Why Invest in WELL?", a one-sentence mission, a TSX quote block with Open, Last, Change, Volume, Day High, Day Low, a Download Investor Deck link (HubSpot form), a factsheet PDF (October 2026 edition) and a 2026 CEO letter PDF. The quote block rendered empty in both the raw fetch and the live browser pane on 23 Oct 2026.
- **Quote and chart vendor:** Not identifiable; fields blank at load (a broken widget).
- **Financials and SEDAR+:** Year tabs 2026 to 2021; per quarter: Financial Statements, Management Discussion and Analysis, Earnings Presentation. Text sends readers to SEDAR for the full set (AIF, circulars, AGM voting results). Page weight is about 1.25 MB.
- **News releases:** On the subdomain: year selector 2016 to 2026, a disclaimer that releases may be superseded by later disclosure, plain list. They issue event-participation releases (for example "WELL Health to Present at The Cantech Investment Conference on October 8 in Toronto", 2 Oct 2026).
- **KPIs and operating metrics:** None as tiles; the quarterly factsheet PDF carries them.
- **Share structure:** A "Share Structure" block exists in the layout (basic shares outstanding, market cap basic, last, change) but showed blank.
- **Governance and board:** The governance page lists 11 documents (articles, chairman's position description, audit, compensation and governance and risk charters, code, disclosure, governance guidelines, mandate, human rights policy, insider trading, majority voting). Board and committees live on The WELL Team page with anchors.
- **FAQ:** 12 questions with FAQPage JSON-LD: contact IR, exchanges and symbols (TSX WELL, OTCQX WHTCF, Frankfurt, Munich, Stuttgart), CEO, age and go-public date (RTO, 2017), HQ, fiscal year end, CUSIP, dividends, trading and reporting currency, auditors and counsel, transfer agent, where to find public filings.
- **Alerts:** HubSpot form "Sign up for WELL updates and receive our latest news" (separate WELLSTAR form too).
- **Events and presentations:** Events page with Upcoming (none) and Past cards, each with date, title, description, webcast and dial-in plus replay numbers.
- **Analyst coverage:** At least seven firms with name, email, location and phone, re-sorted by company with a script.
- **IR contact:** investor@well.company in the FAQ and a Contact Us page.
- **SEO and schema:** Keyword-led titles: "Investors | WELL Stock Information | TSX", "WELL Health Technologies | WELL Stock FAQ | TSX", "Financial Information | Investors | WELL Health Technologies"; meta descriptions on IR pages; the Events title is blank ("Events |"); FAQPage schema on the FAQ; BreadcrumbList and Organization graph throughout.
- **Worth copying:** FAQ with FAQPage schema and the exact question list; a monthly factsheet PDF; the "A Word From the CEO" letter; keyword-led titles with "Stock".
- **Avoid:** a 16-item submenu mixing IR with business units and careers; a blank quote block; 1 MB pages; a gated deck; a blank title tag on Events.

## 9. What an online auto company says about itself

### 9a. E Automotive (E INC), https://investors.e.inc

- **Status:** voluntarily delisted from the TSX in 2023, remains a reporting issuer. Site last updated Aug 2023.
- **Pages visited:** home, /financial-reports, /presentations, /board-of-directors, news list.
- **Platform and nav:** Duda-style builder (irp.cdn-website.com; footer "Powered by .inc Web Solutions"); releases from CNW; RSS and Atom feeds. Menu: Overview | Press Releases | Presentations | Financials | Governance | Resources | Contact Us.
- **What it says about itself:** mission "to enable the automotive ecosystem to do business however they choose and with increased velocity", describes an online wholesale auction marketplace plus dealer software (digital retailing, inventory management). Board page with bios (CEO ex ADESA, KAR, TradeRev), a Financials grid for 2023, 2022, 2021 by quarter (MD&A, statements, AIF, management information), Presentations with a Featured (2 Feb 2023) and Past list.
- **IR contact:** an outside advisor (LodeRock Advisors), no in-house name.
- **Avoid:** the page still shows leftover text from another client of the site builder ("Contact Phytome Today" button and a Phytome press release link in the footer area), titles are bare ("Overview", "Financials"), nothing newer than Aug 2023. A reminder to scrub every template string before launch.

### 9b. Canada Drives (private, Vancouver), https://www.canadadrives.ca

- **Pages visited:** /about-us ; /newsroom ; /media-kit ; /press (serves the home page, a soft 404).
- **Platform:** Nuxt application on Cloudflare.
- **Message:** "Our Mission Is To Be the Easiest Place To Buy and Sell Your Car in Canada." Since 2010, over one million Canadians approved or sold a car. Three blocks (Trusted Service, National Network, Simple Process). Explicit order of operations: get pre-approved for financing first, then a local partner dealership helps you into a car, which is the same approval-first shape as OCAL.
- **Newsroom:** tabs Articles, Awards, Media Inquiries, Media Kit; each item is outlet name, date, headline, one-line summary, "Read this Story" (third-party coverage; the newest shown is 6 Oct 2022, stale). Media Kit page: company summary, mission, Quick Facts (Founded 2010, HQ Vancouver, Industries, Sectors), brand guidelines link, logo download.
- **Trust signals:** the footer lists dealer registrations by province with licence numbers (MVSABC, OMVIC, AMVIC).
- **SEO and schema:** titles such as "Newsroom - Latest News and Updates | Canada Drives" with descriptions; Organization and ContactPoint JSON-LD on the home page.
- **Worth copying:** the Quick Facts box and brand-asset download for press; licence numbers in the footer; the plain approval-first explanation.
- **Avoid:** a stale newsroom, and a /press URL that silently serves the home page.

### 9c. Clutch (private, Toronto), https://www.clutch.ca/about

- **Pages visited:** /about ; /press (404, "There's nothing here"); blog link only. There is no press or investor page.
- **Platform:** React single page app, one JSON-LD block, meta description "Bringing Canadians high-quality vehicles, with the convenience of buying online and peace of mind knowing your car is certified with a 7day return policy."
- **Message and KPI strip:** "Reinventing how Canadians buy and sell cars" with four proof tiles: 95,000+ cars bought and sold, $1.7B paid out to Canadians for their vehicles, 650+ employees, 4.8 stars across 10,000+ verified reviews. Founder story, three operating principles, four "factory of the future" points, leadership and board (including venture investors).
- **Worth copying:** the four-tile proof strip (volume, dollars, scale, rating) near the top; the founder story in three short paragraphs.
- **Avoid:** no press page means journalists and analysts have nowhere to land.

## 10. TSXV microcap pick: Quantum Critical Metals Corp. (TSXV: LEAP)

- **Why this one:** After searching for TSX Venture issuers with a full IR page, I compared Quantum Critical Metals (market cap C$7.14M on its own page, so well under C$50M), Atlas Salt, Zentek, FeralX, Doubleview, Colibri, PTX Metals and Jericho. Quantum ticks the most TMX best-practice items on one page for the least money: Why Invest up front, quote and chart, full capital structure, financials, presentation, named IR contact, FAQ with schema, recent news, alert signup. Atlas Salt is the nicer build but its market value is well above C$50M (a Simply Wall St snapshot in June 2026 showed about C$206M) and it hosts third-party research PDFs, which TMX guidance says not to do.
- **URLs visited:** https://www.quantumcriticalmetals.com/investors (live in the browser pane and raw HTML) ; sitemap.xml ; robots.txt. Other IR pages seen via Exa extracts: https://www.atlassalt.com/investors ; https://triera.ca/investors/ (Zentek) ; https://www.feralx.ca/investors/.
- **Platform:** React single page app (Vite assets), TradingView free symbol-overview widget, no IR vendor.
- **Menu in order:** Home | About | Projects | Refining | Investors | News | Contact | Download Presentation (button). Footer groups: Company; Investors (Stock Information, Financials, Corporate Presentation); News; Resources; Privacy, Terms, Qualified Person Statement, Disclaimer.
- **Top of IR page:** "Investor Center: Stock information, corporate documents, financials, and direct contact with the Company", then "Why Invest: Five compelling reasons" (supply gap, refining pathway, 100% ownership, government tailwinds, multi-metal portfolio), each one short paragraph with one hard fact.
- **Quote and chart:** TradingView widget for TSXV:LEAP (area chart, 12M), listing block (TSXV LEAP, OTCQB ATOXF, Frankfurt 86A1).
- **Financials and SEDAR+:** Year tabs (2026, 2025); rows show file name, file size (2 MB, 185 KB) and a PDF tag; a sentence points to the SEDAR+ profile.
- **Capital structure:** table with shares outstanding, options (10.8M at an average exercise price), warrants (20.8M at an average exercise price with expiry), fully diluted (151.5M), and a market cap tile (C$7.14M with the live quote line). Dated "as of April 2, 2026" (stale next to Q2 filings, see below).
- **News:** three latest releases with Read Release, View All News; releases at their own pages.
- **Alerts:** "Investor Updates" signup (monthly digest, "no spam, ever", unsubscribe) and a Telegram channel link.
- **FAQ:** five questions with FAQPage JSON-LD.
- **IR contact:** named CEO, phone and email; no form (matches the TMX preference).
- **SEO and schema:** rendered title "Investor Center | LEAP Stock | Quantum Critical Metals Corp."; meta description lists all three tickers and the content ("stock quotes, financial statements, corporate presentation, and investor FAQ"); JSON-LD FAQPage, WebSite, Organization, PostalAddress, ContactPoint; sitemap.xml with changefreq and priority; robots allows all.
- **Worth copying:** the single-scroll investor page for a company with little to show; the fully diluted table with strike and expiry; "Why Invest" as five short fact-led blocks; FAQ schema; file size on downloads.
- **Avoid:** the cap table date is six months old while a Q2 filing is posted (always show the as-of date and refresh it with each filing); a presentation dated February 2026; static HTML returns a generic title and empty body before JavaScript runs, a crawler risk (use server rendering or a static build); a Telegram channel raises selective-disclosure and moderation questions for an issuer.
- **Other TSXV ideas seen (extracts only, not verified live):** Zentek has a plain-English Q&A on its Nasdaq delisting ("what it changes and what it does not", with a last-updated date), a model for explaining a market-structure event; FeralX (new TSXV listing) shows share structure with escrowed shares and release schedule, an upcoming-events list, and a stated owner metric for shareholders ("contracted revenue converted into free cash flow per share").

---

## (a) Top 12 ideas OCAL should steal, ranked

1. **A one-screen "Why Invest" landing with six dated, footnoted KPI tiles, the latest results card, the current deck and the three latest releases.** Source: Propel (tile set and footnotes), Orion Digital (market cap, cash, insider ownership, guidance with its date), Clutch (four-tile proof strip). Every tile carries an "as of" date and a source line. Matches the Signal call ask for an investor page rebuild.
2. **Operating metrics as a standing block in every release, repeated as tiles, with two KPIs in the headline.** Source: Propel (record-quarter bullets), Orion (metric-bearing headlines), Kraken (orders as headline KPIs), AutoCanada (Highlights plus table). One definition sheet, same numbers in release, tile and deck. Fits the standing operating-update section agreed on the Signal call.
3. **A capital structure table with an as-of date:** basic shares, options with average strike, warrants with strike and expiry, RSUs, fully diluted, escrow, insider ownership, market cap. Source: Quantum, Atlas Salt, FeralX, with WELL's "Share Structure" layout as the page pattern. Highest value for a C$5M market-cap issuer where dilution is the first question.
4. **One row per quarter with every artifact (release, financial statements, MD&A, deck, transcript, audio), with year tabs and a SEDAR+ profile link.** Source: VitalHub (transcript and audio), goeasy (Q1 to Q4 grid), Propel ("Listen"), Quantum (file sizes).
5. **An investor FAQ with FAQPage schema, written from questions investors actually ask** (what OCAL is, how a sale works, who funds, how it makes money, listing, transfer agent, fiscal year end, auditors, filings, dividends, share count, how to buy). Source: WELL (question list and schema), Quantum, Orion (earnings timing answer), Zentek (event explainer).
6. **Keyword title tags and meta descriptions that carry the ticker:** "Page | OCAL Financial (TSXV: OCAL)". Source: Kraken, WELL, Quantum. Avoid the bare titles seen on Orion, goeasy and E INC.
7. **A free embedded quote and chart.** Source: TradingView free widget (Quantum, Atlas Salt) for zero cost, or QuoteMedia (goeasy, Propel, Orion, Chesswood) if a detailed quote, price history and calculator are wanted. A header ticker that links to the stock page is a nice add (goeasy).
8. **Granular email alerts with double opt-in:** news, filings, events, optional price summary. Source: AutoCanada (category checkboxes including "All SEDAR Filings"), Propel (activation email), Orion (inline footer form).
9. **A SEDAR+ filings page:** a link to the OCAL SEDAR+ issuer profile on every financials page plus a short manual table of filings by type and date. goeasy shows the automated version with filters by year and type; for OCAL a maintained table is enough.
10. **Governance on one page with a committee membership matrix, a document list with codes, a whistleblower line and bios in expanders.** Source: AutoCanada (matrix, codes, whistleblower), Propel (expanders), goeasy (independence label per director). Note: bios must be reviewed under the OCAL rules before posting.
11. **Events with webcast registration and a calendar feed (iCal), plus a Notice and Access shelf for the AGM (10 Dec 2026).** Source: AutoCanada (events plugin, iCal, per-event webcast pages), Propel (webinar registration links).
12. **A named IR contact with direct email and phone, no form, plus a transfer agent, auditor, counsel and fiscal year end block.** Source: goeasy (named contact), AutoCanada (full contact page), Chesswood (the block), Atlas Salt and Orion (FAQ answers). TMX prefers direct contact details over forms.

Also worth borrowing in smaller doses: a shareholder letter shelf called "Insights" (Propel); an acquisitions or "deals and milestones" timeline (VitalHub), adapted as a funded-deals timeline; a media kit with Quick Facts and logo download (Canada Drives); licence numbers in the footer (Canada Drives); file size beside every download (Chesswood, Quantum); a 301 from any old address (Mogo to Orion); a CEO letter PDF (WELL).

## (b) Five things these sites do that OCAL's size means it should NOT copy

1. **Analyst tables and research libraries.** goeasy (ten firms), Propel, Kraken, WELL and AutoCanada list coverage with names and sometimes phones; Atlas Salt hosts third-party research PDFs. OCAL has no sell-side coverage to list, and TMX guidance is to host no analyst reports. Leave the section out until there is real coverage, and then list names and firms only.
2. **Enterprise IR platforms, two-domain stacks and iframes.** goeasy and AutoCanada run Cision InvestorRoom behind a second domain with a different look; Propel carries a Q4 feed. These cost real money per year, split SEO across domains and (in AutoCanada's case) leak an unrelated page description. Build OCAL on one domain (WordPress or a static build) with a free quote widget and hand-maintained tables.
3. **Mega-menus and mixed navigation.** WELL's 16-item submenu mixes IR with business units and careers; VitalHub's mega-menu swamps each page with menu text; goeasy puts a consumer app promo in the IR footer. OCAL should keep a seven-item IR menu and keep lead-gen and consumer calls to action out of the investor pages.
4. **Large-cap financial engineering content:** 15-year archives, dividend history tables, CAGR and annualized ROE tiles, adjusted non-IFRS tiles, NCIB and guidance blocks, investment calculators. OCAL has one audited year on the books (FY2025 revenue C$6.48M), no dividend and no formal guidance, so these tiles would be thin or invite forward-looking-statement exposure. Show a few plain, dated, historical operating metrics instead.
5. **Friction and noise:** gated decks (VitalHub, WELL), contact-form-only IR (VitalHub), cookie walls, social channels used as disclosure (Quantum's Telegram), audio and webcast stacks, and "as of" dates left to go stale (Quantum cap table, goeasy tile footnote, Orion market cap tile). OCAL should publish the deck as a plain PDF, use a named email, and put an owner and refresh date on every number.

## (c) Recommended IR navigation for a microcap (derived from the pattern)

Seven items plus two utility buttons, in this order. The home of the section is the Why Invest page.

1. **Why Invest** (`/investors/`): headline, one-paragraph story, six dated KPI tiles, quote strip, current deck button, latest results card, three latest releases, alert signup, IR contact line.
2. **Stock and Share Structure** (`/investors/stock/`): quote and chart (TradingView or QuoteMedia), listing, fully diluted capital structure table with as-of date, insider ownership, transfer agent.
3. **News** (`/investors/news/`): release list with year filter, per-release pages at `/investors/news/YYYY/slug/`, each with a Highlights bullet block and the standing operating-update section, RSS feed.
4. **Financials and Filings** (`/investors/financials/`): year tabs; one row per period with release, statements, MD&A, deck; SEDAR+ profile link and a short filings-by-type table.
5. **Presentations and Events** (`/investors/presentations/`): current deck on top (plain PDF), archive, upcoming earnings and conference dates with calendar download, AGM and notice-and-access materials.
6. **Governance** (`/investors/governance/`): board and management bios, committee matrix, policy and charter documents, whistleblower contact.
7. **Investor FAQ** (`/investors/faq/`): 12 to 15 questions with FAQPage schema.

Utility (right side of the bar, on every page): **Email Alerts** button (double opt-in, categories) and **Contact** (named IR contact, direct email and phone, no form; transfer agent, auditor, counsel and fiscal year end below).

Page furniture on every investor page: header ticker linking to Stock and Share Structure; footer with SEDAR+ link, forward-looking statement and non-IFRS notice, address; breadcrumb.

SEO pattern drawn from the best sites: title `{Page} | OCAL Financial (TSXV: OCAL)`; one meta description per page naming the ticker and what is on the page (about 150 characters); canonical tags; a Yoast-type XML sitemap with a news sitemap; JSON-LD Organization and WebSite on the home, BreadcrumbList on every page, FAQPage on the FAQ, NewsArticle on every release; keep release URLs permanent and dated; 301 any old address.

OCAL-specific guardrails for the build (internal, from the house rules):
- Every number on the site must trace to a filed document or a released statement; tiles carry an as-of date. Example tiles for the first build, all to be confirmed before launch (the per-vehicle figures from Terence are still pending): FY2025 revenue C$6.48M (audited); funded deals to date; average price; gross profit per vehicle; gross margin, each historical only.
- Use the agreed pitch wording ("zero standing inventory", "digital inventory of more than 3,000 vehicles via OPENLANE"), never "zero inventory" alone, and mirror the language of filed releases given the current CIRO pre-file process.
- Keep the Executive Chairman and CEO titles exactly as filed on the Governance page, and run every bio past Matthew before it is posted.
- Keep sales calls to action off the investor pages (TMX guidance).
