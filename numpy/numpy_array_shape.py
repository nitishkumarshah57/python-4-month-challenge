# Numpy practice day 5
# Topic : Array shape 

import numpy as np

image_batch = np.array([
    [[0.1, 0.2, 0.3, 0.4], [0.5, 0.6, 0.7, 0.8], [0.9, 1.0, 1.1, 1.2], [1.3, 1.4, 1.5, 1.6]],
    [[2.1, 2.2, 2.3, 2.4], [2.5, 2.6, 2.7, 2.8], [2.9, 3.0, 3.1, 3.2], [3.3, 3.4, 3.5, 3.6]],
    [[4.1, 4.2, 4.3, 4.4], [4.5, 4.6, 4.7, 4.8], [4.9, 5.0, 5.1, 5.2], [5.3, 5.4, 5.5, 5.6]]
])
print("image batch shape:",image_batch.shape)
second_image = image_batch[1]
print(second_image)
print("second image shape:",second_image.shape)
target_patch = second_image[2:,2:].copy().astype()
print(target_patch.shape)
target_patch[0,0] = 99
print(target_patch)
print(image_batch)