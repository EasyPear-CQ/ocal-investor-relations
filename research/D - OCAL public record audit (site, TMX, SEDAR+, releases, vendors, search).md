# D. OCAL Financial Inc. public record audit

Prepared 23 Oct 2026 (research run about 11:30 to 12:45 Cayman time) for the investor site build (CQ and Has).
Scope: public web only. No confidential source was used. Every fact carries a URL and the date on the source where one exists. Anything I could not confirm is marked UNVERIFIED.
House rule applied: no em dashes or en dashes in this file. Where a source used one, I replaced it with a hyphen or a comma inside the quote.

## How this was gathered, and its limits

- ocalfinancial.ca was read two ways: (a) the live, JavaScript-rendered page in a browser (what a visitor sees), and (b) the raw HTML the server sends first (what a non-JavaScript crawler sees). They differ a lot, see section 1.9.
- TMX Money (money.tmx.com) was read in a browser: overview, key data, news and insider tabs. The filings and financials tabs returned "Something went wrong".
- SEDAR+ (sedarplus.ca) itself is a JavaScript application and could not be fetched. I rebuilt its filing list from copies that Newsfile mirrors (newsfile.futunn.com and moomoo "SEDAR_PLUS" attachments), the Futubull announcement feed, TMX/Newsfile and the OCAL investor page. The filing statement and the audited FY2025 financial statements were NOT read. Section 4 says exactly what is verified.
- Search results (section 11) come from the WebSearch tool (US index) and Exa, not from a logged-out Google results page. Treat the positions as indicative, not as a Google rank report.
- Third-party profile pages are scraped data and change daily. Quotes are as they read on 23 Oct 2026.

---

## 0. Findings that matter most for the build

1. The live investor page is much fuller than its raw HTML. Rendered, it has a hero, corporate information table, 18 press releases (paginated), 35 FAQ answers in 4 groups, two PDF downloads, two YouTube videos, and an IR contact. Raw HTML (what non-JS crawlers and some tools see) is 4 short paragraphs and no ticker symbol.
2. It has no financial statements, MD&A, filing statement link, SEDAR+ link, stock quote, subscribe form, governance documents, share structure table, bios or events calendar. The FAQ text promises several of these ("linked from this page", "subscribe to email alerts below") that are not on the page.
3. The page is missing the 22 Oct 2026 release (OCAL Showroom) and four other wire releases (see section 5).
4. FY2025 revenue appears four ways: $6.48M (audited, 6 Oct 2026 release, Yahoo), $6.88M (corporate presentation PDF and fact sheet on the investor page, "management information"), $6.84M (Feb 2026 unaudited LOI release) and "$6.8M" (Signal Capital LinkedIn post, 1 Sep 2026). The downloadable PDFs conflict with the audited figure. Recorded as fact only; the decision on the Signal deck is Matthew's and is not reopened here. The new site should quote the audited $6.48M.
5. The corporate presentation PDF has visible errors: "filing statement dated July 9, 2025" (should be 2026), a placeholder "Contact information: add an address", "Mehdi Mehdi brings", and it names Hasneen Jalil as CTO and an acquisition of Canada AutoExperts / EasyPear as complete. I found no news release or SEDAR+ item announcing that acquisition (UNVERIFIED).
6. Two statements on the live page are contradicted by the 31 Jul 2026 interim financial statements: "Revenue comes from financing commissions and related services" (vehicle sales were 89% of nine-month revenue) and "no inventory" (balance sheet inventory $86,300 and a floorplan facility of $222,033 at 31 May 2026). Those statements also carry a going-concern note that the page does not mention.
7. Brokerage wording is still live on the investor page: the two 18 Mar 2026 letters call OCAL a "technology-enabled brokerage platform", and the site's llms.txt calls it an "auto finance broker" operating as "One Click Auto Loan". The Feb 2026 LOI and the Newsfile company profile also use "virtual brokerage" / "licensed automotive finance platform".
8. Eight of 14 data vendors still carry the old description (auto, power sports, RV, personal loans, auto repair, healthcare financing); Google Finance has a wrong sector and share count; CNBC lists Ronin's former CEO. Full list with URLs in section 10.
9. TMX Money: last trade $0.11 on 20 Oct 2026 (2,000 shares), market cap $4,033,459, 36,667,803 shares, 52-week range $0.08 to $0.55, escrowed shares 23,638,104, 20-day average volume 19,114. TMX sector Finance, industry Credit Finance.
10. Search: for "OCAL Financial", "OCAL stock", "OCAL TSXV" and "OCAL share price", ocalfinancial.ca and money.tmx.com do not appear in the top 9 results; wire copies, Stockwatch, aggregators and algorithmic stock sites do. The company's own IR page appeared only at position 10 on one query.

---

## 1. Investor relations page

### 1.1 URLs

| URL | Result on 23 Oct 2026 |
|---|---|
| https://ocalfinancial.ca/investor-relations | The investor page. Linked from header nav ("Investor Relations") and footer ("Investor relations"). Canonical is itself. |
| https://ocalfinancial.ca/investor-relations/press-release/{slug} | 17 sub-pages, one per release or letter (listed in 1.4). All in sitemap.xml. |
| https://ocalfinancial.ca/investors | Returns HTTP 200 with the text "Page not found" (soft 404). Title "Page not found | OCAL Financial". Not redirected to the investor page. |
| https://ocalfinancial.ca/investor-relations/ | Same page (trailing slash). |
| /investor, /news | Same behaviour: every unknown path returns HTTP 200 with the home HTML shell (single page app). |
| https://ocalfinancial.com | Serves the same site (ends at ocalfinancial.ca). https://ocal.ca returns 301 to ocalfinancial.com. |
| https://ocalfinancial.ca/robots.txt | Allows all; disallows /admin, /dashboard, /auth, /paid-leads; points to https://ocalfinancial.ca/sitemap.xml. |
| https://ocalfinancial.ca/sitemap.xml | 286 URLs: 147 /inventory, 85 /blog, 19 /investor-relations (IR page plus 17 press-release pages plus 1), 9 /newsletters, 8 /service-areas. Latest lastmod values: 2 Oct, 6 Oct, 13 Oct, 15 Oct, 19 Oct 2026. The 22 Oct release has no page. |
| https://ocalfinancial.ca/llms.txt | Exists (see section 10, stale description). |

Search "site:ocalfinancial.ca investor": the search tool ignored the operator and returned unrelated regulator pages. Not a finding about the site.

Header nav (rendered): Financing, Inventory, Sell Your Car, About Us, Contact Us, Resources, Investor Relations, Sign In, and a "Get approved" button.

### 1.2 Title tag, meta description, structured data

- Title tag: `Investor Relations | OCAL Financial`
- Meta description: `OCAL Financial is building an AI-driven digital automotive dealership platform. Learn about our investment opportunity, technology platform, and growth strategy.` (no ticker, no TSXV, no mention of listing)
- Canonical: https://ocalfinancial.ca/investor-relations
- Open Graph and Twitter: same title and description; og:image https://ocalfinancial.ca/og-image.jpg; og:type website; twitter:card summary_large_image.
- H1 on the rendered page: "Light on assets. Heavy on technology." (search engines using the H1 show this as the page title, for example Exa).
- Structured data on the page: two JSON-LD blocks, both site-wide, no investor-specific markup.
  - `FinancialService`: name "OCAL Financial"; description "Vehicle financing in British Columbia and Alberta for all credit types. Customers are approved first, then the vehicle is sourced and delivered."; address 500 - 885 Dunsmuir Street, Vancouver, BC V6C 1N5; telephone +1-877-495-2012; email general@ocal.ca; sameAs: LinkedIn (ca.linkedin.com/company/ocalfinancial), Facebook (facebook.com/OCALFinancial/), TMX Money (money.tmx.com/en/quote/OCAL), Boerse Frankfurt (boerse-frankfurt.de/equity/CA67449X1050). There is no tickerSymbol, no exchange, no legalName, no NewsArticle markup on releases.
  - `WebSite` with a SearchAction to /inventory?search=.
- Other page facts: Google Analytics G-77WRSSJB5G; Google Ads AW-18057327187; YouTube embeds (2).

### 1.3 Full visible text of the investor page (rendered, 23 Oct 2026)

Dashes normalised. "[button]" marks a link or button.

**Hero**

TSXV: OCAL
# Light on assets. Heavy on technology.

OCAL is building an AI-driven digital automotive dealership platform, designed to scale nationally without the overhead of traditional dealerships. OCAL Financial Inc. (TSX Venture Exchange: OCAL; Frankfurt Stock Exchange: JC3) began trading following completion of its qualifying transaction in July 2026.

[Corporate presentation] [Investor fact sheet] [Press releases] [Management team]

Listed on the TSX Venture Exchange under the trading symbol OCAL.

**Track OCAL on the markets**

View live pricing, charts and quote data for TSXV: OCAL.
[TradingView chart] [TMX Money quote]

**Why invest in OCAL Financial**

The company combines automotive retail expertise with financial technology infrastructure built to scale across North America.

- A technology platform for automotive commerce. OCAL Financial is building a modern digital infrastructure designed to simplify how consumers access vehicles and financing. By integrating technology, lender networks, and automotive expertise into a single platform, the company is positioned to participate in one of the largest consumer markets in North America.
- Positioned at the intersection of auto and fintech. The vehicle purchasing process increasingly relies on digital financing, data analytics, and automated customer engagement. OCAL combines automotive retail expertise with financial technology infrastructure designed to streamline approvals, documentation, and lender connectivity.
- Asset-light model designed for scale. Unlike traditional dealerships that rely on large lots and physical locations, OCAL runs an asset-light, technology-enabled model. Zero standing inventory and no cars on a lot. Digital access to 3,000+ vehicles through OPENLANE, OCAL's exclusive auction and sourcing channel. Revenue comes from financing commissions and related services without holding vehicle inventory or assuming credit risk.
- Expansion strategy across North America. The company has established operations in Western Canada and intends to expand into additional Canadian provinces and selected U.S. markets. The scalability of OCAL's technology platform allows the company to enter new markets without traditional dealership infrastructure requirements.
- Experienced leadership with industry depth. OCAL Financial is led by a management team with extensive experience across automotive retail, automotive auctions, and capital markets. The leadership combines operational knowledge of vehicle distribution with expertise in financing and technology development.
- Large and fragmented market opportunity. The North American automotive market represents one of the largest consumer sectors globally. Despite its scale, the process of purchasing and financing vehicles remains fragmented across thousands of dealerships and lenders. OCAL's platform simplifies this through a unified digital experience.

**Investment highlights** (six items): Asset-light, lender-first model. Technology-driven financing platform. National lender network integration. Scalable digital infrastructure. Experienced leadership in automotive and capital markets. Positioned within a multi-trillion-dollar automotive ecosystem.

