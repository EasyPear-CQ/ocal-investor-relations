# -*- coding: utf-8 -*-
"""Patch 3 (23 Oct 2026): align the site with the release program rebuilt the same day
(OCAL\\Press Releases\\02 Scheduled\\00 Release program 2026-10-23 ... (internal).md): monthly operating update,
two-basis gross profit per vehicle, audited FY2024 comparatives, 28-vehicle break-even arithmetic, seven lenders,
public funded-deal count 1,250+, SEDI founder holdings. Kept for the record."""
import ast, os
p = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'content.py')
s = open(p, encoding='utf-8').read()

def rep(a, b, count=1):
    global s
    assert a in s, a[:80]
    s = s.replace(a, b, count)

# Funded deals: match the public record (6 Oct release) until a new cumulative count is released
rep('"1,500+", "funded vehicle deals since 2021", "Two provinces, no growth capital, a visible repeat and referral habit"',
    '"1,250+", "funded vehicle deals since 2021", "As disclosed 6 October 2026; two provinces, no growth capital, 17.6% repeat and referral"')
rep('("1,500+", "funded deals", "with a repeat and referral habit"),', '("1,250+", "funded deals", "as disclosed 6 October 2026"),')
rep('("1,500+", "funded deals", "two provinces, no growth capital"),', '("1,250+", "funded deals", "two provinces, no growth capital"),')
rep('more than 1,500 funded deals since 2021; licensed in British Columbia', 'more than 1,250 funded deals since 2021; licensed in British Columbia')
rep('We have more than 1,500 deals of data on which leads convert', 'We have more than 1,250 deals of data on which leads convert')
rep('a team that has done more than 1,500 of these deals', 'a team that has done more than 1,250 of these deals')
rep('"sub": "Approval first. Car second. Five years, more than 1,500 funded deals, zero standing inventory.",',
    '"sub": "Approval first. Car second. Five years, more than 1,250 funded deals, zero standing inventory.",')
rep('"THE CAR DEALER WITH NO CARS  |  TSXV: OCAL  |  FIVE YEARS, 1,500 FUNDED DEALS, ZERO INVENTORY"', '"x"') if 'FIVE YEARS, 1,500' in s else None

# Financials: audited comparatives from the FY2025 statements
rep('("$6.48M", "revenue, FY2025 audited", "$6,480,254; up 19% from $5.45M in FY2024"),',
    '("$6.48M", "revenue, FY2025 audited", "$6,480,254; up 18.8% from $5,454,893 in FY2024"),')
rep('("$810,751", "gross profit, FY2025 audited", "12.5% gross margin, up from 11.2%"),',
    '("$810,751", "gross profit, FY2025 audited", "12.5% gross margin, up from $610,787 and 11.2%"),')
rep('''            ["Revenue", "about $5.3M", "$5.45M", "$6.48M", "Closed 31 August 2026"],
            ["Gross profit", "about $0.40M", "about $0.61M", "$0.81M", "Audited statements"],
            ["Gross margin", "about 7.5%", "11.2%", "12.5%", "and MD&A due"],
            ["Operating result", "loss", "loss, narrowing", "($303,444)", "by 29 December 2026"],
        ], "FY2024 and FY2025 from the audited financial statements for the year ended 31 August 2025 (DMCL LLP); FY2023 per the corporate presentation. [[Terence confirms the FY2023 and FY2024 lines and the gross margin for FY2024 against the audited comparatives.]]"),''',
    '''            ["Revenue", "about $5.3M", "$5,454,893", "$6,480,254", "Closed 31 August 2026"],
            ["Of which vehicle sales", "", "", "$5,630,980", "Audited statements"],
            ["Of which finance, insurance and other", "", "", "$849,274", "and MD&A due"],
            ["Gross profit", "about $0.40M", "$610,787", "$810,751", "by 29 December 2026"],
            ["Gross margin", "about 7.5%", "11.2%", "12.5%", ""],
            ["Operating loss", "", "", "($303,444)", ""],
            ["Net loss", "", "", "($322,090)", ""],
        ], "FY2024 and FY2025 from the audited financial statements for the year ended 31 August 2025 (DMCL LLP), which include $353,094 of vehicle write-downs in FY2025 cost of sales; FY2023 per the corporate presentation. [[Terence confirms the FY2023 line.]]"),''')
rep('("($303K)", "operating loss, FY2025 audited", "$303,444, before the one-time costs of going public in FY2026"),',
    '("($322K)", "net loss, FY2025 audited", "operating loss $303,444; the costs of going public fall in FY2026"),')

