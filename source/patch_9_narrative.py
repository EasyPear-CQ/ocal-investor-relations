# -*- coding: utf-8 -*-
"""Patch 9 (28 Oct 2026, Matthew): bring the investor site onto the narrative Mehdi and Shushu agreed on 27 Oct
(WhatsApp) and Shushu's 23 Oct notes: OCAL is a technology-enabled automotive financing and purchasing platform that
solves the customer's problem first (approval, the right vehicle, distance, financial understanding); never "virtual
dealership", "online car dealer" or "the car dealer with no cars"; every page follows problem, platform, solution,
thesis; Shushu's three investor themes (proven traction, operating leverage, valuation opportunity) lead the case;
About text is the 27 Oct boilerplate with counsel's sentences; break-even arithmetic is about 27 vehicles at $5,970
(audited fiscal 2025 basis), replacing 28 at $5,500. Kept for the record; content.py is the source of truth."""
import os, ast
HERE = os.path.dirname(os.path.abspath(__file__))
p = os.path.join(HERE, "content.py"); s = open(p, encoding="utf-8").read()

def rep(a, b, n=1):
    global s
    c = s.count(a)
    assert c == n, (c, a[:90])
    s = s.replace(a, b)

ABOUT = ("OCAL Financial Inc. (TSXV: OCAL; FSE: JC3) is a technology-enabled automotive financing and purchasing platform "
         "transforming how Canadians finance and purchase vehicles. Built around an approval-first approach, OCAL connects "
         "customers with suitable financing options before sourcing a vehicle that meets their needs and budget. Its "
         "integrated platform brings together credit assessment and financial guidance, lender matching, vehicle sourcing, "
         "digital transactions and home delivery anywhere in the provinces it serves, eliminating the need to visit a "
         "traditional dealership. OCAL holds no standing vehicle inventory; it sources each vehicle only after a customer is "
         "approved, through OPENLANE Canada, its exclusive auction and sourcing channel. OCAL earns revenue from vehicle "
         "sales and related finance and protection products, and does not hold consumer loans or assume credit-default "
         "risk. Licensed in British Columbia and Alberta, OCAL generated revenue of $6.48 million (audited) in the fiscal "
         "year ended August 31, 2025 and has completed more than 1,500 funded vehicle transactions to date.")

# ---------------------------------------------------------------- lines that hold
rep('''    "Zero standing inventory. No cars on a lot. We stock access. Never 'zero inventory' on its own.",''',
    '''    "OCAL is a technology-enabled automotive financing and purchasing platform that solves the customer's problem first. Never 'virtual dealership', 'online car dealer' or 'the car dealer with no cars' (Mehdi and Shushu, 27 October 2026). Every page follows the same spine: problem, platform, solution, thesis.",
    "Zero standing inventory. No cars on a lot. We stock access. Never 'zero inventory' on its own.",''')

# ---------------------------------------------------------------- home
rep('''    description="OCAL Financial (TSXV: OCAL): the approval-first online car dealer with zero standing inventory. Stock, filings, operating metrics, news, alerts.",''',
    '''    description="OCAL Financial (TSXV: OCAL): the technology-enabled automotive financing and purchasing platform. Approval first, zero standing inventory, audited growth.",''')
rep('''        "h1": "The car dealer with <em>no cars</em>.",
        "sub": "OCAL gets the customer approved by a lender first, then buys the one vehicle that approval supports from OPENLANE's marketplace and delivers it to the driveway. No lot, no standing inventory, no loans on our books. Five years in, the numbers are audited and the copies are being made.",''',
    '''        "h1": "We solve the problem first. <em>The vehicle follows.</em>",
        "sub": "OCAL Financial is a technology-enabled automotive financing and purchasing platform. We redesigned the entire vehicle purchasing process around the customer's financial eligibility, needs and convenience: approved by a lender first, then the one vehicle that approval supports, sourced through OPENLANE and delivered to the driveway anywhere in the province. Zero standing inventory, no loans on our books, and five years of audited numbers.",''')
rep('''            ("$0", "consumer loans held", "Lenders fund the contract and carry the credit risk; OCAL keeps the dealer's margin"),''',
    '''            ("$0", "consumer loans held", "Lenders fund the contract and carry the credit risk; OCAL earns the margin on every transaction"),''')
