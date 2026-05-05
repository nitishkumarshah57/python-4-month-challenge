# Numpy practice day 3
# Topic Array Data types

import numpy as np
data = np.array([
    [100.45, 102.11, 99.89, 101.05],
    [105.32, 107.88, 104.12, 106.99],
    [98.55,  97.21,  99.01, 98.88],
    [110.15, 109.45, 111.02, 110.87]
])
print(data.dtype)
core = data[1:3,1:3]
new_array = data.astype(int)
print(core)
print(new_array)
