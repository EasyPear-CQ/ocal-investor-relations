# -*- coding: utf-8 -*-
"""Patch 4 (23 Oct 2026, Matthew's instruction): no competitor is named or described on the investor site.
Industry statistics with a named source stay; named companies go. Kept for the record."""
import ast, os
p = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'content.py')
s = open(p, encoding='utf-8').read()

def rep(a, b):
    global s
    assert a in s, a[:90]
    s = s.replace(a, b, 1)

# Home cards
rep('''            ("01", "The failures all owned cars", "Canada Drives raised more than $200M, pivoted into inventory and filed for creditor protection. Vroom and Shift went bankrupt. OCAL never owns a car without a funded approval behind it.", "/why-ocal/#failures"),
            ("02", "The winners proved the demand", "Carvana sold 596,641 cars online in 2025. Clutch is valued above $575M on $320M of revenue. Buyers want the financing step online, and that is the step OCAL moved first.", "/why-ocal/#demand"),
            ("03", "The payment is the purchase", "77% of Canadian new-vehicle buyers finance or lease, 57% of loans run 84 months or longer, and the big banks retreated to franchise dealers. OCAL finances prime and non-prime alike through a panel of lenders.", "/why-ocal/#payment"),''',
    '''            ("01", "The lot is where dealers lose money", "The average dealership clears about $1,234 of gross on a used vehicle, pays about $90 of floorplan interest on it and holds it 48 days (Presidio-NCM, Cox, 2024 to 2026). OCAL never owns a car without a funded approval behind it, and holds it three to five days.", "/why-ocal/#problem"),
            ("02", "Buyers want the financing step online", "48% of buyers want to apply for credit online but only 33% can (Cox, 2026), and 68% of Canadians do not trust dealerships to act in their interest (Angus Reid, 2025). The step buyers most want online is the one OCAL moved first.", "/why-ocal/#demand"),
            ("03", "The payment is the purchase", "77% of Canadian new-vehicle buyers finance or lease and 57% of loans run 84 months or longer (J.D. Power, 2025), while the large banks have pulled back to the biggest dealerships. OCAL finances prime and non-prime alike through a panel of lenders.", "/why-ocal/#payment"),''')

# Why OCAL section 1
rep('''        ("anchor", "failures"),
        ("p", "The online disruptors kept the worst part: they bought inventory first and looked for customers second. Vroom and Shift went bankrupt. Canada Drives lost $80.5M on $298M of revenue, said holding inventory had become unviable, and filed for creditor protection in 2023. Clutch survived a 97% down round and is now valued above $575M with hubs and a fleet. Carvana made it only after spending US$2.2B on auction sites. Demand was never the problem. Capital was."),''',
    '''        ("anchor", "failures"),
        ("p", "Most online car retailers kept the worst part of the old model: they bought inventory first and looked for customers second, then carried the write-downs, the reconditioning plants and the logistics when used-vehicle prices turned. Demand for buying a car online was never the problem. The capital tied up in cars was."),''')
# Section 4 bullets
rep('''("The big banks walked away from the little guy.", "Six in ten households earn under $100,000 and 28% of credit-active Canadians sit below prime, about nine million people (TransUnion). BMO left indirect auto lending in 2023; the others retreated to franchise dealers selling over 100 cars a month. OCAL's panel covers both ends, prime and non-prime."),''',
    '''("The big banks walked away from the little guy.", "Six in ten households earn under $100,000 and 28% of credit-active Canadians sit below prime, about nine million people (TransUnion). Several large banks have pulled back from indirect auto lending or restricted it to the largest dealerships. OCAL's panel covers both ends, prime and non-prime."),''')
# Section 8 window
rep('''        ("p", "OCAL trades at a market value of roughly one year of audited revenue, while the market paid about 1.8 times revenue for the Canadian competitor that owns its cars. The founders hold about 54 percent,''',
    '''        ("p", "OCAL trades at a market value of roughly one year of audited revenue. The founders hold about 54 percent,''')
rep('''        ("note", "Market facts from Statistics Canada, TransUnion, Equifax, J.D. Power, Cox Automotive, Angus Reid, the Federal Reserve Bank of Dallas and the public filings of Carvana, Clutch and Canada Drives. Audited figures from the financial statements filed on SEDAR+."),''',
    '''        ("note", "Market facts from Statistics Canada, TransUnion, Equifax, J.D. Power, Cox Automotive, Angus Reid, Presidio-NCM and the Federal Reserve Bank of Dallas. Audited figures from the financial statements filed on SEDAR+."),''')
