# Topic : NumPy joining array

import numpy as np

# --- Setup Data ---
prices_day1_to_3 = np.array([
    [100.5, 102.0, 99.0, 101.5],
    [101.5, 103.5, 100.5, 102.8],
    [102.8, 104.0, 101.0, 103.2]
])

volume_day1_to_3 = np.array([1500, 1800, 1600])

data_day4_and_5 = np.array([
    [103.2, 105.0, 102.5, 104.5, 2000],
    [104.5, 106.0, 103.0, 105.8, 2200]
])


new_volume = volume_day1_to_3.reshape(3, 1)

initial_batch = np.concatenate((prices_day1_to_3, new_volume), axis=1)

full_dataset = np.concatenate((initial_batch, data_day4_and_5), axis=0)
print("Shape of full_dataset:", full_dataset.shape) 

close_prices = full_dataset[:, 3].copy().astype(int)
print("Close Prices (Integers):", close_prices)