# Operating metrics page: monthly, two bases, the program's definitions
rep('''        ("h2", "Definitions, fixed"),
        ("table", ["Metric", "How OCAL calculates it"], [
            ["Vehicles funded", "The number of retail vehicle sale contracts for which the lender advanced funds to OCAL in the period. A deal counts once, in the period the lender funds it, regardless of when the contract was signed or the vehicle delivered."],
            ["Average vehicle price", "Total retail vehicle sale price of vehicles funded in the period, before taxes and before protection products, divided by vehicles funded."],
            ["Gross profit per vehicle", "Revenue recognized on vehicles funded in the period (vehicle sale price, lender reserve and program incentives, protection products, delivery and permitted fees) less the cost of the vehicle including reconditioning, transport and auction fees, divided by vehicles funded. Before commissions, media and overhead."],
            ["Gross margin per vehicle", "Gross profit per vehicle divided by total revenue per vehicle funded, expressed as a percentage."],
            ["Period", "[[Calendar month or fiscal quarter: decide once and keep it.]] Fiscal quarters end 30 November, 28 February, 31 May and 31 August."],
        ], NON_IFRS_NOTE),''',
    '''        ("h2", "Definitions, fixed"),
        ("table", ["Metric", "How OCAL calculates it"], [
            ["Vehicles funded and delivered", "Retail vehicle sale contracts funded by a lender and delivered to the customer in the calendar month. A deal counts once, in the month the lender funds it."],
            ["Average vehicle selling price", "Vehicle sales revenue in the month divided by vehicles funded and delivered, before taxes and before protection products."],
            ["Deal gross profit per vehicle (management basis)", "Gross profit on the vehicle plus finance, insurance and protection product income, per funded vehicle, before inventory write-downs and before the auction, reconditioning and transport costs that IFRS places in cost of sales. Shown split into vehicle margin and finance, insurance and protection income. A non-IFRS ratio; management information."],
            ["Gross profit per vehicle (IFRS basis)", "Gross profit as reported in the financial statements for the month, divided by vehicles funded and delivered. The items that make up the difference from the deal basis are stated beside it each time. For fiscal 2025 the audited figure was about $4,100 per vehicle after $353,094 of vehicle write-downs, or about $5,900 before them."],
            ["Gross margin", "Gross profit (IFRS basis) as a percentage of total revenue in the month. Fiscal 2025 audited: 12.5 percent."],
            ["Period and cadence", "Calendar month, reported in the first release after the month closes, starting with October 2026 (release planned for early November 2026). Each figure is shown beside the prior month. Monthly figures are stated as approximate; once started, the series continues in weak months."],
        ], NON_IFRS_NOTE),''')
rep('''        ("table", ["Period", "Vehicles funded", "Average vehicle price", "Gross profit per vehicle", "Gross margin per vehicle", "Source release"], [
            ["[[Month or quarter ended ...]]", "[[units]]", "[[$ avg price]]", "[[$ GP per vehicle]]", "[[%]]", "[[release date and link]]"],
            ["[[Prior period]]", "[[units]]", "[[$ avg price]]", "[[$ GP per vehicle]]", "[[%]]", "[[release date and link]]"],
            ["Fiscal 2025 (year ended 31 August 2025)", "[[units]]", "[[$ avg price]]", "[[$ GP per vehicle]]", "[[%]]", "Audited statements for the totals; per-vehicle figures derived by management"],
        ], "Terence Lee, CFO, confirms every figure from the ledger before it is released. The first period appears with the first news release carrying the operating update section."),''',
    '''        ("table", ["Month", "Vehicles funded and delivered", "Average selling price", "Deal gross profit per vehicle", "Gross profit per vehicle, IFRS basis", "Gross margin", "Source release"], [
            ["October 2026", "[[units]]", "[[$]]", "[[$ deal basis]]", "[[$ IFRS basis]]", "[[%]]", "[[release, early November 2026]]"],
            ["September 2026 (prior month, for comparison)", "[[units]]", "[[$]]", "[[$ deal basis]]", "[[$ IFRS basis]]", "[[%]]", "same release"],
            ["Fiscal 2025 (year ended 31 August 2025)", "[[units, about 190 to 200]]", "about $29,000", "about $5,900 before write-downs", "about $4,100 after $353,094 of write-downs", "12.5%", "Audited statements; per-vehicle figures derived by management"],
        ], "Terence Lee, CFO, confirms every figure from the ledger before it is released. The first month appears with the first news release carrying the operating update section."),''')
rep('''        ("p", "These are the numbers an investor or a banker needs to reconstruct OCAL's operating leverage: how many vehicles, at what price, earning how much each, against a fixed-cost base that management describes in the MD&A. They are reported for closed periods only. Targets, run-rates and break-even arithmetic belong in the investor presentation under its forward-looking legend, not in a news release, and we keep it that way. A metric reported once is reported every time, including in a slow month."),''',
    '''        ("p", "These are the numbers an investor or a banker needs to reconstruct OCAL's operating leverage: how many vehicles, at what price, earning how much each, against a fixed-cost base of about $160,000 a month that management describes in the MD&A. Gross profit per vehicle is shown two ways, the way Carvana shows it, because the deal-level figure the founders quote (before write-downs and the auction, reconditioning and transport costs that IFRS places in cost of sales) and the audited figure answer different questions; both are stated, with the difference. The metrics are reported for closed months only. Targets and run-rates belong in the investor presentation under its forward-looking legend, not in a news release. A metric reported once is reported every month, including in a slow one."),''')