**Who is OCAL Financial?** A sit-down with CEO Mehdi Moghareh. [YouTube embed https://www.youtube.com/embed/TrGWP1ECD8I]

**Corporate information**

OCAL Financial Inc. is a Vancouver-based technology-enabled automotive commerce company. The company completed its qualifying transaction by way of a three-cornered amalgamation involving 1301756 B.C. Ltd. (dba OCAL Financial) and 1580785 B.C. Ltd., a wholly-owned subsidiary of the company.

OCAL common shares commenced trading on the TSX Venture Exchange under the symbol OCAL at the opening of markets on July 21, 2026. The company also trades on the Frankfurt Stock Exchange under the symbol JC3. OCAL Financial completed its private placement on July 7, 2026, for gross proceeds of $1,507,375.

The corporate presentation and investor fact sheet are available for download above. For investor enquiries, contact investors@ocal.ca. Public-company information is provided for general information only and is not a guarantee of future performance.

| Field | Value |
|---|---|
| Legal name | OCAL Financial Inc. |
| Head office | Vancouver, British Columbia |
| Trading symbol | TSXV: OCAL / Frankfurt: JC3 |
| CUSIP | 67449X105 |
| ISIN | CA67449X1050 |
| Transfer agent | Endeavor Trust Company |
| Auditors | DMCL LLP |
| Legal counsel | Lawson Lundell LLP |
| Corporate secretary | Terence Lee, CPA |
| Licensing | BC VSA #D50207 / Alberta AMVIC #B2036050 |
| Filing statement | Filed July 9, 2026 (text only, no link) |
| Investor contact | investors@ocal.ca |

Leadership: Mehdi Moghareh, Chief Executive Officer & Director. Matthew Friesen, Chairman & Director. Terence Lee, CFO & Corporate Secretary, CPA. Michael Stier, Director. Robert Birmingham, Director.

**Press releases** (4 per page, 5 pages, newest first; list in 1.4). Then "Related filings & announcements": Ronin, amalgamation agreement (links to ronin-qt-closing.pdf); Ronin, definitive agreement announcement (TheNewswire); Ronin, TSXV conditional acceptance and transaction update (TheNewswire); Qualifying transaction release (same ronin-qt-closing.pdf).

**The OCAL team** (photos, names, titles): Mehdi Moghareh, Chief Executive Officer & Director. Matthew Friesen, Chairman & Director. Terence Lee, CFO & Corporate Secretary, CPA. Michael Stier, Director. Robert Birmingham, Director. Shushu Feng, Investor Relations Manager. (No biographies on the page although the FAQ says they are in the "Management team section".)

**The OCAL investor story** (long-form text, verbatim)

The automotive industry is one of the largest consumer markets in the world. Every year millions of vehicles are purchased, financed, traded, and delivered through a complex ecosystem of dealerships, lenders, auctions, brokers, and logistics providers.

Despite the scale of the market, much of the infrastructure supporting these transactions has changed very little over the past several decades.

Consumers often face a fragmented process when purchasing a vehicle. Financing options can be limited, approvals may take time, and the process of connecting buyers, lenders, and vehicle suppliers frequently involves multiple intermediaries.

At the same time, consumer expectations have changed dramatically. Today's buyers increasingly expect the same level of speed, transparency, and digital convenience in automotive purchasing that they experience in other sectors of the economy.

This shift is beginning to reshape how vehicles are financed and sold.

Across North America, digital platforms are emerging that simplify the process of connecting buyers and sellers. These platforms are beginning to replace traditional models that relied heavily on physical infrastructure and manual processes.

OCAL Financial was founded to participate in this transition.

The company is developing a technology-enabled automotive commerce platform designed to connect consumers, lenders, and vehicle suppliers through a streamlined digital marketplace.

Rather than operating as a traditional dealership, OCAL Financial focuses on the financial and transactional infrastructure that sits at the center of the vehicle purchasing process.

By connecting consumers seeking financing with a network of lenders and vehicle sources, the company aims to simplify the automotive purchasing experience while expanding access to vehicles and financing options.

This approach allows OCAL Financial to operate with a capital-efficient structure while participating in a large and growing market.

As the platform expands and additional lenders, customers, and vehicle suppliers participate, the network effect of the system has the potential to strengthen the value of the platform over time.

Companies that successfully build these types of marketplaces often benefit from significant operating leverage as their platforms grow.

OCAL Financial believes the automotive marketplace is entering a period of transformation as digital infrastructure becomes increasingly important to the way vehicles are financed and distributed.

The company's strategy is to build the technology, partnerships, and distribution channels required to support that transformation.
For investors, the opportunity lies in participating in the early stages of a company working to position itself within one of the largest consumer industries in North America.

[Corporate presentation]

**Contact investor relations.** For investor inquiries, please reach out to our IR team. investors@ocal.ca / 1-604-687-7765

**Investor centre FAQ** (35 questions in four groups; every answer is reproduced in 1.3a below).

**Forward-looking information:** This website may contain forward-looking statements regarding the company's business strategy, expansion plans, and anticipated market opportunities. These statements are based on management's current expectations and are subject to risks and uncertainties that could cause actual results to differ materially.

**Closing banner:** Interested in OCAL Financial? Download our corporate presentation to learn more about the platform, the market and our growth strategy. [Corporate presentation]

Footer (all pages): see section 2.

#### 1.3a Investor centre FAQ, all answers (verbatim, dashes normalised)

**Investor centre: About OCAL**

What is OCAL Financial? OCAL Financial Inc. (TSX Venture Exchange: OCAL; Frankfurt Stock Exchange: JC3) is an asset-light, AI-native virtual automotive dealership and vehicle-finance platform. OCAL is currently licensed in British Columbia and Alberta and operates remotely: a customer applies online, is matched with a lender from OCAL's network, is approved, and only then has a vehicle sourced and delivered to their door. OCAL's common shares trade on the TSX Venture Exchange under the symbol OCAL and on the Frankfurt Stock Exchange under the symbol JC3.

What problem does OCAL solve? The traditional dealership sells the car first and arranges financing second, which is why so many Canadians with imperfect credit leave a lot without a vehicle. OCAL reverses the order. Approval comes first, from a lender chosen to fit the customer's file, and the vehicle is sourced to fit the approval. The customer never visits a lot and never negotiates in a finance office.

How does OCAL make money? OCAL earns revenue from vehicle sales and from related finance and protection products arranged for the customer. OCAL does not lend its own money, does not hold consumer loans and does not assume credit-default risk. Financing is provided by third-party lenders; OCAL arranges it.

Does OCAL hold inventory? No. Zero standing inventory and no cars on a lot. Digital access to 3,000+ vehicles through OPENLANE, OCAL's exclusive auction and sourcing channel. OCAL sources each vehicle only after the customer is approved, drawing on the OPENLANE auction network and select partner dealers. Because no vehicle is bought before it is sold, capital is not tied up in stock and the balance sheet carries no used-vehicle price exposure. The vehicles shown on the Inventory page are network and partner listings that OCAL can source, not OCAL-owned stock.

Where does OCAL operate? OCAL is licensed and delivers in British Columbia and Alberta, with offices in Vancouver and Edmonton. Manitoba and Ontario are the next provinces planned. Selected U.S. states have been identified for later consideration. Any expansion depends on licensing, lender coverage and capital, and there is no assurance as to timing.

What regulatory framework applies? Vehicle sales and dealer conduct are regulated provincially. In British Columbia OCAL is licensed under the Motor Dealer Act and regulated by the Vehicle Sales Authority of British Columbia (VSA #D50207); in Alberta OCAL is licensed under the Consumer Protection Act and regulated by the Alberta Motor Vehicle Industry Council (AMVIC #B2036050). Consumer credit is provided by OCAL's lending partners under their own regulatory regimes. As a reporting issuer, OCAL is subject to Canadian securities law and the policies of the TSX Venture Exchange.

Who are OCAL's customers? Working Canadians who need a vehicle and want financing settled before they shop: first-time buyers, newcomers to Canada without a Canadian credit file, self-employed and gig-economy earners whose income is real but harder to document, people rebuilding after a consumer proposal or bankruptcy, mid- and sub-prime borrowers, and prime borrowers who simply prefer a remote process to a Saturday on a lot.

What does the technology do? OCAL's systems run the transaction end to end. Workflow orchestration moves each file from first contact to funding without anything sitting in an inbox. A lender-routing credit-intelligence system reads the whole application, not only the score, and routes it to the lender most likely to approve. Voice AI, in production since 2025, answers and qualifies inbound leads in seconds, with people stepping in when it matters. A centralized business-intelligence system (CBIS) measures every step. Conversational AI sales agents, built on OCAL's own knowledge base and delivered with SalesCloser's technology, are being added to the front of the funnel.

Does OCAL own its technology? OCAL owns its knowledge base, its workflow and lender-routing logic, its data and its business-intelligence system. Some capabilities, including voice infrastructure and conversational-AI delivery, use third-party technology under commercial agreements. OCAL's agreement with SalesCloser Technologies Ltd. is non-exclusive. OCAL holds no patents and protects its systems through trade secrets, contracts and the data it has accumulated.

Who leads the company? Mehdi Moghareh is Chief Executive Officer and a director. Matthew Friesen is Chairman and a director. Terence Lee, CPA, is Chief Financial Officer and Corporate Secretary. Michael Stier and Robert Birmingham are independent directors; Mr. Stier chairs the Audit Committee. Biographies are in the Management team section and in the Filing Statement.

How does OCAL find customers? Through paid search and social, an owned content program (blog, newsletters and buyer guides), referrals, and lender and dealer partners. A six-month video-first brand campaign with DIBO Marketing was announced in August 2026. Every lead is answered by voice AI within seconds and routed to a specialist.

What is the long-term plan? To become the way Canadians with any credit profile buy and finance a used vehicle: approved first, sourced second, delivered to the door, in every province where OCAL is licensed. Growth is planned province by province, with technology carrying the volume so headcount does not have to.

**Investor centre: Listing and capital markets**

Is OCAL a public company? Yes. OCAL Financial Inc. completed its qualifying transaction with Ronin Ventures Corp. and began trading on the TSX Venture Exchange on July 21, 2026 under the symbol OCAL. OCAL is a Tier 2 issuer. The Filing Statement dated July 9, 2026 is available under OCAL's profile on SEDAR+.

Where can I trade OCAL shares? On the TSX Venture Exchange (TSXV: OCAL) through any Canadian brokerage, and on the Frankfurt Stock Exchange (symbol JC3, WKN A42K21) since August 25, 2026. The ISIN is CA67449X1050 and the CUSIP is 67449X105. Live quotes are on TMX Money and Börse Frankfurt; links are in the Corporate information section.

How many shares are outstanding? As at completion of the qualifying transaction on July 21, 2026, OCAL had 36,667,803 common shares outstanding, approximately 11.0 million common share purchase warrants with exercise prices from $0.10 to $0.50 (including 6,029,500 warrants at $0.50 expiring July 7, 2028), and 600,000 stock options, for approximately 48.3 million shares on a fully diluted basis. Securities held by principals are subject to TSX Venture Exchange escrow and are released on the exchange's schedule.

What did OCAL raise? OCAL closed a concurrent financing on July 7, 2026 for gross proceeds of $1,507,375 through the sale of 6,029,500 units at $0.25, each unit consisting of one common share and one warrant exercisable at $0.50 for 24 months.

When is OCAL's fiscal year end, and when does it report? OCAL's fiscal year ends August 31. As a venture issuer OCAL files audited annual financial statements and MD&A within 120 days of year end, and interim financial statements and MD&A within 60 days of each quarter end. All filings are on SEDAR+ and linked from this page.

Does OCAL pay a dividend? No. OCAL is an early-stage growth company and does not anticipate paying dividends. Any future decision would be made by the board based on the company's financial position and capital needs.

Does OCAL have analyst coverage or a market maker? OCAL has engaged Integral Wealth Securities Limited to provide market-making services on the TSX Venture Exchange. OCAL has engaged Signal Capital Advisors Inc. for investor relations and capital markets advisory, subject to TSX Venture Exchange acceptance. OCAL is not aware of published research coverage at this time.

How can investors receive updates? Press releases are posted on this page the day they are disseminated and filed on SEDAR+. Investors can subscribe to email alerts below, follow OCAL on TMX Money, or contact investor relations at the address in the Contact section.

**Investor centre: Risk and governance**

What are the principal risks? OCAL is an early-stage company with a short operating history as a public issuer. Its results depend on consumer demand for used vehicles, the availability and pricing of credit from its lending partners, access to vehicle supply through auctions and partners, provincial licensing and consumer-protection regulation, competition from dealers, brokers and online platforms, and OCAL's ability to raise capital as it grows. The complete risk factors are set out in the Filing Statement dated July 9, 2026 and in each MD&A on SEDAR+, and investors should read them.

How does OCAL manage inventory and credit risk? By not taking either. Vehicles are sourced only after a customer is approved, so OCAL does not carry stock that can lose value. Loans are made by third-party lenders, so OCAL does not hold consumer receivables or bear default risk. OCAL's exposure is to transaction volume and to the terms its lending partners offer.

How is OCAL governed? OCAL is governed by a board of four directors, two of whom are independent. The Audit Committee is chaired by Michael Stier. OCAL complies with the governance and disclosure requirements of Canadian securities law and the TSX Venture Exchange, including timely disclosure of material changes, insider reporting, and quarterly and annual financial reporting. Governance documents are filed on SEDAR+.

What regulatory oversight applies to the business? Provincial motor-dealer regulators in British Columbia and Alberta license and supervise OCAL's dealer activity. Consumer credit is regulated by federal and provincial law and by the regulators of OCAL's lending partners. Personal information is governed by the Personal Information Protection Act in British Columbia and Alberta and by PIPEDA where it applies. Anti-money-laundering and know-your-customer checks are built into OCAL's transaction workflow.

How does OCAL manage technology and data risk? Customer data is held in access-controlled cloud infrastructure with encryption in transit and at rest, role-based permissions and audit logging. AI systems operate inside OCAL's workflow with human review of credit submissions and contracts. OCAL's Privacy Policy describes what is collected, why, and with whom it is shared.

What are the delivery and operational risks? Vehicle transport is performed by licensed carriers under OCAL's delivery process, and every vehicle is inspected before delivery. Operational risk is managed through dealer-licence compliance, controlled sourcing channels, standardised contracting and the measurement built into OCAL's systems.

How does OCAL address competition? Most competitors do one piece: a lender, a listing site, a broker or a dealer. OCAL runs the whole transaction, from lead to lender to vehicle to driveway, on one system and one dataset, without owning inventory. That combination is hard to copy from inside a dealership or a lending book.

Are there related-party arrangements investors should know about? Related-party transactions, if any, are disclosed in the Filing Statement and in OCAL's financial statements and MD&A on SEDAR+. Consultants and advisors engaged by OCAL, including its investor relations advisor, are arm's length unless disclosed otherwise.

**Investor centre: Technology and platform**

What runs the OCAL platform? Four connected systems: workflow orchestration from first contact to funded deal; a lender-routing credit-intelligence system; voice AI for lead response and qualification; and CBIS, the centralized business-intelligence system that records every step. Together they let a small team move a high volume of files with nothing lost between stages.

Where does AI actually operate today? In production: voice AI that answers and qualifies leads, and the credit-intelligence routing that recommends a lender for each file. In deployment: conversational AI sales agents that hold voice, video and browser conversations in multiple languages, built on OCAL's knowledge base and delivered with SalesCloser's technology. Planned and not yet built: an end-to-end AI sales closer. OCAL describes each stage as it is, and does not present planned capability as current.

Is the platform proprietary? The knowledge base, routing logic, workflow, data and business-intelligence layer are OCAL's own. Delivery components such as voice infrastructure and conversational-AI engines are licensed from third parties under non-exclusive commercial agreements. OCAL holds no patents.

Can the platform scale to new provinces? The platform is not tied to a physical location, so entering a province is primarily a licensing, lender-coverage and delivery-logistics exercise rather than a real-estate one. Manitoba and Ontario are next. Each new market still requires provincial dealer licensing and lender onboarding before OCAL can transact there.

How does financing integrate with the process? The application is the first step, not the last. The credit-intelligence system reads the file and routes it to a lender in OCAL's network; the customer receives an approved budget and terms before any vehicle is discussed; the vehicle is then sourced to fit the approval and the contract is signed digitally.

How does the platform improve the customer experience? One specialist, one file, one place. The customer applies from a phone in about two minutes, knows their real budget before looking at a car, signs without printing anything and takes delivery at home. Every on-time payment is reported to the credit bureaus by the lender, so the loan rebuilds credit while the customer drives.

What is the long-term technology vision? A transaction that runs from first contact to delivered vehicle with AI carrying the routine work and people handling judgment, in every province OCAL serves. That is a direction, not a product; OCAL will announce capabilities when they are in production.

### 1.4 Press releases and letters listed on the investor page

Source: https://ocalfinancial.ca/investor-relations (pagination 1 to 5). The page shows the headline without the "OCAL Financial" prefix. "List date" is what the investor page shows; "Release page date" is the date printed on the release's own page; "Wire date" is the Newsfile time stamp (ET).

| Page | List date | Headline as listed | Release page date | Wire date (ET) | Page URL |
|---|---|---|---|---|---|
| 1 | Oct 13, 2026 | Outlines Its Integrated AI Demand Engine | Oct 13 | Oct 13, 8:54 AM | /investor-relations/press-release/ocal-integrated-ai-demand-engine-october-2026 |
| 1 | Oct 6, 2026 | Surpasses 1,250 Funded Vehicle Deals | Oct 6 | Oct 6, 9:42 AM | /ocal-1250-funded-vehicle-deals-october-2026 |
| 1 | Oct 1, 2026 | to Present at the 2026 Cantech Investment Conference in Toronto | Oct 1 | Oct 1, 9:10 AM | /ocal-cantech-investment-conference-october-2026 |
| 1 | Sep 29, 2026 | Offers a Digital Inventory of 3,000+ Vehicles via OPENLANE, With Zero Standing Inventory | Sep 29 | Sep 29, 7:30 AM | /ocal-openlane-digital-inventory-september-2026 |
| 2 | Sep 22, 2026 | Explains Its Proprietary Knowledge Base, the Data Asset Behind Its AI | Sep 22 | Sep 22, 8:49 AM (first issued Sep 15, 8:13 AM) | /ocal-proprietary-knowledge-base-september-2026 |
| 2 | Sep 8, 2026 | Appoints Ryan McDonald as Vice President of Sales | Sep 8 | Sep 8, 9:08 AM | /ocal-ryan-mcdonald-vp-sales-september-2026 |
| 2 | Aug 29, 2026 | Launches Video-First Brand Campaign With DIBO Marketing and Engages Signal Capital for Investor Relations | Aug 29 | Aug 29, 10:42 AM (a Saturday) | /ocal-dibo-campaign-signal-capital-august-2026 |
| 2 | Aug 25, 2026 | Common Shares Now Trading on the Frankfurt Stock Exchange | Aug 25 | Aug 25, 8:15 AM | /ocal-frankfurt-stock-exchange-listing-august-2026 |
| 3 | Aug 18, 2026 | Describes CBIS, the System That Runs Its Operations and Data | Aug 18 | Aug 18, 8:15 AM | /ocal-cbis-august-2026 |
| 3 | Aug 11, 2026 | Adds AI Sales-Agent Technology Built Around Its Proprietary Knowledge Base | Aug 11 (wrong; this is the corrected release) | Aug 14, 8:57 AM ("CORRECTION FROM SOURCE") | /ocal-salescloser-ai-technology-august-2026 |
| 3 | Aug 11, 2026 | Explains Its Credit and Lender-Routing System, and the Underserved Market It Serves | Aug 11 | Aug 11, 8:15 AM | /ocal-credit-intelligence-august-2026 |
| 3 | Aug 6, 2026 | Describes the Voice AI Behind Its Lead Engagement and Provides Business Update | Aug 6 | Aug 6, 8:30 AM | /ocal-voice-ai-august-2026 |
| 4 | Aug 4, 2026 | Explains How Its Integrated Model Differs From Online Auto Retailers, Brokers and Fintech Lenders | Aug 4 | Aug 4, 8:30 AM | /ocal-competitive-positioning-august-2026 |
| 4 | Jul 29, 2026 | Outlines How Its Virtual, Finance-First Model Differs From the Traditional Dealership | Jul 30 | Jul 30, 8:30 AM | /ocal-vs-traditional-dealership-july-2026 |
| 4 | Jul 28, 2026 | Details Its End-to-End Digital Vehicle-Financing Process | Jul 28 | Jul 28, 8:30 AM | /ocal-end-to-end-process-july-2026 |
| 4 | Jul 22, 2026 | Provides Corporate Overview Following TSX Venture Exchange Listing | Jul 23 | Jul 23, 8:30 AM | /ocal-corporate-overview-july-2026 |
| 5 | Mar 18, 2026 | Letter to Investors - CEO (Mehdi Moghareh) | Mar 18 | none (site only) | /investor-relations/press-release/press-release-ceo |
| 5 | Mar 18, 2026 | Letter to Investors - Director (Matthew Friesen) | Mar 18 | none (site only) | /investor-relations/press-release/press-release-director |

Observations: two list dates are one day off the release page and wire (Jul 22 vs Jul 23, Jul 29 vs Jul 30); the corrected SalesCloser release is listed and dated 11 Aug but went out 14 Aug; the original 13 Aug "exclusive agreement" release is not listed. The two March letters pre-date the 26 Mar definitive agreement and describe OCAL as a "technology-enabled brokerage platform" (Mehdi) and say OCAL's "focus on technology and brokerage services" (Matthew). They have no wire release and are signed "Matthew Friesen, Director".

### 1.5 Downloads offered

| Item | URL | Notes |
|---|---|---|
| Corporate presentation (PDF, "Investor Presentation September 2026") | https://ocalfinancial.ca/__l5e/assets-v1/61be8bc3-94a2-417f-a28b-33d0c914f060/OCAL_Investor_Presentation_September_2026.pdf | Linked three times on the page. Read in full (no local download made; read through a fetch tool). Contents in 1.6b. |
| Investor fact sheet (PDF, "August 2026") | https://ocalfinancial.ca/__l5e/assets-v1/a48af621-4490-4dbe-9009-ef020c436e72/OCAL_Investor_Fact_Sheet_August_2026.pdf | Dated August 2026 but lists September and October 2026 milestones. |
| Ronin / QT closing release (PDF) | https://ocalfinancial.ca/__l5e/assets-v1/73a49d08-a734-40f0-86a5-e74dca99fbc8/ronin-qt-closing.pdf | Dated 16 Jul 2026. Linked as "Ronin, amalgamation agreement" and "Qualifying transaction release" (the first label does not describe the file). Its footer still carries the pre-closing cautionary note and "TSXV: RVC.P". |
| Ronin definitive agreement release (TheNewswire) | https://www.thenewswire.com/press-releases/1AXXF32MW-ronin-ventures-corp-announces-definitive-agreement-with-1301756-b-c-ltd-dba-ocal-financial-for-proposed-qualifying-transaction.html | 26 Mar 2026 |
| Ronin conditional acceptance release (TheNewswire) | https://www.thenewswire.com/press-releases/1kEjFqlRQ-ronin-ventures-corp-announces-conditional-acceptance-by-the-tsx-v-of-previously-announced-qualifying-transaction-with-1301756-b-c-ltd-dba-ocal-financial-and-transaction-update.html | 2 Jul 2026 |

No other documents: no annual report, financial statements, MD&A, filing statement, AIF, circular, governance charters, policies, or presentations archive.

### 1.6 Every claim and number on the investor page

#### 1.6a Page text (rendered)

| Claim | Where | Check against the record |
|---|---|---|
| TSXV: OCAL; Frankfurt: JC3; trading from QT completed July 2026 | hero, corporate info | Confirmed (releases, TMX, Boerse Frankfurt). |
| Trading began July 21, 2026 at the open | corporate info | Confirmed (21 Jul release; TSXV bulletin dated 17 Jul 2026 for the name change). |
| Private placement completed July 7, 2026, gross proceeds $1,507,375 | corporate info | Confirmed (material change report, 22 Jul 2026; 16 Jul closing release). Funds were held in escrow until closing on 15 Jul. |
| 36,667,803 shares; about 11.0M warrants ($0.10 to $0.50); 600,000 options; about 48.3M fully diluted | FAQ | Confirmed as at 21 Jul 2026 (material change report). Not updated since. 36,667,803 + 11,029,501 + 39,760 + 600,000 = 48,337,064. |
| 6,029,500 warrants at $0.50 expiring July 7, 2028 | FAQ | Matches the material change report (24 months from closing 7 Jul 2026). |
| Concurrent financing: 6,029,500 units at $0.25 | FAQ | Confirmed. |
| Frankfurt JC3, WKN A42K21 since August 25, 2026 | FAQ | Confirmed (25 Aug release; Boerse Frankfurt page). |
| CUSIP 67449X105; ISIN CA67449X1050 | corporate info | Confirmed (material change report). |
| Transfer agent "Endeavor Trust Company" | corporate info | Material change report uses the same name; TSX Infoventure and the interim statements say "Endeavor Trust Corporation". Verify the legal name. |
| Auditors DMCL LLP; counsel Lawson Lundell LLP | corporate info | UNVERIFIED (not seen in a SEDAR+ document). TSX Infoventure still lists Crowe MacKay LLP (Ronin's auditor), see section 9. |
| Licensing VSA #D50207; AMVIC #B2036050 | corporate info, footer | Numbers match the footer disclaimer on every page. Registry check not done here. |
| Filing statement filed July 9, 2026 | corporate info | Confirmed (Stockwatch, 11 Jul 2026). No link on the page. |
| Tier 2 issuer | FAQ | Confirmed; material change report says "Tier 2 Technology issuer". |
| Zero standing inventory; digital access to 3,000+ vehicles through OPENLANE, "OCAL's exclusive auction and sourcing channel" | hero, FAQ | "Exclusive" appears in the 13 Oct and 22 Oct releases too. Deck says OPENLANE and "other partners"; 1 Oct Cantech Letter release says "OPENLANE auction network and five auction supply channels". Wording differs across public documents. |
| Revenue from "financing commissions and related services" | Why invest | Conflicts with the FAQ ("vehicle sales and related finance and protection products") and the financial statements. |
| Licensed BC and Alberta; offices Vancouver and Edmonton; Manitoba and Ontario next; selected U.S. states later | FAQ | Offices and licences match releases. Site home page names Washington, Arizona and Nevada. No release on Manitoba or Ontario licence status. |
| Board of four, two independent; Audit Committee chaired by Michael Stier | FAQ | Confirmed (material change report). The release does not name which two are independent; site says Stier and Birmingham. |
| Dividend: none | FAQ | Consistent with TMX (no dividend). |
| Integral Wealth Securities market maker; Signal Capital IR, subject to TSXV acceptance | FAQ | Confirmed (6 Aug and 29 Aug releases). Acceptance not reported. |
| FY end Aug 31; AFS and MD&A within 120 days; interims within 60 days | FAQ | OSC filing calendar for Aug 31 year end, venture: annual Dec 29, 2026; Q1 (Nov 30) Jan 29, 2027. The 31 Jul filings include a form titled "becoming non-venture issuer" (see 4), so the 120/60 day statement should be checked. |
| Voice AI in production since 2025; SalesCloser agents "in deployment"; non-exclusive | FAQ | Matches 13 Oct release ("in final testing"). |
| No patents; trade secrets | FAQ | UNVERIFIED. |
| "Press releases ... filed on SEDAR+"; "subscribe to email alerts below" | FAQ | No subscribe control found in the rendered page. |
| "All filings are on SEDAR+ and linked from this page" | FAQ | No SEDAR+ link on the page. |
| "Biographies are in the Management team section" | FAQ | Section has names and titles only. |
| Management: Mehdi Moghareh CEO and Director; Matthew Friesen Chairman and Director; Terence Lee CFO and Corporate Secretary; Michael Stier, Robert Birmingham Directors; Shushu Feng "Investor Relations Manager" | team section | Feng is described in the 29 Aug release as owner of Signal Capital Advisors Inc., an arm's length consultant. |
| Investor phone 1-604-687-7765; investors@ocal.ca | contact | Matches Oct releases; Jul to Sep releases list general@ocal.ca. |
| Embedded video "Who is OCAL Financial?" | video | Content is pre-listing and stale, see section 10. |

#### 1.6b Corporate presentation PDF ("Investor Presentation September 2026"): claims and numbers

- Cover: "Canada's AI-native virtual car dealership", TSXV: OCAL.
- Legal disclaimer cites "filing statement dated July 9, 2025" (typo; should be 2026).
- Headline: $6.88M FY25 revenue; 1,250+ funded deals; $5.5K to $8K gross profit per funded deal; "Zero standing inventory and consumer loans"; 17.64% repeat and referral share; blended CAC from $1,027 to $250; Manitoba and Ontario licensing.
- Market: Canadian used-car sales $17.71B (2025) to $24.54B (2030E), 6.74% CAGR; more than 70% prefer digital or fully online financing; fewer than 20% of dealerships offer fully remote financing; Ontario 38% of national automotive transactions.
- Process: six steps; revenue per funded deal $5.5K to $8K.
- OPENLANE slide: "Canada's largest digital wholesale marketplace for used vehicles"; "OPENLANE access is available to licensed dealers".
- Technology: SalesCloser AI "Full implementation October 2026"; CBIS; owned demand engine via "CAE & EasyPear" ("Canada Auto Experts (CAE) acquisition", and elsewhere "Canoply Auto Reports (CAR)").
- Traction: 98% protection attach; 6 days average lead to signed; 3 to 4 days signed to funded; 14% higher approval-to-fund rate from credit intelligence.
- Roadmap: Now BC and Alberta; Sep 2026 Manitoba (licence underway); Dec 2026 to Jan 2027 Ontario launch; 2027 to 2028 Quebec and Canada; 2028 to 2029 United States via Washington State.
- Financial table: FY23 revenue $5,313,921; FY24 $5,838,498; FY25 $6,879,835; gross margin $397,125 / $598,015 / $781,383; EBITDA $(272,058) / $(268,160) / $(111,312); FY26E to FY29E management estimates (chart: 7.2, 14.4, 23.0, 34.6 CAD millions).
- Management: Matthew Friesen "co-founder, chairman and director", "grew a global manufacturing company from $4.5M to $25M", "CEO and Director of a Nasdaq-listed issuer", "28-year auction legacy", "15-company investor" (text also says "25+ public and private companies"). Mehdi Moghareh "co-founder and CEO", "8-institution lender network". Terence Lee CFO. Hasneen Jalil CTO.
- Capital structure (as of 21 Jul 2026): 36.7M shares; founder ownership 54.33%; warrants 11.0M; options 0.6M; fully diluted about 48.3M; "over 50% ownership and 36 months escrow".
- Closing page placeholder: "Contact information: add an address".

#### 1.6c Investor fact sheet PDF ("August 2026"): claims and numbers

- "Canada's AI-native, asset-light virtual automotive dealership and vehicle-finance platform"; "Licensed in British Columbia and Alberta, with Manitoba and Ontario licences underway, a Manitoba licence enables Ontario sales to begin."
- Key stats: $6.88M FY25 revenue (YE Aug 31); 1,250+ funded deals; $5.5K to $8K gross profit per funded deal; 6 days average lead to signed; 98% warranty/protection attach; blended CAC about $250 post-CAE (was $1,027).
- Revenue trajectory chart FY23 5.31, FY24 5.84, FY25 6.88, FY26E 7.20, FY27E 14.40, FY28E 23.00, FY29E 34.60 (CAD millions, FY26E to FY29E "management estimates (unaudited)").
- 2026 milestones: Jul to Aug listed; Aug SalesCloser AI contracted, DIBO signed; Sep "CAE & EasyPear acquisition completes", Hasneen Jalil appointed CTO; Sep Manitoba licence underway; Oct "OPENLANE buying expansion into Manitoba & Saskatchewan; SalesCloser agents live on OCAL's proprietary knowledge base"; Dec 2026 to Jan 2027 Ontario launch.
- Capital structure: concurrent financing $1.5M at $0.25 per unit closed; 36,667,803 shares; warrants about 11.0M ($0.10 to $0.50); options 600,000; fully diluted about 48.3M; "Excludes securities issuable under subsequently announced transactions".
- Leadership list includes Hasneen Jalil, CTO, and Shushu Feng, Investor Relations Manager. Investor contact lists Shushu Feng, Matthew Friesen, Mehdi Moghareh, investors@ocal.ca.
- UNVERIFIED public support: CAE/EasyPear acquisition and CTO appointment, Manitoba licence, OPENLANE expansion, "SalesCloser agents live" (13 Oct release says "in final testing"), 17.64% (release says about 17.6%), 6 days (releases say about seven days median).

### 1.7 What a normal public-company investor page has that this one lacks

| Normal item | OCAL page today |
|---|---|
| Latest financial statements (audited FY, interims) and MD&A, with SEDAR+ link | None. FAQ says filings are "linked from this page"; no link. |
| Filing statement (the listing document) | Named only. |
| Stock quote (delayed price, volume, 52-week range, chart) | None embedded. Two outbound links (TradingView, TMX Money). |
| Share structure table (outstanding, options, warrants, escrow, insider holdings, fully diluted) | One FAQ paragraph, frozen at 21 Jul 2026. No escrow detail, no insider holdings. |
| Email alerts / subscribe, RSS | None, although the FAQ promises "email alerts below". |
| News archive complete and dated | 16 of 22 post-listing releases (see section 5); dates off by a day on two; no Showroom release. |
| Governance: board and committee charters, code of conduct, disclosure, insider trading, whistleblower policies, committee membership | None. FAQ only says Audit chair is Stier. |
| Director and officer biographies | None (titles only). |
| Events and presentations calendar; AGM date and notice | None. (Simply Wall St shows an AGM on Dec 10, 2026; no OCAL source found, UNVERIFIED.) |
| Analyst coverage list | None; FAQ says none known. |
| Financial calendar (next reporting dates) | FAQ rule only. |
| Disclaimer / forward-looking information notice at top | Short notice at bottom. |
| Investor contact | Present (investors@ocal.ca, 1-604-687-7765). |
| Fact sheet and presentation | Present, with the inconsistencies in 1.6. |
| Insider reporting (SEDI) links, early warning reports | None. |
| Operating metrics with definitions | Only inside releases. |
| Machine-readable markup (Organization with tickerSymbol, NewsArticle, FAQPage) | Generic FinancialService only. |

### 1.8 Other issues on or near the page (record only)

- Meta description and title do not mention TSXV, OCAL ticker, or "investor". The page's own wording "AI-driven digital automotive dealership platform" differs from the footer line "Used-car financing for Canadians of every credit profile".
- FAQ says OCAL's "exclusive" OPENLANE channel and "select partner dealers"; "five auction supply channels" appears only in the 1 Oct Cantech Letter release.
- FAQ risk text refers to "each MD&A on SEDAR+" but no MD&A is linked.
- The embedded CEO video "Who is OCAL Financial?" (YouTube TrGWP1ECD8I) was recorded before listing: "originally known as One Click Auto Loans", "partnered up with Adessa Canada", "we are looking to expand in cosmetic financing in dental financing", "hopefully within the next 12 months we would like to be traded publicly".
- A second video (YouTube NkXi9qRAMf0, "How Ocal Financial Is Reinventing Car Buying in Canada") is embedded elsewhere on the site; transcript says OCAL was founded "roughly around 5 years ago", partner "Open Link Canada" (auto-transcript of OPENLANE).
- Home page and About page show testimonials and counters (10+ years, 21 specialists, 5k+ cars sold, 4.5 from 154 Google reviews) that conflict with the listing documents (see section 13).

### 1.9 What non-JavaScript crawlers see (raw HTML from the server)

Fetched with curl on 23 Oct 2026. The `<title>`, description, canonical and JSON-LD are present. The body is a hidden "prerendered crawler fallback" of four short paragraphs:

> Investor relations. OCAL Financial is building an AI-driven digital automotive dealership platform. Learn about our investment opportunity, technology platform, and growth strategy. OCAL Financial is building an AI driven digital automotive retail and finance platform for the Canadian market, combining online origination, a lender network and direct to door vehicle delivery. The opportunity: Canadian used vehicle retail remains largely offline and fragmented. Financing is where the margin sits, and non prime borrowers are underserved by incumbent banks. OCAL addresses both by originating online and matching applicants to lenders programmatically. The platform: An in house CRM handles lead capture, application processing, credit workflow, lender submission and delivery logistics, with automation and AI assistance across intake, document review and customer messaging. Market: Initial operations cover British Columbia and Alberta, with a model designed to extend to other provinces. Press releases and corporate announcements are published on this site.

This fallback has no ticker, no TSXV, no Frankfurt, no numbers, no release list, no downloads, no management, no FAQ. Tools that do not run JavaScript (the WebFetch tool, curl, some AI crawlers and link previews) see only this. The About, Team, Contact, FAQ and Home pages have equally thin or different fallbacks (the Home fallback calls OCAL a company that "arranges used vehicle financing"; there is no investor language). 

---

## 2. Main site: nav, footer, licence lines, phones, addresses, self-description

Sources: https://ocalfinancial.ca/, /about, /team, /contact, /faqs, /llms.txt (rendered pages read 23 Oct 2026).

**Nav (header):** Financing, Inventory, Sell Your Car, About Us, Contact Us, Resources, Investor Relations, Sign In; "Get approved" button.

**Footer (every page):**
- Tagline: "Used-car financing for Canadians of every credit profile. Approved first, vehicle second, delivered to your door."
- Phones: 1-877-495-2012 toll free; 1-604-687-7765 local; Alberta 587-570-8452; Manitoba 431-441-7800; Ontario 289-201-6208. Email general@ocal.ca.
- Address: Suite 500, 885 Dunsmuir Street, Vancouver, BC V6C 1N5 ("Directions" opens Google Maps). Contact page also lists: "500 - 885 Dunsmuir Street, Vancouver BC, V6C 1N5"; hours Mon to Fri 7:30am to 6:00pm Pacific, Sat 9:00am to 5:00pm Pacific; "We respond within 24 hours". Offices per FAQ: Vancouver and Edmonton (no Edmonton address on the site).
- Columns: Financing (Get approved, Bad credit financing, Payment calculator, Loan rates, Sell your car, Inventory); Company (About OCAL, Our team, FAQs, Become a partner, Careers, Investor relations, Contact); Serving (British Columbia, Vancouver, Surrey, Alberta, Calgary, Edmonton, Used truck financing (Alberta), All service areas); Insight (Blog and tips, Newsletters).
- Copyright line: "(c) 2026 OCAL Financial Inc. / TSXV: OCAL"; links Privacy, Terms, Sitemap, Contact.
- Legal disclaimer (verbatim): "OCAL Financial Inc. arranges vehicle financing through a network of third-party lenders. OCAL does not underwrite loans, hold consumer loans, or assume credit-default risk. Pre-qualification uses a soft credit inquiry that does not affect your credit score; a hard inquiry is made only with your consent once you proceed with a specific vehicle. Approval, rate and term are set by the lender and depend on creditworthiness, income and the vehicle financed. Payment figures shown are illustrative estimates, not offers of credit. OCAL Financial Inc., licensed motor dealer, VSA #D50207 (British Columbia). AMVIC-licensed business, AMVIC #B2036050 (Alberta). Services are not offered in provinces where OCAL is not licensed. Financing OAC. Nothing on this page is an offer to sell or a solicitation to buy securities."
- Note: the footer lists Manitoba (431-441-7800) and Ontario (289-201-6208) phone numbers while the disclaimer says services are not offered in unlicensed provinces.

**Home page (title tag):** `Used Car Financing in BC & Alberta | OCAL Financial`. Meta description: "Apply online in about two minutes. We match you with a lender from our network and deliver your vehicle to your door. Checking your options does not affect your credit score." No canonical tag on the home page (all other pages have one). Rendered content: hero "Approved first." with ticker strip "TSXV: OCAL / APPROVAL FIRST / VEHICLE SECOND / DELIVERED TO YOUR DOOR / LICENSED IN BC & ALBERTA / MANITOBA AND ONTARIO NEXT"; "Car buying, backwards. On purpose."; "Everyone else finds the car first, then hopes for financing. We start with your approval. Then the car finds you."; six steps (Apply, Match, Approve, Source, Sign, Drive); "About seven days from hello to signed"; "Been told no before? We built this for you. Gig workers, Self-employed, New to Canada, Thin credit files"; counters "days Apply to signed", "days Signed to funded", "provinces Licensed today. Manitoba and Ontario next", "inventory No stock held. No credit risk" with the note "Cycle-time figures are unaudited internal operating metrics disclosed by OCAL Financial Inc. in 2026."; "One system, start to finish. Most companies do one piece. We run all four: financing, sourcing, delivery, and the technology in between."; a public-company block ("TSXV: OCAL / Light on assets. Heavy on technology. / OCAL Financial Inc. trades on the TSX Venture Exchange following completion of its qualifying transaction in July 2026. / Nothing held. No inventory, no loans, no credit risk. / Everything connected. Four businesses, one system. / AI-native. Scale without headcount. / Growing. BC and Alberta today. Manitoba and Ontario next. / Offices in Vancouver and Edmonton, with Washington, Arizona and Nevada identified for later consideration."); leadership list (Friesen Chairman & Director, Moghareh CEO & Director, Lee CFO & Corporate Secretary CPA, Stier Director, Birmingham Director); "36,667,803 common shares outstanding following the qualifying transaction completed in July 2026. Securities held by principals are subject to exchange-mandated escrow. Continuous disclosure is filed on SEDAR+."; Investor centre button; three testimonials (K. Larsen, M. Rodriguez, D. Jenkins); FAQ teaser; "Start with your yes."

**About (title tag):** `About OCAL Financial | Used Car Financing in BC and Alberta` (rendered H1 "Financing made simple."). Meta: "Learn how OCAL Financial arranges used vehicle financing for Canadians, including drivers with bad credit or no credit history." Rendered text: "Getting financed should feel straightforward, not stressful. That is the whole point of OCAL Financial. We are licensed in British Columbia and Alberta. We work with a network of Canadian lenders rather than a single bank. That is what lets us place files a single lender would decline, and talk honestly about rate and term before you commit." Three points (your approval comes first; one specialist, one file; the car comes to you). Stat strip: "10+ Years in business", "21 Specialists", "5k+ Cars sold", "4.5 from 154 Google reviews". "Bad credit, or no credit" four-step rebuild. Public-company block: "A public company, built light. OCAL Financial Inc. trades on the TSX Venture Exchange following completion of its qualifying transaction in July 2026. We hold no inventory and no loans, so capital is never tied up in stock. Offices. Vancouver and Edmonton. Licensed in British Columbia and Alberta today. Manitoba and Ontario next. Disclosure. Filed on SEDAR+." Same shares-outstanding line as home.
Raw HTML fallback for /about (different text): "OCAL Financial is a Canadian automotive finance company arranging used vehicle loans for drivers in British Columbia and Alberta ... We are the layer between the buyer and the lender."

**Team (title tag):** `Meet Our Team | OCAL Financial`. Rendered: "The people behind your approval. 21 specialists across financing, operations and sales."
- Leadership: Mehdi Moghareh CEO; Matthew Friesen Chairman & Director; Terence Lee CFO & Corporate Secretary, CPA; Alex Friesen Controller; Shushu Feng Investor Relations Manager.
- Management Team: Allison Peters Director of Finance; Nik Friesen Automotive Acquisition; James Green Sales Director; Ryan McDonald VP of Sales; Michael Pham Sales Director; Sasha Ruban Sales Director.
- Marketing & Technology: Hasneen Jalil Chief Technology Officer; Denis Cicak Social Media Director.
- Sales Team: Abigail King, Andy Espinoza Rivas, Jeremie Leger, Max McMahon, TK Choto, Carter George (Account Managers).
- The team page does not list Michael Stier or Robert Birmingham (they appear on the IR page).

**Contact (title tag):** `Contact OCAL Financial | Get in Touch`. Phones as above; email general@ocal.ca; hours above.

**FAQs (title tag):** `Car Loan & Financing FAQs Canada | OCAL Financial` (consumer FAQs only).

**Other:** Newsletters page (title "OCAL Newsletters | Automotive Market Insights for Canada and the U.S."): OCAL Signal (monthly, 15th), OCAL Market Monitor (monthly, 15th), OCAL Smart Buy (quarterly); issues Jul to Sep 2026 posted. OCAL Signal bylines name "Matthew Friesen, Chairman, OCAL Financial Inc."

**llms.txt (own site, stale):** "OCAL Financial, operating as One Click Auto Loan, is a Canadian used-car dealership and auto finance broker headquartered in Vancouver, British Columbia ... We work with a network of nine lending partners ... We do not offer personal loans, healthcare financing, powersports financing, RV financing or auto repair financing." (Source: https://ocalfinancial.ca/llms.txt.) Flag: "broker", "One Click Auto Loan", "nine lending partners" conflict with the listed-company language.

---

## 3. TMX Money

Source: https://money.tmx.com/en/quote/OCAL (read in browser 23 Oct 2026, data stamped "Oct 23, 2026, 12:44 PM ET", source QuoteMedia). Also /quote/OCAL/key-data, /quote/OCAL/news, /quote/OCAL/company (insider activity).

| Item | Value |
|---|---|
| Name, exchange, sector, industry | OCAL Financial Inc.; TSXV; Sector Finance; Industry Credit Finance |
| Price | $0.11, change 0.00 (0.00%) |
| Last trade | Oct 20, 2026, 9:46 AM ET, size 2,000 |
| Volume | 2 (consolidated 2; day volume shown as 2.00) |
| NBBO bid / ask | $0.105 / $0.11; sizes 3,500 / 3,000 |
| Prev. close | 0.11 |
| 52-week high / low | 0.55 / 0.08 |
| Market cap | 4,033,459 (both fields) |
| Issued and outstanding listed shares | 36,667,803 (total shares all classes the same) |
| Escrow shares | 23,638,104 (about 64.5% of outstanding) |
| EPS (TTM) | -0.11; P/B 31.57; Beta 6.87; Alpha -0.073 |
| Moving averages | 21-day 0.109; 50-day 0.109; 200-day 0.123 |
| Average volume | 10-day 17,504; 20-day 19,114; 30-day 16,769; 50-day 18,688 |
| Short interest (as of Oct 22, 2026) | 0.02% of float; 0.02 days to cover |
| Dividend | none |
| Upcoming events | "No events" (no earnings date, no AGM) |
| Insider activity (company tab) | "No Data Available" in the last 3, 6 and 12 months |
| Listing date | Not shown on TMX Money. From the record: trading began Jul 21, 2026 (release), TSXV name-change bulletin dated Jul 17, 2026 (TSX Infoventure). |
| Company description | None shown on the overview or company tabs. |
| TMX news tab | 10 most recent: Oct 22 (Showroom), Oct 13, Oct 6, Oct 1 9:10, Oct 1 7:00, Sep 29, Sep 22, Sep 15, Sep 8, Sep 3. |

Price history context (Wealth Awesome, https://wealthawesome.com/stocks/ocal-v, updated 2026-10-20): 10/20 close 0.11 on 5,049 shares; 10/13 close 0.10 on 159,000; 10/7 close 0.14 on 44,950; 10/2 range 0.08 to 0.15 on 153,784. TradingView (https://www.tradingview.com/symbols/TSXV-OCAL/) shows all-time high 0.55 on Jul 21, 2026 and all-time low 0.09 on Aug 19, 2026. Stockwatch quote page (https://www.stockwatch.com/Quote/Detail?C:OCAL, 23 Oct 2026): last trade Oct 20 at 0.11, bid 0.105 x 3.5K, ask 0.11 x 3.0K, year high-low 0.55 / 0.08.

Classification mismatch: TMX shows Finance / Credit Finance; the company told the market it is a Tier 2 Technology issuer (material change report); TSX Infoventure lists business type "All Other Professional, Scientific and Technical Services".

---

## 4. SEDAR+ profile: what I could verify

SEDAR+ could not be fetched. The list below uses mirrored SEDAR+ copies and feeds. "Dates" for Futubull items are Hong Kong time, so they are about 12 hours ahead of ET; I list the underlying document dates where the document itself states them.

**Issuer profile name(s):** OCAL Financial Inc. (formerly Ronin Ventures Corp., TSXV: RVC.P). The acquired private company filed as 1301756 B.C. Ltd. (dba OCAL Financial).

| Date | Type | What | Source |
|---|---|---|---|
| 18 Jun 2026 | Annual MD&A (Ronin, FY ended 28 Feb 2026) | Ronin Ventures Corp. MD&A for fourth quarter ended Feb 28, 2026 (proposed QT description). Earnings results note on MarketScreener (17 Jun): net loss C$54,747. | https://newsfile.futunn.com/public/NN-PersistNoticeAttachment/7781/20260618/SEDAR_PLUS/CSA_SEDAR_PLUS_NOTICE_RECORD_ID_2436646.pdf ; https://ca.marketscreener.com/news/ronin-ventures-corp-reports-earnings-results-for-the-full-year-ended-february-28-2026-ce7f5cdddb8af120 |
| 9 Jul 2026 | Filing statement (TSXV QT) | Filing statement dated July 9, 2026, filed on Ronin's SEDAR+ profile (Stockwatch confirms filing, 11 Jul). NOT READ. It holds the audited FY2025 financial statements, risk factors, bios, principals, escrow. | https://www.stockwatch.com/News/Item/Z-C!RVC-3840417/C/RVC |
| 10 Jul 2026 | News release (Ronin) | Announces filing of the filing statement and projected closing. | Stockwatch link above |
| 16 Jul 2026 | News release (Ronin) | "OCAL announces closing of qualifying transaction and anticipated trading date" (the PDF on the IR page, titled "Closing of Subscription Receipt Financing (Tranche 3)" in its metadata). | https://ocalfinancial.ca/__l5e/assets-v1/73a49d08-a734-40f0-86a5-e74dca99fbc8/ronin-qt-closing.pdf |
| 17 Jul 2026 | TSXV bulletin | Name change (OCAL Financial Inc. from 21 Jul 2026). | http://infoventure.tsx.com/TSXVenture/TSXVentureHttpController?GetPage=CompanySummary&PO_ID=1186510 |
| 22 Jul 2026 (filed 22 to 23 Jul) | Material change report (Form 51-102F3) | Date of change 15 Jul 2026: completion of QT, name change, board and officers, concurrent financing, 36,667,803 shares, 11,029,501 warrants, 39,760 broker warrants, 600,000 options, Tier 2 Technology issuer. Executive officer named: Matthew Friesen. | https://newsfile.futunn.com/public/NN-PersistNoticeAttachment/7781/20260723/SEDAR_PLUS/CSA_SEDAR_PLUS_NOTICE_RECORD_ID_2459508.pdf |
| 23 Jul 2026 | "Notice" | Listed in Futubull feed (content not read). | https://www.futunn.com/en/stock/OCAL-CA/announcement |
| 25 Jul 2026 (feed) | Certificate and articles of change of name | Listed in feed (content not read). | same |
| 28 Jul and 30 Jul 2026 | News releases | Process release; "virtual, finance-first model" release. | same |
| 31 Jul 2026 | Interim financial statements (unaudited, no auditor review) | 1301756 B.C. Ltd. (dba OCAL Financial), three and nine months ended 31 May 2026; approved by the board 30 Jul 2026 and signed by Matthew Friesen and Mehdi Moghareh. Key figures in 4.1. | https://newsfile.futunn.com/public/NN-PersistNoticeAttachment/7781/20260731/SEDAR_PLUS/CSA_SEDAR_PLUS_NOTICE_RECORD_ID_2467001.pdf |
| 31 Jul 2026 | Interim MD&A | Listed in feed (content not read). | Futubull feed |
| 31 Jul 2026 | Form 52-109F2 (IPO/RTO) certificates, CEO and CFO | Listed in the feed as "52109F2IPORTO IPORTO BECOMING NONVENTURE ISSUER" for CEO and for CFO. Label as shown; meaning not confirmed. | Futubull feed |
| 31 Jul to 1 Aug 2026 (feed stamp Aug 1) | "Financial statements of RTO acquirer" | Probably the audited annual financial statements of 1301756 B.C. Ltd. for FY ended Aug 31, 2025 and related statements. Content NOT read, so the audit report, auditor name and FY2025 audited figures are UNVERIFIED from SEDAR+ itself. | Futubull feed |
| 4 Aug to 18 Aug 2026 | News releases | Aug 4, Aug 6, Aug 11, Aug 14 (two), Aug 18 and later, as in section 5. | Futubull feed |

Not found in any public source: early warning reports, take-over bid circulars, prospectuses, an AIF, a business acquisition report, an annual MD&A for FY2025 under OCAL's name, filings of the CAE/EasyPear acquisition, or a report of exempt distribution for the IR options. SEDI (insider) shows opening-balance reports on 15 Jul 2026 for Matthew Friesen and Mehdi Moghareh as 10% holders and an indirect report for Terence Lee on 21 Jul 2026 (Yahoo Finance insider pages). Next required filings by OSC calendar for an Aug 31 year end, venture issuer: annual statements and MD&A by 29 Dec 2026; Q1 interim (Nov 30) by 29 Jan 2027 (https://www.osc.ca/en/industry/companies/reporting-issuer-and-issuer-forms/filing-due-dates-calendar-annual-and-interim-filings-reporting-issuers).

### 4.1 Key figures in the 31 Jul 2026 interim statements (nine months ended 31 May 2026)

- Revenue: vehicle sales $4,158,053; finance, insurance and other $513,228; total $4,671,281 (prior-year nine months $4,495,465). Three months to 31 May: $1,627,554 (vs $1,511,905).
- Gross profit nine months $607,026 (vehicle sales $184,048; F&I and other $422,978).
- Net loss nine months $(463,951) (prior year $(248,800)). Operating expenses $1,085,291 including listing expense $183,340 and share-based compensation $45,921.
- Balance sheet 31 May 2026: cash $431,192; inventory $86,300 (31 Aug 2025: $210,000); revolving floorplan facilities $222,033 (31 Aug 2025: $246,072); total assets $812,927; total liabilities $972,832; shareholders' deficiency $(159,905); accumulated deficit $(2,480,673). Due to related parties fell from $1,938,733 to $152,059 after a 14 Jan 2026 debt settlement of $1,889,975 by issuing 19,923,005 shares.
- Going concern: material uncertainty paragraph; "Liquidity risk is assessed as high". The $1,507,375 financing closed 7 Jul 2026 (after the period) and is not reflected.
- Related-party notes name consulting through a firm controlled by the CFO (payable $51,317), advances to the CEO ($37,124 receivable) and loans between the company and the Chairman.
- Revenue mix: vehicle sales were about 89% of nine-month revenue.

---

## 5. News releases since listing (21 Jul 2026 to 22 Oct 2026)

Wire: Newsfile Corp. ("TMX Newsfile"). Company page: https://www.newsfilecorp.com/company/12553/OCAL-Financial. Count: 22 wire distributions, 20 distinct headlines (the 22 Sep knowledge-base release re-issues the 15 Sep one; there are two 1 Oct Cantech releases, one sourced "Cantech Letter" at 7:00 AM and one sourced "OCAL Financial" at 9:10 AM; the 13 Aug SalesCloser release was corrected on 14 Aug). Sixteen appear on the investor page; six do not (marked "not listed").

| # | Date and time (ET) | Headline | Newsfile or best URL | On IR page | Operating or financial numbers inside |
|---|---|---|---|---|---|
| 1 | 21 Jul, 9:30 AM | OCAL Financial Inc. Completes Qualifying Transaction and Begins Trading on the TSX Venture Exchange | https://www.newsfilecorp.com/release/305866/OCAL-Financial-Inc.-Completes-Qualifying-Transaction-and-Begins-Trading-on-the-TSX-Venture-Exchange | Not listed as a release (the 16 Jul Ronin PDF is linked instead) | 36,667,803 shares; board and officer bios. Contains stale QT cautionary note ("Completion of the transaction is subject to..."; "capital pool company"). |
| 2 | 23 Jul, 8:30 AM | OCAL Financial Inc. Provides Corporate Overview Following TSX Venture Exchange Listing | https://www.newsfilecorp.com/release/306175/OCAL-Financial-Inc.-Provides-Corporate-Overview-Following-TSX-Venture-Exchange-Listing | Yes (dated Jul 22) | Founded 2021; vehicle sales "the majority of revenue"; stale QT cautionary note repeated. |
| 3 | 28 Jul, 8:30 AM | OCAL Financial Details Its End-to-End Digital Vehicle-Financing Process | https://www.newsfilecorp.com/release/306770/OCAL-Financial-Details-Its-EndtoEnd-Digital-VehicleFinancing-Process | Yes | Median about 7 days lead to signed, 3 to 4 days signed to funded (trailing 12 months, unaudited). |
| 4 | 30 Jul, 8:30 AM | OCAL Financial Outlines How Its Virtual, Finance-First Model Differs From the Traditional Dealership | https://www.newsfilecorp.com/release/307230/OCAL-Financial-Outlines-How-Its-Virtual-FinanceFirst-Model-Differs-From-the-Traditional-Dealership | Yes (dated Jul 29) | None. |
| 5 | 4 Aug, 8:30 AM | OCAL Financial Explains How Its Integrated Model Differs From Online Auto Retailers, Brokers and Fintech Lenders | newsfilecorp.com company page | Yes | None found. |
| 6 | 6 Aug, 8:30 AM | OCAL Financial Describes the Voice AI Behind Its Lead Engagement and Provides Business Update | https://finance.yahoo.com/technology/ai/articles/ocal-financial-describes-voice-ai-123000418.html | Yes | Market maker fee $6,000 per month plus taxes (Integral Wealth Securities). Voice agents in production since 2025. No operating numbers. |
| 7 | 11 Aug, 8:15 AM | OCAL Financial Explains Its Credit and Lender-Routing System, and the Underserved Market It Serves | https://stockhouse.com/news/press-releases/2026/08/11/ocal-financial-explains-its-credit-and-lender-routing-system-and-the-underserved | Yes | None. "Fee-and-margin business, not a balance-sheet lender." |
| 8 | 13 Aug, 12:35 PM | OCAL Financial Signs Exclusive Agreement With SalesCloser Technologies to Deploy AI Sales Agents Across the Vehicle-Finance Journey | https://stockhouse.com/news/press-releases/2026/08/13/ocal-financial-signs-exclusive-agreement-with-salescloser-technologies-to-deploy | Not listed | None. Later corrected (word "exclusive" was wrong). |
| 9 | 14 Aug, 8:57 AM | CORRECTION FROM SOURCE: OCAL Financial Adds AI Sales-Agent Technology Built Around Its Proprietary Knowledge Base | https://stockhouse.com/news/press-releases/2026/08/14/correction-from-source-ocal-financial-adds-ai-sales-agent-technology-built | Yes (dated Aug 11, retitled without "CORRECTION") | None. Non-exclusive; end-to-end AI closer "early, conceptual". |
| 10 | 18 Aug, 8:15 AM | OCAL Financial Describes CBIS, the System That Runs Its Operations and Data | newsfilecorp.com company page | Yes | None found. |
| 11 | 25 Aug, 8:15 AM | OCAL Financial Common Shares Now Trading on the Frankfurt Stock Exchange | https://www.newsfilecorp.com/release/311394/OCAL-Financial-Common-Shares-Now-Trading-on-the-Frankfurt-Stock-Exchange | Yes | JC3, WKN A42K21, ISIN; trading hours 8:00 to 22:00 CET; no new shares. |
| 12 | 29 Aug, 10:42 AM (Saturday) | OCAL Financial Launches Video-First Brand Campaign With DIBO Marketing and Engages Signal Capital for Investor Relations | https://finance.yahoo.com/small-business/articles/ocal-financial-launches-video-first-144200559.html | Yes | Signal Capital C$7,000 per month plus 100,000 options at $0.13 (4 years, 25% vests at 3, 6, 9, 12 months); either party may end on 15 days' notice; subject to TSXV acceptance. DIBO: 6 months, 20 scripts per month, fee not disclosed. |
| 13 | 3 Sep, 8:27 AM | OCAL Financial Launches Redesigned Website Built for Car Buyers and Investors | https://www.newsfilecorp.com/release/312785/OCAL-Financial-Launches-Redesigned-Website-Built-for-Car-Buyers-and-Investors | Not listed | Says the new IR section holds releases, presentation, fact sheet, "links to the Company's filings on SEDAR+" and TSXV and Frankfurt listings. SEDAR+ links are not on the page today. |
| 14 | 8 Sep, 9:08 AM | OCAL Financial Appoints Ryan McDonald as Vice President of Sales | newsfilecorp.com company page | Yes | Bio figures only ($50M revenue, $15M inventory, teams of 55). |
| 15 | 15 Sep, 8:13 AM | OCAL Financial Explains Its Proprietary Knowledge Base, the Data Asset Behind Its AI | https://www.streetinsider.com/Newsfile/OCAL+Financial+Explains+Its+Proprietary+Knowledge+Base%2C+the+Data+Asset+Behind+Its+AI/27061579.html | Not listed (the 22 Sep copy is) | "More than 1,250 funded deals". |
| 16 | 22 Sep, 8:49 AM | Same headline, re-issued | newsfilecorp.com company page | Yes | Same. |
| 17 | 29 Sep, 7:30 AM | OCAL Financial Offers a Digital Inventory of 3,000+ Vehicles via OPENLANE, With Zero Standing Inventory | https://finance.yahoo.com/small-business/articles/ocal-financial-offers-digital-inventory-113000785.html | Yes | 3,000+ vehicles (OPENLANE network; Toronto, Vancouver, Calgary sites). |
| 18 | 1 Oct, 7:00 AM | OCAL Financial to Present at The Cantech Investment Conference in Toronto (source: Cantech Letter) | https://www.newsfilecorp.com/release/316784/OCAL-Financial-to-Present-at-The-Cantech-Investment-Conference-in-Toronto | Not listed | None. Boilerplate says "five auction supply channels"; names Mehdi only. |
| 19 | 1 Oct, 9:10 AM | OCAL Financial to Present at The 2026 Cantech Investment Conference in Toronto | https://wireapp.newsfilecorp.com/release/316906/OCAL-Financial-to-Present-at-The-2026-Cantech-Investment-Conference-in-Toronto | Yes | Presentation Thu 8 Oct, 4:00 PM ET, Track 3, Arcadian Loft, 401 Bay Street; presenters Mehdi Moghareh and Matthew Friesen, Executive Chairman. |
| 20 | 6 Oct, 9:42 AM | OCAL Financial Surpasses 1,250 Funded Vehicle Deals | https://www.newsfile-prod.tmx.cloud/release/317641/OCAL-Financial-Surpasses-1250-Funded-Vehicle-Deals | Yes | FY2025 revenue about $6.48M (audited year ended Aug 31, 2025); FY2024 about $5.8M; 1,250+ funded deals; about 98% protection attach; median 7 days lead to signed and 3 to 4 days signed to funded; 17.6% repeat and referral (trailing 12 months, unaudited). |
| 21 | 13 Oct, 8:54 AM | OCAL Financial Outlines Its Integrated AI Demand Engine | https://www.newsfilecorp.com/release/318701/OCAL-Financial-Outlines-Its-Integrated-AI-Demand-Engine | Yes | 7 days, 98%, 17.6% (unaudited). Conversational AI "in final testing". |
| 22 | 22 Oct, 7:56 AM | OCAL Financial Introduces OCAL Showroom, a Live Virtual View of Its Dealership Operations | https://stockhouse.com/news/press-releases/2026/10/22/ocal-financial-introduces-ocal-showroom-a-live-virtual-view-of-its-dealership | Not listed (no page, not in sitemap) | None; says no financial guidance. Titles Matthew Friesen "Executive Chairman". |

Releases that carry operating or financial numbers: #3, #6 (market maker fee), #12 (fees and options), #15/#16 and #17 (deal count, vehicle count), #20 and #21. Only #20 carries audited revenue.

Pre-listing releases by Ronin Ventures / OCAL (TheNewswire; the investor page links two of them):
- 13 Feb 2026, LOI: https://www.thenewswire.com/press-releases/1k6WFqNln-1301756-b-c-ltd-dba-ocal-financial-and-ronin-ventures-corp-enter-into-letter-of-intent-to-complete-qualifying-transaction-and-listing-on-the-tsx-venture-exchange.html (revenue FY2025 $6,840,004 and FY2024 $5,769,393, both unaudited; net loss $265,208; "fully licensed virtual brokerage"; "does not carry inventory"; reverse takeover; incorporated 23 Apr 2021).
- 26 Mar 2026, definitive agreement (linked on IR page).
- 2 Jul 2026, conditional TSXV acceptance (25 Jun) and transaction update (linked on IR page; CFO bio; Friesen's residence stated as Cayman Islands).
- 10 Jul 2026, filing of the filing statement (via Stockwatch); 16 Jul 2026, closing release (PDF on IR page).

Other regulatory item: Yahoo Finance shows an earnings date estimate of 27 Oct 2026 (see section 10); no company-announced date found.

---

## 6. Frankfurt listing (JC3)

Confirmed.
- Company release, 25 Aug 2026: shares "listed and available for trading on the Frankfurt Stock Exchange under the trading symbol JC3 (WKN: A42K21; ISIN: CA67449X1050)"; secondary listing; no new shares. https://www.newsfilecorp.com/release/311394/OCAL-Financial-Common-Shares-Now-Trading-on-the-Frankfurt-Stock-Exchange
- Boerse Frankfurt page exists: "OCAL FINANCIAL O.N. Equity | A42K21 | CA67449X1050", trading hours 08:00 to 22:00, but price fields were empty on 23 Oct 2026 (no last price, no turnover shown). https://www.boerse-frankfurt.de/equity/CA67449X1050
- Yahoo Finance JC3.F (Frankfurt, EUR): quote 0.0616 EUR (+5.66%) at the time of the snapshot, "IPO Price 0.0616". https://finance.yahoo.com/quote/JC3.F/community/
- Bloomberg JC3:GR profile, Morningstar fra:JC3 profile and Simply Wall St FRA:JC3 page all exist.
- The investor page FAQ says live quotes are on TMX Money and Börse Frankfurt and that "links are in the Corporate information section"; only a TMX Money link (and TradingView) is on the page. The Börse Frankfurt link exists only in the JSON-LD (https://www.boerse-frankfurt.de/equity/CA67449X1050).

---

## 7. Board of directors and officers (public statements)

| Name | Title in public record | Source and wording |
|---|---|---|
| Matthew Friesen | Chairman and Director (site; releases through 13 Oct; material change report). Executive Chairman (Oct 1 9:10 AM, Oct 22 releases; Yahoo Finance; OCAL's LinkedIn post of 2 Oct). | 21 Jul release: "co-founder of OCAL and a director and chief executive officer of a private equity investment firm". Feb 2026 LOI: director and CEO of Barbizon Ventures Inc.; 15 years in the auto auction business; director of a Nasdaq-listed company. Ronin 2 Jul 2026 release says his jurisdiction of residence is the Cayman Islands. |
| Mehdi Moghareh | Chief Executive Officer and Director; co-founder | 21 Jul release: "automotive-industry veteran with extensive experience in dealership operations, logistics and platform development". LOI: 25+ years, VP and dealership manager roles with Nissan, Mitsubishi, Volkswagen, Porsche, Infiniti, Mazda, Kia, Hyundai. Name misspelled "Medhi" on Yahoo Finance, Simply Wall St, StockAnalysis. |
| Terence Lee, CPA | Chief Financial Officer and Corporate Secretary | 2 Jul 2026 release: partner at Imperium Consulting LLP; ex-BDO; CFO of AI/ML Innovations Inc. and Saga Metals Corp.; BBA Simon Fraser, diploma UBC. Interim statements: consulting through a firm controlled by the CFO. Site and fact sheet add "CPA". |
| Michael Stier | Director (independent); Chair of the Audit Committee | 26 Mar 2026 release and LOI: 20 years in capital markets, ex-CIBC senior financial advisor, board of GoldHaven Resources Corp. |
| Robert (Rob) Birmingham | Director (site says independent) | 26 Mar 2026 release: 15+ years capital markets, President of investor relations company Benaterra Communications Inc., former President and CEO of Pace Metals and GoldHaven. Existing Ronin director before the QT. |
| Shushu Feng | "Investor Relations Manager" (site team page, fact sheet) | 29 Aug release: founder and managing director of Signal Capital Advisors Inc., arm's length consultant, 40 Scollard St., Toronto. |

Other named people on the site team page: Alex Friesen (Controller), Allison Peters (Director of Finance), Nik Friesen (Automotive Acquisition), James Green and Michael Pham and Sasha Ruban (Sales Directors), Ryan McDonald (VP of Sales, appointed 8 Sep 2026), Hasneen Jalil (Chief Technology Officer; no release found), Denis Cicak (Social Media Director; also DIBO Marketing founder per the 29 Aug release).

Public record on the CFO: named as CFO in every source above; the 16 Jul closing release gives "Terence Lee as Chief Financial Officer and Corporate Secretary". The deck calls him "Terence Lee is a Chartered Professional Accountant (CPA) with over 15 years of experience", while the Jul 2 release says "over a decade". Four-person board: Moghareh, Friesen, Stier, Birmingham; two independent (Stier named independent; Birmingham called independent on the site only).

Bio inconsistency inside public documents about the Chairman (record only): deck says "CEO and Director of a Nasdaq-listed issuer" and "28-year auction legacy" and both "25+" and "15-company investor"; the LOI says "has served as a Director and on the Board of a Nasdaq listed company" and "15 years in the auto auction business"; 21 Jul release says "director and chief executive officer of a private equity investment firm".

---

## 8. Share structure as publicly stated

| Item | Figure | Source (date) |
|---|---|---|
| Common shares outstanding | 36,667,803 | 21 Jul release; material change report (22 Jul); TMX Money (23 Oct). No change reported since. |
| Warrants | 11,029,501 (5,000,001 at $0.10 plus 6,029,500 at $0.50, expiring 7 Jul 2028) | Material change report; 2 Jul release (5,000,001 at $0.10). The $0.10 warrants' expiry is not in anything I read. |
| Broker (finder) warrants | 39,760 at $0.50, 24 months; finders also received $9,940 cash | Material change report |
| Options | 600,000: 450,000 at $0.10 to 11 Aug 2027 (legacy Ronin holders); 150,000 at $0.25, 5 years, to a senior officer under a consulting agreement | Material change report |
| Post-listing option grants announced | 100,000 IR options to Signal Capital at $0.13, 4 years (TSXV acceptance pending) | 29 Aug release |
| Fully diluted | about 48.3M (site); my sum 48,337,064 before the Signal options | Site FAQ |
| Concurrent financing | 6,029,500 subscription receipts at $0.25, closed 7 Jul 2026 (converted 15 Jul), gross $1,507,375, one warrant at $0.50 for 24 months per unit | Material change report; interim statements |
| Earlier financings | 14 Jan 2026 debt settlement: 19,923,005 shares issued for $1,889,975 of related-party balances (fair value $914,883); private placement completed 6 Feb 2026 with 5,000,001 warrants; $375,000 net proceeds from share issues in the nine months | 31 Jul interim statements |
| Escrow | 23,638,104 shares escrowed (TMX Money, about 64.5% of shares outstanding); principals' securities subject to TSXV escrow; deck: "36 months escrow" | TMX key data (23 Oct); 21 Jul release; deck |
| Insider holdings (third party) | Yahoo: total insider shares held 22.42M; SEDI opening balances 15 Jul 2026 for Friesen and Moghareh as 10% holders and 21 Jul for Lee. Simply Wall St (UNVERIFIED, derived): Friesen 38.76%, Moghareh 15.57%, Stier 2.73%, Lee 0.59%, Birmingham 0.55%. Deck: "Founder ownership 54.33%" (equals Friesen plus Moghareh). | https://finance.yahoo.com/quote/OCAL.V/insider-transactions/ ; https://simplywall.st/ja/stocks/de/diversified-financials/fra-jc3/ocal-financial-shares/management |
| Insider activity since listing | TMX: none in 3, 6, 12 months | TMX company tab |
| Early warning reports | None found | n/a |
| Planned acquisition consideration | Deck and fact sheet say CAE/EasyPear consideration is "common shares vest against delivered performance milestones". No release found. | UNVERIFIED |

Market data for scale: at $0.11, market cap $4.03M; deck cites FY25 revenue $6.88M.

---

## 9. Auditor, transfer agent, counsel, market maker and other named parties

| Role | Name | Source and caveat |
|---|---|---|
| Auditor | DMCL LLP | Site corporate information table only. UNVERIFIED in a SEDAR+ audit report. TSX Infoventure still shows "Crowe MacKay LLP" (Ronin's former auditor). |
| Transfer agent and subscription receipt agent | Endeavor Trust Company (site, closing release) or Endeavor Trust Corporation (TSX Infoventure, interim statements) | Name inconsistent across sources. |
| Legal counsel | Lawson Lundell LLP | Site only; UNVERIFIED elsewhere. |
| Market maker | Integral Wealth Securities Limited | 6 Aug 2026 release: $6,000 per month plus taxes and approved expenses; minimum three months, then 30 days' notice; no shares or options; subject to TSXV approval. TSXV approval not reported. |
| Investor relations | Signal Capital Advisors Inc. (Shushu Feng), Toronto | 29 Aug 2026 release: month-to-month, C$7,000 per month plus 100,000 options at $0.13; arm's length. |
| Marketing agency | DIBO Marketing (Denis Cicak) | 29 Aug 2026 release: six-month social media program; no fee given. |
| Technology vendor | SalesCloser Technologies Ltd. (TSXV: SCAI; OTCQB: SCTLF) | 13 and 14 Aug releases; non-exclusive. |
| Auction partner | OPENLANE (NYSE: OPNL) | OPENLANE Canada described as "exclusive auction and sourcing channel" (13 Oct and 22 Oct releases, site). |
| Wire | Newsfile Corp. (TMX Newsfile) | All 22 post-listing releases. |
| Sponsor | None named | Not found. |
| Exchange classification | Tier 2 Technology issuer | Material change report, 22 Jul 2026. |

---

## 10. Third-party profiles: what each says OCAL does, and what is stale

Flag key: STALE = describes services or details OCAL no longer or never offered (powersports, RV, personal loans, auto repair, healthcare), or uses an old name or old officer, or "brokerage".

| Source (URL) | What it says (quoted) | Flag |
|---|---|---|
| Yahoo Finance OCAL.V profile https://finance.yahoo.com/quote/OCAL.V/profile/ ; JC3.F https://finance.yahoo.com/quote/JC3.F/profile/ | "OCAL Financial Inc., through its finance platform, offers vehicle financing solutions. It offers auto, power sports, recreational vehicles, personal loans, auto repair, and healthcare financing services. It also sells insurance and vehicle warranties. The company is based in Vancouver, Canada." Sector Financial Services; Industry Credit Services. Officers: Matthew Friesen Executive Chairman; "Medhi Moghareh" CEO and Director; Terence Lee CFO and Corporate Secretary. Phone (604) 687-7765. | STALE description; misspelled CEO name. |
| Stockhouse quote and bullboard https://stockhouse.com/companies/quote?symbol=ocalf ; https://www.stockhouse.com/companies/bullboard/v.ocal/ocal-financial-inc ; also https://stockhouse.com/companies/bullboard?symbol=v.rvc.p | Same text as Yahoo. Page header "GREY:OCALF ... OCAL Financial Inc (GM)". The Ronin bullboard (v.rvc.p) shows the OCAL description. No posts found. | STALE description; ticker shown as GREY:OCALF; old Ronin board still live. |
| Simply Wall St https://simplywall.st/stocks/ca/diversified-financials/tsxv-ocal/ocal-financial-shares | Same description. "Has not reported any financial data." Market cap CA$4.0m. Founded n/a. CEO "Medhi Moghareh". Lists "Annual General Meeting, Dec 10, 2026, Vancouver" (UNVERIFIED). | STALE description; no financials; AGM date UNVERIFIED. |
| StockAnalysis (S&P Global Market Intelligence data) https://stockanalysis.com/quote/tsxv/OCAL/company/ | Same description. Industry Credit Services; sector Financials; SIC 6141; executives Moghareh, Friesen (Executive Chairman), Lee. Price shown 0.095 (23 Sep). | STALE description; stale price page. |
| Weiss Ratings https://weissratings.com/en/stock/ocal-v-tsx/profile | Same description; sector Financials; market cap $2.87M; "Day's range $0.13 to $0.15". | STALE description and market cap. |
| Wealth Awesome https://wealthawesome.com/stocks/ocal-v | Same description; market cap $4.03M; statistical forecasts; algorithmic "why is the stock..." articles. | STALE description. |
| Google Finance https://www.google.com/finance/quote/OCAL:CVE | "Sector: Payment service provider"; "Shares outstanding 13.03M"; EPS -$0.04; market cap 4.03M. | WRONG sector and WRONG share count (actual 36,667,803). |
| MarketScreener https://ae.marketscreener.com/quote/stock/OCAL-FINANCIAL-INC-212887150/company/ | "...Canada-based fintech company. ... fully virtual, artificial intelligence (AI)-native licensed automotive finance platform that connects borrowers, ranging from prime to deep subprime, to a nationwide network of regulated lenders ... intends to expand into Ontario, Quebec, and the United States market (Washington, Arizona, and Nevada) ... Its financial services includes pre-owned vehicle financing, powersports financing, RV financing, personal loan financing, auto repair financing, and healthcare financing." Sector: Consumer Lending. | STALE (powersports, RV, personal, repair, healthcare). |
| CNBC https://www.cnbc.com/quotes/OCALF | Same S&P Capital IQ style text as MarketScreener. Quote header "OCAL Financial Inc OCALF:OTCQB". Officer listed: "Anthony Zelen, Chief Executive Officer, Chief Financial Officer, Corporate Secretary, Director". | STALE description; STALE officer (Ronin's former CEO/CFO); OTCQB label UNVERIFIED (Stockhouse shows GREY). |
| Bloomberg https://www.bloomberg.com/profile/company/JC3:GR | "OCAL Financial Inc. operates as a fintech company. The Company offers an AI-driven digital automotive dealership platform for users which enables them to access auto and personal loans. OCAL Financial serves customers in Canada." | Partly STALE ("personal loans"). |
| Morningstar (AU) https://www.morningstar.com.au/investments/security/fra/JC3 | "Ocal Financial Inc is a Canadian financial technology company that provides a digital platform for vehicle financing. Its platform connects borrowers with regulated lenders and facilitates vehicle financing. The company generates revenue from vehicle sales, arranging vehicle financing, and the sale of vehicle warranties. It serves customers in British Columbia and Alberta." Sector Financial Services; Credit Services; "Fiscal Year End 31 August 2027". | Broadly right; omits dealership, asset-light; FY end date odd. Morningstar Canada page could not be fetched. |
| TradingView https://www.tradingview.com/symbols/TSXV-OCAL/ | "OCAL Financial, Inc is a Canadian fintech company that is redefining vehicle financing through a technology-enabled, fully licensed virtual automotive dealership platform ... founded in April 2021". Sector Finance; Industry "Financial Conglomerates". News headline "OCAL Financial Inc. (OCAL) Details Zero-Inventory Sourcing Model" (https://www.tradingview.com/news/tradingview:ebdec116ef67c:0-ocal-financial-inc-ocal-details-zero-inventory-model-using-openlane/). | Mostly right; "zero-inventory" phrasing in headline; industry odd. |
| TMX Money https://money.tmx.com/en/quote/OCAL | Sector Finance; Industry Credit Finance; no description. | Classification differs from Tier 2 Technology. |
| TSX Infoventure http://infoventure.tsx.com/TSXVenture/TSXVentureHttpController?GetPage=CompanySummary&PO_ID=1186510 | Fiscal year end February 29; incorporated 18 Jan 2022; business type "All Other Professional, Scientific and Technical Services"; auditor "Crowe MacKay LLP"; transfer agent Endeavor Trust Corporation. | STALE (Ronin data: FYE, incorporation date, auditor, business type). |
| Newsfile company profile https://www.newsfilecorp.com/company/12553/OCAL-Financial | "OCAL is a Canadian fintech company redefining how consumers access vehicle financing. OCAL is Canada's first fully virtual, AI-native licensed automotive finance platform, that connects borrowers, ranging from prime to deep subprime, to a nationwide network of regulated lenders through a proprietary digital platform." | STALE boilerplate (finance platform, "nationwide network"; no dealership, asset-light). |
| LinkedIn company page https://linkedin.com/company/ocalfinancial (via aggregator view, 23 Oct) | "OCAL Financial is transforming how Canadians buy and finance vehicles. We are a virtual automotive dealership and financial technology platform that allows customers to purchase and finance vehicles entirely online..." 17 employees; founded 2021; aliases "One Click Auto Loans"; no TSXV mention in the quoted About text. Official posts continue (29 Sep, 1 Oct, 2 Oct, 5 Oct, 17 Oct). | Mostly current; no listing language; alias exposes old name. |
| LinkedIn profile, CEO https://linkedin.com/in/mehdi-moghareh-b94800171 | Title "Senior Managing Partner @ OCAL Financial"; company text: "OCAL Financial is a financial services company that offers pre-owned vehicle financing, powersports financing, rv financing, personal loan financing, auto repair financing, healthcare financing, and service ... 1-10 employees". | STALE title and description. |
| Crunchbase (person) https://www.crunchbase.com/person/mehdi-moghareh | "Co-Founder and Chief Executive Officer ... since Mar 2022 ... previously worked at Carbone Restaurant Group as Vice President of Sales Division." | Employment line looks like the wrong person; UNVERIFIED. Crunchbase organization page could not be fetched. |
| Own site llms.txt https://ocalfinancial.ca/llms.txt | "operating as One Click Auto Loan ... used-car dealership and auto finance broker ... nine lending partners". | STALE (old name, "broker"). |
| Own site IR letters https://ocalfinancial.ca/investor-relations/press-release/press-release-ceo and .../press-release-director | "technology-enabled brokerage platform" (CEO, 18 Mar 2026); "technology and brokerage services" (Director). | STALE ("brokerage"). |
| Ronin LOI release (TheNewswire, 13 Feb 2026) | "Operating as a fully licensed virtual brokerage ... earns commission-based revenue by brokering financing". | STALE (pre-listing); sourced by search snippets and aggregator copies. |
| YouTube "Tech ShowCase F1 02" by Ace Le https://www.youtube.com/watch?v=yPgrzCCM-H4 | 5:40 voice AI demo using the OCAL name; 147 views; claims of "chat GPT4", "up to 1 million concurrent calls". | Unofficial, STALE, uses the brand. |
| Official YouTube video 1 https://www.youtube.com/watch?v=TrGWP1ECD8I (embedded on IR page) | See 1.8. | STALE content on the IR page. |
| Wikipedia / Wikidata | No page found. | None. |
| Reuters, Crunchbase organization, Investing.com company page | Not retrievable in this run (Investing.com URL https://www.investing.com/equities/ronin-ventures still carries the Ronin slug and was listed as "OCAL Financial Inc (OCAL)"). | UNVERIFIED. |

Frequency: of 14 data vendors checked for a description (Yahoo, Stockhouse, Simply Wall St, StockAnalysis, Weiss, Wealth Awesome, Google, MarketScreener, CNBC, Bloomberg, Morningstar, TradingView, TMX, Newsfile), 8 use the old multi-product description (Yahoo, Stockhouse, Simply Wall St, StockAnalysis, Weiss, Wealth Awesome, MarketScreener, CNBC) and 1 has wrong core data (Google).
Share price in Yahoo Finance snapshots varies by crawl date (0.14 on one crawl, 0.135 on 7 Oct); ignore unless freshly checked.

---

## 11. Search visibility (23 Oct 2026)

Method: WebSearch tool (US index, "standard" mode) and, for the last query, also "extended" mode. Top 5 results, in the order returned. ocalfinancial.ca and money.tmx.com are marked where they appear.

**"OCAL Financial"**
1. OCAL Financial Inc. Provides Corporate Overview Following TSX Venture Exchange Listing, https://www.newsfilecorp.com/release/306175/OCAL-Financial-Inc.-Provides-Corporate-Overview-Following-TSX-Venture-Exchange-Listing?lang=fr
2. OCAL Financial, https://www.newsfilecorp.com/company/12553/OCAL-Financial
3. OCAL Financial Inc. Completes Qualifying Transaction and Begins Trading..., https://www.webull.com/news/15265548337177600
4. OCAL Financial Inc. Finalizes Qualifying Transaction ... AI-Driven Remote Auto Dealership, https://kalkinemedia.com/ca/news/announcements/ocal-financial-inc-finalizes-qualifying-transaction-begins-trading-on-tsx-venture-exchange-as-ai-driven-remote-auto-dealership
5. weissratings.com, https://weissratings.com/en/stock/ocal-v-tsx/profile
(6 to 10: kalkinemedia.com unveils process; finanznachrichten.de x2; Stockwatch RVC 3840417. ocalfinancial.ca and TMX Money not in the top 10.)

**"OCAL stock"**
1. OCAL Financial Inc (OCAL), https://www.investing.com/equities/ronin-ventures
2. finance.yahoo.com, https://finance.yahoo.com/quote/OCAL.V/
3. (irrelevant) tickertape.in UCAL Fuel Systems, https://www.tickertape.in/stocks/ucal-fuel-systems-UCAF
4. what's going on with OCAL Financial Inc stock Tuesday 10/13/2026, https://wealthawesome.com/whats-going-on-with-ocal-financial-inc-stock-tuesday-10132026-wgo
5. why OCAL Financial Inc stock is skyrocketing today 08/13/2026, https://wealthawesome.com/why-ocal-financial-inc-stock-is-skyrocketing-today-08132026
(Remaining results are other tickers named UCAL, OCAC, a 2014 Bloomberg article. OCAL's own site and TMX are absent. Name collision with UCAL and OCAC.)

**"OCAL TSXV"**
1. Stockwatch, 18:08 Sat 14 Feb 2026 (Ronin LOI), https://wwww.stockwatch.com/News/Item/Z-C!RVC-3785211/C/RVC
2. Stockwatch, 18 Jul 2026 (delisting of Ronin, OCAL begins trading), https://wwww.stockwatch.com/News/Item/Z-C!RVC-3842323/C/RVC
3. miningstockeducation.com, LOI copy, https://www.miningstockeducation.com/2026/02/1301756-b-c-ltd-dba-ocal-financial-and-ronin-ventures-corp-enter-into-letter-of-intent-to-complete-qualifying-transaction-and-listing-on-the-tsx-venture-exchange/
4. miningstockeducation.com, definitive agreement copy, https://www.miningstockeducation.com/2026/03/ronin-ventures-corp-announces-definitive-agreement-with-1301756-b-c-ltd-dba-ocal-financial-for-proposed-qualifying-transaction/
5. wealthawesome.com, why OCAL stock surged yesterday (7 Oct), https://wealthawesome.com/why-ocal-financial-inc-stock-surged-yesterday-10072026
(6 to 9: Wealth Awesome stock page; Wikipedia TMX Group; TradingView TSXV-OCI minds; Yahoo OCO.V. The top two are pre-listing Ronin-era items, which is why the search tool's summary called OCAL "a virtual brokerage".)

**"OCAL Financial investor relations"** (two runs)
Standard run: 1. https://www.newsfilecorp.com/release/305866/... (QT completion); 2. https://www.newsfilecorp.com/release/307230/... (virtual vs dealership, ?lang=fr); 3. https://www.newsfilecorp.com/release/306175/... ; 4. https://finance.yahoo.com/quote/OCAL.V/ ; 5. Stockwatch RVC 3840417 (11 Jul 2026 filing statement). Then Weiss, TipRanks (OceanFirst, irrelevant), Euronext (irrelevant). ocalfinancial.ca not in top 10.
Extended run: 1. https://www.streetinsider.com/Newsfile/OCAL+Financial+Inc.+Completes+Qualifying+Transaction+and+Begins+Trading+on+the+TSX+Venture+Exchange/26793565.html ; 2. https://finance.yahoo.com/markets/stocks/articles/ocal-financial-inc-provides-corporate-123000623.html ; 3. https://finance.yahoo.com/small-business/articles/ocal-financial-launches-video-first-144200559.html ; 4. https://finance.yahoo.com/small-business/articles/ocal-financial-offers-digital-inventory-113000785.html ; 5. https://www.newsfilecorp.com/release/306175/... ; 6 Nasdaq.com press release; 7 TradingView news; 8 Newsfile 312785; 9 Newsfile 311394; 10 **https://ocalfinancial.ca/investor-relations/** (the company's own IR page).

**"OCAL share price"**
1. (irrelevant) 5paisa UCAL, https://www.5paisa.com/hindi/stocks/ucal-share-price
2. wealthawesome.com, what's going on with OCAL stock Tuesday 10/06/2026, https://wealthawesome.com/whats-going-on-with-ocal-financial-inc-stock-tuesday-10062026-wgo
3. (irrelevant) zerodha UCAL, https://www.zerodha.com/markets/stocks/NSE/UCAL/
4. (irrelevant) choiceindia UCAL, https://choiceindia.com/stocks/ucal-ltd-share-price
5. wealthawesome.com, OCAL Financial Inc. (OCAL : TSX-V), https://wealthawesome.com/stocks/ocal-v
(The tool's summary quoted a 22 Jul price of $0.22; stale. TMX Money and Yahoo did not appear in the top 9.)

Reading across the five: the top results are wire copies, Stockwatch, aggregator and algorithmic sites; OCAL's own IR page ranks 10th at best; three of five queries are polluted by UCAL or OCAC; the two Stockwatch hits for "OCAL TSXV" are Ronin-era news.

---

## 12. Analyst, newsletter and media coverage since listing

No analyst research found; the site says the same ("OCAL is not aware of published research coverage"). No podcast found. No Cantech Letter editorial item found (only the conference listing and the paid-or-wire release of 1 Oct).

| Date | Outlet | Item | URL |
|---|---|---|---|
| 21 Jul | Kalkine | Completes QT and launches trading (announcement summaries, two versions) | https://kalkine.ca/news/announcements/ocal-financial-inc-completes-qualifying-transaction-and-launches-trading-on-tsx-venture-exchange |
| 21 Jul | MT Newswires | OCAL Financial Begins Trading on TSX Venture Exchange | via https://www.futunn.com/en/stock/OCAL-CA/news |
| 28 Jul | Kalkine | OCAL Financial Unveils Fully Remote, AI-Driven Digital Vehicle Financing Process | https://kalkinemedia.com/ca/news/announcements/ocal-financial-unveils-fully-remote-ai-driven-digital-vehicle-financing-process |
| 13 Aug | Wealth Awesome | Why OCAL stock is skyrocketing today (algorithmic) | https://wealthawesome.com/why-ocal-financial-inc-stock-is-skyrocketing-today-08132026 |
| 14 Aug | MT Newswires; Webull | SalesCloser strikes deal with OCAL Finance; OCAL Financial corrects release, says SalesCloser AI deal is non-exclusive | https://www.webull.com/news/15401302232540160 |
| 31 Aug | Kalkine (Ankur Sharma) | OCAL Goes Video-First (DIBO and Signal analysis) | https://kalkine.ca/news/financial/ocal-goes-video-first-the-approval-first-car-financing-disruptor-wants-all-of-canada-watching |
| 1 Sep | Signal Capital Advisors (LinkedIn post) | "Welcome OCAL Financial ... closed FY2025 with $6.8M in revenue" | https://www.linkedin.com/posts/linkedin%2Ecom-company-signalcapitaladvisors_httpsocalfinancialcainvestor-relations-activity-7500643571755257857-LgXF |
| 3, 9, 10 Sep | Wealth Awesome | "Why OCAL stock is plummeting today", "What's going on with OCAL / Ronin stock" | https://wealthawesome.com/why-ocal-financial-inc-stock-is-plummeting-today-09032026 |
| 8 Sep | Investing.com (Vietnamese) | OCAL Financial appoints Ryan McDonald | https://vn.investing.com/news/company-news/ocal-financial-bo-nhiem-ryan-mcdonald-lam-pho-chu-tich-kinh-doanh-93CH-2708061 |
| 30 Sep | Kalkine | Why OCAL is testing an asset-light, approval-first model for car buying | https://kalkine.ca/news/retail/why-ocal-financial-inc-ocal-is-testing-an-asset-light-approval-first-model-for-car-buying |
| 29 Sep | TradingView | OCAL Financial Inc. Details Zero-Inventory Sourcing Model | https://www.tradingview.com/news/tradingview:ebdec116ef67c:0-ocal-financial-inc-ocal-details-zero-inventory-model-using-openlane/ |
| 7 Oct | Fintech.ca (Knowlton Thomas) | OCAL Enters Online Auto-Selling Space with "Backwards on Purpose" Approach | https://www.fintech.ca/2026/10/07/ocal-online-auto-selling-backwards-approach/ |
| 6, 7, 13 Oct | Wealth Awesome | Daily algorithmic articles | https://wealthawesome.com/why-ocal-financial-inc-stock-surged-yesterday-10072026 |
| 8 Oct | Kalkine | How Will Cantech Shape Value? | https://kalkinemedia.com/ca/stocks/value/ocal-financial-inc-tsxvocal-how-will-cantech-shape-value |
| 12 to 14 Oct | Kalkine | Can its model succeed in Ontario?; Is Ontario the next step; four-part AI demand engine | https://kalkinemedia.com/ca/stocks/retail/ocal-financial-tsxvocal-can-its-model-succeed-in-ontario |
| 13 Oct | TipRanks | OCAL Financial Showcases Integrated AI Demand Engine for Auto Finance Growth | https://www.tipranks.com/news/company-announcements/ocal-financial-showcases-integrated-ai-demand-engine-for-auto-finance-growth |
| every release | Stockwatch (one-line summaries), StreetInsider, Globe and Mail (Newsfile), Yahoo Finance (TMX Newsfile), Nasdaq.com, MarketScreener, finanznachrichten.de | Syndication of each release | e.g. https://www.theglobeandmail.com/investing/markets/markets-news/Newsfile/3383576/ocal-financial-inc-completes-qualifying-transaction-and-begins-trading-on-the-tsx-venture-exchange/ |
| Sep to Oct | OCAL LinkedIn page | Official posts 29 Sep (sourcing model), 1 Oct (public auctions guide), 2 Oct (Cantech), 5 Oct (1,250 deals), 17 Oct (approval first) | https://linkedin.com/company/ocalfinancial |
| undated | YouTube (OCAL channel) | "Who is OCAL Financial? A Sit-Down with CEO Mehdi Moghareh"; "How Ocal Financial Is Reinventing Car Buying in Canada" | https://www.youtube.com/watch?v=TrGWP1ECD8I ; https://www.youtube.com/watch?v=NkXi9qRAMf0 |
| n/a | Stockhouse bullboard, StockTwits (OCALF) | No posts, sentiment N/A | https://stocktwits.com/symbol/OCALF |

Kalkine and Wealth Awesome pieces appear to be automatically or commercially generated; I did not verify whether any is paid.

---

## 13. Conflicts register (facts that disagree across public sources)

| # | Topic | What conflicts | Where |
|---|---|---|---|
| 1 | FY2025 revenue | $6.48M (audited, 6 Oct release; Yahoo 6.48M) vs $6,879,835 / $6.88M (deck, fact sheet) vs $6,840,004 (LOI, unaudited) vs "$6.8M" (Signal post, 1 Sep). Gross profit FY2025: Yahoo 810.75K vs deck $781,383. Net loss FY2025: Yahoo $(322.09K) vs LOI $(265,208). | sections 1.6, 5, 12 |
| 2 | FY2024 revenue | "about $5.8M" (release), $5,838,498 (deck), $5,769,393 (LOI), Yahoo 5.45M | same |
| 3 | Inventory | "zero standing inventory", "no inventory", "balance sheet carries no used-vehicle price exposure" vs interim FS inventory $86,300 (31 May 2026) and $210,000 (31 Aug 2025) and floorplan $222,033; Ronin 10 Jul release: "holds limited vehicle inventory from time to time". | IR FAQ; section 4.1 |
| 4 | Revenue source | IR page "Revenue comes from financing commissions and related services" vs FAQ "vehicle sales and related finance and protection products" vs 23 Jul release (vehicle sales the majority) vs FS (89% vehicle sales). | IR page |
| 5 | Business description | "brokerage", "broker" (18 Mar letters, LOI, llms.txt) vs "virtual dealership" (all releases since 21 Jul) vs "licensed automotive finance platform" (Newsfile profile). | section 10 |
| 6 | Years in business | About page "10+ Years in business" vs incorporated 23 Apr 2021 (LOI), "founded in 2021" (23 Jul release), "born in May 2021" (CEO video). | https://ocalfinancial.ca/about |
| 7 | Cars sold | About page "5k+ Cars sold" vs "1,250+ funded deals to date". | About page vs releases |
| 8 | Chairman title | Chairman (site, MCR, releases to 13 Oct) vs Executive Chairman (1 Oct 9:10, 22 Oct releases, Yahoo, LinkedIn). | section 7 |
| 9 | SalesCloser | 13 Aug "exclusive" corrected 14 Aug to non-exclusive; IR list shows corrected release as 11 Aug; fact sheet says agents "live" in Oct vs 13 Oct release "in final testing"; deck "full implementation October 2026". | sections 1.4, 5 |
| 10 | OPENLANE wording | "exclusive auction and sourcing channel" vs "OPENLANE auction network and select partner dealers" vs "OPENLANE and other partners" vs "five auction supply channels" (1 Oct 7:00 release). | IR page; releases; deck |
| 11 | CAE / EasyPear and CTO | Deck and fact sheet say complete; team page lists Hasneen Jalil CTO; no release or SEDAR+ item found. Deck names the target as "Canada Auto Experts (CAE)", "Canoply Auto Reports (CAR)"; fact sheet "Canada AutoExperts". | UNVERIFIED |
| 12 | Licences | "Manitoba (Sept 2026) licence underway" and "OPENLANE buying expansion into Manitoba & Saskatchewan (Oct)" in fact sheet vs only "next" on site; no release. Footer lists Manitoba and Ontario phone numbers. | UNVERIFIED |
| 13 | Release dates | Jul 22 vs Jul 23 and Jul 29 vs Jul 30 on IR list; corrected release dated Aug 11. | section 1.4 |
| 14 | Stale QT cautionary language | 21 Jul and 23 Jul releases carry "Completion of the transaction is subject to ... capital pool company" paragraph after the transaction closed; the 16 Jul PDF on the IR page too. | releases 1 and 2 |
| 15 | Deck errors | "July 9, 2025"; "add an address"; "Mehdi Mehdi". Fact sheet dated August 2026 shows September and October items. | section 1.6 |
| 16 | Chairman bio | Nasdaq "CEO and Director" vs "Director and on the Board"; "28-year" vs "15 years" auction experience; "25+" vs "15-company investor". | section 7 |
| 17 | IR contact | investors@ocal.ca (IR page, Oct releases) vs general@ocal.ca (Jul to Sep releases, JSON-LD); the 1 Oct 9:10 release also lists a Signal Capital Advisors contact for Shushu Feng. | releases |
| 18 | Transfer agent | Endeavor Trust Company vs Endeavor Trust Corporation. | section 9 |
| 19 | Auditor | DMCL LLP (site) vs Crowe MacKay LLP (TSX Infoventure; Ronin's). | section 9 |
| 20 | Share count and market cap on vendors | 36,667,803 and $4.03M (TMX) vs 13.03M shares (Google) vs $2.87M market cap (Weiss). | section 10 |
| 21 | Sector | TMX Finance / Credit Finance; Yahoo Financial Services / Credit Services; Google "Payment service provider"; TradingView "Financial Conglomerates"; company "Tier 2 Technology". | sections 3, 10 |
| 22 | IR manager | "Investor Relations Manager" (site) vs external, arm's length consultant (29 Aug release). | sections 1.3, 7 |
| 23 | Going concern | Interim FS material uncertainty note and shareholders' deficiency; investor page and releases do not mention it (the page directs readers to MD&A and filings). | section 4.1 |
| 24 | Reporting standard | FAQ cites 120 and 60 day deadlines as a venture issuer; 31 Jul filings include "IPO/RTO becoming non-venture issuer" certificates. | section 4 |

---

## 14. Not verified, or could not be accessed

- SEDAR+ itself (profile list, filing statement text, audited FY2025 statements and audit report, interim MD&A text, Form 52-109 certificates, any early warning or exemption filings).
- TSXV listing page details (final exchange bulletin text, Tier 2 Technology classification wording, escrow agreement terms), TMX filings and financials tabs.
- OTC Markets page for OCALF (page returned only the site shell); OTCQB claim on CNBC is not supported by anything seen; Stockhouse labels it GREY.
- Crunchbase organization page, Morningstar Canada, Reuters, Investing.com company profile.
- Public announcement of the CAE / EasyPear acquisition, Hasneen Jalil's appointment, Manitoba licence status, and the "OPENLANE buying expansion into Manitoba and Saskatchewan".
- Whether TSXV accepted the Integral and Signal Capital engagements.
- AGM date (Dec 10, 2026 is shown only on Simply Wall St).
- Registry status of VSA #D50207 and AMVIC #B2036050 (not checked in this run).
- Which two directors the company counts as independent (Stier is named; Birmingham is called independent on the site only).
- YouTube publish dates for the two embedded videos.
- Ownership percentages other than the deck's 54.33% (third-party derived only).
