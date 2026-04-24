# Numpy practice day 1
# Topic : Array Indexing 

import numpy as np

prices = np.array([150, 200, 250, 300, 350])

image_pixels = np.array([
    [10,  20,  30,  40],
    [50,  60,  70,  80],
    [90,  100, 110, 120],
    [130, 140, 150, 160]
])

print("third price:",prices[2])
print("first three prices:",prices[0:3])
print("last two price:",prices[-2:])
print("extracting 70:",image_pixels[1,2])
print("extracting third row:",image_pixels[2])
print("extracting 2*2 square:",image_pixels[:2,:2])

