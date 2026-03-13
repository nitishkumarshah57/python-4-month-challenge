# Day 06: Dictionary in Python
# Topic: lists of dictionary and chained indexing

database = [
            {"name":"Nitish","role":"Admin","access_level":5},
            {"name":"Sam","role":"Intern","access_level":1},
            {"name":"Himanshu","role":"Manager","access_level":3}
            ]
user_id = int(input("enter your employee ID number(0,1 or 2):"))
employee = database[user_id]
if employee ["access_level"] >= 3:
    print(f"Access Granted for {employee['name']} Role : {employee['role']}")
else:
    print(f"Access Denied for {employee['name']}. Level {employee['access_level']} is too low.")   