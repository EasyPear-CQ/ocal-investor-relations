# -*- coding: utf-8 -*-
"""One-off patch applying the 23 Oct public-record audit (research file D) to content.py. Kept for the record."""
import ast, os
p = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'content.py')
s = open(p, encoding='utf-8').read()

old_start = s.index('# Public news releases since listing.'); old_end = s.index('EVENTS = [')
news = '''# Public news releases since listing (Newsfile; verified 23 Oct 2026 in research file D). Newest first.
NEWS = [
    ("2026-10-22", "OCAL Financial Introduces OCAL Showroom, a Live Virtual View of Its Dealership Operations", "/news/2026-10-22-ocal-showroom/", "Operations"),
    ("2026-10-13", "OCAL Financial Outlines Its Integrated AI Demand Engine", "https://www.newsfilecorp.com/release/318701/OCAL-Financial-Outlines-Its-Integrated-AI-Demand-Engine", "Technology"),
    ("2026-10-06", "OCAL Financial Surpasses 1,250 Funded Vehicle Deals", "https://www.newsfilecorp.com/release/317641/OCAL-Financial-Surpasses-1250-Funded-Vehicle-Deals", "Operating update"),
    ("2026-10-01", "OCAL Financial to Present at The 2026 Cantech Investment Conference in Toronto", "https://www.newsfilecorp.com/release/316906/OCAL-Financial-to-Present-at-The-2026-Cantech-Investment-Conference-in-Toronto", "Events"),
    ("2026-09-29", "OCAL Financial Offers a Digital Inventory of 3,000+ Vehicles via OPENLANE, With Zero Standing Inventory", "https://www.newsfilecorp.com/company/12553/OCAL-Financial", "Operations"),
    ("2026-09-15", "OCAL Financial Explains Its Proprietary Knowledge Base, the Data Asset Behind Its AI", "https://www.newsfilecorp.com/company/12553/OCAL-Financial", "Technology"),
    ("2026-09-08", "OCAL Financial Appoints Ryan McDonald as Vice President of Sales", "https://www.newsfilecorp.com/company/12553/OCAL-Financial", "People"),
    ("2026-09-03", "OCAL Financial Launches Redesigned Website Built for Car Buyers and Investors", "https://www.newsfilecorp.com/release/312785/OCAL-Financial-Launches-Redesigned-Website-Built-for-Car-Buyers-and-Investors", "Corporate"),
    ("2026-08-29", "OCAL Financial Launches Video-First Brand Campaign With DIBO Marketing and Engages Signal Capital for Investor Relations", "https://www.newsfilecorp.com/company/12553/OCAL-Financial", "Corporate"),
    ("2026-08-25", "OCAL Financial Common Shares Now Trading on the Frankfurt Stock Exchange", "https://www.newsfilecorp.com/release/311394/OCAL-Financial-Common-Shares-Now-Trading-on-the-Frankfurt-Stock-Exchange", "Listing"),
    ("2026-08-18", "OCAL Financial Describes CBIS, the System That Runs Its Operations and Data", "https://www.newsfilecorp.com/company/12553/OCAL-Financial", "Technology"),
    ("2026-08-14", "OCAL Financial Adds AI Sales-Agent Technology Built Around Its Proprietary Knowledge Base (correction from source)", "https://www.newsfilecorp.com/company/12553/OCAL-Financial", "Technology"),
    ("2026-08-11", "OCAL Financial Explains Its Credit and Lender-Routing System, and the Underserved Market It Serves", "https://www.newsfilecorp.com/company/12553/OCAL-Financial", "Operations"),
    ("2026-08-06", "OCAL Financial Describes the Voice AI Behind Its Lead Engagement and Provides Business Update", "https://www.newsfilecorp.com/company/12553/OCAL-Financial", "Corporate"),
    ("2026-08-04", "OCAL Financial Explains How Its Integrated Model Differs From Online Auto Retailers, Brokers and Fintech Lenders", "https://www.newsfilecorp.com/company/12553/OCAL-Financial", "Operations"),
    ("2026-07-30", "OCAL Financial Outlines How Its Virtual, Finance-First Model Differs From the Traditional Dealership", "https://www.newsfilecorp.com/release/307230/OCAL-Financial-Outlines-How-Its-Virtual-FinanceFirst-Model-Differs-From-the-Traditional-Dealership", "Operations"),
    ("2026-07-28", "OCAL Financial Details Its End-to-End Digital Vehicle-Financing Process", "https://www.newsfilecorp.com/release/306770/OCAL-Financial-Details-Its-EndtoEnd-Digital-VehicleFinancing-Process", "Operations"),
    ("2026-07-23", "OCAL Financial Inc. Provides Corporate Overview Following TSX Venture Exchange Listing", "https://www.newsfilecorp.com/release/306175/OCAL-Financial-Inc.-Provides-Corporate-Overview-Following-TSX-Venture-Exchange-Listing", "Corporate"),
    ("2026-07-21", "OCAL Financial Inc. Completes Qualifying Transaction and Begins Trading on the TSX Venture Exchange", "https://www.newsfilecorp.com/release/305866/OCAL-Financial-Inc.-Completes-Qualifying-Transaction-and-Begins-Trading-on-the-TSX-Venture-Exchange", "Listing"),
]
# [[CQ: each release gets its own page at /news/YYYY-MM-DD-slug/ in the template shown by the 22 Oct sample; until then the links go to Newsfile.]]

'''
s = s[:old_start] + news + s[old_end:]

