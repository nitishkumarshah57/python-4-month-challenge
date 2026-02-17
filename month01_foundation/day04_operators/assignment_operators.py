# Day 04: operators in python 
# Topic : assignment operator (+=, -=, *=)

wallet = 0
paycheck_amount = int(input("enter paycheck amount :"))
wallet += paycheck_amount
grocery_cost = int(input("enter grocery cost :"))
wallet -= grocery_cost
wallet *= 1.1
print("final balance :",wallet)