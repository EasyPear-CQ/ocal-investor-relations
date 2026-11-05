# -*- coding: utf-8 -*-
"""
OCAL Financial investor site (investors.ocal.ca): every word on every page, in one place.

Block types used by build_site.py (HTML) and build_docs.py (review deck):
  ("kicker", text)                      small lime letterspaced label
  ("h2", text) / ("h3", text)
  ("lead", text)                        standfirst paragraph
  ("p", text)                           body paragraph; **bold** and [text](url) allowed
  ("kpis", [(figure, label, caption), ...])
  ("bullets", [(lead, body), ...])      lead may be ""
  ("table", headers, rows, note)
  ("steps", [(num, title, body), ...])
  ("faq", [(q, a), ...])                rendered with FAQPage schema
  ("cards", [(kick, title, body, href), ...])
  ("quote", text, who)
  ("cta", title, body, [(label, href, primary), ...])
  ("note", text)                        small print
  ("widget", name)                      tradingview | subscribe | deals-chart | news-list | filings | events | kpi-strip
  ("anchor", id)

Placeholders: anything inside [[double brackets]] would render as a yellow marker and be listed in source/PLACEHOLDERS.txt.
Since 4 November 2026 there are none: the build must print "placeholders: 0". The two values CQ and Has swap at go-live are
SITE["form_action"] (the Brevo form action URL; empty means the email-request fallback) and, if a direct link is captured,
SITE["sedar_profile"] (today the SEDAR+ search page).
"""

SITE = {
    "domain": "investors.ocal.ca",
    "base_url": "https://investors.ocal.ca",
    "name": "OCAL Financial Investor Relations",
    "legal_name": "OCAL Financial Inc.",
    "ticker": "OCAL",
    "exchange": "TSX Venture Exchange",
    "fse": "JC3",
    "isin": "CA67449X1050",
    "cusip": "67449X105",
    "wkn": "A42K21",
    "lei": "984500E70698C2C2AC97",
    "email": "investors@ocal.ca",
    "phone": "1 (604) 687-7765",
    "phone_tel": "+16046877765",
    "address": "Suite 500, 885 Dunsmuir Street, Vancouver, BC V6C 1N5",
    "edmonton": "10515 103 Avenue NW, Edmonton, AB T5J 4P7",
    "consumer_site": "https://ocalfinancial.ca",
    "tmx": "https://money.tmx.com/en/quote/OCAL",
    "sedar": "https://www.sedarplus.ca",
    "sedar_profile": "https://www.sedarplus.ca",
    "sedar_profile_note": "On SEDAR+, search the issuer name OCAL Financial Inc.",
    "frankfurt": "https://www.boerse-frankfurt.de/equity/ocal-financial-inc",
    "linkedin": "https://www.linkedin.com/company/ocal-financial",
    "tradingview_symbol": "TSXV:OCAL",
    "booking_link": "mailto:investors@ocal.ca?subject=Book%20a%2030-minute%20investor%20call",
    "form_action": "",   # Has: paste the Brevo form action URL here when the list exists; empty = the email-request fallback
    "updated": "November 2026",
    "facts_date": "4 November 2026",
}

# The NI 52-112 definition sentence for the funded-deal count (Garrett Lee, 31 October 2026; wording as issued in the
# 3 November 2026 release). It sits beside the first use of "more than 1,500" on every page.
FUNDED_DEF = ("A funded vehicle transaction is a retail vehicle sale arranged through OCAL's platform for which the customer's "
              "financing contract was funded by a lender and the vehicle was delivered to the customer. The cumulative count is "
              "drawn from the Company's transaction records and lender reporting since its first funded transaction in 2021 and "
              "is not a measure presented in its financial statements.")

NEWSFILE_08 = "https://www.newsfilecorp.com/release/322277/OCAL-Financial-Reports-a-Historical-Repossession-Rate-Under-One-Percent-Highlighting-the-Strength-of-Its-AssetLight-Automotive-Financing-Platform-and-Announces-Meeting-Date-for-Its-2026-Annual-General-and-Special-Meeting"

# Lines that hold everywhere (copied into the wording guide). Updated 4 November 2026.
LINES_THAT_HOLD = [
    "Matthew Friesen is Executive Chairman and Director. Mehdi Moghareh is Chief Executive Officer.",
    "OCAL is a technology-enabled automotive financing and purchasing platform that solves the customer's problem first. Never 'virtual' anywhere in the descriptor, never 'virtual dealership', 'online car dealer' or 'the car dealer with no cars' (Mehdi and Shushu, 27 October 2026; Matthew, 1 November 2026). Every page follows the same spine: problem, platform, solution, thesis.",
    "Zero standing inventory. No cars on a lot. We stock access. Never 'zero inventory' on its own.",
    "OPENLANE is OCAL's auction and sourcing channel, never 'exclusive' (Garrett Lee, 31 October 2026). More than 3,000 vehicles are visible on its Canadian marketplace on a typical day (marketplace visibility, not owned inventory); OCAL owns none of them until a customer is approved.",
    "OCAL is the licensed motor dealer of record on every transaction. It is not a broker. The lender holds the loan; OCAL holds none.",
    "FY2025 revenue is $6.48 million, audited (year ended 31 August 2025). Every financial figure on the site is from the audited FY2025 and FY2024 statements (DMCL LLP). Nothing from FY2026 until the audited statements are filed.",
    "More than 1,500 funded vehicle transactions since 2021, everywhere, never 1,250. The count is a supplementary financial measure (NI 52-112), so the definition sentence sits beside its first use on every page: " + FUNDED_DEF,
    "Rates carry their period: fewer than one percent of vehicle loans arranged have resulted in repossession and about 99 percent of signed contracts were funded, both from the first funded transaction in 2021 to 30 September 2026, management information based on lender reporting; about 98 percent of funded transactions include a protection product; repeat and referral customers about 17.6 percent of funded transactions over the trailing twelve months (3 November 2026 release).",
    "No per-vehicle dollar figures, no fixed-cost figure, no break-even count, no forecast, no plan-case table, no growth-capital amount and no cash figure between reporting dates anywhere on the site. Operating leverage is told with the audited lines (revenue up 18.8 percent, gross profit up 32.7 percent, operating expenses down 9.8 percent, operating loss halved) and the words 'the cost base is largely fixed'. Per-vehicle figures appear only as reported in a monthly or annual results release, labelled and reconciled there.",
    "Roadmap wording: British Columbia and Alberta now; Manitoba next (dealer permit application under way with the regulator, office inside the OPENLANE Winnipeg auction facility arranged, opening targeted for December 2026 when the permit is granted; also serves Saskatchewan and northwestern Ontario); Ontario registration under way, targeted for 2027, subject to registration and capital; then the Maritimes; the United States from 2028, after the Canadian roll-out. No Texas, no Quebec, never Washington State, no US detail beyond that line.",
    "Lenders named publicly: RBC, Santander, iA Auto Finance, Eden Park, LendCare, Rifco and Iceberg (seven). No others, and never 'half of Canada's auto lenders'.",
    "Hasneen Jalil leads technology and the demand engine; never CTO. Lead generation, the CRM and the AI sales agents run on one platform; nothing about who owns the supplier. Matthew's bio: his family owned and operated the Vancouver Auto Auction for 28 years and he was part of its $50 million sale to ADESA (now OPENLANE); he led the $56 million sale of Global Plastics to Kinderhook; he was part of the approximately $300 million sale of Dispensing Dynamics International (DDI) to Hunter Industries. No other company boards.",
    "Operating metrics are management information, unaudited, defined once and reported every month in the monthly results release, historical only. The first monthly results release is 10 November 2026 (October 2026).",
    "No share-price target, no valuation line, no financing terms, and no statement about who has been buying or selling the stock, anywhere.",
    "Forward-looking material carries the legend and points to the assumptions and the risk factors in the Filing Statement.",
    "No competitor is named or described on the investor site. Industry statistics with a named source are fine; other companies are not.",
    "Nothing about an OTC quotation, DTC eligibility or any United States structure until a release carries it.",
    "No em dashes or en dashes. Canadian spelling.",
]

FLI_LEGEND = (
    "This page contains forward-looking statements, including statements about planned markets, licensing, "
    "operating metrics and financing. They are based on management's current expectations "
    "and assumptions, are not guidance, and are subject to the risks described in OCAL's Filing Statement dated "
    "9 July 2026 and its continuous disclosure on SEDAR+. Actual results may differ materially. OCAL does not "
    "undertake to update them except as required by law."
)

NON_IFRS_NOTE = (
    "Vehicles funded and delivered is a supplementary financial measure, and average vehicle selling price, gross profit per vehicle "
    "and gross margin per vehicle are non-GAAP financial measures or ratios; none is a measure defined under IFRS. OCAL calculates them "
    "as described on the Operating metrics page, applies the same definitions every period, reports them unaudited, and reconciles the "
    "per-vehicle figures to the revenue and gross profit lines of its financial statements in the release that carries them. They should "
    "be read with the financial statements and MD&A filed on SEDAR+."
)

NAV = [
    ("Why OCAL", "/why-ocal/"),
    ("How it works", "/how-it-works/"),
    ("Stock", "/stock/"),
    ("Financials", "/financials/"),
    ("Metrics", "/operating-metrics/"),
    ("News", "/news/"),
    ("Governance", "/governance/"),
    ("FAQ", "/faq/"),
    ("Contact", "/contact/"),
]

FOOTER_COLS = [
    ("Company", [("Why OCAL", "/why-ocal/"), ("How it works", "/how-it-works/"), ("Leadership", "/leadership/"), ("Governance", "/governance/"), ("Company facts", "/facts/"), ("Fact sheet", "/fact-sheet/")]),
    ("Investors", [("Stock information", "/stock/"), ("Financial reports", "/financials/"), ("Operating metrics", "/operating-metrics/"), ("Presentations", "/presentations/"), ("Events", "/events/")]),
    ("News and contact", [("News releases", "/news/"), ("Investor FAQ", "/faq/"), ("Email alerts", "/subscribe/"), ("Contact IR", "/contact/"), ("Legal", "/legal/")]),
]

# Public news releases since listing (Newsfile per-release URLs captured 4 November 2026). Newest first.
# Where a release was corrected or reissued (13 and 14 August; 15 and 22 September), the final version is listed.
NEWS = [
    ("2026-11-03", "OCAL Financial Reports a Historical Repossession Rate Under One Percent, Highlighting the Strength of Its Asset-Light Automotive Financing Platform, and Announces Meeting Date for Its 2026 Annual General and Special Meeting", "/news/2026-11-03-repossession-rate-and-agm/", "Operating update"),
    ("2026-10-22", "OCAL Financial Introduces OCAL Showroom, a Live Virtual View of Its Dealership Operations", "https://www.newsfilecorp.com/release/320374/OCAL-Financial-Introduces-OCAL-Showroom-a-Live-Virtual-View-of-Its-Dealership-Operations", "Operations"),
    ("2026-10-13", "OCAL Financial Outlines Its Integrated AI Demand Engine", "https://www.newsfilecorp.com/release/318701/OCAL-Financial-Outlines-Its-Integrated-AI-Demand-Engine", "Technology"),
    ("2026-10-06", "OCAL Financial Surpasses 1,250 Funded Vehicle Deals", "https://www.newsfilecorp.com/release/317641/OCAL-Financial-Surpasses-1250-Funded-Vehicle-Deals", "Operating update"),
    ("2026-10-01", "OCAL Financial to Present at The 2026 Cantech Investment Conference in Toronto", "https://www.newsfilecorp.com/release/316906/OCAL-Financial-to-Present-at-The-2026-Cantech-Investment-Conference-in-Toronto", "Events"),
    ("2026-09-29", "OCAL Financial Offers a Digital Inventory of 3,000+ Vehicles via OPENLANE, With Zero Standing Inventory", "https://www.newsfilecorp.com/release/316470/OCAL-Financial-Offers-a-Digital-Inventory-of-3000-Vehicles-via-OPENLANE-With-Zero-Standing-Inventory", "Operations"),
    ("2026-09-22", "OCAL Financial Explains Its Proprietary Knowledge Base, the Data Asset Behind Its AI", "https://www.newsfilecorp.com/release/315409/OCAL-Financial-Explains-Its-Proprietary-Knowledge-Base-the-Data-Asset-Behind-Its-AI", "Technology"),
    ("2026-09-08", "OCAL Financial Appoints Ryan McDonald as Vice President of Sales", "https://www.newsfilecorp.com/release/313345/OCAL-Financial-Appoints-Ryan-McDonald-as-Vice-President-of-Sales", "People"),
    ("2026-09-03", "OCAL Financial Launches Redesigned Website Built for Car Buyers and Investors", "https://www.newsfilecorp.com/release/312785/OCAL-Financial-Launches-Redesigned-Website-Built-for-Car-Buyers-and-Investors", "Corporate"),
    ("2026-08-29", "OCAL Financial Launches Video-First Brand Campaign With DIBO Marketing and Engages Signal Capital for Investor Relations", "https://www.newsfilecorp.com/release/312032/OCAL-Financial-Launches-VideoFirst-Brand-Campaign-With-DIBO-Marketing-and-Engages-Signal-Capital-for-Investor-Relations", "Corporate"),
    ("2026-08-25", "OCAL Financial Common Shares Now Trading on the Frankfurt Stock Exchange", "https://www.newsfilecorp.com/release/311394/OCAL-Financial-Common-Shares-Now-Trading-on-the-Frankfurt-Stock-Exchange", "Listing"),
    ("2026-08-18", "OCAL Financial Describes CBIS, the System That Runs Its Operations and Data", "https://www.newsfilecorp.com/release/310239/OCAL-Financial-Describes-CBIS-the-System-That-Runs-Its-Operations-and-Data", "Technology"),
    ("2026-08-14", "OCAL Financial Adds AI Sales-Agent Technology Built Around Its Proprietary Knowledge Base (correction from source)", "https://www.newsfilecorp.com/release/309652/CORRECTION-FROM-SOURCE-OCAL-Financial-Adds-AI-SalesAgent-Technology-Built-Around-Its-Proprietary-Knowledge-Base", "Technology"),
    ("2026-08-11", "OCAL Financial Explains Its Credit and Lender-Routing System, and the Underserved Market It Serves", "https://www.newsfilecorp.com/release/309006/OCAL-Financial-Explains-Its-Credit-and-LenderRouting-System-and-the-Underserved-Market-It-Serves", "Operations"),
    ("2026-08-06", "OCAL Financial Describes the Voice AI Behind Its Lead Engagement and Provides Business Update", "https://www.newsfilecorp.com/release/307662/OCAL-Financial-Describes-the-Voice-AI-Behind-Its-Lead-Engagement-and-Provides-Business-Update", "Corporate"),
    ("2026-08-04", "OCAL Financial Explains How Its Integrated Model Differs From Online Auto Retailers, Brokers and Fintech Lenders", "https://www.newsfilecorp.com/release/307659/OCAL-Financial-Explains-How-Its-Integrated-Model-Differs-From-Online-Auto-Retailers-Brokers-and-Fintech-Lenders", "Operations"),
    ("2026-07-30", "OCAL Financial Outlines How Its Virtual, Finance-First Model Differs From the Traditional Dealership", "https://www.newsfilecorp.com/release/307230/OCAL-Financial-Outlines-How-Its-Virtual-FinanceFirst-Model-Differs-From-the-Traditional-Dealership", "Operations"),
    ("2026-07-28", "OCAL Financial Details Its End-to-End Digital Vehicle-Financing Process", "https://www.newsfilecorp.com/release/306770/OCAL-Financial-Details-Its-EndtoEnd-Digital-VehicleFinancing-Process", "Operations"),
    ("2026-07-23", "OCAL Financial Inc. Provides Corporate Overview Following TSX Venture Exchange Listing", "https://www.newsfilecorp.com/release/306175/OCAL-Financial-Inc.-Provides-Corporate-Overview-Following-TSX-Venture-Exchange-Listing", "Corporate"),
    ("2026-07-21", "OCAL Financial Inc. Completes Qualifying Transaction and Begins Trading on the TSX Venture Exchange", "https://www.newsfilecorp.com/release/305866/OCAL-Financial-Inc.-Completes-Qualifying-Transaction-and-Begins-Trading-on-the-TSX-Venture-Exchange", "Listing"),
]
# CQ: each new release gets its own page at /news/YYYY-MM-DD-slug/ on the pattern of the 3 November 2026 page below; earlier releases link to Newsfile.

