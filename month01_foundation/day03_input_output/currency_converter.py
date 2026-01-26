# Day 03 - variables, user input, math & type conversion
# Topic : converting the currency - 1 USD = 0.85 Euros & 1 USD = 110 Yen


budget = float(input("what is your total budget : "))
budget_europe = budget/2
budget_japan = budget/2
rate_euro = 0.85
rate_yen = 110
budget_euro = budget_europe*rate_euro
budget_yen = budget_japan*rate_yen
print(f" budget for europe in euro is {budget_euro}, budget for japan in yen is {budget_yen}")