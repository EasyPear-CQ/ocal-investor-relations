# -*- coding: utf-8 -*-
"""
patch_11_turnkey_nov2026.py  (4 November 2026, Matthew's instruction: "make it turn key for Has and CQ ... compliant, but still amazing")

Applies to content.py:
  - every [[placeholder]] cleared with a turnkey value (mailto booking and subscribe fallbacks, SEDAR+ search links,
    Endeavor Trust details, GLEIF record, Ryan McDonald's bio from the 8 September 2026 release, Matthew's photo);
  - Garrett Lee, 31 October 2026: OPENLANE is "its auction and sourcing channel", never "exclusive"; the funded-deal
    count carries the NI 52-112 definition sentence beside its first use on every page; rates carry their period;
    per-vehicle and fixed-cost dollar figures are off the site (audited statement lines only);
  - 30 October evening review and OCAL/CLAUDE.md: no statement about who has been selling the stock, no unverified
    market anecdotes, acquisition cost "expected to fall" only, Hasneen "leads technology and the demand engine";
  - the 3 November 2026 release (08) added as the per-release page pattern (text as issued on Newsfile), the Showroom
    page retired to its Newsfile link, per-release Newsfile URLs for every release, events and AGM details from 08;
  - Manitoba wording "dealer permit application under way", opening targeted for December 2026;
  - dates moved to 4 November 2026.
Backups: content_2026-11-04 (pre turnkey rebuild).py.bak, build_site_2026-11-04 (pre turnkey rebuild).py.bak.
"""
import io, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(HERE, "content.py")
src = io.open(PATH, encoding="utf-8").read()
N = 0

def rep(old, new, count=1):
    global src, N
    c = src.count(old)
    if c != count:
        print("REPLACE FAILED (%d found, %d expected): %s" % (c, count, old[:90]))
        sys.exit(1)
    src = src.replace(old, new)
    N += 1

def span(start, end, new):
    """Replace from the first occurrence of start (inclusive) to the first following occurrence of end (exclusive)."""
    global src, N
    a = src.find(start)
    if a < 0:
        print("SPAN START NOT FOUND:", start[:80]); sys.exit(1)
    b = src.find(end, a + len(start))
    if b < 0:
        print("SPAN END NOT FOUND:", end[:80]); sys.exit(1)
    src = src[:a] + new + src[b:]
    N += 1

# ------------------------------------------------------------------ docstring and SITE
rep('''Placeholders: anything inside [[double brackets]] is a value that must be filled or confirmed before go-live.
The build lists every one of them in source/PLACEHOLDERS.txt and the CQ handoff.''',
'''Placeholders: anything inside [[double brackets]] would render as a yellow marker and be listed in source/PLACEHOLDERS.txt.
Since 4 November 2026 there are none: the build must print "placeholders: 0". The two values CQ and Has swap at go-live are
SITE["form_action"] (the Brevo form action URL; empty means the email-request fallback) and, if a direct link is captured,
SITE["sedar_profile"] (today the SEDAR+ search page).''')

rep('''    "sedar_profile_note": "[[Replace with the exact SEDAR+ profile URL for OCAL Financial Inc. once CQ has it; until then the link opens SEDAR+ search.]]",''',
'''    "sedar_profile_note": "On SEDAR+, search the issuer name OCAL Financial Inc.",''')
rep('''    "booking_link": "[[30-minute investor call booking link]]",
    "form_action": "[[Brevo or Mailchimp form action URL]]",
    "updated": "October 2026",
    "facts_date": "30 October 2026",''',
'''    "booking_link": "mailto:investors@ocal.ca?subject=Book%20a%2030-minute%20investor%20call",
    "form_action": "",   # Has: paste the Brevo form action URL here when the list exists; empty = the email-request fallback
    "updated": "November 2026",
    "facts_date": "4 November 2026",''')

# ------------------------------------------------------------------ lines that hold, definitions
span("# Lines that hold everywhere", "FLI_LEGEND = (", r'''# The NI 52-112 definition sentence for the funded-deal count (Garrett Lee, 31 October 2026; wording as issued in the
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

''')

span("NON_IFRS_NOTE = (", "NAV = [", r'''NON_IFRS_NOTE = (
    "Vehicles funded and delivered is a supplementary financial measure, and average vehicle selling price, gross profit per vehicle "
    "and gross margin per vehicle are non-GAAP financial measures or ratios; none is a measure defined under IFRS. OCAL calculates them "
    "as described on the Operating metrics page, applies the same definitions every period, reports them unaudited, and reconciles the "
    "per-vehicle figures to the revenue and gross profit lines of its financial statements in the release that carries them. They should "
    "be read with the financial statements and MD&A filed on SEDAR+."
)

''')