rep('''        ("kicker", "WHY INVESTORS LEAN IN"),
        ("cards", [
            ("01", "The lot is where dealers lose money", "The average dealership clears about $1,234 of gross on a used vehicle, pays about $90 of floorplan interest on it and holds it 48 days (Presidio-NCM, Cox, 2024 to 2026). OCAL never owns a car without a funded approval behind it, and holds it three to five days.", "/why-ocal/#problem"),
            ("02", "Buyers want the financing step online", "48% of buyers want to apply for credit online but only 33% can (Cox, 2026), and 68% of Canadians do not trust dealerships to act in their interest (Angus Reid, 2025). The step buyers most want online is the one OCAL moved first.", "/why-ocal/#demand"),
            ("03", "The payment is the purchase", "77% of Canadian new-vehicle buyers finance or lease and 57% of loans run 84 months or longer (J.D. Power, 2025), while the large banks have pulled back to the biggest dealerships. OCAL finances prime and non-prime alike through a panel of lenders.", "/why-ocal/#payment"),
        ]),''',
    '''        ("kicker", "WHY INVESTORS LEAN IN"),
        ("cards", [
            ("01", "The problems OCAL solves", "Some people cannot get approved where they shop. Some cannot find the right vehicle at a payment they can carry. Some live hours from the nearest lot. Some have never had financing explained to them. OCAL solves each of these, in that order, and every one solved is a funded transaction.", "/why-ocal/#problem"),
            ("02", "Proven commercial traction", "More than 1,500 funded vehicle transactions since 2021 and audited revenue of $6.48 million in fiscal 2025, up 19 percent, from two provinces with no growth capital. OCAL generates revenue today; it is not developing a product.", "/why-ocal/#traction"),
            ("03", "Operating leverage", "About $5,970 of deal gross profit per vehicle on the audited fiscal 2025 basis, against a fixed cost base of about $160,000 a month that does not grow with volume. That cost base equals the deal gross profit from about 27 vehicles; the number that moves is the count.", "/why-ocal/#economics"),
        ]),''')
rep('''        ("quote", "Everybody else stocks cars. We stock access. There is a difference between no inventory and no access.", "Mehdi Moghareh, Chief Executive Officer"),''',
    '''        ("quote", "Most of the people who come to us have a problem a dealership cannot solve: getting approved, finding the right vehicle, living far from the nearest lot, or simply understanding how financing works. We solve the problem first and the vehicle follows.", "Mehdi Moghareh, Chief Executive Officer"),''')
rep('''            ("READ", "The investment case", "Why approval-first wins, the economics that make people lean in, and the plan to copy one machine into five more markets.", "/why-ocal/"),''',
    '''            ("READ", "The investment case", "The problem, the platform, the solution and the thesis: proven traction, operating leverage, and a plan to copy one machine into five more markets.", "/why-ocal/"),''')

# ---------------------------------------------------------------- why ocal
rep('''    description="The investment case for OCAL: approval first, car second, zero standing inventory, audited revenue growth and a plan to copy one machine into new markets.",''',
    '''    description="Why invest in OCAL: the problem it solves, the platform, the solution and the thesis. Approval first, zero standing inventory, audited growth, operating leverage.",''')
rep('''        "h1": "Approval first. <em>Car second.</em>",
        "sub": "Remember driving to Blockbuster on a Friday night, or booking a holiday across a desk at Flight Centre? That is still how most Canadians buy a car: drive to a lot, pick from what is sitting there, and let a finance manager fit the loan to the car the dealer needs to move. OCAL turned it around.",''',
    '''        "h1": "Problem. Platform. <em>Solution. Thesis.</em>",
        "sub": "Most Canadians still buy a vehicle the way the industry was built: drive to a lot, choose from what is parked there, and let the finance desk fit a loan to that vehicle. OCAL redesigned the entire process around the customer's financial eligibility, needs and convenience. Here is the problem, the platform that solves it, what the customer gets, and the economics that make investors lean in.",''')
