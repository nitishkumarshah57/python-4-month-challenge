# Day 07: loops in python 
# Topic: looping through Dictionaries using.item()

menu = {"Black coffee":3.00,"latte":4.50,"blueberry muffin":4.00}
updated_menu = {}
for item, price in menu.items():
    new_price = price + 1.50
    updated_menu[item] = new_price
print(updated_menu)  