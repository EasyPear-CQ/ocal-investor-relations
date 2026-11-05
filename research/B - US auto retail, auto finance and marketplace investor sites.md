# B. US auto retail, auto finance and marketplace investor sites: competitive review for the OCAL investor site rebuild

Prepared for: OCAL Financial investor site rebuild (CQ and Has)
Date visited: 23 Oct 2026 (all ten sites, same day)
Scope: 10 peer IR sites, IR home plus at least 3 subpages each where the site allowed it

## 0. How this was done and what it can and cannot tell you

- Tools: direct page fetch, a second crawler (Exa) for pages the first one could not load, raw HTML pulls (curl) for page-source clues, and the companies' own earnings release PDFs and SEC exhibits for metric definitions.
- Blocked or broken, and what I did instead:
  - ir.upstart.com, investors.openlending.com, investors.cargurus.com: HTTP 403 to the first fetcher and to curl. Read through the second crawler instead (text only, so no page source, no JSON-LD check, no script inspection for those three).
  - ir.creditacceptance.com: TLS handshake error, and curl could not connect. Read through the alias www.ir.creditacceptance.com and creditacceptancecorporation.gcs-web.com via the second crawler. Menu order for this site comes from a search snippet, not a rendered page.
  - investors.openlane.com: the host does not exist (DNS "non-existent domain"). OPENLANE's investor site is **ir.corporate.openlane.com**. Everything below for OPENLANE is from that host. The URL in the brief should be corrected.
  - Q4 Inc. sites (CarMax, America's Car-Mart, OPENLANE) and Carvana load their stock quote, news list, SEC filings list, analyst list and some FAQ content with JavaScript. Those modules came back empty in text. Where a module is blank below it is marked "not captured", which means I could not see it, not that it does not exist.
- Page text was summarized by tools, so wording is quoted (in quotation marks) only where it came from a company PDF, release text or a fetched page. Numbers are as published on or before 23 Oct 2026.
- CarGurus: only the home, the Q2 2026 release and the Quarterly Results page were readable (2 subpages, not 3). Analyst coverage and FAQ URLs I guessed returned not found. Search snippets fill the gap and are labeled.
- Dashes: this file contains no em dashes or en dashes.

## 1. One-screen summary of the ten platforms

| # | Company | IR URL (as tested) | IR platform | Stock quote vendor visible | Per-unit economics on site |
|---|---|---|---|---|---|
| 1 | Carvana | https://investors.carvana.com | Custom Sitecore build ("Powered by Sitecore" badge, /~/media/ paths), Cloudflare in front | Not named (Stock Info is a separate "Share Price Chart" page) | Yes: every quarterly shareholder letter and release (Retail, Wholesale, Other, Total GPU; SG&A per unit) |
| 2 | CarMax | https://investors.carmax.com | Q4 Inc. (footer "Powered By Q4 Inc. 5.190.1.9", s27.q4cdn.com, ASP.NET .aspx URLs) | Q4 stockQuote widget (widgets.q4app.com); Xignite referenced in page source | Yes: release table "Gross Profit per Unit" |
| 3 | Credit Acceptance | https://ir.creditacceptance.com (alias www.ir.creditacceptance.com) | Notified-type Drupal platform (inferred from the creditacceptancecorporation.gcs-web.com alias, /static-files/ and /node/ URLs) | "Minimum 15 minutes delayed. Source: LSEG" | No per-unit retail metric. Unit volume of loan assignments and forecasted collection rates by vintage |
| 4 | America's Car-Mart | https://ir.car-mart.com | Q4 Inc. (footer, s205.q4cdn.com, .aspx) | Q4 stockQuote widget; Xignite in source | Yes: "Total gross profit per retail unit sold" plus customer metrics |
| 5 | Upstart | https://ir.upstart.com | Notified-type platform (inferred from /news-releases/news-release-details/ and /static-files/ patterns) | Not captured | Dollar and count metrics, not per car. Monthly originations release |
| 6 | Open Lending | https://investors.openlending.com | Notified-type platform (theme folder "nir_pid3666", /static-files/, SEC table "Data provided by Kaleidoscope") | Not captured | Per certified loan: profit share revenue, program fee revenue |
| 7 | ACV Auctions | https://investors.acvauto.com | Hosted IR platform, vendor not named (CloudFront assets, "::" title pattern, schema.org JSON-LD) | QuoteMedia (named on page, 15 minute delay) | Marketplace Units and GMV, no per-unit profit |
| 8 | OPENLANE Inc. | https://ir.corporate.openlane.com (investors.openlane.com does not resolve) | Q4 Inc. (footer "Powered By Q4 Inc. 5.184.0.5", s202.q4cdn.com) | Q4 widget, Xignite in source; also an IndigoTools "Interactive Financials" link | Vehicles sold growth rates and GMV, no per-unit profit |
| 9 | CarGurus | https://investors.cargurus.com | Notified-type platform (same URL patterns) | Not captured | Paying dealers, QARSD (revenue per subscribing dealer) |
| 10 | Cars.com (Cars Commerce) | https://investor.cars.com | Vendor not named. Page source carries "webDriver" file-icon paths, OneTrust, webinar.net webcasts | Not captured | Dealer Customers, ARPD (monthly average revenue per dealer) |

Takeaways on platform: 3 of 10 are on Q4 (the leading small-cap IR CMS), 4 look like the Notified Digital IR (Drupal) platform, Carvana is custom, ACV and Cars.com are hosted by vendors that do not advertise. The cheapest professional route for OCAL is a Q4, Notified or similar template, or a clean custom build modelled on Carvana's flat structure and Cars.com's clean URLs.

## 2. Per-site profiles

### 2.1 Carvana (CVNA)

- URL: https://investors.carvana.com. Pages read: home; /financial-reports/quarterly-results/2026; /investor-resources/shareholder-letters; /investor-resources/investor-materials; /events-and-presentations; /investor-resources/analyst-coverage; /corporate-governance/governance-documents; /corporate-governance/management-and-directors; /stock-info; /contact-us/email-alerts; /financial-reports/sec-filings; https://press.carvana.com/press-releases/; Q2 2026 earnings release PDF and shareholder letter PDF.
- Platform: custom Sitecore. Cloudflare email obfuscation on the investor email.
- Navigation order: IR Home; Investor Resources (Shareholder Letters, Investor Materials, Letters from Ernie, Annual Reports and Proxies, Analyst Coverage); Events & Presentations; Financial Reports (SEC Filings, Quarterly Results); Newsroom (external, press.carvana.com); Corporate Governance (Governance Documents, Management and Directors, Committee Composition); Contact Us (Contact Us, Email Alerts).
- Home hero: almost bare. Heading "Investor Relations", a "Stock Price" link to the Stock Info page (no price shown on the home), one latest-news item that links out to the press site (a sports sponsorship dated Oct 21, 2026), the next earnings call (Oct 28, 5:30 PM ET), and an "Investor Kit": Overview Video, "Intro Deck, Q2 2026" PDF, Analyst Day video and 2018 slides. No KPI tiles.
- Financial reports: the Quarterly Results page is a table by year (2017 to 2026 tabs) with four columns per quarter: Earnings Press Release, Letter to Shareholders, Supplemental Financial Tables, Webcast. The shareholder letter is the main document (the press release is one page and points to it). A separate Shareholder Letters page lists every letter from Q1 2017 with its date. SEC Filings page: module blank in text (not captured).
- News: none on the IR site itself. The Newsroom (press.carvana.com) lists releases newest first with a year filter (All, 2013 to 2026) and a search box. Release titles are plain ("Carvana Announces Record Second Quarter 2026 Results").
- Operating metrics: yes, the heart of the site. See section 3. Letter structure: summary bullets (units, revenue, gross profit, GPU, non-GAAP GPU, net income margin, adjusted EBITDA margin), outlook, a short themed essay, "Appendix I: GPU and SG&A expense detail", then full financial tables including "Results of Operations" with per-unit rows and a non-GAAP reconciliation. Quarterly line: "10th consecutive quarter of industry-leading growth and profitability".
- Why invest page: none. The thesis is carried by the "Introduction to Carvana" deck (July 2026 edition, refreshed on a schedule), "Benefits of Carvana's Differentiated Business Model" (Sep 2025), "Cost Structure Details" (Nov 2023), "Carvana 101" explainers (finance platform, securitization, pre-securitization financing), market launches and capacity, and the "Letters from Ernie" page.
- Share structure: not on its own page. The shareholder letter states weighted basic and diluted shares of Class A stock (718 million and 740 million) and then "assuming full conversion of LLC units and other dilutive effects... 1.127 billion shares of Class A common stock outstanding", a fully-exchanged share count. A 5 for 1 forward split (13 Mar 2026) appears only as a press release.
- Governance: three pages. Governance Documents (code of conduct for the board, code of ethics for senior financial officers, code of ethics and business conduct, audit committee charter, compensation and nominating committee charter, corporate governance guidelines, stock ownership guidelines), Management and Directors (long biographies), Committee Composition.
- FAQ: none.
- Email alerts: "Sign up now" on the home and a dedicated page for events and webcasts, financial reports, SEC filings and more. The form itself did not load in text.
- Events archive: one page with three blocks: the intro decks, upcoming events (with Add to Calendar), and past events from Nov 2025 back, each row linking Webcast, Letter, Supplemental Tables, Earnings Release, or the conference presentation.
- Analyst coverage: a table of 26 firms with analyst name (Baird, Bank of America, Barclays, BTIG, Citi, and so on to William Blair), no ratings or targets.
- IR contact: one obfuscated email (Investors@carvana.com), no phone, no named person.
- SEO: title pattern "Page | Carvana" (home "Investor Relations | Carvana", sub "Quarterly Results 2026 | Carvana"). Meta description on the home is just "Investor Relations". og:title, og:image, og:url and a canonical tag present. No JSON-LD.
- Distinctive and worth copying: the four-column quarterly grid; the standing deck refreshed with a date; the explainer decks ("Carvana 101", "Cost Structure Details") that teach analysts how to model the business; "Letters from Ernie".
- Avoid: a bare home with no KPIs and a 2018 Analyst Day video still in the kit; the only "latest news" item on the home is a sports sponsorship; an empty-looking SEC page.

### 2.2 CarMax (KMX)

- URL: https://investors.carmax.com (IR home at /ir-home/default.aspx). Pages read: home; /financials/financial-information; /resources/investor-faqs; /stock-information/stock-details; /news-and-events/news; /governance/board-of-directors; /stock-information/analyst-coverage; Q2 FY2027 release PDF (s27.q4cdn.com).
- Platform: Q4 Inc. (footer credit, q4cdn, .aspx).
- Navigation order: IR Home; News & Events (News, Events & Presentations); Stock Information (Stock Details, Analyst Coverage); Financials (Financial Information, SEC Filings); Governance (Board of Directors, Executive Management, Governance Documents); Resources (Investor FAQs, Email Alerts, Contact Information).
- Home hero: full-width "Corporate Overview" banner with an "Investor Relations" heading and a paragraph (nation's largest used-auto retailer, retail plus wholesale plus auto finance, 255+ stores, 22 consecutive years on a best-companies list). Four "Why Invest" KPI tiles: 255+ store locations; $26B FY26 revenue; 1.3M combined units sold in FY26; $16B auto loan portfolio. Quick links: Annual Reports, Quarterly Reports, Information Request, RSS Feed. News list and Featured Reports did not render. Footer: "Powered By Q4 Inc.".
- Stock chart: Q4 widget (not captured in text). "End of Day Stock Quote" is an email alert option.
- Financial reports and SEC filings: the Financial Information page carries an Asset-Backed Securities block (CarMax Auto Owner Trust pool performance and prospectuses). Quarterly and annual reports sit on the same page (Q4 grid, not captured). The earnings release is a Business Wire release mirrored as a PDF on q4cdn.
- News: year selector ("Selecting a year value will change the news content"), RSS feed page.
- Operating metrics: yes, in every release. See section 3. The release also reports comparable store used unit sales (stores enter the comp base in their 14th full month, with a footnote), financing penetration by channel (CAF, Tier 2, Tier 3, Other), CAF income and interest margin, and average selling prices.
- Why invest: the four-tile strip on the home only. No page.
- FAQ: a page titled Investor FAQs exists but has no questions (it holds contact details, quick links and the alert form). Avoid.
- Governance: Board of Directors with four committee charters (audit, compensation and personnel, nominating and governance, technology and innovation), Executive Management, Governance Documents.
- Email alerts: double opt-in form with six list types: News Release, Events & Presentations, SEC Filings, End of Day Stock Quote, Financial Report, Annual Report. "Will not be shared with third parties" statement.
- Events archive: Events & Presentations page (not captured), RSS available.
- Analyst coverage: page exists (not captured).
- IR contact: three named people (VP, Director, Manager), phone with extension, email (investor_relations@carmax.com). Best contact block of the ten for a small team.
- SEO: title "Carmax - IR Home" and "Carmax - Financials - Financial Information" (company, section, page). No meta description, no og tags, no JSON-LD in the home source.
- Distinctive: the ABS and securitization data page; double opt-in alerts with six granular lists; a named IR team; "Why Invest" tiles that are all one-line facts with units.
- Avoid: an FAQ page with no FAQs; no meta description.

### 2.3 Credit Acceptance (CACC)

- URL: https://ir.creditacceptance.com (the host refuses plain TLS from my tools; it serves at https://www.ir.creditacceptance.com and via the vendor alias creditacceptancecorporation.gcs-web.com). Pages read: home; /reports-and-financials; Investor Questions (node 16141); a press release item (node 8776, a 2007 release); the Q2 2026 earnings release (SEC 8-K exhibit).
- Platform: Notified-type Drupal (inferred). Stock info block: "Minimum 15 minutes delayed. Source: LSEG".
- Navigation order (from a search snippet of the rendered menu): Investor Relations, Stock Transfer Agent, Reports and Financials, Proxy Materials, Stock Price Info, Earnings Calls and Transcripts, Press Releases, Investor Questions, Board Members, Executive Leadership, Corporate Governance, ESG.
- Home: a three-sentence mission paragraph (financing "regardless of their credit history", dealer network, credit-score benefit), two latest press releases with "Summary Toggle", "CEO Letter to Shareholders" (2025 letter), the next earnings call (Oct 29, 2026 5:00 PM EDT) and a Stock Information block, plus a link to "view our 2025 Annual Report on-line or request a printed copy". No KPI tiles.
- Reports and Financials page: a full forward-looking-statements safe-harbor block sits at the top of the page, above the documents.
- **Investor Questions page (distinctive):** all requests must be in writing (mail or web form to the IR department), "written responses will be posted under the 'Investor Questions and CA Responses' link below and furnished to the Securities and Exchange Commission on Form 8-K". This is a fair-disclosure way to answer retail investors without taking calls.
- Operating metrics: not retail per-unit. The release gives "Consumer Loan assignment unit volume declined 1.0% to 84,615 while dollar volume grew 0.1% to $1.0 billion", the average loan portfolio balance ($8.0 billion), and a table of "Forecasted Collection Percentage" by assignment period (for example the Jan to Mar 2026 vintage at 66.5%) with the current forecast against the initial forecast and the variance. Definition in the release: forecasted collection rate is the percentage "we expect to collect on the Consumer Loans as a percentage of the repayments that we were contractually owed... at the time of assignment, including both principal and interest."
- Governance: Board Members, Executive Leadership, Corporate Governance, ESG as top-level items.
- Email alerts: not captured.
- IR contact: ir@creditacceptance.com and a named Chief Treasury Officer (in a Dec 2024 release).
- SEO: title pattern "Page | Credit Acceptance Corporation".
- Distinctive: the Investor Questions and CA Responses mechanism; the vintage table (shows how forecasts held up against the original estimate); a printed annual report on request.
- Avoid: the safe-harbor wall of text above the actual documents; 2007 releases still indexed under the live IR host.

### 2.4 America's Car-Mart (CRMT)

- URL: https://ir.car-mart.com. Pages read: home; /overview; /news-events/press-releases; /financials/quarterly-results; /resources/investor-faqs; /stock-info; /stock-info/analyst-coverage; /governance/governance-documents; the Q1 FY2027 release (9 Sep 2026, read in a newswire copy).
- Platform: Q4 Inc.
- Navigation order: Overview; News & Events (Press Releases, Event Calendar); Stock Info (Stock Quote, Stock Chart, Historical Stock Quote, Investment Calculator, Analyst Coverage); Financials (Quarterly Results, Annual Reports, SEC Filings); Governance (Governance Documents, Senior Management, Board of Directors, Committee Composition); Resources (Investor FAQs, Information Request Form, Investor Email Alerts, Investor Contacts).
- Home: no banner, a "Corporate Overview" paragraph, three panels (Latest News, Latest Events, Latest Quarterly Reports, each with View All, items not captured), a contact block (phone, email), quick links (SEC Filings, Investor FAQs, Information Request Form, Corporate Site). The overview text says "over 90" dealerships in 12 states and "more than 100,000 active customer accounts", which no longer matches the latest release (94 dealerships after consolidating 60 locations, 85,753 active customers). Stale facts on the home are a trust problem.
- Financial reports: Quarterly Results, Annual Reports, SEC Filings pages (Q4 modules, not captured).
- Operating metrics: yes, a "Key Operating Results" table in each release. See section 3. Release structure: CEO commentary at the top ("This is a capital structure story, not a demand story"), then a business review by topic (sales volume, total revenue, gross profit, SG&A, credit and finance receivables), then tables: Key Operating Results, Operating Data, Period End Data, consolidated results, balance sheet, cash flow, a debt-to-receivables calculation, and adjusted SG&A and adjusted loss per share reconciliations.
- Why invest: none.
- FAQ: a page exists with no questions in the text (title only).
- Analyst coverage: two firms (Jefferies, Stephens), with a typo in one analyst surname on the page.
- Governance: four documents (code of conduct and ethics at 11.97 MB, audit and compliance charter, compensation and human capital charter, nominating and governance charter). An 11.97 MB code of conduct file is too heavy.
- Email alerts: double opt-in, six lists (News, Quarterly Reports, Annual Reports, SEC Filings, End of Day Stock Quote, Events & Presentations).
- IR contact: phone and email only, no named person. An "Information Request Form" page.
- SEO: title "America's Car-Mart, Inc. - Investor Relations", sub pages "America's Car-Mart, Inc. - Financials - Quarterly Results". No meta description in the home source.
- Distinctive: the Information Request Form (a form instead of an inbox); the Investment Calculator (not worth copying).
- Why it matters: it is the closest business-model peer (used cars, customer credit) and a case study in candour. The release leads with the problem (capital constrained, units down 81.9%) and still publishes the full unit table. Copy the candour, not the stale overview, empty FAQ and 12 MB code PDF.

### 2.5 Upstart (UPST)

- URL: https://ir.upstart.com. Pages read (second crawler): home; /ir-resources/investor-faqs; /ir-resources/contact-ir; the 3 Aug 2026 originations and UMI release; the Q2 2026 release. Direct fetch returned 403.
- Platform: Notified-type (inferred).
- Navigation order (from a search snippet): News & Events (news releases, events and presentations); Financials (SEC filings, quarterly results, annual reports); Governance (leadership, board, committees); IR Resources (Investor FAQs, Contact IR). Overview first.
- Home hero (the best thesis-led hero of the ten): headline "Upstart is the leading AI lending marketplace", a three-sentence vision paragraph, a "Download Q2'26 earnings presentation" button, then a "Since inception (as of Q2'26)" counter strip: Loan volume 6M+, Originations $61B+, Repayment events 110M+, Bank partners 100+. Then an AI Day block (investor day replay and presentation), News releases (latest 3 with "See all"), Latest earnings, Latest Annual Report and Proxy (download buttons), Events (upcoming and past six, each with a "Click here for webcast" link), and a Shareholder letter block with a quote from the Executive Chairman.
- Financial reports: quarterly results are a news release plus the earnings presentation; the annual report and proxy are direct downloads on the home.
- News: list of releases with date and title; per-release URL pattern /news-releases/news-release-details/<slug>.
- Operating metrics: dollars and counts (not per car). A monthly release on the third day of the month ("Upstart Publishes July 2026 Originations and Latest UMI") with a table: Period, Originations ($1,397.4M), Origination days (27.4), Originations dollars per day ($51.0M). The release carries a definitions block: "Originations" refers to Transaction Volume, Dollars, defined as "the total principal amount of loan originations (or committed amounts for HELOCs and draws for Cash Line) facilitated through Upstart's marketplace during the periods presented"; "Origination days" are effective funding days (a business day counts 1.0, weekends and bank holidays 0.55, month-end rolled to the next business day when it falls on a weekend or holiday); "Originations, Dollars per day" is originations divided by origination days. It says the data are preliminary until quarterly financials close and points to upstart.com/volume. Q2 2026 release highlights: Originations $4.2 billion and 558,014 loans originated, Contribution Profit $193 million, Contribution Margin 55%, with a segment split (unsecured and secured).
- FAQ (12 plain-fact questions): HQ address, state of incorporation, fiscal year end, who is on management and the board, where to find SEC filings, where to find news releases, independent auditor, how the stock trades (exchange and symbol), IPO date, dividend policy, transfer agent (named, with phone and email), how to contact IR.
- Events: includes retail-friendly events (a CEO Q&A on X, an influencer Q&A) next to bank conferences.
- Governance: Leadership, Board, Committees (not captured).
- IR contact: single email ir@upstart.com.
- SEO: "Investor Relations | Upstart Holdings, Inc.", "Investor FAQs | Upstart Holdings, Inc.".
- Distinctive: since-inception counter strip; a monthly operating release with a definitions block and a normalizing "per funding day" metric; shareholder letter and investor day on the home; retail-oriented events.
- Avoid: home items go stale quickly (the cached home still listed a September event as upcoming and August news as latest); keep the home to what can be maintained monthly.

### 2.6 Open Lending (LPRO)

- URL: https://investors.openlending.com. Pages read (second crawler): home; /financial-information/quarterly-results; /financial-information/sec-filings; /investor-resources/investor-faq; /corporate-governance/governance-highlights; /news-and-events/presentations; the Q1 2026 release.
- Platform: Notified-type (inferred), SEC table credited "Data provided by Kaleidoscope".
- Navigation order: Overview; Stock Information (Stock Quote & Chart); News & Events (News Releases, Events, Presentations); Financial Information (SEC Filings, Quarterly Results); Corporate Governance (Governance Highlights, Management Team, Board of Directors, Committee Composition); Investor Resources (Investor FAQ, Email Alerts, Contact IR). A utility strip on every page: Print Page, Email Alerts, RSS Feeds, Contact IR.
- Home: a one-paragraph corporate profile (what the product is, where, founded in Austin in 2000), a banner link to the notice of redemption of public warrants, News Releases (latest two, including the 16 Jun 2026 merger agreement to be acquired), Events (three past earnings calls). No KPI tiles, no quote text.
- Quarterly results page: one block per year and quarter with three links: press release, "Q1 2026 Earnings Supplement" (PDF, size shown), Form 10-Q or 10-K (internal link). Back to Q2 2020. Simple and fast to scan.
- SEC filings: filter by group (Annual Filings, Current Reports, Mergers & Acquisitions, Other, Proxy Filings, Quarterly Filings, Registration Statements) and by filing year; items per page 10, 25 or 50; each row offers PDF, RTF, XLS and HTML views; the page counted 554 results.
- Operating metrics: release "Business Highlights" give unit economics per certified loan: "Average profit share revenue per certified loan was $363 in the first quarter of 2026, compared to $278", "Average program fee revenue per certified loan was $538... compared to $550", certified loans facilitated (21,064 vs 27,638), and credit unions and banks as a share of certified loans (90.2%). The 10-Q computes the profit-share average as dollars divided by new certified loans (for example "$19.0 million... 34,354 new certified loans for an average of $553 per loan" in a 2023 10-Q). No standalone definition on the IR site.
- FAQ (13 questions): HQ, IPO and SPAC history, dividend policy, transfer agent (named), who to call about stock, how to transfer stock or replace a certificate, auditor, CUSIP and ticker, warrant CUSIP, SIC code, where to find the warrant redemption notice, investor inquiries email. The most complete "plumbing" FAQ of the ten.
- Governance: Governance Highlights (a paragraph plus the code of conduct and three committee charters with file sizes), Management Team, Board, Committee Composition.
- Presentations: one item (a November 2024 investor presentation), so the page is a year stale.
- SEO: "Investor Relations | Open Lending", "Quarterly Results | Open Lending".
- Distinctive: per-loan revenue lines in the headline bullets; file sizes next to every download; a Print Page utility; CUSIP and SIC in the FAQ.
- Avoid: the warrant notice banner and a 2024 deck left on the site; no hero and no thesis.

### 2.7 ACV Auctions (ACVA)

- URL: https://investors.acvauto.com. Pages read: home; /company-information/faq; /company-information; /financial-information/financial-results; /corporate-governance; the Q2 2026 release (/news-events/press-releases/detail/111/...).
- Platform: hosted IR platform, vendor not named; CloudFront assets; Chorus Call webcasts; QuoteMedia quote and chart; ICR Inc. as IR agency; Computershare as transfer agent.
- Navigation order: IR Overview; News & Events (Press Releases, IR Calendar, Presentations, Email Alerts); Company Info (Company Profile, Executive Team, Contacts, FAQ); Financial Info (Financial Results, Income Statement, Balance Sheet, Cash Flow); Stock Data (Quote and Chart, Historical Data, Lock-Up Release FAQ (PDF), ACVA Share Conversion Form (PDF)); SEC Filings (All SEC Filings, Annual Reports, Quarterly Reports, Section 16 Filings); Governance (At-a-Glance, Board of Directors, Board Committees, Governance Documents); Back to acvauto.com.
- Home: the latest quarter as the hero card (quarter ended Jun 30, 2026) with links to earnings release, webcast, presentation, key figures and 10-Q; Latest news (4 items, newest first, including the Copart acquisition announcement of 10 Sep 2026); a "Stock Snapshot" block; customer testimonial videos from dealers. No KPI tiles in the text.
- Financial results page (the best document grid): one block per quarter or fiscal year. Each block lists Earnings Release (HTML and PDF), Earnings Webcast (audio), Presentation (PDF), **Key Figures (XLSX)**, and 10-Q or 10-K (HTML, PDF, XBRL ZIP). The site also publishes standalone Income Statement, Balance Sheet and Cash Flow pages.
- News: per-release URL /news-events/press-releases/detail/<id>/<slug>, each with "Download as PDF".
- Operating metrics: release highlights give "Marketplace GMV of $2.7 billion" and "Marketplace Units of 211,472", plus Marketplace and Service Revenue, with history in the "Key Figures XLSX". No per-unit profit published.
- Why invest: none. Company Profile gives a description plus Industry Classifications (Sector, Industry, NAICS, SIC).
- FAQ (13 questions): HQ, symbol and exchange, listing date, fiscal year end, who to contact about stock, transfer agent (named), how to transfer, how to obtain SEC documents, dividends, direct stock purchase plan, who is management and board, how to get more information, investor inquiries.
- Share structure: the Stock Data section carries a Lock-Up Release FAQ and a Share Conversion Form (a post-IPO legacy, but it shows how to give holders a practical form).
- Governance: **Governance at a Glance** matrix (board members by committee, with chair or member icons, a chairman star and a financial expert icon), then Committee Charters and long director biographies.
- Email alerts: a Sign Up page in the News & Events section; an RSS news feed; a Sitemap link in the footer.
- IR contact: a named officer plus the agency, with transfer agent and company address in the footer.
- SEO: home title "ACV Auctions Inc. (ACVA)", sub pages "FAQ :: ACV Auctions Inc. (ACVA)". og:title "Investors", og:image, canonical, and schema.org JSON-LD of type Corporation with name, legal name, address and description. The only site I could inspect with structured data.
- Distinctive: the Key Figures XLSX; HTML plus PDF plus XBRL on each filing; the governance matrix; schema.org markup; a footer with sitemap and RSS.
- Avoid: a "Stock Snapshot" heading shipped with no figures in the text; a testimonial-video wall on an IR home.

### 2.8 OPENLANE Inc. (OPLN), formerly KAR

- URL: **https://ir.corporate.openlane.com** (the requested investors.openlane.com does not resolve). Pages read: home; /investor-relations/events-and-presentations; /investor-news; /financials/financial-reports; /resources/faqs; /stock-info; /resources/investor-toolkit; /governance (Corporate Governance Guidelines text); Q2 2026 earnings release PDF.
- Platform: Q4 Inc. (footer credit, s202.q4cdn.com). The site is branded OPENLANE with a second KAR-branded menu still present in the source.
- Navigation order: Our Company (About, Brands, CSR & ESG, Leadership, Contact); Media Center; Investors (Overview, Investor News, Events & Presentations, Stock Info, Financials (Financial Reports, SEC Filings, Interactive Financials), Governance (Corporate Governance Guidelines, Board of Directors, Executive Bios, Committee Composition, Code of Conduct and Ethics, Code of Ethics for Principal and Senior Financial Officers, Lead Independent Director Charter), CSR & ESG, Resources (Contact, Investor Toolkit, FAQs, Email Alerts & RSS)); Careers; Marketplace (US, Canada, Europe).
- Home: heading "Investors" and a Latest Events panel with "View All Events". No hero, KPI tiles or news in text (modules did not render).
- Financials: "Interactive Financials" links to an IndigoTools web app (apps.indigotools.com) for building custom statement comparisons. The corporate governance guidelines are published as full text on the page (adopted Oct 29, 2024).
- Operating metrics: the Q2 2026 release gives growth rates, not unit counts: "Marketplace commercial vehicles sold growth of 39% YoY", "Marketplace dealer vehicles sold growth of 13% YoY, driven by 31% growth in US dealer vehicles sold", "Gross Merchandise Value (GMV) of approximately $10.5 billion". Segment contribution (Marketplace $57 million and AFC $46 million of Adjusted EBITDA) is quoted in the text. No per-vehicle profit table in the release.
- Why invest, FAQ questions, email alert form, analyst list: not captured.
- IR contact: investor_relations@openlane.com; a named VP of Investor Relations (appointed Oct 2025, per a company release found by search).
- SEO: title "OPENLANE - Investors" and "OPENLANE - Investor Relations - <Page>". No meta description or JSON-LD in the home source.
- Distinctive: Interactive Financials (a third-party app, simple to link); a Lead Independent Director Charter; a three-region marketplace switcher in the footer.
- Avoid: two brand menus (OPENLANE and KAR) side by side; a home that renders as a heading and nothing else when JavaScript fails.
- Relevance to OCAL: OPENLANE is OCAL's auction supply channel. Its investor site discloses nothing per unit that OCAL could cite; it reports the marketplace in GMV and vehicles-sold growth only. Any OCAL page that leans on OPENLANE should link here for the company description, not for volumes.

### 2.9 CarGurus (CARG)

- URL: https://investors.cargurus.com. Pages read (second crawler): home; the Q2 2026 release; /financial-information/quarterly-results. Search snippets for the rest. Direct fetch returned 403.
- Platform: Notified-type (inferred from URL patterns /news-releases/news-release-details/ and /static-files/).
- Navigation: not captured in text. Known URLs: /news-releases, /financial-information/quarterly-results.
- Home: the latest quarter as the hero ("CarGurus Second Quarter 2026 Financial Results", date and time, a webcast link, a presentation link), then a list: Webcast, Presentation, Press Release, "CARG Q2'26 Key Financials and Supplemental Tables", Form 10-Q, Transcript. Then **Key Metrics tiles with numbered footnotes**: 46M Monthly Unique Visitors (footnote: as of 6/30/2026, monthly average for the quarter); $907M FY 2025 Revenue; 34,629 Global Paying Dealers (as of 6/30/2026); $6,771 QARSD ("Quarterly Average Revenue Per Subscribing Dealer... for the three months ended 6/30/2026"). A company paragraph with numbered third-party source footnotes (Similarweb ranking), and the sentence "Please reference our most recent annual or quarterly report filed with the SEC for how we define our monthly unique visitors, paying dealers and QARSD". A named IR contact (VP, Head of Investor Relations) and an investors@ mailbox.
- Quarterly Results page: one block per quarter, each with Webcast, Presentation, Press Release, 10-Q or 10-K, Transcript, back to Q3 2017. Data error to avoid: the page showed "Released October 21, 2026" for the Q1, Q2 and Q4 blocks (a copied date).
- News: standard release list, per-release page, highlights as bold lead lines ("Q2'26 revenue grew 13% YoY to $251.0 million", "Repurchased $29.2 million worth of shares").
- Share structure: reported in the release balance sheet (75,571,320 Class A and 13,763,613 Class B shares outstanding at 30 Jun 2026). A search snippet of an older annual report says Class B carries ten votes per share and the founder holds a controlling vote. No dedicated capitalization page found.
- Why invest, FAQ, analyst coverage, governance: not found at the paths I tried, so not captured.
- SEO: "Investor Relations | CarGurus", "Quarterly Results | CarGurus", release pages "<Release title> | CarGurus".
- Distinctive: footnoted KPI tiles on the home; one list of every earnings resource right on the home; a "Key Financials and Supplemental Tables" file; a buyback message in the headline (">30% of shares since December 2022").
- Avoid: wrong quarter dates on the results page.

### 2.10 Cars.com (CARS, doing business as Cars Commerce)

- URL: https://investor.cars.com. Pages read: home (/overview); /why-invest; /investor-faqs; /analyst-coverage; /quarterly-results; /contact-ir; /governance-documents.
- Platform: vendor not named. Page-source clues only (webDriver paths, OneTrust consent, webinar.net webcasts). Clean flat URLs (no .aspx, no /default).
- Navigation order: Overview; Why Invest; News; Events; Stock Info (Stock Quote and Chart, Historical Stock Price, Investment Calculator, Analyst Coverage); Financials (Quarterly Results, Annual Reports and Proxy, SEC Filings); Governance (Management, Board of Directors, Committee Composition, Governance Documents, Ethics Reporting Guidelines); CSR; Resources (FAQs, Investor Alerts, Request Information, Contact IR, Video Hub); Search.
- Home hero: a carousel with one KPI slide ("$689MM Full Year 2023 Revenue" with a stray "Full Year 2021 metrics" note in the same slide, while the Why Invest page shows FY2025 revenue of $723MM, so the hero is stale and self-contradicting), a "Who we are" section naming four brands, the latest three news items, the next earnings call (events page, with Add to Calendar and Set Email Reminder), a Quarterly Results strip (press release, webcast, presentation for Q2 2026), and a document strip (Investor Presentation 3.9 MB, Fact Sheet 1.3 MB with file sizes shown, Video Hub, Industry Insights Report, Annual Report, Proxy Statement).
- Financials: the Quarterly Results page has a Featured Financials file ("Quarterly Financials and Metrics (197 KB)") and a **grid: years 2019 to 2026 across, document types down** (Press Release, Earnings Presentation, Earnings Transcript, 10-Q/10-K, Annual Reports) with Q1 to Q4 links in each cell. A Tax Information block (spin-off Form 8937). Annual Reports and Proxy is its own page.
- **Why Invest page (the most useful model here):** title "Why Should You Invest? | Cars Commerce Investor Relations". Order: one-paragraph company story; a Key Metrics strip (FY 2025: Revenue $723 MM, Adj. EBITDA $211 MM, Avg. Monthly Unique Visitors 25.7 MM, Visits 627 MM, Dealers 19,544); then five all-caps argument blocks: Platform Advantage; Asset Light Business Model with Attractive Free Cash Flow and Strong Balance Sheet (states "we do not disintermediate transactions or take ownership of vehicles", "convert upwards of 60% of our Adjusted EBITDA to Free Cash Flow", subscription about 90% of revenue, a net leverage target range of 2.0x to 2.5x, and the capital allocation order); Leading Consumer Brand with Strong Organic Traffic; Significant Headroom in a Multi-Billion Dollar Addressable Market ($50 billion); Strong, Experienced Management Team. Weaknesses: no forward-looking statements disclaimer on the page, and no sources for the market-size or traffic claims.
- FAQ: 21 questions (ticker and exchange; "Can I buy shares in Cars Commerce?" (name change explained); who is the transfer agent; how to buy; dividend; name change date and why; spin-off date; HQ; spin-off mechanics and ratio; tax basis form; board; management; how to contact the board and non-management directors; CSR; how to contact IR; calendar year; auditor; where to find SEC filings; analyst coverage; how to sign up for alerts).
- Analyst coverage: seven firms with analyst names.
- Governance: management, board, committees, documents (organization documents and policies), and a separate ethics reporting guidelines page.
- Email alerts: a Subscribe button on the home, and an Investor Alerts page.
- IR contact: a named VP, Investor Relations, with phone and email on the Contact IR page; a Request Information page.
- SEO: the only site with a real meta description: "Learn about investing in Cars Commerce today. See our stock history, quarterly and annual results, upcoming events, governance structure, press releases and more." Title "Investor Relations | Cars Commerce"; canonical set to the root; og tags present; no JSON-LD.
- Distinctive: Why Invest with a KPI strip and stated cash conversion; a Fact Sheet PDF with its size shown; a Video Hub; Add to Calendar and Set Email Reminder on each event; a document grid by year and type; CSR as a top-level item.
- Avoid: a stale and contradictory hero KPI; unsourced superlatives ("#1 most recognized").

## 3. Per-unit economics: how Carvana, CarMax and America's Car-Mart define and present them

### 3.1 (b) Per-unit metric definitions table

All figures are the latest quarter published as of 23 Oct 2026. Definitions are quoted from the company's own release where in quotation marks; otherwise the wording is my description of the table label and calculation, marked "table label".

| Company | Metric name (as the company labels it) | Definition as the company states it | Latest value | Where it appears on the site |
|---|---|---|---|---|
| Carvana | Retail units sold / "Retail vehicle unit sales" | Table label only ("Unit sales information: Retail vehicle unit sales"). It is the denominator of every GPU line. No standalone definition in the letter | 197,325 (Q2 2026), up 38% | Q2 2026 release (highlight) and shareholder letter (summary bullets and Results of Operations), both reached from /financial-reports/quarterly-results/2026 |
| Carvana | Total gross profit per unit ("GPU") | Letter: "Total Gross profit per unit ('GPU') was $7,014". Table: total gross profit divided by retail units, under "Per retail unit gross profit: Total gross profit" | $7,014 GAAP | Shareholder letter summary bullets and Results of Operations table |
| Carvana | Non-GAAP Total GPU | "Total gross profit per retail unit, non-GAAP... are the respective gross profits, non-GAAP divided by retail vehicle unit sales." Gross profit, non-GAAP is GAAP gross profit "plus depreciation and amortization expense in cost of sales and share-based compensation expense in cost of sales, minus revenue related to our Warrants" | $7,125 | Letter summary bullets and the non-GAAP reconciliation tables |
| Carvana | Retail GPU (Retail gross profit per retail unit) | Retail vehicle gross profit divided by retail vehicle unit sales. Part of the GPU components shown in the Results table and Appendix I | $3,547 GAAP (non-GAAP about $3,629 in the reconciliation) | Results of Operations table, Appendix I "GPU and SG&A Expense Detail", non-GAAP reconciliation |
| Carvana | Wholesale GPU (Wholesale gross profit per retail unit) | Wholesale gross profit divided by **retail** units (not wholesale units), so the three components add to Total GPU | $801 GAAP (non-GAAP about $862) | Same tables. A separate row, "Per wholesale unit gross profit: Wholesale vehicle gross profit", divides by wholesale units and excludes wholesale marketplace units and profit (footnote 4) |
| Carvana | Other GPU (Other gross profit per retail unit) | Other gross profit divided by retail units. The letter does not say what "other" contains | $2,666 GAAP (non-GAAP about $2,635) | Same tables. Commentary: "Other GPU, which was lower due to increasing benchmark rates" |
| Carvana | Total SG&A expenses per retail unit | SG&A divided by retail units. Non-GAAP: SG&A "minus depreciation and amortization expense in SG&A expenses and share-based compensation expense in SG&A expenses", divided by retail vehicle unit sales | about $3,568 GAAP, about $3,228 non-GAAP (my arithmetic from $704M and $637M over 197,325 units) | Results of Operations, non-GAAP reconciliations, components of SG&A table (compensation, advertising, market occupancy, logistics, other) |
| Carvana | Per-unit revenue rows | "Per unit revenue" for retail vehicles and wholesale vehicles (wholesale excludes marketplace units) | $27,908 retail; $10,633 wholesale | Results of Operations table |
| CarMax | Used vehicle units / "Retail used unit sales" | Table "Unit Sales: Used vehicles". Comparable store used unit sales is reported separately; stores join the comp base "beginning in their fourteenth full month of operation" | 227,391 (Q2 FY2027, quarter ended 31 Aug 2026), up 13.8% | Q2 FY2027 release (Business Wire copy and PDF reached from the News page) |
| CarMax | Used vehicle gross profit per unit (headline text: "gross profit per retail used unit") | Footnote: "Calculated as category gross profit divided by its respective units sold, except the other category, which is divided by total used units sold." Shown with a second column, % of sales (7.6%) | $2,105, down $111 | "Gross Profit per Unit" table in the release; headline bullet |
| CarMax | Wholesale vehicle gross profit per unit | Same footnote (wholesale gross profit divided by wholesale units); 10.1% of sales | $858, down $135 | Same table |
| CarMax | Other gross profit per unit | Other gross profit divided by **total used units**, per the footnote; 87.9% of "other" revenue | $806 | Same table |
| CarMax | EPP margin per retail unit | "Extended Protection Plans (EPP) margin per retail unit of $623, an increase of $46 per unit" (no formal definition in the release) | $623 | Headline bullet and the Other gross profit discussion |
| CarMax | SG&A per total unit | Total SG&A divided by total units (used plus wholesale), in a row labelled "SG&A per total unit" | $1,621 | SG&A table in the release |
| CarMax | Average selling price, used and wholesale | "Average Selling Prices" table | $27,623 used; $8,036 wholesale | Release |
| CarMax | Used vehicle financing penetration by channel | "Calculated as used vehicle units financed for respective channel as a percentage of total used units sold" (CAF, Tier 2, Tier 3, Other) | CAF 43.3% before 3-day payoffs | Release table |
| America's Car-Mart | Retail units sold | Text ("Retail units sold decreased 81.9% to 2,450 units"); no separate definition | 2,450 (Q1 FY2027, quarter ended 31 Jul 2026) | Release (Key Operating Results table), newswire copy, Press Releases page |
| America's Car-Mart | Total gross profit per retail unit sold | "Total gross profit per retail unit sold is calculated based on total gross profit, which includes the loss on third-party wholesale sales, divided by a retail unit count that declined 81.9%." (the release adds that wholesale produced an aggregate loss of $4.7 million) | $8,015, up 7.5% (fixed costs spread over fewer units, not a better business) | Key Operating Results table and Business Review text |
| America's Car-Mart | Average retail sales price, excluding ancillary products | Table label (no separate definition) | $18,530, up 7.0% | Key Operating Results table |
| America's Car-Mart | Total gross profit percentage (gross profit margin) | "Gross profit margin as a percentage of sales was 21.8%, compared to 36.6%"; third-party wholesale carried lower margins and was 23.4% of total sales | 21.8% | Business Review and tables |
| America's Car-Mart | Average down-payment percentage | Table label | 5.4% (4.9% prior) | Key Operating Results |
| America's Car-Mart | Weighted average total contract term | Table label (months implied; the unit is not printed in the text I read) | 49.3 (48.3 prior) | Key Operating Results |
| America's Car-Mart | Average total collected per active customer per month | Table label. "Total collected" is described as "(principal, interest and late fees)" | $594 ($585 prior) | Key Operating Results |
| America's Car-Mart | Active customer count | Table label | 85,753 (104,691 prior) | Key Operating Results |
| America's Car-Mart | Net charge-offs as a percentage of average finance receivables; accounts over 30 days past due | Text and tables | 9.5%; 4.6% | Credit section of the release |
| Open Lending | Certified loans; average profit share revenue per certified loan; average program fee revenue per certified loan | Release bullets ("Average profit share revenue per certified loan was $363... compared to $278"). The formal definition sits in the 10-Q, not restated on the IR site | 21,064; $363; $538 | Release "Business Highlights" |
| Cars.com | Dealer Customers; ARPD (monthly average revenue per dealer) | Release table. The definition appears in the call transcript glossary (monthly subscription income per dealership customer), not in a release footnote I could read | 19,343; $2,500 | Quarterly results release and presentation |
| CarGurus | Paying Dealers; QARSD | "A dealer account with an active, paid marketplace subscription at the end of a defined period." QARSD is subscription revenue for the quarter divided by the average number of paying dealers in the quarter (per the 10-Q) | 34,629; $6,771 | IR home Key Metrics tiles with footnotes |
| ACV | Marketplace Units; Marketplace GMV | Release highlight lines | 211,472; $2.7 billion | Release highlights; Key Figures XLSX |
| Credit Acceptance | Consumer Loan assignment unit volume; forecasted collection rate | Quoted in section 2.3 | 84,615; 66.5% for the Jan to Mar 2026 vintage | Earnings release |
| Upstart | Originations (Transaction Volume, Dollars); Origination days; Originations dollars per day | Quoted in section 2.5 | $1,397.4M; 27.4; $51.0M (July 2026) | Monthly release |

### 3.2 What the three retailers teach about presentation

1. **They all divide by retail units, and say so.** Carvana divides every gross profit line, including wholesale and other, by retail units so the parts add to a total. CarMax divides each category by its own units except "Other", which uses total used units. Car-Mart divides total gross profit, including losses on wholesale, by retail units. Whatever OCAL picks, state the denominator in a footnote right under the table.
2. **They show the total and the parts.** Carvana: Retail, Wholesale, Other and Total GPU, each with a year-over-year change, plus SG&A per unit and the reconciliation to adjusted EBITDA. CarMax: Used, Wholesale, Other, each with a "% of sales" column next to the dollars per unit, which doubles as a gross margin line. Car-Mart: one total, then a short ladder of unit metrics (price, down payment, term, collections per customer, active customers, credit).
3. **They tie the per-unit number to a cause in one sentence.** Carvana: the shift between Retail and Other GPU, "we followed the market on retail pricing but kept customer-facing interest rates stable". CarMax: "reflecting the continuation of pricing actions implemented to support an improved sales trend". Car-Mart: fixed costs "spread over a substantially reduced retail sales base". OCAL should do the same.
4. **Per-unit lines sit in the release or letter, not on a dedicated web page.** None of the three publishes a per-unit table as a standalone IR page, and none shows a GPU tile on the home. The tables live in the quarterly PDF, reachable from the Quarterly Results page. A dedicated, always-current per-vehicle page with the last eight quarters in an XLSX (see ACV's Key Figures idea) would be new for this peer group and is the opportunity for OCAL.
5. **GAAP first, non-GAAP second.** Carvana leads with GAAP GPU ($7,014) and shows the non-GAAP ($7,125) beside it with the reconciliation. CarMax's GPU table is GAAP only. Car-Mart reports GAAP GPU with non-GAAP only for SG&A, debt and earnings per share.
6. **Candour when the numbers are bad.** Car-Mart's GPU rose 7.5% in a quarter when units fell 81.9%, and the release says exactly why. A per-unit table that rises for a bad reason needs the same sentence.

### 3.3 Draft microcap version: OCAL per-unit table (for CQ and Has to build; numbers to be confirmed by OCAL finance before anything is published)

| Metric | Draft definition (footnote under the table) |
|---|---|
| Vehicles funded | Number of vehicles for which the customer's lender approved and funded the purchase and OCAL completed the sale in the period. One vehicle is counted once. |
| Average vehicle price | Total vehicle sale price of vehicles funded in the period divided by vehicles funded. Say whether taxes, registration and lender fees are in or out. |
| Gross profit per vehicle | Total gross profit for the period (as in the financial statements, with every revenue source included) divided by vehicles funded. State which revenue lines are included (vehicle sale, lender or program fees, ancillary products) and, if possible, show the same split CarMax and Carvana do (vehicle, finance and other). |
| Gross margin | Total gross profit divided by total revenue for the period, as a percentage. Same period as the other three. |

Presentation rules lifted from the peers: show the current quarter, the same quarter a year earlier and the change; add trailing twelve months for stability when unit counts are small; one footnote block with every denominator; one sentence on what moved the number; the same table in the press release, the investor page and the quarterly letter; archive an XLSX of every quarter.

## 4. (a) Top 12 ideas OCAL should steal, ranked

1. **A three-to-four line per-unit table with a "% of sales" column and a footnote stating every denominator.** Source: CarMax (Gross Profit per Unit table) and Carvana (Retail, Wholesale, Other, Total GPU and SG&A per unit). For OCAL: Vehicles funded, Average vehicle price, Gross profit per vehicle, Gross margin, each with a prior-year comparison.
2. **Footnoted KPI tiles on the investor home**, each tile carrying its period and a numbered definition, and a pointer to the filing for the formal definition. Source: CarGurus (46M, $907M, 34,629, $6,771 with footnotes) and CarMax (255+ stores, $26B revenue, 1.3M units, $16B loan book). For OCAL: four tiles matching the per-unit table, plus FY2025 audited revenue.
3. **A quarterly results grid: one row per quarter, fixed columns** (Press Release, Letter to Shareholders, Supplemental Tables, Webcast), plus a separate list of all letters. Source: Carvana. Cars.com's grid by year and document type is the compact alternative. For OCAL: Release, Letter, Per-vehicle table (XLSX), Financial statements, MD&A and a SEDAR+ link.
4. **A monthly operating page or release with a definitions block and a normalized rate** ("per funding day"). Source: Upstart (monthly originations, origination days, dollars per day, "preliminary until quarterly financials close"). For OCAL: monthly vehicles funded with a funding-days normalizer, if the board and its disclosure review are comfortable with a monthly cadence.
5. **A real Why Invest page** with a KPI strip, five argument blocks and stated capital and cash facts. Source: Cars.com (platform advantage; asset-light and free cash flow; brand and organic traffic; market size; management). For OCAL the matching blocks would be: approval first, car second; zero standing inventory with digital inventory via OPENLANE; unit economics per vehicle; market size; management and board. Add the forward-looking caution that Cars.com omits, and source every claim.
6. **A written Investor Questions page** where questions are answered once, in writing, and posted publicly. Source: Credit Acceptance (answers posted and furnished on Form 8-K). For OCAL: a posted Q&A page, with material answers also made public through the usual disclosure channels, which keeps selective disclosure risk low and removes the need to take calls.
7. **A plumbing FAQ of 12 to 20 questions.** Sources: Open Lending (CUSIP, SIC, transfer agent, certificate replacement, warrants, auditor), Cars.com ("Can I buy shares?", "Which analysts cover the company?", "How do I sign up for alerts?"), Upstart (fiscal year end, auditor, IPO date, dividend policy). For OCAL add: TSXV symbol and CUSIP or ISIN, fiscal year end 31 Aug, transfer agent, auditor, how to buy through a Canadian broker, dividend policy, OTC status (only once it is true), where to find filings.
8. **An evergreen introduction deck, dated, plus explainer decks that teach the model.** Source: Carvana ("Introduction to Carvana" July 2026, "Cost Structure Details", "Carvana 101"). For OCAL: "Introduction to OCAL" refreshed each quarter and a one-page "How OCAL earns money on one vehicle".
9. **A quarterly shareholder letter in a fixed structure**: summary bullets, a short theme, then the tables. Source: Carvana's letter (summary bullets, outlook, theme, appendix of unit detail). Take the structure; leave the numerical guidance and the long-term margin goal out (see section 5).
10. **A Key Figures workbook, and HTML plus PDF plus XBRL on every filing.** Source: ACV (Financial Results page with Key Figures XLSX), Cars.com ("Quarterly Financials and Metrics" file), Open Lending (file sizes beside each download, earnings supplement). For OCAL: one XLSX with eight quarters of per-vehicle data and statements.
11. **Double opt-in alerts with granular list types, and a named IR contact.** Source: CarMax and Car-Mart (News, Events, SEC Filings, End of Day Quote, Financial Report, Annual Report; confirmation by activation email; "will not be shared"), CarMax (named IR people with phone and email), Cars.com (named VP, phone and email), Car-Mart (an Information Request Form). For OCAL add SEDAR+ filings and press releases as the two lists that matter.
12. **Governance at a glance and a share structure block.** Source: ACV (board by committee matrix with chair, member and financial expert icons), Carvana (basic and fully-exchanged share count in the letter), CarGurus (Class A and Class B counts in the release). For OCAL: board and committee matrix, shares outstanding, options, warrants and any escrow or resale restrictions on one page. None of the ten peers has a standalone capitalization page, so this is a chance to be clearer than the peer group.

Runners-up: Upstart's since-inception counter strip on the home (loans, originations, partners); Cars.com's Add to Calendar and Set Email Reminder on events; ACV's schema.org Corporation markup together with Cars.com's descriptive meta description (no Q4 page or Carvana page has a useful one, so an OCAL page with both beats all ten on basic SEO); OPENLANE's Interactive Financials link; Credit Acceptance's printed annual report on request; Open Lending's Print Page utility and file sizes.

## 5. (c) Five things these sites do that OCAL's size means it should NOT copy

1. **A mega-menu with 25 to 35 pages and modules that arrive empty.** Carvana, CarMax, OPENLANE and Car-Mart each have 20 or more destinations, and several (SEC Filings, Investor FAQs, Analyst Coverage) render nothing without JavaScript or have no content. OCAL should ship about eight pages that are always populated: Home, Why Invest, Per-Vehicle Results, Financials and Filings, News, Presentations and Events, Governance and Share Structure, FAQ and Contact. Never publish a page title with nothing behind it.
2. **Adjusted EBITDA, non-GAAP GPU and long reconciliation tables.** Carvana and OPENLANE build their story on non-GAAP lines with page-long reconciliations. For a company with roughly $5M market value and audited revenue of $6.48M, non-GAAP lines invite prominence and reconciliation obligations under Canadian non-GAAP rules and add little. Publish GAAP-based per-vehicle numbers with a plain definition and keep the non-GAAP stack off the site.
3. **Numerical guidance and long-term targets.** Carvana's outlook (sequential unit growth, a full-year adjusted EBITDA range) and its "3 million cars a year and 13.5% adjusted EBITDA margin by 2030 to 2035" goal, ACV's and OPENLANE's guidance ranges, and Upstart's full-year outlook are standard for large caps with analysts. For OCAL they create forward-looking-information exposure and a number the company then has to meet. OCAL's plan to publish an operating update that is historical only should stand. If a long-term ambition is stated at all, state it qualitatively and put the forward-looking caution on the same page (the Cars.com Why Invest page has no such caution, which is also not worth copying).
4. **Analyst coverage lists, price calculators and historical price tools.** Carvana lists 26 firms, Cars.com seven, Car-Mart two, and Cars.com and Car-Mart carry an Investment Calculator and a Historical Stock Quote tool. OCAL has no sell-side coverage to list, and an empty or padded analyst page, or a prominent chart on a thinly traded stock, does more harm than good. Use a small delayed quote and a link to the TSXV listing page, and either say plainly "No analyst coverage at this time" or omit the page.
5. **Superlative, comparative claims in the investor voice.** "Industry-leading growth and profitability" (Carvana), "No. 1 visited" (CarGurus), "#1 most recognized" (Cars.com) and "largest used-auto retailer" (CarMax) rest on third-party rankings and billion-dollar scale. OCAL is a small TSXV issuer, so every comparative on the site must be sourced on the page or removed, and pitch phrases such as "zero standing inventory" and "digital inventory of 3,000+ vehicles via OPENLANE" should always appear with their plain-language qualification.

## 6. Things to avoid (stale or wrong content seen on live peer sites)

- Cars.com home hero KPI: "$689MM Full Year 2023 Revenue" with a "Full Year 2021 metrics" label while the Why Invest page shows FY 2025 $723 MM.
- America's Car-Mart overview: "over 90" dealerships and "100,000+" active accounts against 94 dealerships and 85,753 customers in the latest release.
- CarGurus Quarterly Results: three quarters tagged "Released October 21, 2026".
- Open Lending: a 2024 deck as the only item in Presentations; a warrant-redemption banner still on the home.
- Carvana: a 2018 Analyst Day video and slides still in the Investor Kit; the only home news item is a sponsorship.
- CarMax and Car-Mart: an "Investor FAQs" page with no questions.
- Upstart: the cached home still listed a September event as upcoming on 23 Oct.
- Investor email shown only through a script (Carvana, via Cloudflare obfuscation): fine against spam, bad when the script fails. Publish the address as plain text with a mailto link.

## 7. SEO signals observed

| Site | Home title | Meta description | Structured data | Other |
|---|---|---|---|---|
| Carvana | Investor Relations \| Carvana | "Investor Relations" only | none seen | og:title, og:image, og:url, canonical |
| CarMax | Carmax - IR Home | none | none seen | sub titles "Carmax - Section - Page" |
| Credit Acceptance | Investor Relations \| Credit Acceptance Corporation | not captured | not captured | "Page \| Company" pattern |
| America's Car-Mart | America's Car-Mart, Inc. - Investor Relations | none | none seen | sub titles "Company - Section - Page" |
| Upstart | Investor Relations \| Upstart Holdings, Inc. | not captured | not captured | "Page \| Company" pattern |
| Open Lending | Investor Relations \| Open Lending | not captured | not captured | "Page \| Company" |
| ACV | ACV Auctions Inc. (ACVA) | not captured | schema.org Corporation JSON-LD (name, legal name, address, description) | og:title "Investors", og:image, canonical, "Page :: Company (TICKER)" |
| OPENLANE | OPENLANE - Investors | none | none seen | sub titles "OPENLANE - Investor Relations - Page" |
| CarGurus | Investor Relations \| CarGurus | not captured | not captured | release pages "Title \| CarGurus" |
| Cars.com | Investor Relations \| Cars Commerce | a full descriptive sentence | none seen | canonical to root, og:type article, "Page \| Cars Commerce Investor Relations" |

Reading: the peer set barely competes on SEO. A page title pattern of "Page | OCAL Financial (TSXV: OCAL)", a descriptive meta description per page, canonical tags, Open Graph tags and Organization or Corporation JSON-LD (as ACV has) would put OCAL ahead of most of them with little effort. For the four Notified-type sites I could not inspect page source, so their meta tags and structured data are unknown.

## 8. What I could not verify (so it is not in the recommendations as fact)

- Rendered stock quote and chart vendor for Carvana, Credit Acceptance (beyond "LSEG" in text), Upstart, Open Lending, CarGurus and Cars.com.
- Analyst lists for CarMax, Credit Acceptance, Upstart, Open Lending, OPENLANE, CarGurus and ACV.
- Navigation menus for CarGurus (not rendered in text) and Credit Acceptance (snippet only).
- Carvana's non-GAAP per-unit components (about $3,629 retail, $862 wholesale, $2,635 other) come from a PDF whose tables extracted in jumbled order. The GAAP components ($3,547, $801, $2,666, total $7,014) and the totals tie to the release arithmetic ($700M, $158M and $526M of gross profit over 197,325 units).
- Whether any peer site exposes per-unit data outside the release PDFs (none seen).
- Open Lending, Cars.com and Upstart formal definitions of per-loan, per-dealer and contribution metrics sit in 10-Qs I did not open; the tables say so.
- Company events such as the Copart agreement to acquire ACV (announced 10 Sep 2026), the ANV tender offer for Open Lending (June 2026) and Car-Mart's special committee review are as read on those sites on the visit date. Do not cite them anywhere without a fresh check.