# ------------------------------------------------------------------ news, events, filings, team
span("# Public news releases since listing", "DOCUMENTS_SOURCE = ", r'''# Public news releases since listing (Newsfile per-release URLs captured 4 November 2026). Newest first.
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

''')

span("EVENTS = [", "FILINGS = [", r'''EVENTS = [
    ("2026-11-10", "October 2026 monthly results release (the first monthly operating update)", "The first monthly results release: vehicles funded and delivered, average vehicle selling price, gross profit per vehicle and gross margin for October 2026, under the definitions on the Operating metrics page, with the prior month beside each figure.", "upcoming"),
    ("2026-12-10", "Annual general and special meeting of shareholders", "9:00 am Vancouver time, Suite 1600, 925 West Georgia Street, Vancouver. Record date 2 November 2026. Business: set the number of directors at four, elect the directors, approve a new omnibus equity incentive plan and reappoint DMCL LLP as auditor. The management information circular and form of proxy are sent to shareholders and filed on SEDAR+ before the meeting; the voting results are posted here afterwards.", "upcoming"),
    ("2026-12-29", "Audited fiscal 2026 results and MD&A (filing deadline)", "Year ended 31 August 2026. Statements posted here the day they are filed, with a plain-language summary and an email to the list.", "upcoming"),
    ("2027-01-29", "First quarter fiscal 2027 interim results (filing deadline)", "Quarter ended 30 November 2026.", "upcoming"),
    ("2026-11-03", "News release: repossession rate under one percent; AGM date set", "Fewer than one percent of the vehicle loans arranged since 2021 have resulted in repossession and about 99 percent of signed contracts were funded (2021 to 30 September 2026, management information); more than 1,500 funded vehicle transactions; the annual general and special meeting set for 10 December 2026. [Read the release](/news/2026-11-03-repossession-rate-and-agm/).", "past"),
    ("2026-10-08", "Cantech Investment Conference, Toronto", "Mehdi Moghareh presented OCAL at 4:00 pm ET, Track 3. The presentation was not recorded. The current investor presentation is on the Presentations page.", "past"),
    ("2026-08-25", "Frankfurt Stock Exchange listing", "OCAL began trading in Frankfurt under the symbol JC3.", "past"),
    ("2026-07-21", "TSX Venture Exchange listing", "First day of trading as OCAL on TSXV Tier 2.", "past"),
]

''')

span("FILINGS = [", "TEAM = [", r'''# Each link opens SEDAR+ (the public search page); the issuer profile is found by searching "OCAL Financial Inc.".
# CQ or Has: when a direct document URL is captured from the profile, paste it in place of SITE["sedar"] and rebuild.
FILINGS = [
    ("Audited financial statements, year ended 31 August 2025", "Annual", "DMCL LLP, auditor", SITE["sedar"]),
    ("Management's discussion and analysis, year ended 31 August 2025", "Annual", "", SITE["sedar"]),
    ("Interim financial statements and MD&A, nine months ended 31 May 2026", "Interim", "Unaudited", SITE["sedar"]),
    ("Filing Statement dated 9 July 2026 (qualifying transaction)", "Listing", "The document to read first: business, risk factors, capital structure, escrow, audit committee charter", SITE["sedar"]),
    ("Material change reports and news releases", "Continuous", "Every release is filed on SEDAR+ the day it is issued", SITE["sedar"]),
]

''')

span("TEAM = [", "BOARD = [", r'''TEAM = [
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

''')

# ------------------------------------------------------------------ HOME
rep('''            ("$0", "consumer loans held", "Lenders fund the contract and carry the credit risk; OCAL earns the margin on every transaction"),
        ]),
        ("kicker", "WHY INVESTORS LEAN IN"),''',
'''            ("$0", "consumer loans held", "Lenders fund the contract and carry the credit risk; OCAL earns the margin on every transaction"),
        ]),
        ("note", FUNDED_DEF),
        ("kicker", "WHY INVESTORS LEAN IN"),''')
rep('''("03", "Operating leverage", "Fixed operating costs are about $160,000 a month, per the MD&A, and do not grow with the count. As volume increases the Company has the potential to spread them across more vehicle sales. Gross profit grew 33 percent in fiscal 2025 while operating expenses fell 10 percent; the number that moves is the count.", "/why-ocal/#economics"),''',
'''("03", "Operating leverage", "The cost base is largely fixed: licences, people, systems and an office that do not grow with the count. In fiscal 2025 revenue rose 18.8 percent and gross profit 32.7 percent while operating expenses fell 9.8 percent, and the operating loss halved. As volume increases the Company has the potential to spread its fixed costs across more vehicle sales. The number that moves is the count.", "/why-ocal/#economics"),''')
rep('''From the October 2026 operating update, the operating metrics are published every month under fixed definitions."),''',
'''From 10 November 2026, the operating metrics for each closed month are published in a monthly results release under fixed definitions and kept on the Operating metrics page."),''')