rep('''        ("anchor", "problem"),
        ("h2", "1. The problem with every car dealer you have ever met"),
        ("p", "Since 1910 the industry has run on supply: build cars, ship them to lots, advertise the lot, hope the right customer walks in. The average dealership now clears about $1,234 of gross on a used unit, pays about $90 of floorplan interest on each one, and holds it 48 days at about $32 a day (Presidio-NCM, Cox, 2024 to 2026). The lot eats the margin before the customer arrives. Public dealer groups typically hold 35 to 50 percent of their assets in inventory and floorplan debt."),
        ("anchor", "failures"),
        ("p", "Most online car retailers kept the worst part of the old model: they bought inventory first and looked for customers second, then carried the write-downs, the reconditioning plants and the logistics when used-vehicle prices turned. Demand for buying a car online was never the problem. The capital tied up in cars was."),
        ("h3", "What OCAL does instead"),
        ("p", "No lot, no standing inventory, no seasonality, because we do not wait for anyone to walk in. A car is ours for three to five days, financed on a purchase line for exactly those days. We are the licensed dealer that sells the car and arranges the loan. OPENLANE is our exclusive auction and sourcing channel: more than 3,000 vehicles are visible on its Canadian marketplace on a typical day, and none of them is on our balance sheet."),
        ("anchor", "customer"),
        ("h2", "2. What the customer gets"),''',
    '''        ("anchor", "problem"),
        ("h2", "1. The problem OCAL exists to solve"),
        ("p", "Four problems bring a customer to OCAL. They cannot get approved where they shop. They cannot find the right vehicle at a payment they can carry. They live hours from the nearest lot, with few options and no delivery. Or nobody has ever explained to them how vehicle financing works. The industry was built to sell what is parked on the lot, so the lot, not the customer, drives the sale: the average dealership holds a used vehicle 48 days and pays about $90 of floorplan interest on it to clear about $1,234 of gross (Presidio-NCM, Cox, 2024 to 2026). 68 percent of Canadians say they do not trust dealerships to act in their interest (Angus Reid, 2025), and 48 percent want to apply for credit online but only 33 percent can (Cox, 2026). The demand to buy differently was never the problem. The process was."),
        ("anchor", "platform"),
        ("h2", "2. The platform"),
        ("p", "OCAL is a technology-enabled automotive financing and purchasing platform. One workflow carries the customer from a credit application on their phone to lender approval, financial guidance in plain terms, vehicle sourcing, digital contracting and delivery anywhere in the province. The approval comes first, so the vehicle is chosen to fit the customer's eligibility and budget, never the other way around. OPENLANE is OCAL's exclusive auction and sourcing channel: more than 3,000 vehicles are visible on its Canadian marketplace on a typical day, and none of them is on OCAL's balance sheet. OCAL is the licensed motor dealer of record on every transaction, holds no standing inventory, and owns a vehicle for three to five days between purchase and delivery, financed on a purchase line for exactly those days. The lender funds the contract and carries the credit risk."),
        ("anchor", "customer"),
        ("h2", "3. The solution, as the customer sees it"),''')
rep('''            ("They know what they can afford before they fall in love with a truck.", "The approval comes first, so nobody is steered from the Dodge pickup they wanted into the Ford pickup the dealer needed to move. The choice is not forty cars on a lot: it is any vehicle on OPENLANE's marketplace that fits the approval, bought the day they say yes."),''',
    '''            ("They know what they can afford before they fall in love with a truck.", "The approval comes first, so nobody is steered into the vehicle someone else needs to move. The choice is not forty vehicles on a lot: it is any vehicle on OPENLANE's marketplace that fits the approval, bought the day they say yes."),''')
rep('''A prime customer gets a prime rate; a 600 score still gets a bank or finance-company loan, not a dealer note with a GPS cut-off switch."),''',
    '''A prime customer gets a prime rate; a 600 score still gets a bank or finance-company loan, explained in plain terms, not a high-rate note with a GPS cut-off switch."),''')
rep('''        ("anchor", "economics"),
        ("h2", "3. The economics that make people lean in"),
        ("p", "Put simply, every dollar we spend finding a customer comes back as roughly ten dollars of profit after the people who work the file are paid. A thousand leads cost about $30,000; a quarter to a third become conversations; about seven percent of those fund; and each funded deal carries several thousand dollars of gross profit from the vehicle, the lender reserve and protection products. The constraint has never been demand. It is licences, people and lender capacity, and all three are being added now."),''',
    '''        ("anchor", "traction"),
        ("anchor", "economics"),
        ("h2", "4. Traction and operating leverage"),
        ("p", "OCAL already generates revenue: more than 1,500 funded vehicle transactions since 2021 and audited revenue of $6.48 million in fiscal 2025, up 19 percent, on an asset-light structure with no standing inventory. The operating leverage is arithmetic. Deal gross profit per vehicle was about $5,970 on the audited fiscal 2025 basis ($2,370 of vehicle margin and $3,600 of finance, insurance and protection income). Fixed operating costs are about $160,000 a month, which equals the deal gross profit from about 27 funded vehicles, and that cost base does not grow with the count. Put simply, every dollar spent finding a customer comes back as roughly ten dollars of gross profit after the people who work the file are paid: a thousand leads cost about $30,000, a quarter to a third become conversations, about seven percent of those fund. The constraint has never been demand. It is licences, people and lender capacity, and all three are being added now."),''')