rep('''("p", "Since 1910 the industry has run on supply: build cars, ship them to lots, advertise the lot, hope the right customer walks in. The average dealership now clears about $1,234 of gross on a used unit, pays about $90 of floorplan interest on each one, and holds it 48 days at about $32 a day (Presidio-NCM, Cox, 2024 to 2026). The lot eats the margin before the customer arrives."),''',
    '''("p", "Since 1910 the industry has run on supply: build cars, ship them to lots, advertise the lot, hope the right customer walks in. The average dealership now clears about $1,234 of gross on a used unit, pays about $90 of floorplan interest on each one, and holds it 48 days at about $32 a day (Presidio-NCM, Cox, 2024 to 2026). The lot eats the margin before the customer arrives. Public dealer groups typically hold 35 to 50 percent of their assets in inventory and floorplan debt."),''')

# Metrics page
rep("Gross profit per vehicle is shown two ways, the way Carvana shows it, because the deal-level figure", "Gross profit per vehicle is shown two ways because the deal-level figure")

# Presentations: long-form description
rep("Eighteen sections for investors who want everything: market, model, lenders, technology, numbers, competitors, plan, people, capital structure, risks and twenty-five questions answered.",
    "Eighteen sections for investors who want everything: market, model, lenders, technology, numbers, the landscape, plan, people, capital structure, risks and twenty-five questions answered.")

# Fact sheet
rep('''            ("The failures all owned cars.", "Canada Drives, Vroom and Shift bought inventory first. OCAL never owns a car without a funded approval."),
            ("The winners proved the demand.", "Carvana sold 596,641 cars online in 2025; Clutch is valued above $575M on $320M of revenue."),
            ("The payment is the purchase.", "77% of Canadian buyers finance or lease; the big banks retreated to franchise dealers; OCAL's lender panel covers prime to non-prime."),''',
    '''            ("The lot is where dealers lose money.", "About $1,234 of gross per used vehicle against $90 of floorplan interest and 48 days on the lot (Presidio-NCM, Cox). OCAL never owns a car without a funded approval."),
            ("Buyers want the financing step online.", "48% want to apply for credit online, 33% can (Cox, 2026); 68% of Canadians do not trust dealerships (Angus Reid, 2025)."),
            ("The payment is the purchase.", "77% of Canadian buyers finance or lease; the large banks pulled back to the biggest dealerships; OCAL's lender panel covers prime to non-prime."),''')
rep('''        ("p", "OCAL trades at a market value of roughly one year of audited revenue while the market paid about 1.8 times revenue for the Canadian competitor that owns its cars. Founders hold about 54 percent, escrowed, and have not sold.''',
    '''        ("p", "OCAL trades at a market value of roughly one year of audited revenue. Founders hold about 54 percent, escrowed, and have not sold.''')
rep('''        ("note", "Audited figures from the financial statements on SEDAR+. Market facts from Statistics Canada, TransUnion, J.D. Power, Cox Automotive and the public filings of Carvana, Clutch and Canada Drives. Planned markets and dates are forward-looking statements subject to the risks in the Filing Statement."),''',
    '''        ("note", "Audited figures from the financial statements on SEDAR+. Market facts from Statistics Canada, TransUnion, J.D. Power, Cox Automotive, Angus Reid and Presidio-NCM. Planned markets and dates are forward-looking statements subject to the risks in the Filing Statement."),''')

# FAQ
rep('''            ("How is this different from Carvana?", "Same customer experience, opposite balance sheet. Carvana owns the cars, reconditions them in its own plants, lends the money and sells the loans. OCAL owns none of that. It earns the dealer's margin without holding the paper or the inventory."),''',
    '''            ("How is this different from an online car retailer that owns its inventory?", "Same customer experience, opposite balance sheet. An inventory-owning online retailer buys the cars first, reconditions them in its own facilities, often lends the money and sells the loans. OCAL owns none of that. It earns the dealer's margin without holding the paper or the inventory, and a vehicle is on its books for three to five days."),''')

# Lines that hold: add the rule
rep('''    "No em dashes or en dashes. Canadian spelling.",
]''', '''    "No competitor is named or described on the investor site. Industry statistics with a named source are fine; other companies are not.",
    "No em dashes or en dashes. Canadian spelling.",
]''')

open(p, 'w', encoding='utf-8').write(s)
ast.parse(s)
import re
left = re.findall(r"Carvana|Clutch|Canada Drives|Vroom|Shift |goeasy|AutoCanada|competitor|BMO ", s)
print('patched 4; competitor mentions left:', left)