def rep(a, b):
    global s
    assert a in s, a[:70]
    s = s.replace(a, b, 1)

rep('''            ["Warrants", "About 11.0 million at $0.10 to $0.50, the bulk being 6.0 million financing warrants at $0.50 expiring July 2028", "Filing Statement"],
            ["Options", "About 0.85 million", "Filing Statement; option grants as released"],
            ["Fully diluted", "About 48 million", "Calculated"],
            ["July 2026 financing", "$1.5 million at $0.25 per unit, each unit one share and one warrant at $0.50; closed 7 July 2026; Endeavor Financial as agent", "News release; Filing Statement"],''',
'''            ["Shares in escrow", "23,638,104 (about 64% of shares outstanding): principals' shares in TSXV Tier 2 value escrow over 36 months, plus legacy capital-pool shares in CPC escrow", "TSXV bulletin; TMX Money"],
            ["Warrants", "11,029,501: 5,000,001 at $0.10 and 6,029,500 at $0.50 expiring 7 July 2028; plus 39,760 finder warrants at $0.50", "Material change report, 22 July 2026"],
            ["Options", "600,000: 450,000 at $0.10 to 11 August 2027 and 150,000 at $0.25 over five years; a further 100,000 at $0.13 to the investor relations firm, subject to exchange acceptance", "Material change report; 29 August 2026 release"],
            ["Fully diluted", "About 48.3 million", "Calculated from the above"],
            ["July 2026 financing", "6,029,500 units at $0.25 for gross proceeds of $1,507,375, each unit one share and one warrant at $0.50 for 24 months; closed 7 July 2026", "Material change report"],''')

