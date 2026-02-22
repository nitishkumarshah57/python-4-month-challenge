# Day 05: list in python
# Topic: removing item in list using remove(), membership operator, coditional(if/else)
backpack = ["sword","Broken shield","Potion","Gold coin"]
wallet = 0
item_name = input("what item you want to sell:").capitalize()
if item_name in backpack:
    backpack.remove(item_name)
    wallet += 50
    print("Item Sold")
else:
    print("You don't have that item ")
print("wallet:",wallet)
print("Backpack:",backpack)