# ------------------------------------------------------------------ WHY OCAL
rep('''            ("3 to 5", "days a car is on our books", "purchase to delivery"),
        ]),
        ("anchor", "problem"),''',
'''            ("3 to 5", "days a car is on our books", "purchase to delivery"),
        ]),
        ("note", FUNDED_DEF),
        ("anchor", "problem"),''')
rep('''OPENLANE is OCAL's exclusive auction and sourcing channel: more than 3,000 vehicles are visible on its Canadian marketplace on a typical day, and none of them is on OCAL's balance sheet.''',
'''OPENLANE is OCAL's auction and sourcing channel: more than 3,000 vehicles are visible on its Canadian marketplace on a typical day, and none of them is on OCAL's balance sheet.''')
rep('''Operating expenses fell 10 percent to $1,114,195 in the same year, the operating loss halved, and cash from operating activities turned positive. Fixed operating costs are about $160,000 a month, per the MD&A, and do not grow with the count, so as volume increases the Company has the potential to spread them across more vehicle sales. The constraint has never been demand.''',
'''Operating expenses fell 9.8 percent to $1,114,195 in the same year, the operating loss halved, and cash from operating activities turned positive. The cost base is largely fixed and does not grow with the count, so as volume increases the Company has the potential to spread it across more vehicle sales. The constraint has never been demand.''')
rep('''            ["Vehicles funded and delivered", "[Operating metrics](/operating-metrics/), reported every period from the October 2026 update", "The count is the number the model turns on"],
            ["Gross profit per vehicle and gross margin", "[Operating metrics](/operating-metrics/), under fixed definitions", "Vehicle margin, lender reserve and protection products; most of the gross profit sits in the finance and protection layer"],
            ["Fixed cost base", "MD&A", "About $160,000 a month, largely fixed; commissions and other variable costs are additional"],
        ], "Operating metrics are management information, unaudited, historical only, and are published with every news release under the definitions on the Operating metrics page."),''',
'''            ["Vehicles funded and delivered", "[Operating metrics](/operating-metrics/), reported every month from the 10 November 2026 release", "The count is the number the model turns on"],
            ["Gross profit per vehicle and gross margin", "[Operating metrics](/operating-metrics/), under fixed definitions", "Vehicle margin, lender reserve and protection products; most of the gross profit sits in the finance and protection layer"],
            ["Operating expenses", "Audited statements and MD&A", "$1,114,195 in fiscal 2025, down 9.8 percent while revenue grew 18.8 percent; largely fixed, so each added vehicle carries more of it"],
        ], "Operating metrics are management information, unaudited, historical only, and are published in each monthly results release under the definitions on the Operating metrics page."),''')
rep('''("The big banks walked away from the little guy.", "Six in ten households earn under $100,000 and 28% of credit-active Canadians sit below prime, about nine million people (TransUnion). Several large banks have pulled back from indirect auto lending or restricted it to the largest dealerships. OCAL's panel covers both ends, prime and non-prime."),''',
'''("The banks narrowed the credit box.", "Six in ten households earn under $100,000 and 28% of credit-active Canadians sit below prime, about nine million people (TransUnion). Several large banks have narrowed their indirect auto lending. OCAL's panel covers both ends, prime and non-prime, through seven lenders."),''')
rep('''("The supply moved to where we buy.", "Since 2024 Canadian manufacturers send lease returns to auction, not back to dealers, and OPENLANE holds that flow. Vancouver's auction sold almost 900 cars in one day in October 2026."),''',
'''("The supply is where we buy.", "Dealer trade-ins, off-lease returns, retired rental units and repossessions flow through the wholesale auctions, and OPENLANE is the largest of them in Canada. Only licensed dealers can buy there, and OCAL buys against an approval, never for a lot."),''')
rep('''("table", ["Market", "Status at 30 October 2026", "Planned opening", "What it adds"], [''',
'''("table", ["Market", "Status at 4 November 2026", "Planned opening", "What it adds"], [''')
rep('''["Manitoba", "Dealer licence application filed with the regulator; office and OPENLANE access in place", "Next, when the licence is granted", "Serves Saskatchewan and northwestern Ontario too"],
            ["Ontario", "Registration in progress", "Targeted for 2027, subject to registration and capital", "About 40% of Canada's market"],''',
'''["Manitoba", "Dealer permit application under way with the regulator; office inside the OPENLANE Winnipeg auction facility arranged", "Next: targeted for December 2026, when the permit is granted", "Serves Saskatchewan and northwestern Ontario too"],
            ["Ontario", "Registration under way", "Targeted for 2027, subject to registration and capital", "About 40% of Canada's market"],''')