rep('''        ("p", "Principals' shares (19,024,296) are held in TSXV Tier 2 value escrow: 10 percent was released at listing on 21 July 2026 and 15 percent is released every six months after that, over 36 months. A further 1,875,000 legacy capital-pool shares sit in CPC escrow over 18 months. The 6.03 million shares issued in the July 2026 financing become free trading on 7 November 2026 under the standard four-month hold. We publish this so the overhang is priced as known rather than feared."),
        ("table", ["Value escrow release", "Date", "Shares released", "Cumulative"], [
            ["10% at listing", "21 July 2026", "1,902,430", "1,902,430"],
            ["15%", "21 January 2027", "2,853,644", "4,756,074"],
            ["15%", "21 July 2027", "2,853,644", "7,609,718"],
            ["15%", "21 January 2028", "2,853,644", "10,463,362"],
            ["15%", "21 July 2028", "2,853,644", "13,317,006"],
            ["15%", "21 January 2029", "2,853,644", "16,170,650"],
            ["15%", "21 July 2029", "2,853,646", "19,024,296"],
        ], "Dates follow the standard Tier 2 value escrow schedule from the listing date. [[Confirm against the escrow agreement before go-live.]]"),''',
'''        ("p", "23,638,104 shares, about 64 percent of the shares outstanding, are in escrow. The principals' shares are held in TSXV Tier 2 value escrow: 10 percent was released at listing on 21 July 2026 and 15 percent is released every six months after that, over 36 months. The legacy capital-pool shares sit in CPC escrow released over 18 months. The 6,029,500 shares issued in the July 2026 financing become free trading on 7 November 2026 under the standard four-month hold. We publish this so the overhang is priced as known rather than feared."),
        ("table", ["Value escrow release", "Date", "Share of principals' escrowed shares"], [
            ["At listing", "21 July 2026", "10%"],
            ["Second release", "21 January 2027", "15%"],
            ["Third release", "21 July 2027", "15%"],
            ["Fourth release", "21 January 2028", "15%"],
            ["Fifth release", "21 July 2028", "15%"],
            ["Sixth release", "21 January 2029", "15%"],
            ["Final release", "21 July 2029", "15%"],
        ], "Dates follow the standard TSXV Tier 2 value escrow schedule from the listing date. [[Terence: insert the share count per tranche from the escrow agreement, and the CPC escrow count and dates, before go-live.]]"),''')

rep('''            ["Market making", "[[State the market-making arrangement exactly as released under TSXV Policy 3.4, or omit this row.]]"],''',
    '''            ["Market making", "Integral Wealth Securities Limited, engaged August 2026 at $6,000 a month, as announced on 6 August 2026"],''')

rep('''            ("Is there analyst coverage or a market maker?", "No analyst covers OCAL at this date; we will list every analyst here when one does. [[Market making: state the arrangement exactly as released, or say 'none'.]]"),''',
    '''            ("Is there analyst coverage or a market maker?", "No analyst covers OCAL at this date; we will list every analyst here when one does. Integral Wealth Securities Limited provides market making under an agreement announced on 6 August 2026, at $6,000 a month and no securities compensation. Signal Capital Advisors provides investor relations under an agreement announced on 29 August 2026."),''')

rep('''        ("h2", "The business"),
        ("faq", [
            ("Is OCAL a broker?",''',
'''        ("h2", "The business"),
        ("faq", [
            ("The financial statements show inventory and a floorplan facility. How is that zero standing inventory?", "Because a vehicle bought against an approved customer sits on the balance sheet for the few days between purchase and delivery, and the purchase line that funds it for those days shows as a floorplan facility. At 31 May 2026 inventory was $86,300 and the floorplan balance $222,033, against nine-month revenue of $4.67 million: days of vehicles, not months. Nothing is bought on speculation, and no vehicle is held waiting for a buyer."),
            ("Where does the revenue come from?", "Retail vehicle sales are about nine-tenths of revenue; finance, insurance and other income is the rest. The vehicle sale carries the top line at a modest margin, and the finance and protection layer carries most of the gross profit, which is why gross profit per vehicle is the metric to watch."),
            ("Is OCAL a broker?",''')