DOCUMENTS_SOURCE = r"C:\Users\matth\OneDrive\OCAL\Investor Relations\IR Presentations & Docs"
# (kicker, title, body, filename). build_site.py copies each file from DOCUMENTS_SOURCE into site/assets/documents and links it by this exact name.
DOCUMENTS = [
    ("DECK", "Investor presentation, October 2026", "The current corporate presentation on the audited fiscal 2025 and fiscal 2024 statements: the problem, the platform, the solution, the thesis, the roadmap and the people. Dated and versioned on the cover.", "2026-10-30 OCAL Investor Presentation (October 2026).pdf"),
    ("ONE PAGE", "Elevator pitch, October 2026", "The company in sixty seconds: the four customer problems, approval first and then the vehicle, the audited proof, and where it goes next. Print it, forward it.", "2026-10-30 OCAL Elevator Pitch (one page).pdf"),
    ("FOUR PAGES", "Investor brief, October 2026", "The full case with sources: the problem, the platform, what the customer gets, traction and operating leverage, why now, the roadmap and the people.", "2026-10-30 OCAL Investor Brief (four pages).pdf"),
    ("LONG FORM", "Long form investor briefing, October 2026", "For investors who want everything: market, model, lenders, technology, the audited numbers, roadmap, people, capital structure, risks and the questions investors ask, answered.", "2026-10-30 OCAL Long Form Investor Briefing (October 2026).pdf"),
    ("Q AND A", "Investor questions and answers", "The questions investors ask on calls, answered from the public record: the business model, growth, the shares, governance and disclosure.", "2026-10-30 OCAL Investor Questions and Answers (public).pdf"),
]

EVENTS = [
    ("2026-11-10", "October 2026 monthly results release (the first monthly operating update)", "The first monthly results release: vehicles funded and delivered, average vehicle selling price, gross profit per vehicle and gross margin for October 2026, under the definitions on the Operating metrics page, with the prior month beside each figure.", "upcoming"),
    ("2026-12-10", "Annual general and special meeting of shareholders", "9:00 am Vancouver time, Suite 1600, 925 West Georgia Street, Vancouver. Record date 2 November 2026. Business: set the number of directors at four, elect the directors, approve a new omnibus equity incentive plan and reappoint DMCL LLP as auditor. The management information circular and form of proxy are sent to shareholders and filed on SEDAR+ before the meeting; the voting results are posted here afterwards.", "upcoming"),
    ("2026-12-29", "Audited fiscal 2026 results and MD&A (filing deadline)", "Year ended 31 August 2026. Statements posted here the day they are filed, with a plain-language summary and an email to the list.", "upcoming"),
    ("2027-01-29", "First quarter fiscal 2027 interim results (filing deadline)", "Quarter ended 30 November 2026.", "upcoming"),
    ("2026-11-03", "News release: repossession rate under one percent; AGM date set", "Fewer than one percent of the vehicle loans arranged since 2021 have resulted in repossession and about 99 percent of signed contracts were funded (2021 to 30 September 2026, management information); more than 1,500 funded vehicle transactions; the annual general and special meeting set for 10 December 2026. [Read the release](/news/2026-11-03-repossession-rate-and-agm/).", "past"),
    ("2026-10-08", "Cantech Investment Conference, Toronto", "Mehdi Moghareh presented OCAL at 4:00 pm ET, Track 3. The presentation was not recorded. The current investor presentation is on the Presentations page.", "past"),
    ("2026-08-25", "Frankfurt Stock Exchange listing", "OCAL began trading in Frankfurt under the symbol JC3.", "past"),
    ("2026-07-21", "TSX Venture Exchange listing", "First day of trading as OCAL on TSXV Tier 2.", "past"),
]

# Each link opens SEDAR+ (the public search page); the issuer profile is found by searching "OCAL Financial Inc.".
# CQ or Has: when a direct document URL is captured from the profile, paste it in place of SITE["sedar"] and rebuild.
FILINGS = [
    ("Audited financial statements, year ended 31 August 2025", "Annual", "DMCL LLP, auditor", SITE["sedar"]),
    ("Management's discussion and analysis, year ended 31 August 2025", "Annual", "", SITE["sedar"]),
    ("Interim financial statements and MD&A, nine months ended 31 May 2026", "Interim", "Unaudited", SITE["sedar"]),
    ("Filing Statement dated 9 July 2026 (qualifying transaction)", "Listing", "The document to read first: business, risk factors, capital structure, escrow, audit committee charter", SITE["sedar"]),
    ("Material change reports and news releases", "Continuous", "Every release is filed on SEDAR+ the day it is issued", SITE["sedar"]),
]

TEAM = [
    ("Mehdi Moghareh", "Co-Founder and Chief Executive Officer", "Mehdi Moghareh.png",
     "Twenty-five years inside Canadian automotive retail, in Vice President and General Manager roles across eight brands including Porsche, Infiniti, Volkswagen, Nissan, Mazda, Mitsubishi, Kia and Hyundai. He has bought and sold dealerships, run sales floors, finance offices and sourcing desks, and built OCAL's lender panel. He took one Nissan store from 30 cars a month to 230 in two years by getting more lenders to say yes. He started OCAL in 2021 because he had seen what inventory does to a balance sheet, and he leads operations, lenders and suppliers."),
    ("Matthew Friesen", "Co-Founder, Executive Chairman and Director", "Matthew Friesen.png",
     "Raised inside the wholesale engine of the industry: his family owned and operated the Vancouver Auto Auction for 28 years and he ran its sales desk. He was part of the $50 million sale of the Vancouver Auto Auction to ADESA (now OPENLANE); led the $56 million sale of Global Plastics to Kinderhook; and was part of the approximately $300 million sale of Dispensing Dynamics International (DDI) to Hunter Industries. At OCAL he led the go-public execution and directs strategy and capital planning."),
    ("Terence Lee, CPA", "Chief Financial Officer", "",
     "Fifteen years of financial management, accounting and public-company reporting. BBA, Simon Fraser University; Diploma in Accounting, University of British Columbia. He is responsible for OCAL's financial reporting and continuous disclosure filings, and confirms every operating metric against the ledger before it is released."),
    ("Hasneen Jalil", "Leads technology and the demand engine", "Hasneen Jalil.png",
     "Leads technology and the demand engine: lead generation, the CRM, the AI sales agents, platform architecture, security and delivery, on one platform."),
    ("Ryan McDonald", "Vice President of Sales", "",
     "Appointed September 2026. More than 25 years of leadership across automotive, recreational vehicle, marine, powersports and industrial distribution businesses, including general manager roles at Applewood Performance Centre, Genesis Vancouver, Boundary Hyundai, Fraserway RV, Galaxy RV and Go RV and Marine, running operations of up to $50 million in annual revenue and 55 people. He has consolidated multi-location dealerships onto one CRM and brings direct non-prime finance experience to OCAL's sales floor."),
    ("Shushu Feng", "Investor Relations Manager, Signal Capital Advisors", "Shushu Feng.jpg",
     "Ten years of investor relations across seventy public companies on the NYSE, Nasdaq, TSX, TSXV and CSE. Books investor calls, runs the weekly update and fact-checks every number within the hour."),
]

BOARD = [
    ("Matthew Friesen", "Executive Chairman and Director", "Not independent", "Audit; Compensation, Governance and Nominating"),
    ("Mehdi Moghareh", "Director and Chief Executive Officer", "Not independent", ""),
    ("Michael Stier", "Independent Director", "Independent", "Chair of the Audit Committee; Chair of the Compensation, Governance and Nominating Committee. Fifteen years in capital markets; former CIBC advisor."),
    ("Robert Birmingham", "Independent Director", "Independent", "Audit; Compensation, Governance and Nominating"),
]

# ---------------------------------------------------------------------------------------------
# PAGES
# ---------------------------------------------------------------------------------------------

PAGES = []

def page(**kw):
    PAGES.append(kw)
    return kw