rep('''("p", "The Manitoba dealer licence application has been filed with the regulator, with the office and OPENLANE access in place. Ontario registration is in progress, targeted for 2027, subject to registration and capital.''',
'''("p", "The Manitoba dealer permit application is under way with the regulator, with an office inside the OPENLANE Winnipeg auction facility arranged; opening is targeted for December 2026, when the permit is granted. Ontario registration is under way, targeted for 2027, subject to registration and capital.''')
rep('''We hold BC and Alberta, with Manitoba and Ontario in progress. Seven lenders, prime to non-prime, are on our panel. We have more than 1,500 deals of data on which leads convert, which lenders approve whom and what a car is worth before anyone else bids. Our own CRM runs every deal on one screen, an AI agent takes the 3 am lead (a lead answered inside five minutes is 21 times more likely to qualify than one answered at thirty)."),''',
'''We hold BC and Alberta, with Manitoba and Ontario under way. Seven lenders, prime to non-prime, are on our panel. We have more than 1,500 funded transactions of data on which leads convert, which lenders approve whom and what a car is worth before anyone else bids. Lead generation, the CRM and the AI sales agents run on one platform: every deal on one screen, and an AI agent takes the 3 am lead (a lead answered inside five minutes is about 21 times more likely to qualify than one answered after thirty, per the MIT and InsideSales lead response study)."),''')
rep('''The founders hold about 54 percent, escrowed for 36 months under exchange policy, and have not sold a share. The selling since listing has come from legacy shareholders of the capital pool company; it is small relative to the float."),''',
'''The founders hold about 54 percent, escrowed for 36 months under exchange policy, and have not sold a share."),''')

# ------------------------------------------------------------------ HOW IT WORKS
rep('''is the largest wholesale vehicle marketplace in the country and OCAL's exclusive auction and sourcing channel.''',
'''is the largest wholesale vehicle marketplace in the country and OCAL's auction and sourcing channel.''')
rep('''Repossessions on OCAL's files run under one percent on management information."],''',
'''Fewer than one percent of the vehicle loans arranged through OCAL's platform from its first funded transaction in 2021 to 30 September 2026 have resulted in repossession (management information, based on lender reporting)."],''')
rep('''a credit-intelligence engine that routes each file to the lender most likely to fund it (management reports about 14 percent more approvals funded than single-lender submission), the OCAL Showroom''',
'''a credit-intelligence engine that routes each file to the lender most likely to fund it, the OCAL Showroom''')
rep('''("note", "The repossession rate and the approval lift are management information, unaudited. Consumer pages for customers are at ocalfinancial.ca; financing is on approved credit and the lender makes the final approval."),''',
'''("note", "The repossession rate is management information, unaudited. " + FUNDED_DEF + " Consumer pages for customers are at ocalfinancial.ca; financing is on approved credit and the lender makes the final approval."),''')

# ------------------------------------------------------------------ STOCK
rep('''["Insider selling since listing", "None. Principals' securities are escrowed.", "SEDI"],
        ], "Figures as at " + SITE["facts_date"] + ". [[Terence confirms shares outstanding, warrants and options against the share register before go-live.]]"),''',
'''["Founder selling since listing", "None. The founders' shares are in escrow.", "SEDI"],
        ], "Figures as at " + SITE["facts_date"] + ", from the Filing Statement, the material change report of 22 July 2026 and the news releases of 6 and 29 August 2026."),''')
rep('''The 6,029,500 shares issued in the July 2026 financing become free trading on 7 November 2026 under the standard four-month hold. We publish this so the overhang is priced as known rather than feared."),''',
'''The 6,029,500 shares issued in the July 2026 financing become free trading on 8 November 2026, when the standard four-month hold expires. We publish the schedule so that every investor knows when shares become tradable."),''')
rep('''], "Dates follow the standard TSXV Tier 2 value escrow schedule from the listing date. [[Terence: insert the share count per tranche from the escrow agreement, and the CPC escrow count and dates, before go-live.]]"),''',
'''], "Dates follow the standard TSXV Tier 2 value escrow schedule from the listing date of 21 July 2026. The escrowed securities are described in the Filing Statement on SEDAR+."),''')