rep('''            ["Contribution per deal", "Management information, unaudited", "About $5,500 of deal gross less about $1,500 of variable cost; fixed operating costs of about $160,000 a month equal the contribution from about 28 funded vehicles"],''',
    '''            ["Fixed cost base", "MD&A and management information", "About $160,000 a month, which equals the deal gross profit from about 27 funded vehicles at the audited fiscal 2025 figure of about $5,970; commissions and other variable costs are additional"],''')
rep('''        ("anchor", "payment"),
        ("h2", "4. Why now"),''', '''        ("anchor", "payment"),
        ("h2", "5. Why now"),''')
rep('''        ("anchor", "demand"),
        ("h2", "5. One machine, copied"),''', '''        ("anchor", "demand"),
        ("h2", "6. One machine, copied"),''')
rep('''        ("h2", "6. The plan in numbers"),''', '''        ("h2", "7. The plan in numbers"),''')
rep('''        ("h2", "7. Why nobody can copy it quickly"),
        ("p", "Virtual dealer licences took two years to win in British Columbia.''',
    '''        ("h2", "8. Why it is hard to copy quickly"),
        ("p", "The licences to sell and finance vehicles remotely took two years to win in British Columbia.''')
rep('''        ("h2", "8. The window"),
        ("p", "OCAL trades at a market value of roughly one year of audited revenue.''',
    '''        ("h2", "9. The thesis"),
        ("p", "A revenue-generating, asset-light platform, approaching the volume at which its fixed cost base is covered, with a model designed to scale without the inventory cost of the industry it serves. OCAL trades at a market value of roughly one year of audited revenue.''')

# ---------------------------------------------------------------- how it works
rep('''        ("h2", "How OCAL earns a dealer's margin"),''', '''        ("h2", "How OCAL earns on each transaction"),''')
rep('''which is why the consolidated gross margin reads low while the margin per deal reads like a dealership's finance office."),''',
    '''which is why the consolidated gross margin reads low while the margin per transaction reads like a finance office's."),''')
rep('''and a CRM built for virtual dealerships that OCAL now owns."),''', '''and a CRM built for remote, approval-first transactions that OCAL now owns."),''')

# ---------------------------------------------------------------- operating metrics
rep('''        "sub": "Everyone can run a virtual dealership. What makes OCAL different is the margin per vehicle on a business that owns no cars, and the fixed-cost base that margin has to cover. So we publish the per-vehicle economics with every news release and keep the history here.",''',
    '''        "sub": "Anyone can sell a vehicle. What makes OCAL different is the margin per vehicle on a platform that holds no standing inventory, and the fixed cost base that margin has to cover. So we publish the per-vehicle economics with every news release and keep the history here.",''')
rep('''fixed operating costs of about $160,000 a month equal the contribution from about 28 funded vehicles on management's October 2026 figures''',
    '''fixed operating costs of about $160,000 a month equal the deal gross profit from about 27 funded vehicles at the audited fiscal 2025 figure''')
rep('''            ["Fiscal 2025 (year ended 31 August 2025)", "[[units, about 190 to 200]]", "about $29,000", "about $5,900 before write-downs", "about $4,100 after $353,094 of write-downs", "12.5%", "Audited statements; per-vehicle figures derived by management"],''',
    '''            ["Fiscal 2025 (year ended 31 August 2025)", "about 195 [[Terence to confirm]]", "about $28,900", "about $5,970 before write-downs", "about $4,160 after $353,094 of write-downs", "12.5%", "Audited statements; per-vehicle figures derived by management"],''')
rep('''For fiscal 2025 the audited figure was about $4,100 per vehicle after $353,094 of vehicle write-downs, or about $5,900 before them."],''',
    '''For fiscal 2025 the audited figure was about $4,160 per vehicle after $353,094 of vehicle write-downs, or about $5,970 before them."],''')