# ------------------------------------------------------------------ HOME
page(
    slug="/",
    nav_label="Investors",
    title="OCAL Financial (TSXV: OCAL) Investor Relations",
    description="OCAL Financial (TSXV: OCAL): the technology-enabled automotive financing and purchasing platform. Approval first, zero standing inventory, audited growth.",
    hero={
        "kicker": "TSXV: OCAL  ·  FSE: JC3  ·  INVESTOR RELATIONS",
        "h1": "We solve the problem first. <em>The vehicle follows.</em>",
        "sub": "OCAL Financial is a technology-enabled automotive financing and purchasing platform. We redesigned the entire vehicle purchasing process around the customer's financial eligibility, needs and convenience: approved by a lender first, then the one vehicle that approval supports, sourced through OPENLANE and delivered to the driveway anywhere in the province. Zero standing inventory, no loans on our books, and audited statements on the public record.",
        "ctas": [("Why OCAL", "/why-ocal/", True), ("Download the fact sheet", "/fact-sheet/", False), ("Get email alerts", "/subscribe/", False)],
    },
    blocks=[
        ("widget", "kpi-strip"),
        ("kicker", "THE COMPANY IN FOUR NUMBERS"),
        ("kpis", [
            ("$6.48M", "FY2025 revenue, audited", "Year ended 31 August 2025, up 19% from $5.45M, with no new market opened"),
            ("1,500+", "funded vehicle deals since 2021", "Two provinces, no growth capital, 17.6% repeat and referral (trailing twelve months)"),
            ("$0", "standing inventory", "A vehicle is on our books for three to five days, bought only after its buyer is approved"),
            ("$0", "consumer loans held", "Lenders fund the contract and carry the credit risk; OCAL earns the margin on every transaction"),
        ]),
        ("note", FUNDED_DEF),
        ("kicker", "WHY INVESTORS LEAN IN"),
        ("cards", [
            ("01", "The problems OCAL solves", "Some people cannot get approved where they shop. Some cannot find the right vehicle at a payment they can carry. Some live hours from the nearest lot. Some have never had financing explained to them. OCAL solves each of these, in that order, and every one solved is a funded transaction.", "/why-ocal/#problem"),
            ("02", "Proven commercial traction", "More than 1,500 funded vehicle transactions since 2021 and audited revenue of $6.48 million in fiscal 2025, up 19 percent, from two provinces with no growth capital. OCAL generates revenue today; it is not developing a product.", "/why-ocal/#traction"),
            ("03", "Operating leverage", "The cost base is largely fixed: licences, people, systems and an office that do not grow with the count. In fiscal 2025 revenue rose 18.8 percent and gross profit 32.7 percent while operating expenses fell 9.8 percent, and the operating loss halved. As volume increases the Company has the potential to spread its fixed costs across more vehicle sales. The number that moves is the count.", "/why-ocal/#economics"),
        ]),
        ("kicker", "THE AUDITED RESULTS"),
        ("h2", "Fiscal 2025 beside fiscal 2024, from the audited statements"),
        ("p", "Investors used to spend the first half hour of every call rebuilding OCAL's numbers from scraps. Here are the audited totals for the year ended 31 August 2025 beside the year before (DMCL LLP): revenue up 19 percent, gross profit up 33 percent, operating expenses down 10 percent, the operating loss halved and cash from operations positive. From 10 November 2026, the operating metrics for each closed month are published in a monthly results release under fixed definitions and kept on the Operating metrics page."),
        ("widget", "audited-table"),
        ("p", "[Operating metrics: definitions, cadence and the history](/operating-metrics/). Every figure above is in the statements filed on [SEDAR+](" + SITE["sedar_profile"] + ") under OCAL Financial Inc.; analysts can pull the filed data there. " + SITE["sedar_profile_note"]),
        ("kicker", "LATEST NEWS"),
        ("widget", "news-list"),
        ("kicker", "THE MODEL IN ONE LINE"),
        ("quote", "Many of the people who come to us face challenges with financing approval, finding the right vehicle, accessing a dealership or simply understanding their financing options. We solve the problem first and the vehicle follows.", "Mehdi Moghareh, Chief Executive Officer"),
        ("kicker", "WHERE TO START"),
        ("cards", [
            ("READ", "The investment case", "The problem, the platform, the solution and the thesis: proven traction, operating leverage, and a roadmap that opens one province at a time.", "/why-ocal/"),
            ("CHECK", "Stock and share structure", "Live TSXV chart, listings, shares outstanding, warrants, options, escrow and the July 2026 financing.", "/stock/"),
            ("VERIFY", "Financial reports", "Audited FY2025 statements, MD&A, interims and the Filing Statement, with direct SEDAR+ links.", "/financials/"),
            ("MEET", "Leadership and board", "One founder ran the dealerships. The other one's family ran the auction. Together they removed everything in between.", "/leadership/"),
        ]),
        ("widget", "events"),
        ("widget", "subscribe"),
        ("cta", "Thirty minutes with the founders", "The next step for a serious investor is a call with Mehdi and Matthew, the Showroom on the screen with live files, and the model behind every number on this site.", [("Book an investor call", SITE["booking_link"], True), ("Email investors@ocal.ca", "mailto:investors@ocal.ca", False)]),
    ],
)

# ------------------------------------------------------------------ WHY OCAL
page(
    slug="/why-ocal/",
    nav_label="Why OCAL",
    title="Why Invest in OCAL Financial (TSXV: OCAL)",
    description="Why invest in OCAL: the problem, the platform, the solution and the thesis. Approval first, zero standing inventory, audited growth, operating leverage.",
    hero={
        "kicker": "THE INVESTMENT CASE",
        "h1": "Problem. Platform. <em>Solution. Thesis.</em>",
        "sub": "Most Canadians still buy a vehicle the way the industry was built: drive to a lot, choose from what is parked there, and let the finance desk fit a loan to that vehicle. OCAL redesigned the entire process around the customer's financial eligibility, needs and convenience. Here is the problem, the platform that solves it, what the customer gets, and the economics that make investors lean in.",
        "ctas": [("Download the investor brief", "/presentations/", True), ("Book a call", SITE["booking_link"], False)],
    },
    blocks=[
        ("kpis", [
            ("$6.48M", "FY2025 revenue, audited", "up 19% from $5.45M"),
            ("12.5%", "gross margin, rising", "from 11.2% the year before"),
            ("1,500+", "funded deals", "since April 2021, two provinces"),
            ("3 to 5", "days a car is on our books", "purchase to delivery"),
        ]),
        ("note", FUNDED_DEF),
        ("anchor", "problem"),
        ("h2", "1. The problem OCAL exists to solve"),
        ("p", "Four problems bring a customer to OCAL. They cannot get approved where they shop. They cannot find the right vehicle at a payment they can carry. They live hours from the nearest lot, with few options and no delivery. Or nobody has ever explained to them how vehicle financing works. The industry was built to sell what is parked on the lot, so the lot, not the customer, drives the sale: the average dealership holds a used vehicle 48 days and pays about $90 of floorplan interest on it to clear about $1,234 of gross (Presidio-NCM, Cox, 2024 to 2026). 68 percent of Canadians say they do not trust dealerships to act in their interest (Angus Reid, 2025), and 48 percent want to apply for credit online but only 33 percent can (Cox, 2026). The demand to buy differently was never the problem. The process was."),
        ("anchor", "platform"),
        ("h2", "2. The platform"),
        ("p", "OCAL is a technology-enabled automotive financing and purchasing platform. One workflow carries the customer from a credit application on their phone to lender approval, financial guidance in plain terms, vehicle sourcing, digital contracting and delivery anywhere in the province. The approval comes first, so the vehicle is chosen to fit the customer's eligibility and budget, never the other way around. OPENLANE is OCAL's auction and sourcing channel: more than 3,000 vehicles are visible on its Canadian marketplace on a typical day, and none of them is on OCAL's balance sheet. OCAL is the licensed motor dealer of record on every transaction, holds no standing inventory, and owns a vehicle for three to five days between purchase and delivery, financed on a purchase line for exactly those days. The lender funds the contract and carries the credit risk."),
        ("anchor", "customer"),
        ("h2", "3. The solution, as the customer sees it"),
        ("bullets", [
            ("They know what they can afford before they fall in love with a truck.", "The approval comes first, so nobody is steered into the vehicle someone else needs to move. The choice is not forty vehicles on a lot: it is any vehicle on OPENLANE's marketplace that fits the approval, bought the day they say yes."),
            ("Speed, without a visit.", "Application to approval in hours, approval to delivery in three to five business days anywhere in the province, every step on the phone. The AI agent answers the 3 am application from the night-shift worker who used to wait until 9."),
            ("The right lender for their credit, prime to non-prime.", "Seven lenders are on our panel, prime to non-prime: RBC, Santander, iA Auto Finance, Eden Park, LendCare, Rifco and Iceberg. A prime customer gets a prime rate; a near-prime file can still be placed with a finance company on the panel, explained in plain terms, not a high-rate note with a GPS cut-off switch."),
        ]),
        ("anchor", "traction"),
        ("anchor", "economics"),
        ("h2", "4. Traction and operating leverage"),
        ("p", "OCAL already generates revenue: more than 1,500 funded vehicle transactions since 2021 and audited revenue of $6.48 million in fiscal 2025, up 19 percent, on an asset-light structure with no standing inventory. Gross profit rose 33 percent to $810,751 and the gross margin to 12.5 percent, and 87 percent of that gross profit came from finance, insurance and protection products, the layer that sits on top of every vehicle sale. Operating expenses fell 9.8 percent to $1,114,195 in the same year, the operating loss halved, and cash from operating activities turned positive. The cost base is largely fixed and does not grow with the count, so as volume increases the Company has the potential to spread it across more vehicle sales. The constraint has never been demand. It is licences, people and lender capacity, and all three are being added now."),
        ("table", ["What to watch", "Where to find it", "What it means"], [
            ["Vehicles funded and delivered", "[Operating metrics](/operating-metrics/), reported every month from the 10 November 2026 release", "The count is the number the model turns on"],
            ["Gross profit per vehicle and gross margin", "[Operating metrics](/operating-metrics/), under fixed definitions", "Vehicle margin, lender reserve and protection products; most of the gross profit sits in the finance and protection layer"],
            ["Operating expenses", "Audited statements and MD&A", "$1,114,195 in fiscal 2025, down 9.8 percent while revenue grew 18.8 percent; largely fixed, so each added vehicle carries more of it"],
        ], "Operating metrics are management information, unaudited, historical only, and are published in each monthly results release under the definitions on the Operating metrics page."),
        ("anchor", "payment"),
        ("h2", "5. Why now"),
        ("bullets", [
            ("The payment is the purchase.", "77% of Canadian new-vehicle buyers finance or lease and 57% of new loans run 84 months or longer, at an average payment near $880 (J.D. Power, 2025). The average new auto loan reached $36,979 in mid-2026 while new loan openings fell 9.2% (Equifax): bigger loans, fewer approvals. Approval first sets the payment before the car is chosen, the only order that works for that buyer."),
            ("The banks narrowed the credit box.", "Six in ten households earn under $100,000 and 28% of credit-active Canadians sit below prime, about nine million people (TransUnion). Several large banks have narrowed their indirect auto lending. OCAL's panel covers both ends, prime and non-prime, through seven lenders."),
            ("The supply is where we buy.", "Dealer trade-ins, off-lease returns, retired rental units and repossessions flow through the wholesale auctions, and OPENLANE is the largest of them in Canada. Only licensed dealers can buy there, and OCAL buys against an approval, never for a lot."),
            ("Buyers want the financing step online, and do not trust the desk.", "48% of buyers want to apply for credit online but only 33% can (Cox, 2026); 68% of Canadians do not trust dealerships to act in their interest (Angus Reid, 2025). The step buyers most want online is the one we moved first."),
        ]),
        ("anchor", "demand"),
        ("h2", "6. One machine, copied"),
        ("p", "Every new market is a copy of the first: a licence, a bond, a small office and a small local team, not a building and not a lot. Canadians buy about three million used vehicles a year, more than $100 billion worth, so OCAL needs only a fraction of one percent of any market it enters."),
        ("table", ["Market", "Status at 4 November 2026", "Planned opening", "What it adds"], [
            ["British Columbia and Alberta", "Licensed, five years of history", "Home base", "The proven machine; the head office in Vancouver and the hub in Edmonton"],
            ["Manitoba", "Dealer permit application under way with the regulator; office inside the OPENLANE Winnipeg auction facility arranged", "Next: targeted for December 2026, when the permit is granted", "Serves Saskatchewan and northwestern Ontario too"],
            ["Ontario", "Registration under way", "Targeted for 2027, subject to registration and capital", "About 40% of Canada's market"],
            ["The Maritimes", "Planned", "After Ontario", "Same playbook: one licence, one office, one local team"],
            ["United States", "Planned", "From 2028, after the Canadian roll-out", "The same model: a licence, lender access and the platform"],
        ], "Regulators set licensing timelines. Openings are management's targets and depend on licensing, lenders and capital. See the forward-looking statement at the foot of this page."),
        ("anchor", "plan"),
        ("h2", "7. The plan"),
        ("p", "The Manitoba dealer permit application is under way with the regulator, with an office inside the OPENLANE Winnipeg auction facility arranged; opening is targeted for December 2026, when the permit is granted. Ontario registration is under way, targeted for 2027, subject to registration and capital. The Maritimes follow Ontario, and the United States is on the roadmap from 2028, after the Canadian roll-out. Management's plan assumes growth capital in fiscal 2027; no terms have been set, and nothing on this site is an offer of securities. OCAL does not publish a forecast: the audited statements and the monthly operating update show the machine as it runs."),
        ("anchor", "moat"),
        ("h2", "8. Why it is hard to copy quickly"),
        ("p", "The licences to sell and finance vehicles remotely took two years to win in British Columbia. We hold BC and Alberta, with Manitoba and Ontario under way. Seven lenders, prime to non-prime, are on our panel. We have more than 1,500 funded transactions of data on which leads convert, which lenders approve whom and what a car is worth before anyone else bids. Lead generation, the CRM and the AI sales agents run on one platform: every deal on one screen, and an AI agent takes the 3 am lead (a lead answered inside five minutes is about 21 times more likely to qualify than one answered after thirty, per the MIT and InsideSales lead response study)."),
        ("anchor", "window"),
        ("h2", "9. The thesis"),
        ("p", "A revenue-generating, asset-light platform with a largely fixed cost base and a model designed to scale without the inventory cost of the industry it serves. The founders hold about 54 percent, escrowed for 36 months under exchange policy, and have not sold a share."),
        ("cta", "Read the four-page brief, then call", "The investor brief carries the full case with sources. The fact sheet is one page. The founders are thirty minutes away.", [("Presentations and documents", "/presentations/", True), ("Book an investor call", SITE["booking_link"], False)]),
        ("note", FLI_LEGEND),
        ("note", "Market facts from Statistics Canada, TransUnion, Equifax, J.D. Power, Cox Automotive, Angus Reid and Presidio-NCM. Audited figures from the financial statements filed on SEDAR+."),
    ],
)

