# Numpy practice day 7
# Topic : Array Iterating

import numpy as np

sensor_tensor = np.array([
    [[ 1.2, -0.5,  3.1], [-2.2,  1.5, -0.1], [ 0.8,  2.4, -1.9]],
    [[-0.8,  4.1, -3.3], [ 1.1, -1.4,  2.2], [-0.5, -0.9,  5.0]]
])

flat_sensor = sensor_tensor.reshape(6, 3)


for item in np.nditer(flat_sensor):
    print(item, end=" ") 
print("\n")


amplified_sensors = flat_sensor.copy() 

for item in np.nditer(amplified_sensors, op_flags=['readwrite']):
    item[...] = item * 10 

print(amplified_sensors) 


for index, value in np.ndenumerate(amplified_sensors):
    if value > 25:
        print(f"Location {index} holds the value {value}")