# ---------------------------------------------------------------- presentations
rep('''        ("p", "OCAL Financial (TSXV: OCAL, FSE: JC3) is Canada's approval-first online car dealer. The customer is approved by a lender first; the exact vehicle is then bought at wholesale through OPENLANE, OCAL's exclusive auction and sourcing channel, and delivered to the driveway. Zero standing inventory, no consumer loans held, the licensed dealer of record on every deal. Audited fiscal 2025 revenue of $6.48 million, up 19 percent; more than 1,500 funded deals since 2021; licensed in British Columbia and Alberta with Manitoba, Ontario, the Maritimes and Texas in the plan. The founders hold about 54 percent and have not sold a share."),''',
    '''        ("p", "OCAL Financial (TSXV: OCAL, FSE: JC3) is a technology-enabled automotive financing and purchasing platform. It solves the customer's problem first: approval by a lender, then the one vehicle that approval supports, bought at wholesale through OPENLANE, OCAL's exclusive auction and sourcing channel, and delivered to the driveway. Zero standing inventory, no consumer loans held, the licensed motor dealer of record on every transaction. Audited fiscal 2025 revenue of $6.48 million, up 19 percent; more than 1,500 funded transactions since 2021; about $5,970 of deal gross profit per vehicle on a fixed cost base of about $160,000 a month; licensed in British Columbia and Alberta with Manitoba, Ontario, the Maritimes and Texas in the plan. The founders hold about 54 percent and have not sold a share."),''')
rep('''"The full case with sources: the problem with every dealer, what the customer gets, the economics, why now, the plan, the moat, the people."''',
    '''"The full case with sources: the problem, the platform, what the customer gets, traction and operating leverage, why now, the plan, the moat, the people. [[Being reissued on the problem-first narrative.]]"''')
rep("""'The car dealer with no cars', 'A dollar in, ten out'""", """'We solve the problem first', 'A dollar in, ten out'""")

# ---------------------------------------------------------------- fact sheet
rep('''        "h1": "The car dealer with no cars",
        "sub": "Approval first. Car second. Five years, more than 1,500 funded deals, zero standing inventory.",''',
    '''        "h1": "We solve the problem first. The vehicle follows.",
        "sub": "A technology-enabled automotive financing and purchasing platform. Five years, more than 1,500 funded transactions, zero standing inventory.",''')
rep('''        ("p", "Remember driving to Blockbuster on a Friday night? That is still how Canadians buy a car: drive to a lot, pick from what is sitting there, let the finance manager fit the loan to the car. OCAL flipped it. The customer is approved by a lender first, prime or non-prime; then we buy the one car the approval supports from OPENLANE's marketplace and deliver it to their driveway. No lot, no inventory, no seasonality; a new market costs a licence, a bond and a small office, not a building."),''',
    '''        ("p", "Four problems bring a customer to OCAL: they cannot get approved where they shop, cannot find the right vehicle at a payment they can carry, live hours from the nearest lot, or have never had financing explained to them. OCAL redesigned the vehicle purchase around the customer's financial eligibility, needs and convenience. The customer is approved by a lender first, prime or non-prime; then we buy the one vehicle the approval supports from OPENLANE's marketplace and deliver it to their driveway. No lot, no standing inventory, no seasonality; a new market costs a licence, a bond and a small office, not a building."),''')
rep('''        ("h2", "Why it wins"),
        ("bullets", [
            ("The lot is where dealers lose money.", "About $1,234 of gross per used vehicle against $90 of floorplan interest and 48 days on the lot (Presidio-NCM, Cox). OCAL never owns a car without a funded approval."),
            ("Buyers want the financing step online.", "48% want to apply for credit online, 33% can (Cox, 2026); 68% of Canadians do not trust dealerships (Angus Reid, 2025)."),
            ("The payment is the purchase.", "77% of Canadian buyers finance or lease; the large banks pulled back to the biggest dealerships; OCAL's lender panel covers prime to non-prime."),
        ]),''',
    '''        ("h2", "Why investors lean in"),
        ("bullets", [
            ("Proven commercial traction.", "More than 1,500 funded transactions and audited revenue of $6.48 million in fiscal 2025, up 19 percent, from two provinces with no growth capital."),
            ("Operating leverage.", "About $5,970 of deal gross profit per vehicle (audited fiscal 2025 basis) against a fixed cost base of about $160,000 a month, which equals about 27 vehicles. The cost base does not grow with the count."),
            ("A market that wants it.", "48% of buyers want to apply for credit online, 33% can (Cox, 2026); 77% of Canadian buyers finance or lease; OCAL's lender panel covers prime to non-prime."),
        ]),''')