# ------------------------------------------------------------------ HOW IT WORKS
page(
    slug="/how-it-works/",
    nav_label="How it works",
    title="How OCAL Works | OCAL Financial (TSXV: OCAL)",
    description="How OCAL finances and sources a vehicle, approval first: apply, qualify, approve, match through OPENLANE, deliver. Who carries the risk, how OCAL earns.",
    hero={
        "kicker": "THE MODEL",
        "h1": "Five steps. No lot. <em>No loan book.</em>",
        "sub": "OCAL is the licensed motor dealer of record on every transaction. The customer is approved by a lender first; only then do we buy the vehicle, at wholesale, against that approval. Here is each step, who does it and what it costs.",
        "ctas": [("See the operating metrics", "/operating-metrics/", True)],
    },
    blocks=[
        ("steps", [
            ("1", "Apply", "A full credit application on the customer's phone, from any credit tier, through OCAL's own lead engine."),
            ("2", "Qualify", "AI first contact within minutes, day or night, then a specialist verifies and warms the file."),
            ("3", "Approve", "The file goes to the lender that fits, prime, near-prime or non-prime. The lender sets the rate and the amount."),
            ("4", "Match", "Only now do we shop: two or three vehicles from OPENLANE's marketplace that fit the approval, presented through our own CRM. The customer can be as specific as they like; we are buying for one person, not for a lot."),
            ("5", "Deliver", "Digital signing, we buy and recondition the vehicle, and deliver it anywhere in the province. The test drive is in their driveway. The trade-in leaves on the same truck."),
        ]),
        ("h2", "Where the cars come from"),
        ("p", "OPENLANE, formerly ADESA Canada, is the largest wholesale vehicle marketplace in the country and OCAL's auction and sourcing channel. Dealer trade-ins, off-lease returns, retired rental units, repossessions and consignments flow into it at wholesale, and only licensed dealers can buy there. On a typical day more than 3,000 vehicles are visible on its Canadian marketplace. OCAL owns none of them: a vehicle is bought only when a specific approved customer is ready to buy it, so it is on our books for days, never on speculation. OCAL's own representatives review units at the lanes and run the bidding. Zero standing inventory does not mean zero cars. It means no car is bought before its buyer is approved. We stock access."),
        ("h2", "Who carries the risk"),
        ("table", ["Risk", "Who holds it", "Why"], [
            ["Credit risk on the loan", "The lender", "OCAL originates the contract for a panel of prime, near-prime and non-prime lenders and holds none of the paper. Fewer than one percent of the vehicle loans arranged through OCAL's platform from its first funded transaction in 2021 to 30 September 2026 have resulted in repossession (management information, based on lender reporting)."],
            ["Inventory risk", "Nobody, for more than a few days", "A vehicle is bought against a locked approval and delivered after reconditioning and inspection. Used-vehicle price swings touch a car that is ours for three to five days far less than a lot that holds one for 48."],
            ["Floorplan interest", "Minimal", "A purchase line funds the vehicle for the days OCAL owns it, not for months."],
            ["Regulatory", "OCAL", "Licensed motor dealer in British Columbia (VSA D50207) and Alberta (AMVIC B2036050); each new province is a new registration, bonding where required and a compliant presence."],
        ], ""),
        ("h2", "How OCAL earns on each transaction"),
        ("table", ["Layer", "What it is"], [
            ["Vehicle margin", "The difference between the wholesale price plus reconditioning and the retail price to the approved customer. Deliberately modest: the volume carrier."],
            ["Lender reserve and program incentives", "Paid by the lender for originating the contract at the program's terms. Part of every funded deal."],
            ["Protection products", "Extended warranty, gap coverage and similar, sold at contracting, with a very high attach rate because the budget is set before the car is chosen."],
            ["Delivery, documentation and permitted fees", "Charged where permitted and disclosed by province."],
        ], "The sum of these layers per funded deal is reported as gross profit per vehicle on the Operating metrics page. Retail vehicle sales carry the top line, which is why the consolidated gross margin reads low while the margin per transaction reads like a finance office's."),
        ("h2", "The technology, plainly"),
        ("p", "Capable AI tools are available to anyone, so the advantage is not any one piece of software. It is the combination of licences, lender approvals, five years of transaction data and a team that has done more than 1,500 of these deals. The point of the technology is operating leverage: more funded vehicles per employee, so capacity grows with demand rather than payroll. The pieces: an AI agent that answers every lead in seconds, a credit-intelligence engine that routes each file to the lender most likely to fund it, the OCAL Showroom view of every desk and every deal, and a CRM built for remote, approval-first transactions."),
        ("h2", "The customer, in one story"),
        ("p", "A 34-year-old in Red Deer with a near-prime file needs a truck for work. She applies on Tuesday evening; an agent responds within a minute and books a call for Wednesday morning. The specialist builds the file, the credit engine routes it to a near-prime lender with an appetite for trucks, and the approval locks on Thursday at a budget and a term she can carry. OCAL's buyer finds a two-year-old half-ton at the OPENLANE Edmonton lane on Friday, inside the budget, with a clean history, and buys it against her approval. She signs remotely the following Tuesday, adds an extended warranty, and takes delivery at her workplace on Thursday. The lender funds OCAL the following Monday. OCAL owned the truck for six days and never owned her loan."),
        ("cta", "See the numbers behind the steps", "Vehicles funded, average vehicle price, gross profit per vehicle and gross margin, published every period under fixed definitions.", [("Operating metrics", "/operating-metrics/", True), ("Why OCAL", "/why-ocal/", False)]),
        ("note", "The repossession rate is management information, unaudited. " + FUNDED_DEF + " Consumer pages for customers are at ocalfinancial.ca; financing is on approved credit and the lender makes the final approval."),
    ],
)

# ------------------------------------------------------------------ STOCK
page(
    slug="/stock/",
    nav_label="Stock",
    title="OCAL Stock: Price, Chart, Share Structure (TSXV: OCAL)",
    description="OCAL share price and chart (TSXV: OCAL, Frankfurt: JC3), shares outstanding, warrants, options, escrow schedule and transfer agent.",
    hero={
        "kicker": "SHARE INFORMATION",
        "h1": "TSXV: <em>OCAL</em>",
        "sub": "Live chart, listings, capitalization and escrow, every line traceable to a filing. Updated " + SITE["facts_date"] + ".",
        "ctas": [("TMX Money quote", SITE["tmx"], True), ("Frankfurt (JC3)", SITE["frankfurt"], False)],
    },
    blocks=[
        ("widget", "tradingview"),
        ("h2", "Listings"),
        ("table", ["Market", "Symbol", "Since", "Identifiers"], [
            ["TSX Venture Exchange, Tier 2", "OCAL", "21 July 2026", "ISIN " + SITE["isin"] + "; CUSIP " + SITE["cusip"]],
            ["Frankfurt Stock Exchange", "JC3", "25 August 2026", "WKN " + SITE["wkn"]],
        ], ""),
        ("h2", "Capitalization"),
        ("table", ["Item", "Figure", "Source"], [
            ["Common shares outstanding", "36,667,803", "Filing Statement; July 2026 closing"],
            ["Founder ownership", "About 54%, held in TSXV Tier 2 value escrow", "Escrow agreement"],
            ["Shares in escrow", "23,638,104 (about 64% of shares outstanding): principals' shares in TSXV Tier 2 value escrow over 36 months, plus legacy capital-pool shares in CPC escrow", "TSXV bulletin; TMX Money"],
            ["Warrants", "11,029,501: 5,000,001 at $0.10 and 6,029,500 at $0.50 expiring 7 July 2028; plus 39,760 finder warrants at $0.50", "Material change report, 22 July 2026"],
            ["Options", "600,000: 450,000 at $0.10 to 11 August 2027 and 150,000 at $0.25 over five years; a further 100,000 at $0.13 to the investor relations firm, subject to exchange acceptance", "Material change report; 29 August 2026 release"],
            ["Fully diluted", "About 48.3 million", "Calculated from the above"],
            ["July 2026 financing", "6,029,500 units at $0.25 for gross proceeds of $1,507,375, each unit one share and one warrant at $0.50 for 24 months; closed 7 July 2026", "Material change report"],
            ["Founder selling since listing", "None. The founders' shares are in escrow.", "SEDI"],
        ], "Figures as at " + SITE["facts_date"] + ", from the Filing Statement, the material change report of 22 July 2026 and the news releases of 6 and 29 August 2026."),
        ("h2", "Escrow"),
        ("p", "23,638,104 shares, about 64 percent of the shares outstanding, are in escrow. The principals' shares are held in TSXV Tier 2 value escrow: 10 percent was released at listing on 21 July 2026 and 15 percent is released every six months after that, over 36 months. The legacy capital-pool shares sit in CPC escrow released over 18 months. The 6,029,500 shares issued in the July 2026 financing become free trading on 8 November 2026, when the standard four-month hold expires. We publish the schedule so that every investor knows when shares become tradable."),
        ("table", ["Value escrow release", "Date", "Share of principals' escrowed shares"], [
            ["At listing", "21 July 2026", "10%"],
            ["Second release", "21 January 2027", "15%"],
            ["Third release", "21 July 2027", "15%"],
            ["Fourth release", "21 January 2028", "15%"],
            ["Fifth release", "21 July 2028", "15%"],
            ["Sixth release", "21 January 2029", "15%"],
            ["Final release", "21 July 2029", "15%"],
        ], "Dates follow the standard TSXV Tier 2 value escrow schedule from the listing date of 21 July 2026. The escrowed securities are described in the Filing Statement on SEDAR+."),
        ("h2", "Buying from the United States"),
        ("p", "OCAL trades on the TSX Venture Exchange and in Frankfurt. Most US brokers can buy TSXV-listed shares directly; ask for the Canadian ticker OCAL on the TSX Venture Exchange."),
        ("h2", "Registered holders, transfer agent and advisors"),
        ("table", ["Role", "Firm"], [
            ["Transfer agent and registrar", "Endeavor Trust Corporation, Vancouver. Registered shareholders contact Endeavor for transfers, lost certificates and address changes."],
            ["Auditor", "DMCL LLP (Dale Matheson Carr-Hilton LaBonte), Vancouver"],
            ["Legal counsel", "Lawson Lundell LLP, Vancouver"],
            ["Investor relations", "Signal Capital Advisors, engaged as announced; Shushu Feng, Investor Relations Manager"],
            ["Market making", "Integral Wealth Securities Limited, engaged August 2026 at $6,000 a month, as announced on 6 August 2026"],
            ["Analyst coverage", "None at this date. We will list every analyst who covers OCAL here, whether we agree with them or not."],
        ], ""),
        ("widget", "subscribe"),
        ("note", "Share price data on this page is supplied by third parties and may be delayed. OCAL does not comment on its share price and does not publish price or valuation targets."),
    ],
)

# ------------------------------------------------------------------ FINANCIALS
page(
    slug="/financials/",
    nav_label="Financials",
    title="OCAL Financial Reports and SEDAR+ Filings (TSXV: OCAL)",
    description="Audited statements, MD&A, interims and the Filing Statement with SEDAR+ links. FY2025 revenue $6.48M audited; FY2026 results due by 29 December.",
    hero={
        "kicker": "FINANCIAL REPORTS",
        "h1": "Audited. Filed. <em>Linked.</em>",
        "sub": "Everything an investor needs to verify what we say, from the Filing Statement to the latest interims, posted here the day it is filed on SEDAR+.",
        "ctas": [("OCAL on SEDAR+", SITE["sedar_profile"], True)],
    },
    blocks=[
        ("p", "**Filed record.** Every figure on this page is from the audited financial statements and MD&A filed on [SEDAR+](" + SITE["sedar_profile"] + ") under OCAL Financial Inc. Analysts can pull the filed data there. " + SITE["sedar_profile_note"]),
        ("kpis", [
            ("$6.48M", "revenue, FY2025 audited", "$6,480,254; up 18.8% from $5,454,893 in FY2024"),
            ("$810,751", "gross profit, FY2025 audited", "12.5% gross margin, up from $610,787 and 11.2%"),
            ("($322K)", "net loss, FY2025 audited", "operating loss $303,444"),
            ("29 Dec 2026", "audited FY2026 due", "Year ended 31 August 2026; MD&A filed with it"),
        ]),
        ("h2", "Two years at a glance, audited"),
        ("table", ["Fiscal year ended 31 August", "FY2024 (audited)", "FY2025 (audited)", "Change", "FY2026"], [
            ["Revenue", "$5,454,893", "$6,480,254", "+18.8%", "Closed 31 August 2026"],
            ["Of which vehicle sales", "$4,774,670", "$5,630,980", "+17.9%", "Audited statements"],
            ["Of which finance, insurance and other", "$680,223", "$849,274", "+24.9%", "and MD&A due"],
            ["Gross profit", "$610,787", "$810,751", "+32.7%", "by 29 December 2026"],
            ["Gross margin", "11.2%", "12.5%", "+1.3 pts", ""],
            ["Of which gross profit from finance, insurance and other", "", "$701,727 (87% of gross profit)", "", ""],
            ["Vehicle write-downs included in cost of sales", "$67,243", "$353,094", "", ""],
            ["Operating expenses", "$1,234,843", "$1,114,195", "(9.8%)", ""],
            ["Operating loss", "($624,056)", "($303,444)", "Halved", ""],
            ["Net loss", "($586,206)", "($322,090)", "Down 45%", ""],
            ["Cash from operating activities", "($85,157)", "$64,121", "Positive", ""],
            ["Cash at year end", "$161,680", "$266,936", "+65%", ""],
        ], "From the audited financial statements for the year ended 31 August 2025 with FY2024 comparatives (DMCL LLP), filed on SEDAR+. Nothing from fiscal 2026 is shown until the audited statements are filed."),
        ("h2", "Interim periods and fiscal 2026"),
        ("p", "The interim financial statements and MD&A for the nine months ended 31 May 2026 are filed on SEDAR+ and listed below. Fiscal 2026 closed on 31 August 2026; the audited annual statements and MD&A are due by 29 December 2026 and will be posted here the day they are filed. This site quotes audited figures only."),
        ("p", "At every reporting date the balance sheet shows a small inventory balance and a matching floorplan balance: the vehicles bought against approved customers and awaiting delivery on that day, and the purchase line that funded them. Days of vehicles, not months. That is what zero standing inventory looks like on a balance sheet."),
        ("h2", "One line on a number you may have seen elsewhere"),
        ("p", "Figures for fiscal 2025 circulated before the audit was complete and differ from the audited figure. The audited figure is $6.48 million. Everything OCAL writes uses the audited figure."),
        ("h2", "Cash, and the going-concern note"),
        ("p", "OCAL is at an early stage as a public company. Its financial statements, audited and interim, carry a going-concern note, which is common for Venture-listed companies at this stage: it says the Company needs volume or capital to fund its plan. The July 2026 financing raised $1.5 million. Management's plan assumes growth capital in fiscal 2027; no terms have been set, and nothing on this site is an offer of securities. The operating metrics are published every period so that progress towards profitability is visible rather than asserted. Cash at each reporting date is in the filed statements linked below; OCAL does not publish cash figures between reporting dates."),
        ("h2", "Documents"),
        ("widget", "filings"),
        ("h2", "Reporting calendar"),
        ("table", ["Period", "Filing", "Deadline"], [
            ["Year ended 31 August 2026", "Audited annual financial statements and MD&A", "29 December 2026"],
            ["Quarter ending 30 November 2026", "Interim financial statements and MD&A", "29 January 2027"],
            ["Quarter ending 28 February 2027", "Interim financial statements and MD&A", "29 April 2027"],
            ["Quarter ending 31 May 2027", "Interim financial statements and MD&A", "30 July 2027"],
        ], "OCAL is a venture issuer: annual filings within 120 days of year end, interims within 60 days of quarter end. Each filing is posted here and emailed to the list the day it is filed."),
        ("widget", "subscribe"),
        ("note", NON_IFRS_NOTE),
    ],
)