rep('''        ("h2", "One line on a number you may have seen elsewhere"),''',
'''        ("h2", "Latest interim period"),
        ("kpis", [
            ("$4.67M", "revenue, nine months to 31 May 2026", "up from $4.50M; vehicle sales $4.16M, finance, insurance and other $0.51M"),
            ("$607K", "gross profit, nine months", "$184K on vehicles, $423K on finance, insurance and other"),
            ("($464K)", "net loss, nine months", "including $183K of listing expense and $46K of share-based compensation"),
            ("$431K", "cash at 31 May 2026", "before the $1.51M financing that closed 7 July 2026"),
        ]),
        ("p", "Inventory at 31 May 2026 was $86,300 and the revolving floorplan facility $222,033: the vehicles bought against approved customers and awaiting delivery on that day, and the purchase line that funded them. That is what zero standing inventory looks like on a balance sheet."),
        ("h2", "One line on a number you may have seen elsewhere"),''')

rep('''    ("Hasneen Jalil", "Founder of Canada Auto Experts; leads the demand engine and platform", "Hasneen Jalil.png",
     "Built the lead-generation engine and automotive CRM that OCAL acquired in September 2026 and now runs inside the company: lead generation, the CRM, platform architecture, security and delivery."),''',
'''    ("Hasneen Jalil", "Founder of Canada Auto Experts; leads the demand engine and platform", "Hasneen Jalil.png",
     "Built the lead-generation engine and automotive CRM that now run OCAL's demand side: lead generation, the CRM, platform architecture, security and delivery."),
    ("Ryan McDonald", "Vice President of Sales", "",
     "Appointed September 2026. Two decades running high-volume dealership sales teams in Western Canada. [[One more line from the 8 September 2026 release.]]"),''')

rep('''            ("What did OCAL buy in Canada Auto Experts, and what did it pay?", "Its lead supplier: the operating business, the EasyPear lead-generation engine and CRM, the pipeline and the team, paid mainly in common shares that vest only against delivered performance. The largest recurring cost in the business became an owned asset, paid for in a currency that only costs the Company if it works. Blended acquisition cost was about $1,027 per funded deal before the acquisition; the target is about $250."),''',
    '''            ("How did OCAL cut its customer-acquisition cost?", "By bringing lead generation in-house. OCAL used to buy leads from a supplier at a blended cost of about $1,027 per funded deal. Its demand engine now runs inside the company: its own lead generation, its own CRM and an AI agent that answers every lead in seconds. Lead cost has fallen from about $145 to the low $20s and monthly lead spend from about $25,000 to about $7,000 on management information; the target is about $250 per funded deal. [[If the acquisition of the lead supplier is announced by news release before go-live, add one sentence naming it and the performance-vested share consideration.]]"),''')

rep('''        ("p", "A founder-led demand engine and CRM team from the Canada Auto Experts and EasyPear acquisition; a Maritimes partner from the automotive business; and advisors who ran divisions of Solera, Repairify and AutoZone.''',
    '''        ("p", "A founder-led demand engine and CRM team; a Maritimes partner from the automotive business; and advisors who ran divisions of Solera, Repairify and AutoZone.''')

rep('''            ("Why did a company this size go public?", "To fund a national roll-out of a model that already works, and to have a listed currency for transactions like the Canada Auto Experts acquisition, which was paid mainly in performance-vested shares. Public gave OCAL a currency and a window that private never could."),''',
    '''            ("Why did a company this size go public?", "To fund a national roll-out of a model that already works, and to have a listed currency for acquisitions and for recruiting. Public gave OCAL a currency and a window that private never could."),''')

rep('''and the close rate is up from five percent to seven since we brought the lead company in-house."),''',
    '''and the close rate is up from five percent to seven since lead generation came in-house."),''')

rep('''["Blended customer-acquisition cost", "Fell from about $1,027 per funded deal to a target of about $250 after the lead engine came in-house", "MD&A; operational releases"],''',
    '''["Blended customer-acquisition cost", "About $1,027 per funded deal when leads were bought from a supplier; the target is about $250 with lead generation in-house", "MD&A; operational releases"],''')

open(p, 'w', encoding='utf-8').write(s)
ast.parse(s)
print('patched; em dashes:', s.count('—'), 'en dashes:', s.count('–'))
