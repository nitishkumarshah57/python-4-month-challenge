# Day 09: file input & output in python
# Topic: The.readlines() method, lists, type conversion(int), and math.

with open("expenses.txt","r") as file :
    lines_list = file.readlines()
total_expenses = 0  
for line in lines_list:
    total_expenses += int(line) 
print(f"Total expenses for today:{total_expenses}")    
