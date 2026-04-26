# Numpy practice day 2
# Topic : Array slicing

import numpy as np

grid = np.array([
    [0.1, 0.5, 1.2, 0.4, 0.2],
    [0.3, 2.1, 3.5, 1.8, 0.6],
    [0.8, 4.2, 7.9, 3.8, 1.1],
    [0.4, 1.7, 3.1, 2.0, 0.5],
    [0.2, 0.6, 1.0, 0.5, 0.1]
])

print(grid[2, -2])
print(grid[0:5, -2])
print(grid[1:4,1:4])
print(grid[-2:,-2:])