# ------------------------------------------------------------------ OPERATING METRICS
page(
    slug="/operating-metrics/",
    nav_label="Operating metrics",
    title="OCAL Operating Metrics (TSXV: OCAL)",
    description="Vehicles funded, average selling price, gross profit per vehicle and gross margin, published monthly under fixed definitions. Historical, unaudited.",
    hero={
        "kicker": "OPERATING METRICS",
        "h1": "Four numbers, <em>every period.</em>",
        "sub": "Anyone can sell a vehicle. What makes OCAL different is the margin per vehicle on a platform that holds no standing inventory, and the fixed cost base that margin has to cover. So we publish the operating metrics in a monthly results release, under fixed definitions, and keep the history here.",
        "ctas": [("Latest news release", "/news/", True)],
    },
    blocks=[
        ("h2", "The audited totals the metrics are built on"),
        ("widget", "audited-table"),
        ("p", "The monthly series starts with October 2026, reported in the monthly results release of 10 November 2026. Until then this page shows the audited fiscal 2025 and fiscal 2024 totals only."),
        ("h2", "Monthly history"),
        ("p", "Each month is added here the day its release is issued, beside the prior month, under the definitions below: vehicles funded and delivered, average vehicle selling price, gross profit per vehicle on both bases and gross margin, with the reconciling items stated. The Chief Financial Officer confirms every figure against the ledger before it is released. Once a metric is reported it is reported every month, including in a slow one."),
        ("h2", "Definitions, fixed"),
        ("table", ["Metric", "How OCAL calculates it"], [
            ["Vehicles funded and delivered", "Retail vehicle sale contracts funded by a lender and delivered to the customer in the calendar month. A deal counts once, in the month the lender funds it."],
            ["Average vehicle selling price", "Vehicle sales revenue in the month divided by vehicles funded and delivered, before taxes and before protection products."],
            ["Deal gross profit per vehicle (management basis)", "Gross profit on the vehicle plus finance, insurance and protection product income, per funded vehicle, before inventory write-downs and before the auction, reconditioning and transport costs that IFRS places in cost of sales. Shown split into vehicle margin and finance, insurance and protection income. A non-IFRS ratio; management information."],
            ["Gross profit per vehicle (IFRS basis)", "Gross profit as reported in the financial statements for the month, divided by vehicles funded and delivered. The items that make up the difference from the deal basis are stated beside it each time."],
            ["Gross margin", "Gross profit (IFRS basis) as a percentage of total revenue in the month. Fiscal 2025 audited: 12.5 percent."],
            ["Period and cadence", "Calendar month, reported in the monthly results release after the month closes, starting with October 2026 on 10 November 2026. Each figure is shown beside the prior month. Monthly figures are stated as approximate; once started, the series continues in weak months."],
        ], NON_IFRS_NOTE),
        ("h2", "Why these four, and why historical only"),
        ("p", "These are the numbers an investor or a banker needs to reconstruct OCAL's operating leverage: how many vehicles, at what price, earning how much each, against a cost base that is largely fixed (operating expenses of $1,114,195 in fiscal 2025, audited). Gross profit per vehicle is shown two ways because the deal-level figure the founders quote (before write-downs and the auction, reconditioning and transport costs that IFRS places in cost of sales) and the audited figure answer different questions; both are stated, with the difference. The metrics are reported for closed months only. Targets and run-rates are not published. A metric reported once is reported every month, including in a slow one."),
        ("h2", "What to watch alongside them"),
        ("table", ["Indicator", "Why it matters", "Where you will see it"], [
            ["Vehicles funded and delivered per month", "The single number the model turns on; the largely fixed cost base does not grow with it", "Every monthly results release; quarterly MD&A"],
            ["Acquisition cost per funded deal", "Expected to fall as lead generation, the CRM and the AI sales agents run on one platform; reported when a results release carries it", "Results releases; MD&A"],
            ["Gross profit per vehicle (both bases) and protection attach (about 98 percent of funded transactions, management information)", "Whether volume comes without giving up margin", "Every monthly results release; MD&A"],
            ["Cycle time", "Lead to signed, signed to funded; shorter is cheaper", "Operational releases"],
            ["Licences", "Manitoba (dealer permit application under way), Ontario (registration under way), then the Maritimes", "News releases, when granted"],
            ["Cash and financing", "Runway for the roll-out", "Quarterly statements; financing releases"],
        ], ""),
        ("widget", "subscribe"),
    ],
)

# ------------------------------------------------------------------ NEWS
page(
    slug="/news/",
    nav_label="News",
    title="OCAL Financial News Releases (TSXV: OCAL)",
    description="Every OCAL Financial news release since the TSXV listing on 21 July 2026, filed on SEDAR+ and distributed by Newsfile. Get releases by email.",
    hero={
        "kicker": "NEWS RELEASES",
        "h1": "What we said, <em>when we said it.</em>",
        "sub": "Every release is reviewed by counsel, pre-filed with CIRO, distributed by Newsfile and filed on SEDAR+. From 10 November 2026, a monthly results release reports the operating metrics for the month just closed.",
        "ctas": [("Get releases by email", "/subscribe/", True)],
    },
    blocks=[
        ("widget", "news-list-full"),
        ("note", "Where a release was corrected or reissued, the final version is listed. Releases issued before 15 July 2026 were issued by Ronin Ventures Corp., the capital pool company with which OCAL completed its qualifying transaction, and are available on SEDAR+ under the Company's profile."),
    ],
)

