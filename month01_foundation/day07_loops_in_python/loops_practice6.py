# Day 07: loops in python 
# Topic: Nested loop and 2D list

ocean_grid = [
    ["-","-","-"],
    ["-","s","-"],
    ["-","-","-"]
    ]

for r in range(3):
    for c in range(3):
        if ocean_grid[r][c] == "s":
         print(f"enemy submarine found at row {r}, column {c}!")