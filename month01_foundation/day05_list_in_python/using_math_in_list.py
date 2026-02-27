# Day 05: list in python 
# Topic: using math in list (sum, min, max, len)

sale_ledger = [50, 100, 120, 15, 300, 45]
last_customer = int(input("the amount of the item purchased by the last customer of the day:"))
sale_ledger.append(last_customer)
Total_revenue = sum(sale_ledger)
Total_transactions = len(sale_ledger)
Higest_sale = max(sale_ledger)
lowest_sale = min(sale_ledger)
print(f"Total revenue of the day:{Total_revenue},Total transactions of the day:{Total_transactions},Highest sale of the day:{Higest_sale} and lowest sale of the day:{lowest_sale}")