# Release page: the 3 November 2026 release (08) set in the site template, text as issued on Newsfile. This is the per-release page pattern for CQ.
page(
    slug="/news/2026-11-03-repossession-rate-and-agm/",
    nav_label=None,
    title="Repossession Rate Under One Percent; AGM 10 December | OCAL Financial (TSXV: OCAL)",
    description="OCAL Financial (TSXV: OCAL) reports a repossession rate under one percent since 2021, about 99 percent of contracts funded, and sets its 2026 AGM for 10 December.",
    release={"date": "2026-11-03", "wire": "Newsfile", "category": "Operating update"},
    hero={
        "kicker": "NEWS RELEASE  ·  3 NOVEMBER 2026  ·  VANCOUVER, BRITISH COLUMBIA",
        "h1": "OCAL Financial Reports a Historical Repossession Rate Under One Percent, Highlighting the Strength of Its Asset-Light Automotive Financing Platform, and Announces Meeting Date for Its 2026 Annual General and Special Meeting",
        "sub": "Fewer than one in a hundred vehicle loans arranged since 2021 has ended in repossession; approximately 99 percent of signed contracts have been funded by lenders; annual general and special meeting on December 10, 2026.",
        "ctas": [("Release on Newsfile", NEWSFILE_08, False), ("All news", "/news/", False)],
    },
    blocks=[
        ("p", "Vancouver, British Columbia (Newsfile Corp., November 3, 2026). OCAL Financial Inc. (TSXV: OCAL) (FSE: JC3) (\"OCAL\" or the \"Company\"), the technology-enabled automotive financing and purchasing platform that gets Canadians approved for financing first and holds no standing vehicle inventory, today announced that fewer than one percent of the vehicle loans arranged through its platform since 2021 have resulted in repossession, according to management information for the period from the Company's first funded transaction in 2021 to September 30, 2026, based on lender reporting."),
        ("p", "The Company believes this historical performance reflects the effectiveness of its credit verification procedures, lender relationships, disciplined financing practices, and customer-first approach that prioritizes financial eligibility and affordability before vehicle selection."),
        ("p", "With more than 1,500 cumulative funded vehicle transactions and audited revenue of $6.48 million in the fiscal year ended August 31, 2025, OCAL has an established commercial operating history while maintaining an asset-light structure that eliminates the need for standing vehicle inventory. A funded vehicle transaction is a retail vehicle sale arranged through OCAL's platform for which the customer's financing contract was funded by a lender and the vehicle was delivered to the customer; the cumulative count is drawn from the Company's transaction records and lender reporting since its first funded transaction in 2021 and is not a measure presented in its financial statements."),
        ("h2", "Operating Highlights"),
        ("p", "**Disciplined Transaction Quality and a Scalable Business Model:** OCAL's process begins with financing approval and ends with the vehicle, reversing the conventional dealership sequence. Through its approval-first approach, OCAL verifies each customer's identity, income, creditworthiness and financing eligibility, explains the approval in plain terms, and only then sources a vehicle that fits the approved terms. This approach is designed to improve transaction quality, reduce financing uncertainty and strengthen lender confidence."),
        ("p", "According to management, approximately 99 percent of signed customer contracts were successfully funded by lenders over the period from the Company's first funded transaction in 2021 to September 30, 2026, reflecting the Company's ability to convert approved transactions into completed vehicle sales. Unlike a lender, OCAL does not retain consumer loans on its balance sheet or assume the associated credit-default risk."),
        ("p", "**Commercial Traction and Operating Efficiency:** OCAL's revenue model combines vehicle sales with financing-related compensation and protection products, creating multiple sources of revenue on every transaction. Management reports that approximately 98 percent of funded transactions include a warranty or other protection product, and that repeat and referral customers accounted for approximately 17.6 percent of funded transactions over the previously disclosed trailing twelve-month period. Every vehicle OCAL sells is under five years old, inspected and reconditioned before delivery, and carries a two-year, unlimited-kilometre warranty."),
        ("p", "**Technology-Enabled Compliance and Scalable Infrastructure:** OCAL operates through a centralized digital workflow that integrates customer verification, financing approvals, vehicle sourcing through OPENLANE Canada after approval, digital contracting and delivery to the customer's door, with every disclosure, signature and transaction recorded. The Company is licensed in British Columbia and Alberta and intends to apply the same infrastructure as it expands into additional Canadian markets, subject to applicable licensing and regulatory approvals."),
        ("h2", "Management Commentary"),
        ("quote", "Maintaining a repossession rate below one percent over our operating history reflects the discipline behind every transaction and the trust we work to build with our customers.", "Mehdi Moghareh, Chief Executive Officer"),
        ("quote", "Many customers come to us facing challenges with financing approval, finding the right vehicle, accessing a dealership or simply understanding their financing options. We solve the problem first, and the vehicle follows. Our approval-first model builds trust with customers and lenders while providing a scalable foundation for long-term growth and profitability.", "Mehdi Moghareh, Chief Executive Officer"),
        ("h2", "Operating Performance"),
        ("h3", "Transaction Economics and Path to Profitability"),
        ("p", "OCAL's asset-light business model is designed to generate multiple revenue streams from each funded vehicle transaction while maintaining a largely fixed operating cost structure. In the fiscal year ended August 31, 2025, the Company's audited revenue increased 18.8 percent to $6,480,254, gross profit increased 32.7 percent to $810,751, or 12.5 percent of revenue (fiscal 2024: $610,787, or 11.2 percent), and operating expenses decreased 9.8 percent to $1,114,195, narrowing the operating loss to $303,444 from $624,056. Finance, insurance and other products contributed $701,727 of fiscal 2025 gross profit."),
        ("p", "The Company's operating costs are largely fixed. As transaction volumes increase, OCAL has the potential to spread its fixed costs across more vehicle sales, improving operating efficiency and advancing toward profitability. Beginning with its November 10, 2026 news release, OCAL intends to report operating metrics for each closed month, using the same definitions each time."),
        ("p", "The fiscal 2025 and fiscal 2024 figures above are taken from the Company's audited financial statements for the year ended August 31, 2025, filed on SEDAR+ at www.sedarplus.ca."),
        ("h2", "2026 Annual General and Special Meeting of Shareholders"),
        ("p", "The Company also announces that it will hold its annual general and special meeting of shareholders on December 10, 2026 at 9:00 a.m. (Vancouver time) at Suite 1600, 925 West Georgia Street, Vancouver, British Columbia (the \"Meeting\"). The board of directors of the Company has fixed the close of business on November 2, 2026 as the record date for the Meeting. At the Meeting, shareholders will be asked to: (i) set the number of directors of the Company at four; (ii) elect directors of the Company for the ensuing year; and (iii) approve the adoption of a new omnibus equity incentive plan of the Company to replace the Company's existing stock option plan."),
        ("p", "In connection with the completion of the Company's qualifying transaction on July 15, 2026 (the \"Qualifying Transaction\"), Crowe MacKay LLP resigned as auditor of the Company, and DMCL LLP was appointed as auditor of the Company. Accordingly, at the Meeting, shareholders will also be asked to re-appoint DMCL LLP as auditor of the Company until the next annual meeting of the Company and authorize the directors to fix its remuneration. In the opinion of the Company, no \"reportable event\" (as such term is defined in Section 4.11(1) of National Instrument 51-102 Continuous Disclosure Obligations (\"NI 51-102\")) has occurred. The Company is relying on Section 4.11(3)(a) of NI 51-102 for an exemption from the change of auditor requirements of Section 4.11 of NI 51-102."),
        ("p", "Further details concerning the Meeting will be set out in the Company's management information circular, which will be sent to shareholders and made available under the Company's profile on SEDAR+ at www.sedarplus.ca in advance of the Meeting."),
        ("h2", "About OCAL"),
        ("p", "OCAL Financial Inc. (TSXV: OCAL) (FSE: JC3) is a technology-enabled automotive financing and purchasing platform transforming how Canadians finance and purchase vehicles. Built around an approval-first approach, OCAL connects customers with suitable financing options before sourcing a vehicle that meets their needs and budget. Its integrated platform brings together credit assessment and financial guidance, lender matching, vehicle sourcing, digital transactions and home delivery anywhere in the provinces it serves, eliminating the need to visit a traditional dealership. OCAL holds no standing vehicle inventory; it sources each vehicle only after a customer is approved, through OPENLANE Canada, its auction and sourcing channel. OCAL earns revenue from vehicle sales and related finance and protection products, and does not hold consumer loans or assume credit-default risk. Licensed in British Columbia and Alberta, OCAL generated revenue of $6.48 million (audited) in the fiscal year ended August 31, 2025 and has completed more than 1,500 funded vehicle transactions to date."),
        ("p", "To learn more about OCAL, visit www.ocalfinancial.ca."),
        ("p", "**Investor contact:** Shushu Feng, Investor Relations; Matthew Friesen, Executive Chairman; Mehdi Moghareh, Chief Executive Officer; investors@ocal.ca; 1 (604) 687-7765; ocalfinancial.ca."),
        ("note", "Cautionary notes. This news release does not constitute an offer to sell, or a solicitation of an offer to buy, any securities in the United States. The Company's securities have not been and will not be registered under the United States Securities Act of 1933, as amended (the \"U.S. Securities Act\") or any state securities laws and may not be offered or sold within the United States or to U.S. Persons unless registered under the U.S. Securities Act and applicable state securities laws or an exemption from such registration is available."),
        ("note", "Cautionary note regarding forward-looking information. This news release contains \"forward-looking statements\" and \"forward-looking information\" within the meaning of applicable securities laws (collectively, \"forward-looking statements\") within the meaning of Canadian securities legislation. Forward-looking information generally refers to information about an issuer's business, capital, or operations that is prospective in nature, and includes future-oriented financial information about the issuer's prospective financial performance or financial position. Forward-looking statements are often identified by the words \"may\", \"would\", \"could\", \"should\", \"will\", \"intend\", \"plan\", \"anticipate\", \"believe\", \"estimate\", \"expect\" or similar expressions and includes information regarding: the Company's business plans and technology development; plans to expand into various provinces; the Company's intention to report operating metrics on a monthly basis; the Company's belief that its business model can scale efficiently and advance toward sustainable profitability; the Company's intention to apply its compliance framework and infrastructure in new markets; and the Meeting, including the date of the Meeting and all matters to be voted on thereat. To develop the forward-looking information in this news release, the Company made certain material assumptions, including but not limited to: prevailing market conditions; general business, economic, competitive, political and social uncertainties; delay or failure to receive board, shareholder or regulatory approvals; the continued availability of lender and auction relationships on acceptable terms; the continued performance of customer contracts consistent with historical experience; and the ability of the Company to execute and achieve its business objectives. There can be no assurance that such statements will prove to be accurate, as actual results and future events could differ materially from those anticipated in such statements. Accordingly, readers should not place undue reliance on forward-looking statements. Actual results may vary from the forward-looking information in this news release due to certain material risk factors. These risk factors include, but are not limited to: adverse market conditions; changes in general economic, business and political conditions; changes in applicable laws and regulations; compliance with extensive government regulation; reliance on key and qualified personnel; reliance on third-party lenders and on OPENLANE Canada; risks associated with the technology industry in general; the risk that historical repossession and funding rates are not maintained; and the risk factors disclosed under the heading \"Risk Factors\" in the filing statement of the Company available on SEDAR+ at www.sedarplus.ca. The foregoing list of material risk factors and assumptions is not exhaustive. The Company assumes no obligation to update or revise the forward-looking information in this news release, unless it is required to do so under Canadian securities legislation."),
        ("note", "Neither TSX Venture Exchange nor its Regulation Services Provider (as that term is defined in policies of the TSX Venture Exchange) accepts responsibility for the adequacy or accuracy of this release."),
    ],
)

# ------------------------------------------------------------------ EVENTS
page(
    slug="/events/",
    nav_label="Events",
    title="OCAL Financial Events and AGM (TSXV: OCAL)",
    description="OCAL Financial's AGM on 10 December 2026, filing deadlines, monthly operating updates and conferences, with materials posted the same day.",
    hero={
        "kicker": "EVENTS AND PRESENTATIONS",
        "h1": "Dates that <em>matter.</em>",
        "sub": "The AGM, every reporting deadline and every conference, with materials posted the same day.",
        "ctas": [("Presentations", "/presentations/", True)],
    },
    blocks=[
        ("widget", "events-full"),
        ("widget", "subscribe"),
    ],
)

# ------------------------------------------------------------------ PRESENTATIONS
page(
    slug="/presentations/",
    nav_label="Presentations",
    title="OCAL Investor Presentation and Fact Sheet (TSXV: OCAL)",
    description="OCAL Financial's current investor presentation, elevator pitch, four-page brief, long-form briefing and investor Q&A, October 2026. Dated and versioned, with SEDAR+ links.",
    hero={
        "kicker": "DOCUMENTS",
        "h1": "Dated, versioned, <em>current.</em>",
        "sub": "The October 2026 set: the presentation, the one-page pitch, the four-page brief, the long-form briefing and the investor questions and answers. Each is refreshed when a reported figure changes, and the superseded version is withdrawn.",
        "ctas": [("Fact sheet (one page)", "/fact-sheet/", True), ("OCAL on SEDAR+", SITE["sedar_profile"], False)],
    },
    blocks=[
        ("h2", "In sixty seconds"),
        ("p", "OCAL Financial (TSXV: OCAL, FSE: JC3) is a technology-enabled automotive financing and purchasing platform. It solves the customer's problem first: approval by a lender, then the one vehicle that approval supports, bought at wholesale through OPENLANE, OCAL's auction and sourcing channel, and delivered to the driveway. Zero standing inventory, no consumer loans held, the licensed motor dealer of record on every transaction. Audited fiscal 2025 revenue of $6.48 million, up 18.8 percent, with gross profit up 32.7 percent and operating expenses down 9.8 percent; more than 1,500 funded vehicle transactions since 2021; a largely fixed cost base that does not grow with the count; licensed in British Columbia and Alberta, with the Manitoba dealer permit application under way and Ontario registration under way, targeted for 2027, subject to registration and capital. The founders hold about 54 percent and have not sold a share."),
        ("note", FUNDED_DEF),
        ("h2", "The October 2026 documents"),
        ("cards", [(k, t, b, "/assets/documents/" + f.replace(" ", "%20")) for k, t, b, f in DOCUMENTS]),
        ("p", "Every document is dated on its cover and uses the audited fiscal 2025 and fiscal 2024 figures. The filed record behind them, including the Filing Statement, the audited statements and every news release, is on [SEDAR+](" + SITE["sedar_profile"] + ") under OCAL Financial Inc. " + SITE["sedar_profile_note"]),
        ("h2", "Superseded documents"),
        ("p", "When a document is replaced, the old version is withdrawn from this page so that search engines and AI tools find one set of figures. Historical presentations remain on [SEDAR+](" + SITE["sedar_profile"] + ") where they were filed."),
        ("note", "Presentations contain forward-looking statements and management's estimates that are unaudited and are not guidance. Read each document's cautionary language and the risk factors in the Filing Statement on SEDAR+."),
    ],
)

# ------------------------------------------------------------------ FACT SHEET (printable page)
page(
    slug="/fact-sheet/",
    nav_label="Fact sheet",
    title="OCAL Financial Fact Sheet, November 2026 (TSXV: OCAL)",
    description="One-page OCAL fact sheet: audited FY2025 revenue $6.48M, zero standing inventory, 1,500+ funded deals, the five steps and the roll-out. Printable.",
    printable=True,
    hero={
        "kicker": "INVESTOR FACT SHEET  ·  NOVEMBER 2026  ·  TSXV: OCAL  ·  FSE: JC3",
        "h1": "We solve the problem first. The vehicle follows.",
        "sub": "A technology-enabled automotive financing and purchasing platform. Five years, more than 1,500 funded transactions, zero standing inventory.",
        "ctas": [("Print or save as PDF", "javascript:window.print()", True)],
    },
    blocks=[
        ("kpis", [
            ("$6.48M", "FY2025 revenue, audited", "up 19% with no new market"),
            ("1,500+", "funded deals", "two provinces, no growth capital"),
            ("$0", "standing inventory", "a car is ours 3 to 5 days"),
            ("12.5%", "gross margin, rising", "from 11.2% the year before"),
        ]),
        ("p", "Four problems bring a customer to OCAL: they cannot get approved where they shop, cannot find the right vehicle at a payment they can carry, live hours from the nearest lot, or have never had financing explained to them. OCAL redesigned the vehicle purchase around the customer's financial eligibility, needs and convenience. The customer is approved by a lender first, prime or non-prime; then we buy the one vehicle the approval supports from OPENLANE's marketplace and deliver it to their driveway. No lot, no standing inventory; a new market costs a licence, a bond and a small office, not a building."),
        ("steps", [
            ("1", "Apply", "Full credit application on the phone"),
            ("2", "Qualify", "AI first contact within minutes, day or night"),
            ("3", "Approve", "The lender that fits sets rate and amount"),
            ("4", "Match", "Two or three cars from OPENLANE that fit the approval"),
            ("5", "Deliver", "Digital signing, light recon, delivered to the driveway"),
        ]),
        ("h2", "Why investors lean in"),
        ("bullets", [
            ("Proven commercial traction.", "More than 1,500 funded transactions and audited revenue of $6.48 million in fiscal 2025, up 19 percent, from two provinces with no growth capital."),
            ("Operating leverage.", "A largely fixed cost base that does not grow with the count; as volume increases the Company has the potential to spread it across more vehicle sales. In fiscal 2025 revenue rose 18.8 percent and gross profit 32.7 percent while operating expenses fell 9.8 percent, and the operating loss halved."),
            ("A market that wants it.", "48% of buyers want to apply for credit online, 33% can (Cox, 2026); 77% of Canadian buyers finance or lease; OCAL's lender panel covers prime to non-prime."),
        ]),
        ("h2", "Where it goes"),
        ("table", ["Market", "Status", "Planned"], [
            ["BC and Alberta", "Licensed, five years", "Home base"],
            ["Manitoba", "Dealer permit application under way; office inside the OPENLANE Winnipeg facility arranged", "Next: targeted for December 2026, when the permit is granted"],
            ["Ontario", "Registration under way", "Targeted for 2027, subject to registration and capital"],
            ["The Maritimes", "Planned", "After Ontario"],
            ["United States", "Planned", "From 2028"],
        ], "Targets, subject to licensing, lenders and capital."),
        ("h2", "The window"),
        ("p", "Founders hold about 54 percent, escrowed, and have not sold a share. Shares outstanding 36,667,803; about 48.3 million fully diluted. Operating metrics are published every month from 10 November 2026."),
        ("p", "**Talk to us.** Mehdi Moghareh, CEO; Matthew Friesen, Executive Chairman. investors@ocal.ca, 1 (604) 687-7765, investors.ocal.ca. OCAL Financial Inc., Suite 500, 885 Dunsmuir Street, Vancouver, BC V6C 1N5."),
        ("note", FUNDED_DEF + " Audited figures from the financial statements on SEDAR+. Market facts from Statistics Canada, TransUnion, J.D. Power, Cox Automotive, Angus Reid and Presidio-NCM. Planned markets and dates are forward-looking statements subject to the risks in the Filing Statement."),
    ],
)