# ---------------------------------------------------------------- faq
rep('''            ("What does the Company need to break even?", "Fixed operating costs are about $160,000 a month, which equals the contribution from about 28 funded vehicles at about $5,500 of deal gross and about $1,500 of variable cost per vehicle, on management's October 2026 figures. That is arithmetic, not a target.''',
    '''            ("What does the Company need to break even?", "Fixed operating costs are about $160,000 a month, which equals the deal gross profit from about 27 funded vehicles at the audited fiscal 2025 figure of about $5,970 per vehicle; commissions and other variable costs are additional to the fixed cost base. That is arithmetic, not a target.''')
rep('''            ("How is this different from an online car retailer that owns its inventory?", "Same customer experience, opposite balance sheet. An inventory-owning online retailer buys the cars first, reconditions them in its own facilities, often lends the money and sells the loans. OCAL owns none of that. It earns the dealer's margin without holding the paper or the inventory, and a vehicle is on its books for three to five days."),''',
    '''            ("Does OCAL own the vehicles it sells?", "Only for the three to five days between buying one against an approved customer and delivering it. OCAL does not buy vehicles first and look for buyers second, does not run reconditioning plants, and does not lend the money or hold the loans. It earns the margin on the transaction without holding the paper or the inventory."),''')
rep('''            ("What is the exit?", "Every dealer group in Canada needs this capability and none has built it. A national footprint with the transaction data and the lender panel is worth more to an acquirer than to the Company alone. Management is building it to run it."),''',
    '''            ("What is the exit?", "A national, licensed, approval-first platform with five years of transaction data and a lender panel is worth more to a strategic acquirer than to the Company alone. Management is building it to run it."),''')

# ---------------------------------------------------------------- facts page
rep('''            ["What the company does", "Approval-first online automotive dealership and vehicle-finance platform. The customer is approved by a lender first; OCAL, the licensed motor dealer of record, then sources the vehicle through OPENLANE, its exclusive auction and sourcing channel, and delivers it. Zero standing inventory; no consumer loans held; not a broker."],
            ["Industry", "Automotive retail (online vehicle sales) and vehicle finance arrangement"],''',
    '''            ["What the company does", "Technology-enabled automotive financing and purchasing platform. The customer is approved by a lender first; OCAL, the licensed motor dealer of record, then sources the vehicle through OPENLANE, its exclusive auction and sourcing channel, and delivers it. Zero standing inventory; no consumer loans held; not a broker."],
            ["Industry", "Automotive financing and purchasing platform (vehicle retail and finance arrangement)"],''')
rep('''        ("p", "**Short (one line).** Virtual automotive dealership and vehicle-finance platform, licensed in British Columbia and Alberta."),
        ("p", "**Standard (for data vendors).** OCAL Financial Inc. is a Vancouver-based, asset-light online automotive dealership and vehicle-finance platform. Operating remotely and licensed in British Columbia and Alberta, OCAL takes customers from application to lender approval, vehicle matching, digital contracting and delivery. It sources each vehicle only after approval, through OPENLANE Canada, its exclusive auction and sourcing channel, and earns revenue from vehicle sales and related finance and protection products. It does not hold consumer loans or take credit-default risk."),''',
    '''        ("p", "**Short (one line).** Technology-enabled automotive financing and purchasing platform, licensed in British Columbia and Alberta."),
        ("p", "**Standard (for data vendors).** ''' + ABOUT + '''"),''')

open(p, "w", encoding="utf-8").write(s); ast.parse(s)

# checks: titles and descriptions within limits, no em or en dashes
import importlib.util, sys
sys.path.insert(0, HERE)
spec = importlib.util.spec_from_file_location("content", p); C = importlib.util.module_from_spec(spec); spec.loader.exec_module(C)
bad = []
for pg in C.PAGES:
    if len(pg["title"]) > 60: bad.append(("title", pg["slug"], len(pg["title"])))
    if len(pg["description"]) > 155: bad.append(("desc", pg["slug"], len(pg["description"])))
for ch in ("—", "–"):
    assert ch not in s, "dash found"
for word in ("virtual dealership", "virtual car dealer", "online car dealer", "car dealer with no cars", "Virtual dealer licences", "virtual dealerships"):
    hits = [i for i in range(len(s)) if s.startswith(word, i)]
    if hits: bad.append((word, len(hits)))
print("patched 9; problems:", bad)
