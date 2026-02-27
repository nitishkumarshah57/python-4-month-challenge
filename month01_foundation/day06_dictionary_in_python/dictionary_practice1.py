# Day 06: Dictionary in python
# Topic: creating and empty dictionary, user input, and adding key-value pairs

employee = {}
user_name = input("enter your name:")
user_age = int(input("enter your age:"))
user_dept = input("enter your department name:")
employee["name"] = user_name
employee["age"] = user_age
employee["departement"] = user_dept
print(f"current data :{employee}")
print(f"welcome to the {employee['departement']},{employee['name']}")