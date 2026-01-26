# Day 03 - Input and Output with variables
# Topic swapping the values stored in variables

item_a = input("enter item a :")
item_b = input("enter item b :")
print(f" original : a is {item_a},b is {item_b}")
temp = item_a
item_a = item_b
item_b = temp
print(f"swapped : a is {item_a}, b is {item_b}")
 