# ------------------------------------------------------------------ GOVERNANCE
page(
    slug="/governance/",
    nav_label="Governance",
    title="OCAL Financial Governance (TSXV: OCAL)",
    description="OCAL Financial's board of directors, audit and governance committees, policies, AGM materials, auditor, counsel and transfer agent.",
    hero={
        "kicker": "GOVERNANCE",
        "h1": "Small company. <em>Public standards.</em>",
        "sub": "An independent audit chair, an audit committee charter on the public record, founders escrowed for 36 months, counsel on every release and every number traceable to a filing.",
        "ctas": [("Leadership", "/leadership/", True)],
    },
    blocks=[
        ("h2", "Board of directors"),
        ("table", ["Director", "Role", "Independence", "Committees"], [list(b) for b in BOARD], "Committee composition as recorded at the board meeting of 1 October 2026. The Audit Committee and the Compensation, Governance and Nominating Committee each comprise Michael Stier (chair), Robert Birmingham and Matthew Friesen."),
        ("h2", "Documents"),
        ("table", ["Document", "Where to find it"], [
            ["Audit Committee charter", "Set out in the Filing Statement dated 9 July 2026, filed on SEDAR+"],
            ["Notice of articles and articles", "SEDAR+"],
            ["Management information circular, annual general and special meeting of 10 December 2026", "Posted here when filed, with the form of proxy and the notice of meeting"],
        ], "Additional governance policies are posted here as the board adopts them."),
        ("h2", "Annual general meeting"),
        ("p", "The 2026 annual general and special meeting of shareholders will be held on 10 December 2026 at 9:00 am Vancouver time at Suite 1600, 925 West Georgia Street, Vancouver. The record date is 2 November 2026. Shareholders will be asked to set the number of directors at four, elect the directors, approve a new omnibus equity incentive plan to replace the existing stock option plan, and reappoint DMCL LLP as auditor. The management information circular and form of proxy will be sent to shareholders and filed on SEDAR+ before the meeting; the voting results are posted here and filed after it. Questions sent in advance to investors@ocal.ca are answered in writing on this page after the meeting."),
        ("h2", "Corporate information"),
        ("table", ["Item", "Detail"], [
            ["Legal name", "OCAL Financial Inc. (British Columbia)"],
            ["Head office", SITE["address"]],
            ["Edmonton hub", SITE["edmonton"]],
            ["Fiscal year end", "31 August"],
            ["Exchange listings", "TSX Venture Exchange: OCAL (Tier 2), since 21 July 2026. Frankfurt Stock Exchange: JC3, since 25 August 2026."],
            ["Operating subsidiary", "1301756 B.C. Ltd., wholly owned, holding the dealer licences and operating contracts"],
            ["Dealer licences", "British Columbia: OCAL Financial Inc., licensed motor dealer, VSA D50207. Alberta: AMVIC-licensed business, AMVIC B2036050."],
            ["Auditor", "DMCL LLP, Vancouver"],
            ["Legal counsel", "Lawson Lundell LLP, Vancouver"],
            ["Transfer agent", "Endeavor Trust Corporation, Vancouver"],
            ["Investor relations", "Signal Capital Advisors (Shushu Feng, Investor Relations Manager), engaged as announced"],
            ["Disclosure practice", "Every news release is reviewed by counsel and pre-filed with CIRO before distribution; material information is disclosed immediately through a news release and filed on SEDAR+; operating metrics are defined once and reported every period."],
        ], ""),
        ("h2", "Insider ownership"),
        ("p", "The two founders hold about 54.3 percent of the shares outstanding (Matthew Friesen 14,212,381 shares and Mehdi Moghareh 5,710,825 shares per SEDI, October 2026), in TSXV Tier 2 value escrow released over 36 months from listing. Directors and officers file their holdings and trades on SEDI within five days; the founders have not sold a share since listing. The full table of insider holdings will be in the management information circular for the annual general and special meeting, filed on SEDAR+."),
    ],
)

# ------------------------------------------------------------------ LEADERSHIP
page(
    slug="/leadership/",
    nav_label="Leadership",
    title="OCAL Financial Leadership and Board (TSXV: OCAL)",
    description="The people running OCAL Financial: CEO Mehdi Moghareh, Executive Chairman Matthew Friesen, CFO Terence Lee, the team and the board.",
    hero={
        "kicker": "LEADERSHIP",
        "h1": "One ran the dealerships. The other's family <em>ran the auction.</em>",
        "sub": "Together they removed everything between the two. The founders hold about 54 percent, escrowed, and have not sold a share.",
        "ctas": [("Governance and board", "/governance/", True)],
    },
    blocks=[
        ("widget", "team"),
        ("h2", "The bench"),
        ("p", "A founder-led technology and demand-engine team. The sales team are account managers who have each closed hundreds of approval-first files; the logistics team delivers anywhere in the province with a part-time driver network."),
        ("h2", "Board of directors"),
        ("table", ["Director", "Role", "Independence"], [[b[0], b[1], b[2]] for b in BOARD], "Michael Stier chairs the Audit Committee and the Compensation, Governance and Nominating Committee."),
        ("cta", "Thirty minutes with the founders", "Mehdi tells the model; Matthew adds the auction and capital-markets line. Bring your hardest question.", [("Book an investor call", SITE["booking_link"], True), ("Email investors@ocal.ca", "mailto:investors@ocal.ca", False)]),
    ],
)

# ------------------------------------------------------------------ FAQ
page(
    slug="/faq/",
    nav_label="FAQ",
    title="OCAL Financial Investor FAQ (TSXV: OCAL)",
    description="Thirty investor questions answered plainly: is OCAL a broker, where the cars come from, who takes the credit risk, going concern, escrow, insiders.",
    hero={
        "kicker": "INVESTOR FAQ",
        "h1": "The hard questions, <em>answered first.</em>",
        "sub": "Dated answers, in the same words we use in the presentation and on investor calls. If your question is not here, email it and it will be.",
        "ctas": [("Ask a question", "mailto:investors@ocal.ca?subject=Investor%20question", True)],
    },
    blocks=[
        ("h2", "The three questions every diligent investor asks first"),
        ("faq", [
            ("What is the going-concern note, and what is the plan?", "The audited and interim statements carry a note that the Company needs volume or capital to fund its plan, which is common for Venture-listed companies at OCAL's stage. The July 2026 financing raised $1.5 million. Management's plan assumes growth capital in fiscal 2027; no terms have been set, and nothing on this site is an offer of securities. The operating metrics are published every period so that progress towards profitability is visible. Cash at each reporting date is in the filed statements; OCAL does not publish cash between reporting dates. (Answer dated 4 November 2026.)"),
            ("I have seen more than one FY2025 revenue figure. Which is right?", "$6.48 million, audited. Other figures circulated before the audit was complete. Everything OCAL writes uses the audited figure."),
            ("What does 'more than 3,000 vehicles' mean, and what does OCAL own?", "More than 3,000 vehicles are visible on OPENLANE's Canadian marketplace on a typical day. OCAL owns none of them. OPENLANE is OCAL's auction and sourcing channel; a vehicle is bought only after a specific customer is approved, and it is on OCAL's books for three to five days before delivery. Zero standing inventory means no car is bought before its buyer is approved."),
        ]),
        ("h2", "The business"),
        ("faq", [
            ("The financial statements show inventory and a floorplan facility. How is that zero standing inventory?", "Because a vehicle bought against an approved customer sits on the balance sheet for the few days between purchase and delivery, and the purchase line that funds it for those days shows as a floorplan facility. At every reporting date those balances are days of vehicles, not months. Nothing is bought on speculation, and no vehicle is held waiting for a buyer."),
            ("Where does the revenue come from?", "Retail vehicle sales are about 87 percent of revenue ($5,630,980 of $6,480,254 in fiscal 2025); finance, insurance and other income is the rest. The vehicle sale carries the top line at a modest margin, and the finance and protection layer carries most of the gross profit, which is why gross profit per vehicle is the metric to watch."),
            ("Is OCAL a broker?", "No. OCAL is the licensed motor dealer of record on every transaction: it approves, sources, contracts, delivers and takes the trade-in. A broker hands a customer to a lender or a dealer and steps away. What OCAL does not do is park cars on a lot and pay interest on them."),
            ("Where do the cars come from?", "OPENLANE, the largest wholesale marketplace in Canada and OCAL's auction and sourcing channel, with partner dealers and trade-ins behind it. OCAL's own representatives are at the auction sites to review units and run the bidding."),
            ("How long does OCAL own a vehicle?", "Days. It is bought against an approved customer and delivered after reconditioning and inspection. It is never bought on speculation."),
            ("Why is the consolidated gross margin only about 12 percent?", "Because retail vehicle sales carry the top line at a deliberately modest margin, and the margin per deal sits in the layer on top: lender reserve, protection products and fees. That layer is what the operating metrics report as gross profit per vehicle. Gross margin expanded from 11.2 percent in fiscal 2024 to 12.5 percent in fiscal 2025, audited, and 87 percent of fiscal 2025 gross profit came from finance, insurance and protection products."),
            ("How does volume change the economics?", "The cost base is largely fixed: licences, people, systems and an office that do not grow with the count; commissions and other variable costs are additional. In fiscal 2025 revenue rose 18.8 percent and gross profit 32.7 percent while operating expenses fell 9.8 percent, and the operating loss halved. As volume increases, the Company has the potential to spread its fixed costs across more vehicle sales, and management is working towards profitability through volume. OCAL does not publish a profitability target, a date or financial guidance; Manitoba and Ontario are the volume markets, and the monthly results release shows the actual count."),
            ("Who are the lenders?", "Seven lenders are live on OCAL's submission portal, prime to non-prime: RBC, Santander, iA Auto Finance, Eden Park, LendCare, Rifco and Iceberg. No single lender is the business; routing each file to the right one is."),
            ("Who takes the credit risk?", "The lender. OCAL originates the contract and holds none of the paper. From the Company's first funded transaction in 2021 to 30 September 2026, about 99 percent of signed customer contracts were funded by lenders, and fewer than one percent of the vehicle loans arranged through the platform have resulted in repossession (management information, based on lender reporting)."),
            ("Does OCAL own the vehicles it sells?", "Only for the three to five days between buying one against an approved customer and delivering it. OCAL does not buy vehicles first and look for buyers second, does not run reconditioning plants, and does not lend the money or hold the loans. It earns the margin on the transaction without holding the paper or the inventory."),
            ("What is the AI actually doing?", "Answering every lead in seconds so none go cold, packaging the credit file the way each lender wants it, routing it to the lender most likely to fund it, and showing management every desk and every deal in the Showroom. The result is more funded vehicles per employee."),
            ("What is happening to the customer-acquisition cost?", "Lead generation, the CRM and the AI sales agents now run on one platform, with an AI agent answering every lead in seconds. The Company expects its acquisition cost per funded deal to fall as a result, and will report it when a results release carries it."),
            ("Does OCAL finance prime customers or only non-prime?", "Both. A prime customer gets a prime rate from a bank on the panel; a near-prime or non-prime customer gets a finance-company loan. The market the big banks left behind is large, but it is not OCAL's whole customer base."),
        ]),
        ("h2", "The shares"),
        ("faq", [
            ("Why did a company this size go public?", "To fund a national roll-out of a model that already works, and to have a listed currency for acquisitions and for recruiting. Public gave OCAL a currency and a window that private never could."),
            ("Who underwrote the listing?", "It was a qualifying transaction with a capital pool company, Ronin Ventures Corp., not an underwritten IPO. The July 2026 financing was a private placement of 6,029,500 units at $0.25 for gross proceeds of $1,507,375."),
            ("Are insiders selling?", "No. The founders hold about 54 percent, escrowed under exchange policy for 36 months, and have not sold a share. Insider trades are reported on SEDI within five days."),
            ("Are insiders buying?", "Escrow and blackout rules limit insider purchases around results and material events. Any purchases are reported on SEDI within five days and summarized on the Governance page."),
            ("What is the warrant overhang?", "About 11 million warrants, the bulk of them 6.0 million at $0.50 expiring July 2028. The full table, with exercise prices and expiry dates, is on the Stock page."),
            ("When do escrowed and hold-period shares become tradable?", "The escrow schedule is on the Stock page: 15 percent of the principals' shares every six months from January 2027. The 6.03 million shares from the July 2026 financing become free trading on 8 November 2026."),
            ("Can US investors buy the shares?", "Yes, on the TSX Venture Exchange through most US brokers, and in Frankfurt as JC3."),
            ("Is there analyst coverage or a market maker?", "No analyst covers OCAL at this date; we will list every analyst here when one does. Integral Wealth Securities Limited provides market making under an agreement announced on 6 August 2026, at $6,000 a month and no securities compensation. Signal Capital Advisors provides investor relations under an agreement announced on 29 August 2026."),
            ("Does OCAL publish a share-price or valuation target?", "No, never, in any forum. We publish the operating metrics and the audited statements and let investors do the arithmetic."),
        ]),
        ("h2", "The plan"),
        ("faq", [
            ("When is Manitoba?", "The dealer permit application is under way with the regulator, with an office inside the OPENLANE Winnipeg auction facility arranged. Opening is targeted for December 2026, when the permit is granted; regulators set the timing, and OCAL does not announce a permit before it is granted. A Manitoba permit also serves Saskatchewan and northwestern Ontario customers."),
            ("When is Ontario?", "Registration is under way, targeted for 2027, subject to registration and capital. Ontario is about 40 percent of Canadian vehicle transactions."),
            ("When is the rest of Canada?", "After Ontario, the Maritimes, each market a copy of the first: a licence, a bond, a small office and a local team. Everything is subject to licensing, lenders and capital."),
            ("When is the United States?", "On the roadmap from 2028, after the Canadian roll-out. Everything is subject to licensing, lenders and capital."),
            ("How much capital does the Company need?", "Management's plan assumes growth capital in fiscal 2027 to fund Manitoba, Ontario and the provinces that follow. No terms have been set, and nothing on this site is an offer of securities."),
            ("Does OCAL publish a forecast?", "No. OCAL publishes its audited statements, the operating metrics every period under fixed definitions, and the roadmap of markets with the status of each. Plan figures and targets are not published on this site."),
            ("What is the exit?", "Management is building a national, licensed, approval-first platform to run it. OCAL does not comment on valuation or on any transaction."),
            ("What are the next milestones?", "The first monthly results release on 10 November 2026; the annual general and special meeting on 10 December 2026; audited fiscal 2026 results by 29 December 2026; the Manitoba permit when granted; Ontario registration; and the first quarter of fiscal 2027 by 29 January 2027."),
        ]),
        ("cta", "Still have a question?", "Email it. Every question asked in an investor meeting is added to this page, with its answer and the date.", [("investors@ocal.ca", "mailto:investors@ocal.ca?subject=Investor%20question", True)]),
        ("note", FLI_LEGEND),
    ],
)

