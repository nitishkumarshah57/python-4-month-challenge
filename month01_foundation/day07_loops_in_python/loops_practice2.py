# Day 07: loops in python
# Topic: The for loop, range(), math operator and f-string

base_num = int(input("enter a base number:"))
for i in range(1,11):
    result = base_num * i
    print(f"{base_num} x {i} = {result}")