# ------------------------------------------------------------------ OPERATING METRICS
rep('''So we publish the operating metrics with every news release, under fixed definitions, and keep the history here.",''',
'''So we publish the operating metrics in a monthly results release, under fixed definitions, and keep the history here.",''')
span('''        ("p", "The monthly metrics begin with the October 2026 operating update.''', '''        ("h2", "Definitions, fixed"),''',
'''        ("p", "The monthly series starts with October 2026, reported in the monthly results release of 10 November 2026. Until then this page shows the audited fiscal 2025 and fiscal 2024 totals only."),
        ("h2", "Monthly history"),
        ("p", "Each month is added here the day its release is issued, beside the prior month, under the definitions below: vehicles funded and delivered, average vehicle selling price, gross profit per vehicle on both bases and gross margin, with the reconciling items stated. The Chief Financial Officer confirms every figure against the ledger before it is released. Once a metric is reported it is reported every month, including in a slow one."),
''')
rep('''["Period and cadence", "Calendar month, reported in the first release after the month closes, starting with October 2026 (release planned for early November 2026). Each figure is shown beside the prior month.''',
'''["Period and cadence", "Calendar month, reported in the monthly results release after the month closes, starting with October 2026 on 10 November 2026. Each figure is shown beside the prior month.''')
rep('''against a fixed-cost base of about $160,000 a month that management describes in the MD&A. Gross profit per vehicle''',
'''against a cost base that is largely fixed (operating expenses of $1,114,195 in fiscal 2025, audited). Gross profit per vehicle''')
rep('''["Vehicles funded and delivered per month", "The single number the model turns on; fixed operating costs of about $160,000 a month, per the MD&A, do not grow with it", "Every monthly release; quarterly MD&A"],
            ["Customer-acquisition cost", "Reported in the MD&A as it changes", "MD&A; operational releases"],
            ["Gross profit per vehicle (both bases) and protection attach (about 98 percent, trailing twelve months)", "Whether volume comes without giving up margin", "Every monthly release; MD&A"],''',
'''["Vehicles funded and delivered per month", "The single number the model turns on; the largely fixed cost base does not grow with it", "Every monthly results release; quarterly MD&A"],
            ["Acquisition cost per funded deal", "Expected to fall as lead generation, the CRM and the AI sales agents run on one platform; reported when a results release carries it", "Results releases; MD&A"],
            ["Gross profit per vehicle (both bases) and protection attach (about 98 percent of funded transactions, management information)", "Whether volume comes without giving up margin", "Every monthly results release; MD&A"],''')
rep('''["Licences", "Manitoba (application filed), Ontario (registration in progress), then the Maritimes", "News releases, when granted"],''',
'''["Licences", "Manitoba (dealer permit application under way), Ontario (registration under way), then the Maritimes", "News releases, when granted"],''')

# ------------------------------------------------------------------ NEWS and the release page
rep('''From the October 2026 operating update, issued in November 2026, each one carries the operating update section.",''',
'''From 10 November 2026, a monthly results release reports the operating metrics for the month just closed.",''')
rep('''("note", "Releases issued before 15 July 2026 were issued by Ronin Ventures Corp.,''',
'''("note", "Where a release was corrected or reissued, the final version is listed. Releases issued before 15 July 2026 were issued by Ronin Ventures Corp.,''')

span("# Sample release page:", "# ------------------------------------------------------------------ EVENTS", r'''# Release page: the 3 November 2026 release (08) set in the site template, text as issued on Newsfile. This is the per-release page pattern for CQ.
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

''')

# ------------------------------------------------------------------ PRESENTATIONS
rep('''"sub": "The October 2026 set: the presentation, the one-page pitch, the four-page brief, the long-form briefing and the investor questions and answers. Each is refreshed within ten days of every reported period.",''',
'''"sub": "The October 2026 set: the presentation, the one-page pitch, the four-page brief, the long-form briefing and the investor questions and answers. Each is refreshed when a reported figure changes, and the superseded version is withdrawn.",''')
rep('''bought at wholesale through OPENLANE, OCAL's exclusive auction and sourcing channel, and delivered to the driveway. Zero standing inventory, no consumer loans held, the licensed motor dealer of record on every transaction. Audited fiscal 2025 revenue of $6.48 million, up 19 percent, with gross profit up 33 percent; more than 1,500 funded transactions since 2021; fixed operating costs of about $160,000 a month, per the MD&A, that do not grow with the count; licensed in British Columbia and Alberta, with the Manitoba dealer licence application filed and Ontario registration in progress, targeted for 2027, subject to registration and capital. The founders hold about 54 percent and have not sold a share."),''',
'''bought at wholesale through OPENLANE, OCAL's auction and sourcing channel, and delivered to the driveway. Zero standing inventory, no consumer loans held, the licensed motor dealer of record on every transaction. Audited fiscal 2025 revenue of $6.48 million, up 18.8 percent, with gross profit up 32.7 percent and operating expenses down 9.8 percent; more than 1,500 funded vehicle transactions since 2021; a largely fixed cost base that does not grow with the count; licensed in British Columbia and Alberta, with the Manitoba dealer permit application under way and Ontario registration under way, targeted for 2027, subject to registration and capital. The founders hold about 54 percent and have not sold a share."),
        ("note", FUNDED_DEF),''')
