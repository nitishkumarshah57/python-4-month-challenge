# Day 06: Disctionary in Python
# Topic: Disctionaries, list, Math, Memebrship(in) & conditionals.

items = {"Sword":50,"Shield":20,"Potion":10}
wallet = 45
backpack = []
item_name = input("What would you like to buy ? (Sword,Shield,Potion):").strip().title()

if item_name in items :
    if wallet >=(items[item_name]):
        wallet -= items[item_name]
        backpack.append(item_name)
        print("Purchase Successfull !")
    else:
        print("Not enough gold coin !")
else:
    print("The merchant does not sell that.")
print(f"Wallet: {wallet}")
print(f"Backpack: {backpack}")          
