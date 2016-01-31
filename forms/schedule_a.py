schedule_a=dict(
adiv1=cell('>>>>>>>>>>>> Medical and Dental                       ', 0.9, '0'),
adiv2=cell('>>>>>>>>>>>> Taxes you paid                           ', 4.9, '0'),
adiv3=cell('>>>>>>>>>>>> Interest you paid                        ', 9.9, '0'),
adiv4=cell('>>>>>>>>>>>> Gifts to charity                         ', 15.9, '0'),
adiv5=cell('>>>>>>>>>>>> Casualty and theft losses                ', 19.9, '0'),
adiv6=cell('>>>>>>>>>>>> Job expenses                             ', 20.9, '0'),
adiv7=cell('>>>>>>>>>>>> Other                                    ', 27.9, '0'),
adiv8=cell('>>>>>>>>>>>> Total                                    ', 28.9, '0'),

medical_expenses=cell('Medical and dental expenses', 1, flag='u', situation=itemizing),
agi_yet_again=cell('AGI', 2, 'CV("agi_again")', ('agi_again',)),
agi_scaled=cell('AGI scaled', 2, 'CV("agi_again")* (.075 if (over_65 or spouse_over_65) else .1)', ('agi_yet_again',)),
excess_medical=cell('Medical expenses minus fraction of AGI', 4, 'max(CV("medical_expenses") - CV("agi_scaled"), 0)',
                               ('medical_expenses', 'agi_scaled')),
local_taxes=cell('State/local Income OR general sales tax', 5, flag='u', situation=itemizing),
real_estate_taxes=cell('Real estate taxes', 6, flag='u', situation=itemizing),
property_taxes=cell('Personal property taxes', 7, flag='u', situation=itemizing),
other_taxes=cell('Other taxes', 8, flag='u', situation=itemizing),
total_taxes_deducted=cell('Total taxes paid to be deducted', 9,
    'CV("local_taxes")+CV("real_estate_taxes")+CV("property_taxes")+CV("other_taxes")', 
    ("local_taxes", "real_estate_taxes", "property_taxes", "other_taxes")),

reported_mort_interest=cell('Home mortgage interest/points reported on Form 1099', 10, flag='u', situation=itemizing),
unreported_mort_interest=cell('Home mortgage interest not reported on Form 1098', 11, flag='u', situation=itemizing),
unreported_mort_points=cell('Home mortgage points not reported on Form 1098', 12, flag='u', situation=itemizing),
mort_insurance_premia=cell('Mortgage insurance premia', 13, flag='u', situation=itemizing),
investment_interest=cell('Investment interest', 14,  flag='u', situation=itemizing),
total_interest_deduction=cell('Total interest to deduct', 15,
    'CV("reported_mort_interest")+ CV("unreported_mort_interest")+ CV("unreported_mort_points")+ CV("mort_insurance_premia")+ CV("investment_interest")',
    ("reported_mort_interest", "unreported_mort_interest", "unreported_mort_points", "mort_insurance_premia", "investment_interest")),

charity_cash=cell("Gifts to charity by cash or check", 16, flag='u', situation=itemizing),
charity_noncash=cell("Gifts to charity other than by cash or check", 17, flag='u', situation=itemizing),
charity_carryover=cell("Gifts to charity, carryover from prior year", 18, flag='u', situation=itemizing),
charity_total=cell("Gifts to charity, total", 19, 'CV("charity_cash")+ CV("charity_noncash") + CV("charity_carryover")',
                                 ("charity_cash","charity_noncash","charity_carryover")),

casualty_or_theft_losses=cell("Casualty and Theft Losses", 20, flag='u', situation=itemizing),

employee_expenses=cell("Unreimbursed employee expenses—job travel, union dues, job education, etc.", 21, flag='u', situation=itemizing),
tax_prep_fees=cell("Tax prep fees", 22, flag='u', situation=itemizing),
other_work_expenses=cell("Other expenses—investment, safe deposit box, etc.", 23, flag='u', situation=itemizing),

total_expenses=cell("Total expenses", 24, 
    'CV("employee_expenses") + CV("tax_prep_fees") + CV("other_work_expenses")',
    ("employee_expenses", "tax_prep_fees", "other_work_expenses")),
agi_yet_agaain=cell('AGI', 25, 'CV("agi_again")', ('agi_again',)),
agi_scaaled=cell('AGI scaled', 26, 'CV("agi_again")* 0.02 ', ('agi_yet_agaain',)),
expenses_minus_agi_slice=cell("Expenses minus fraction of AGI", 27, 
        "max(CV('total_expenses') - CV('agi_scaaled'), 0)", ("total_expenses", "agi_scaaled",)),

other_deductions=cell("Other deductions", 28, flag='u', situation=itemizing),
total_itemized_deductions=cell("Total itemized deductions (assuming income < $155k)", 29, 
        "CV('excess_medical') + CV('total_taxes_deducted') + CV('total_interest_deduction') \
        + CV('charity_total') + CV('casualty_or_theft_losses') + CV('expenses_minus_agi_slice') + CV('other_deductions')"
        , ('agi_again', 'excess_medical', 'total_taxes_deducted',
        'total_interest_deduction', 'charity_total', 'casualty_or_theft_losses',
        'expenses_minus_agi_slice', 'other_deductions'), situation=itemizing)
        )