span('''        ("h2", "Video"),''', '''        ("h2", "Superseded documents"),''', "")

# ------------------------------------------------------------------ FACT SHEET
rep('''title="OCAL Financial Fact Sheet, October 2026 (TSXV: OCAL)",''', '''title="OCAL Financial Fact Sheet, November 2026 (TSXV: OCAL)",''')
rep('''"kicker": "INVESTOR FACT SHEET  ·  OCTOBER 2026  ·  TSXV: OCAL  ·  FSE: JC3",''', '''"kicker": "INVESTOR FACT SHEET  ·  NOVEMBER 2026  ·  TSXV: OCAL  ·  FSE: JC3",''')
rep('''No lot, no standing inventory, no seasonality; a new market costs a licence, a bond and a small office, not a building."),''',
'''No lot, no standing inventory; a new market costs a licence, a bond and a small office, not a building."),''')
rep('''("Operating leverage.", "Fixed operating costs of about $160,000 a month (MD&A) that do not grow with the count; as volume increases the Company has the potential to spread them across more vehicle sales. Gross profit up 33 percent and operating expenses down 10 percent in fiscal 2025."),''',
'''("Operating leverage.", "A largely fixed cost base that does not grow with the count; as volume increases the Company has the potential to spread it across more vehicle sales. In fiscal 2025 revenue rose 18.8 percent and gross profit 32.7 percent while operating expenses fell 9.8 percent, and the operating loss halved."),''')
rep('''["Manitoba", "Dealer licence application filed; office and OPENLANE access in place", "Next, when the licence is granted"],
            ["Ontario", "Registration in progress", "Targeted for 2027, subject to registration and capital"],''',
'''["Manitoba", "Dealer permit application under way; office inside the OPENLANE Winnipeg facility arranged", "Next: targeted for December 2026, when the permit is granted"],
            ["Ontario", "Registration under way", "Targeted for 2027, subject to registration and capital"],''')
rep('''("p", "Founders hold about 54 percent, escrowed, and have not sold a share. Shares outstanding 36,667,803; about 48 million fully diluted. Operating metrics are published with every release."),''',
'''("p", "Founders hold about 54 percent, escrowed, and have not sold a share. Shares outstanding 36,667,803; about 48.3 million fully diluted. Operating metrics are published every month from 10 November 2026."),''')
rep('''("note", "Audited figures from the financial statements on SEDAR+. Market facts from Statistics Canada, TransUnion, J.D. Power, Cox Automotive, Angus Reid and Presidio-NCM. Planned markets and dates are forward-looking statements subject to the risks in the Filing Statement."),''',
'''("note", FUNDED_DEF + " Audited figures from the financial statements on SEDAR+. Market facts from Statistics Canada, TransUnion, J.D. Power, Cox Automotive, Angus Reid and Presidio-NCM. Planned markets and dates are forward-looking statements subject to the risks in the Filing Statement."),''')

# ------------------------------------------------------------------ GOVERNANCE
rep('''"sub": "An independent audit chair, two committees with written charters, founders escrowed for 36 months, counsel on every release and every number traceable to a filing.",''',
'''"sub": "An independent audit chair, an audit committee charter on the public record, founders escrowed for 36 months, counsel on every release and every number traceable to a filing.",''')
span('''        ("h2", "Documents"),
        ("table", ["Document", "Status"], [''', '''        ("h2", "Annual general meeting"),''',
'''        ("h2", "Documents"),
        ("table", ["Document", "Where to find it"], [
            ["Audit Committee charter", "Set out in the Filing Statement dated 9 July 2026, filed on SEDAR+"],
            ["Notice of articles and articles", "SEDAR+"],
            ["Management information circular, annual general and special meeting of 10 December 2026", "Posted here when filed, with the form of proxy and the notice of meeting"],
        ], "Additional governance policies are posted here as the board adopts them."),
''')
rep('''("p", "The 2026 annual general meeting of shareholders will be held on 10 December 2026 in Vancouver, with online access. The meeting materials, a short management presentation and the voting results will be posted here and filed on SEDAR+. Questions submitted in advance to investors@ocal.ca are answered in writing on this page after the meeting."),''',
'''("p", "The 2026 annual general and special meeting of shareholders will be held on 10 December 2026 at 9:00 am Vancouver time at Suite 1600, 925 West Georgia Street, Vancouver. The record date is 2 November 2026. Shareholders will be asked to set the number of directors at four, elect the directors, approve a new omnibus equity incentive plan to replace the existing stock option plan, and reappoint DMCL LLP as auditor. The management information circular and form of proxy will be sent to shareholders and filed on SEDAR+ before the meeting; the voting results are posted here and filed after it. Questions sent in advance to investors@ocal.ca are answered in writing on this page after the meeting."),''')
rep('''Directors and officers file their holdings and trades on SEDI within five days; no insider has sold a share since listing. [[Add the full insider holdings table from the AGM circular when filed.]]"),''',
'''Directors and officers file their holdings and trades on SEDI within five days; the founders have not sold a share since listing. The full table of insider holdings will be in the management information circular for the annual general and special meeting, filed on SEDAR+."),''')

