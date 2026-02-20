# Day 04: operator in python
# Topic : operator Precedence
user_income = int(input("enter the income :"))
user_cc = int(input("enter the credit score :"))
user_debt = int(input("enter the debt amount :"))
is_approved = ((user_income > 50000 or user_cc >= 700) and user_debt < 10000)
print(f"Loan Approved :{is_approved}")