# ------------------------------------------------------------------ CONTACT
page(
    slug="/contact/",
    nav_label="Contact",
    title="Contact OCAL Investor Relations (TSXV: OCAL)",
    description="Contact OCAL investor relations: investors@ocal.ca, 1 (604) 687-7765, book a call with the founders, transfer agent details and email alerts.",
    hero={
        "kicker": "CONTACT",
        "h1": "Talk to the people <em>who run it.</em>",
        "sub": "Investor questions are answered within one business day. Serious investors get thirty minutes with both founders and the Showroom on the screen.",
        "ctas": [("Book a 30-minute call", SITE["booking_link"], True), ("Email investors@ocal.ca", "mailto:investors@ocal.ca", False)],
    },
    blocks=[
        ("cards", [
            ("INVESTORS", "Investor relations", "investors@ocal.ca · " + SITE["phone"] + ". The mailbox is monitored daily by Matthew Friesen, Executive Chairman, and Shushu Feng, Investor Relations Manager (Signal Capital Advisors).", "mailto:investors@ocal.ca"),
            ("REGISTERED HOLDERS", "Transfer agent", "Endeavor Trust Corporation, Suite 702, 777 Hornby Street, Vancouver, BC V6Z 1S4; 604-559-8880; info@endeavortrust.com. For share transfers, lost certificates, address changes and registered-holder enquiries.", "https://www.endeavortrust.com"),
            ("MEDIA", "Media enquiries", "investors@ocal.ca with 'Media' in the subject line. Facts only, all on SEDAR+; numbers fact-checked within the hour.", "mailto:investors@ocal.ca?subject=Media"),
            ("CUSTOMERS", "Buying a car", "This site is for investors. If you want a vehicle, start at ocalfinancial.ca or call 1-877-495-2012, Monday to Saturday.", SITE["consumer_site"]),
        ]),
        ("h2", "Offices"),
        ("table", ["Office", "Address"], [
            ["Head office, Vancouver", SITE["address"]],
            ["Edmonton hub", SITE["edmonton"]],
        ], "OCAL Financial Inc., licensed motor dealer, VSA D50207 (British Columbia). AMVIC-licensed business, AMVIC B2036050 (Alberta)."),
        ("widget", "subscribe"),
        ("h2", "How we handle investor conversations"),
        ("p", "OCAL follows National Policy 51-201 on selective disclosure: nothing material is said in a one-on-one that is not already on the public record, no share-price view is offered, and no forecast. If you want a number that is not public, the answer is the next filing date."),
    ],
)

# ------------------------------------------------------------------ SUBSCRIBE
page(
    slug="/subscribe/",
    nav_label="Email alerts",
    title="OCAL Financial Email Alerts (TSXV: OCAL)",
    description="Every OCAL Financial news release, operating update and filing by email within the hour of distribution. Double opt-in, unsubscribe any time.",
    hero={
        "kicker": "EMAIL ALERTS",
        "h1": "Every release, <em>within the hour.</em>",
        "sub": "News releases, operating updates, financial filings and event reminders. One field, double opt-in, unsubscribe any time. The welcome email carries the fact sheet.",
        "ctas": [],
    },
    blocks=[
        ("widget", "subscribe-large"),
        ("p", "We send what we file and nothing else: no promotion, no third-party content, no sharing of your address. Each email states that it is issued by OCAL Financial Inc. and links to the release on SEDAR+."),
    ],
)


# ------------------------------------------------------------------ FACTS (entity page)
page(
    slug="/facts/",
    nav_label="Company facts",
    title="OCAL Financial Company Facts (TSXV: OCAL)",
    description="Reference facts for OCAL Financial Inc.: legal name, TSXV and Frankfurt symbols, ISIN, CUSIP, LEI, head office, officers, auditor, transfer agent.",
    hero={
        "kicker": "COMPANY FACTS",
        "h1": "The facts, <em>in one place.</em>",
        "sub": "The reference page for data vendors, journalists, AI assistants and anyone checking a detail. Same facts as the structured data on every page. No marketing.",
        "ctas": [],
    },
    blocks=[
        ("table", ["Fact", "Value"], [
            ["Legal name", "OCAL Financial Inc."],
            ["Former name", "Ronin Ventures Corp. (capital pool company; qualifying transaction completed 15 July 2026)"],
            ["Operating subsidiary", "1301756 B.C. Ltd., incorporated 23 April 2021, wholly owned"],
            ["What the company does", "Technology-enabled automotive financing and purchasing platform. The customer is approved by a lender first; OCAL, the licensed motor dealer of record, then sources the vehicle through OPENLANE, its auction and sourcing channel, and delivers it. Zero standing inventory; no consumer loans held; not a broker."],
            ["Industry", "Automotive financing and purchasing platform (vehicle retail and finance arrangement)"],
            ["Stock exchange listings", "TSX Venture Exchange: OCAL (Tier 2), trading since 21 July 2026. Frankfurt Stock Exchange: JC3, since 25 August 2026."],
            ["ISIN", SITE["isin"]],
            ["CUSIP", SITE["cusip"]],
            ["WKN", SITE["wkn"]],
            ["LEI", SITE["lei"] + " (GLEIF status issued; legal address Suite 1600, 925 West Georgia Street, Vancouver, the registered and records office; headquarters Suite 500, 885 Dunsmuir Street)"],
            ["Shares outstanding", "36,667,803 (as at " + SITE["facts_date"] + ")"],
            ["Fiscal year end", "31 August"],
            ["Head office", SITE["address"]],
            ["Edmonton hub", SITE["edmonton"]],
            ["Telephone", SITE["phone"]],
            ["Investor relations email", SITE["email"]],
            ["Websites", "Investors: investors.ocal.ca. Customers: ocalfinancial.ca."],
            ["Chief Executive Officer", "Mehdi Moghareh (Co-Founder, Director)"],
            ["Executive Chairman", "Matthew Friesen (Co-Founder, Director)"],
            ["Chief Financial Officer", "Terence Lee, CPA"],
            ["Independent directors", "Michael Stier (Chair of the Audit Committee and of the Compensation, Governance and Nominating Committee); Robert Birmingham"],
            ["Auditor", "DMCL LLP, Vancouver"],
            ["Transfer agent and registrar", "Endeavor Trust Corporation, Vancouver"],
            ["Legal counsel", "Lawson Lundell LLP, Vancouver"],
            ["Investor relations firm", "Signal Capital Advisors Inc. (Shushu Feng, Investor Relations Manager)"],
            ["Market maker", "Integral Wealth Securities Limited"],
            ["Newswire", "Newsfile Corp."],
            ["Dealer licences", "British Columbia: OCAL Financial Inc., licensed motor dealer, VSA D50207. Alberta: AMVIC-licensed business, AMVIC B2036050."],
            ["Operating since", "April 2021"],
            ["Employees", "About 30 people plus a part-time driver network (management information)"],
            ["Continuous disclosure", "SEDAR+ (www.sedarplus.ca), issuer profile OCAL Financial Inc."],
            ["Last updated", SITE["facts_date"]],
        ], "Each line is traceable to a filing, a news release or a public register. Corrections to investors@ocal.ca."),
        ("h2", "Standard description for third parties"),
        ("p", "**Short (one line).** Technology-enabled automotive financing and purchasing platform, licensed in British Columbia and Alberta."),
        ("p", "**Standard (for data vendors).** OCAL Financial Inc. (TSXV: OCAL; FSE: JC3) is a technology-enabled automotive financing and purchasing platform transforming how Canadians finance and purchase vehicles. Built around an approval-first approach, OCAL connects customers with suitable financing options before sourcing a vehicle that meets their needs and budget. Its integrated platform brings together credit assessment and financial guidance, lender matching, vehicle sourcing, digital transactions and home delivery anywhere in the provinces it serves, eliminating the need to visit a traditional dealership. OCAL holds no standing vehicle inventory; it sources each vehicle only after a customer is approved, through OPENLANE Canada, its auction and sourcing channel. OCAL earns revenue from vehicle sales and related finance and protection products, and does not hold consumer loans or assume credit-default risk. Licensed in British Columbia and Alberta, OCAL generated revenue of $6.48 million (audited) in the fiscal year ended August 31, 2025 and has completed more than 1,500 funded vehicle transactions to date."),
        ("note", FUNDED_DEF),
        ("p", "Media and data vendors may use either description without further permission. Logo files are available from investors@ocal.ca."),
    ],
)

# ------------------------------------------------------------------ LEGAL
page(
    slug="/legal/",
    nav_label="Legal",
    title="Legal Notices | OCAL Financial Investor Site",
    description="Forward-looking information, non-IFRS measures, no offer of securities, third-party data, privacy and terms for the OCAL Financial investor site.",
    hero={
        "kicker": "LEGAL NOTICES",
        "h1": "Read this <em>once.</em>",
        "sub": "The notices that apply to every page of investors.ocal.ca.",
        "ctas": [],
    },
    blocks=[
        ("h2", "Forward-looking information"),
        ("p", FLI_LEGEND),
        ("p", "Specific forward-looking statements on this site include: the planned openings of Manitoba, Ontario and the Maritimes and a planned United States entry from 2028; the intention to raise growth capital in fiscal 2027; and the planned features of OCAL Showroom. Material assumptions include regulatory approvals on the timelines described, lender programs extended to new markets, availability of capital on acceptable terms, used-vehicle supply through OPENLANE, and operating economics consistent with the trailing period. Material risks include licensing delay or refusal, lender appetite through the credit cycle, used-vehicle price movements, competition, technology and data reliability, dependence on key people, availability of capital and the going-concern uncertainty described in the financial statements."),
        ("h2", "Non-IFRS and supplementary financial measures"),
        ("p", NON_IFRS_NOTE),
        ("p", "Management information identified as unaudited (repossession rate, approval lift, cycle times, protection attach, repeat and referral share) is drawn from OCAL's operating systems and has not been audited or reviewed. OCAL does not publish forecasts or plan figures on this site."),
        ("h2", "No offer of securities"),
        ("p", "Nothing on this site is an offer to sell or a solicitation of an offer to buy securities in any jurisdiction. OCAL's securities have not been and will not be registered under the United States Securities Act of 1933 and may not be offered or sold in the United States absent registration or an exemption. Investors should read the Filing Statement, the financial statements and the MD&A on SEDAR+ and consult their own advisors."),
        ("h2", "Third-party data"),
        ("p", "Share price and chart data are supplied by third parties, may be delayed and are provided for information only. Market statistics are cited to their sources and have not been independently verified by OCAL."),
        ("h2", "Privacy"),
        ("p", "The email alert list is held by OCAL's email service provider under a double opt-in; addresses are used only to send OCAL's own releases, filings and event notices and are never sold or shared. The site uses Google Analytics 4 to measure visits; no personal information is collected beyond what you submit. Requests about your data go to investors@ocal.ca. OCAL complies with Canada's Anti-Spam Legislation."),
        ("h2", "Exchange disclaimer"),
        ("p", "Neither TSX Venture Exchange nor its Regulation Services Provider (as that term is defined in policies of the TSX Venture Exchange) accepts responsibility for the adequacy or accuracy of this site."),
        ("h2", "Corporate"),
        ("p", "OCAL Financial Inc., " + SITE["address"] + ". OCAL Financial Inc., licensed motor dealer, VSA D50207 (British Columbia). AMVIC-licensed business, AMVIC B2036050 (Alberta). Consumer financing is on approved credit; the lender makes the final approval."),
    ],
)