# ------------------------------------------------------------------ FAQ
rep('''(Answer dated 30 October 2026.)"),''', '''(Answer dated 4 November 2026.)"),''')
rep('''OCAL owns none of them. OPENLANE is OCAL's exclusive auction and sourcing channel; a vehicle is bought''',
'''OCAL owns none of them. OPENLANE is OCAL's auction and sourcing channel; a vehicle is bought''')
rep('''("Where do the cars come from?", "OPENLANE, the largest wholesale marketplace in Canada and OCAL's exclusive auction and sourcing channel, with partner dealers and trade-ins behind it.''',
'''("Where do the cars come from?", "OPENLANE, the largest wholesale marketplace in Canada and OCAL's auction and sourcing channel, with partner dealers and trade-ins behind it.''')
rep('''("How does volume change the economics?", "Fixed operating costs are about $160,000 a month, per the MD&A, and do not grow with the count; commissions and other variable costs are additional. As volume increases, the Company has the potential to spread that cost base across more vehicle sales and is working towards profitability. OCAL does not publish a profitability target, a date or financial guidance; Manitoba and Ontario are the volume markets, and the monthly operating update shows the actual count."),''',
'''("How does volume change the economics?", "The cost base is largely fixed: licences, people, systems and an office that do not grow with the count; commissions and other variable costs are additional. In fiscal 2025 revenue rose 18.8 percent and gross profit 32.7 percent while operating expenses fell 9.8 percent, and the operating loss halved. As volume increases, the Company has the potential to spread its fixed costs across more vehicle sales, and management is working towards profitability through volume. OCAL does not publish a profitability target, a date or financial guidance; Manitoba and Ontario are the volume markets, and the monthly results release shows the actual count."),''')
rep('''("Who takes the credit risk?", "The lender. OCAL originates the contract and holds none of the paper. About 99 percent of signed contracts fund, and the five-year repossession rate on OCAL's files is under one percent as reported by lenders (management information)."),''',
'''("Who takes the credit risk?", "The lender. OCAL originates the contract and holds none of the paper. From the Company's first funded transaction in 2021 to 30 September 2026, about 99 percent of signed customer contracts were funded by lenders, and fewer than one percent of the vehicle loans arranged through the platform have resulted in repossession (management information, based on lender reporting)."),''')
rep('''("How did OCAL cut its customer-acquisition cost?", "Through its demand engine: lead generation, the CRM and an AI agent that answers every lead in seconds, on one platform. Both the cost of a lead and monthly lead spend have fallen sharply since, on management information."),''',
'''("What is happening to the customer-acquisition cost?", "Lead generation, the CRM and the AI sales agents now run on one platform, with an AI agent answering every lead in seconds. The Company expects its acquisition cost per funded deal to fall as a result, and will report it when a results release carries it."),''')
rep('''The July 2026 financing was a private placement agented by Endeavor Financial."),''',
'''The July 2026 financing was a private placement of 6,029,500 units at $0.25 for gross proceeds of $1,507,375."),''')
rep('''("Are insiders selling?", "No. The founders hold about 54 percent, escrowed under exchange policy for 36 months, and have not sold a share. The selling since listing has come from legacy shareholders of the capital pool company."),''',
'''("Are insiders selling?", "No. The founders hold about 54 percent, escrowed under exchange policy for 36 months, and have not sold a share. Insider trades are reported on SEDI within five days."),''')
rep('''The 6.03 million shares from the July 2026 financing become free trading on 7 November 2026."),''',
'''The 6.03 million shares from the July 2026 financing become free trading on 8 November 2026."),''')
rep('''("When is Manitoba?", "The dealer licence application is with the regulator, with the office and auction access in place. Regulators set the timing; OCAL does not announce a licence before it is granted. A Manitoba licence also serves Saskatchewan and north-western Ontario customers."),''',
'''("When is Manitoba?", "The dealer permit application is under way with the regulator, with an office inside the OPENLANE Winnipeg auction facility arranged. Opening is targeted for December 2026, when the permit is granted; regulators set the timing, and OCAL does not announce a permit before it is granted. A Manitoba permit also serves Saskatchewan and northwestern Ontario customers."),''')
rep('''("When is Ontario?", "Registration is in progress, targeted for 2027,''', '''("When is Ontario?", "Registration is under way, targeted for 2027,''')
rep('''("What are the next milestones?", "The first news release carrying the operating update section; the AGM on 10 December 2026; audited fiscal 2026 results by 29 December 2026; the Manitoba licence when granted; Ontario registration; and the first quarter of fiscal 2027 by 29 January 2027."),''',
'''("What are the next milestones?", "The first monthly results release on 10 November 2026; the annual general and special meeting on 10 December 2026; audited fiscal 2026 results by 29 December 2026; the Manitoba permit when granted; Ontario registration; and the first quarter of fiscal 2027 by 29 January 2027."),''')

