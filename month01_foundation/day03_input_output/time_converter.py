# Day 03: variables, Input, Integer Math(floor Division & Modulo)
# Topic : time converter

given_second = int(input("enter total seconds : "))
hours = given_second // 3600
minutes = (given_second % 3600)//60
seconds = given_second % 60
print(f"{hours} hours, {minutes} minutes , {seconds} seconds ")