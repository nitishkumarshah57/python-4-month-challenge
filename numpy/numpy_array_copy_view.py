# Numpy practice day 4
# Topic:  Numpy Array copy and view

import numpy as np 

brain_scan = np.array([
    [1.2, 1.5, 0.8, 1.1, 1.0],
    [1.4, 1.9, 0.7, 0.9, 1.2],
    [0.9, 0.8, 1.0, 1.3, 1.5],
    [1.1, 1.0, 1.2, 2.1, 2.5],
    [1.0, 0.9, 1.1, 2.4, 2.8]
])
frontal_lobe = brain_scan[0:2,0:2]
occipital_lobe = brain_scan[-2:,-2:].copy()
new_occipital_lobe = occipital_lobe.astype(int)
frontal_lobe[0,0] = 99.9
occipital_lobe[0,0] = 88
print(brain_scan)
print(occipital_lobe)
print(frontal_lobe)
print(new_occipital_lobe)