# ------------------------------------------------------------------ CONTACT
rep('''("REGISTERED HOLDERS", "Transfer agent", "Endeavor Trust Corporation, Vancouver, for share transfers, lost certificates, address changes and registered-holder enquiries. [[Endeavor phone and email]]", "[[Endeavor URL]]"),''',
'''("REGISTERED HOLDERS", "Transfer agent", "Endeavor Trust Corporation, Suite 702, 777 Hornby Street, Vancouver, BC V6Z 1S4; 604-559-8880; info@endeavortrust.com. For share transfers, lost certificates, address changes and registered-holder enquiries.", "https://www.endeavortrust.com"),''')

# ------------------------------------------------------------------ FACTS
rep('''then sources the vehicle through OPENLANE, its exclusive auction and sourcing channel, and delivers it. Zero standing inventory; no consumer loans held; not a broker."],''',
'''then sources the vehicle through OPENLANE, its auction and sourcing channel, and delivers it. Zero standing inventory; no consumer loans held; not a broker."],''')
rep('''["LEI", SITE["lei"] + " [[Confirm the registered address on GLEIF matches Suite 500, 885 Dunsmuir Street; the register shows a West Georgia Street address.]]"],''',
'''["LEI", SITE["lei"] + " (GLEIF status issued; legal address Suite 1600, 925 West Georgia Street, Vancouver, the registered and records office; headquarters Suite 500, 885 Dunsmuir Street)"],''')
rep('''["Investor relations firm", "Signal Capital Advisors Inc., Toronto (Shushu Feng)"],''',
'''["Investor relations firm", "Signal Capital Advisors Inc. (Shushu Feng, Investor Relations Manager)"],''')
rep('''through OPENLANE Canada, its exclusive auction and sourcing channel. OCAL earns revenue from vehicle sales and related finance and protection products, and does not hold consumer loans or assume credit-default risk. Licensed in British Columbia and Alberta, OCAL generated revenue of $6.48 million (audited) in the fiscal year ended August 31, 2025 and has completed more than 1,500 funded vehicle transactions to date."),
        ("p", "Media and data vendors may use either description without further permission. Logos are in the [media kit](/presentations/)."),''',
'''through OPENLANE Canada, its auction and sourcing channel. OCAL earns revenue from vehicle sales and related finance and protection products, and does not hold consumer loans or assume credit-default risk. Licensed in British Columbia and Alberta, OCAL generated revenue of $6.48 million (audited) in the fiscal year ended August 31, 2025 and has completed more than 1,500 funded vehicle transactions to date."),
        ("note", FUNDED_DEF),
        ("p", "Media and data vendors may use either description without further permission. Logo files are available from investors@ocal.ca."),''')

# ------------------------------------------------------------------ LEGAL
rep('''("p", "The email alert list is held with [[Brevo or Mailchimp]] under a double opt-in; addresses are used only to send OCAL's own releases, filings and event notices and are never sold or shared. The site uses [[Google Analytics 4]] to measure visits; no personal information is collected beyond what you submit.''',
'''("p", "The email alert list is held by OCAL's email service provider under a double opt-in; addresses are used only to send OCAL's own releases, filings and event notices and are never sold or shared. The site uses Google Analytics 4 to measure visits; no personal information is collected beyond what you submit.''')

# ------------------------------------------------------------------ write
left = [m.group(0) for m in re.finditer(r".{0,60}\[\[(?!b\[).{0,80}", src) if "double brackets" not in m.group(0)]
if left:
    print("SURVIVING [[:"); [print("  ", x) for x in left]; sys.exit(1)
assert "exclusive" not in src.lower().replace("exclusive' (garrett", "").replace("never 'exclusive'", ""), "'exclusive' survived"
assert "—" not in src and "–" not in src, "dash"
io.open(PATH, "w", encoding="utf-8", newline="\n").write(src)
print("content.py patched: %d edits" % N)