rep('''            ["Vehicles funded per month", "The single number the model turns on", "Every release; quarterly MD&A"],''',
    '''            ["Vehicles funded and delivered per month", "The single number the model turns on; fixed operating costs of about $160,000 a month equal the contribution from about 28 funded vehicles on management's October 2026 figures", "Every monthly release; quarterly MD&A"],''')
rep('''            ["Gross profit per vehicle and protection attach", "Whether volume comes without giving up margin", "Every release; MD&A"],''',
    '''            ["Gross profit per vehicle (both bases) and protection attach (about 98 percent, trailing twelve months)", "Whether volume comes without giving up margin", "Every monthly release; MD&A"],''')

# Home page operating update paragraph
rep('''        ("p", "Investors used to spend the first half hour of every call rebuilding OCAL's gross margin from scraps. Now the four numbers that describe the business are published with every news release and kept here, with the same definitions every time. Historical only, unaudited, read with the filed statements."),''',
    '''        ("p", "Investors used to spend the first half hour of every call rebuilding OCAL's gross margin from scraps. From the October 2026 operating update, the numbers that describe the business are published every month with the same definitions every time and kept here: vehicles funded and delivered, average selling price, gross profit per vehicle on both the deal basis and the IFRS basis, and gross margin. Historical only, unaudited, read with the filed statements."),''')

# Why OCAL economics table and the FAQ break-even line
rep('''            ["Contribution per deal", "Management information, unaudited", "After commission, verification and delivery; the fixed base is covered in the low thirties of deals a month"],''',
    '''            ["Contribution per deal", "Management information, unaudited", "About $5,500 of deal gross less about $1,500 of variable cost; fixed operating costs of about $160,000 a month equal the contribution from about 28 funded vehicles"],''')
rep('''            ("What does the Company need to break even?", "Management's estimate is in the low thirties of funded vehicles a month in the current footprint, with a fixed base of about $160,000 a month. Manitoba and Ontario are the volume markets. The operating metrics show progress against it every period."),''',
    '''            ("What does the Company need to break even?", "Fixed operating costs are about $160,000 a month, which equals the contribution from about 28 funded vehicles at about $5,500 of deal gross and about $1,500 of variable cost per vehicle, on management's October 2026 figures. That is arithmetic, not a target. Manitoba and Ontario are the volume markets, and the monthly operating update shows the actual count."),''')

# Lenders: seven live on the portal; no name list
rep('''            ("Who are the lenders?", "A panel across prime, near-prime and non-prime, including RBC, TD, Scotiabank, iA Auto Finance, Santander, Eden Park, LendCare and Standard Financial. No single lender is the business; routing each file to the right one is."),''',
    '''            ("Who are the lenders?", "Seven lenders are live on OCAL's submission portal across prime, near-prime and non-prime: about half of Canada's auto lenders and all of the non-prime lenders. No single lender is the business; routing each file to the right one is."),''')
rep('''            ("Who takes the credit risk?", "The lender. OCAL originates the contract and holds none of the paper. Repossessions on OCAL's files run near one percent on management information, far below industry norms for the non-prime segment."),''',
    '''            ("Who takes the credit risk?", "The lender. OCAL originates the contract and holds none of the paper. About 99 percent of signed contracts fund, and the five-year repossession rate on OCAL's files is under one percent as reported by lenders (management information), far below industry norms for the non-prime segment."),''')

# Governance insider ownership: SEDI figures
rep('''        ("p", "The two founders hold about 54 percent of the shares outstanding, in TSXV Tier 2 value escrow released over 36 months from listing. Directors and officers file their holdings and trades on SEDI within five days; no insider has sold a share since listing. [[Insert the insider holdings summary table from the most recent circular when filed.]]"),''',
    '''        ("p", "The two founders hold about 54.3 percent of the shares outstanding (Matthew Friesen 14,212,381 shares and Mehdi Moghareh 5,710,825 shares per SEDI, October 2026), in TSXV Tier 2 value escrow released over 36 months from listing. Directors and officers file their holdings and trades on SEDI within five days; no insider has sold a share since listing. [[Add the full insider holdings table from the AGM circular when filed.]]"),''')

# Events: monthly operating update as a standing item
rep('''EVENTS = [
    ("2026-12-10",''', '''EVENTS = [
    ("2026-11-03", "October 2026 operating update (first monthly release)", "The first news release carrying the monthly operating update: vehicles funded and delivered, average selling price, gross profit per vehicle on both bases, gross margin. [[Date to confirm; planned for the first week of November.]]", "upcoming"),
    ("2026-12-10",''')

open(p, 'w', encoding='utf-8').write(s)
ast.parse(s)
print('patched 3; dashes:', s.count('—') + s.count('–'), '| 1,500 left:', s.count('1,500'))
