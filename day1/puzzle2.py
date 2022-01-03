"""
Count the number of times the sum of measurements in this sliding window 
increases from the previous sum.

Three-measurement sliding window
"""

import numpy as np

# ========= #
# Funcitons #
# ========= #

def open_file(path: str):
    
    file = open(path)
    
    return file
    

# ==== #
# Main #
# ==== #

# Open the file
file = open_file('./input.txt')

# Iterate the content looking for increment in the depth
increments = 0  # Final result. Number increases in the septh

# Read the entire file
inputs = file.read() 

# Split the long sring and convert values to ints
lines_ints = [int(line) for line in inputs.split("\n") if line!=""]

# Groups of three values
groups = [lines_ints[i:i+3] for i in range(0, len(lines_ints), 1)]

# Sum groups until no group of three can be created
sums = [np.sum(group) for group in groups if len(group)==3]

# Check the number of increments
increments = 0

sum_previous = sums[0]
for sum_next in sums[1:]:
    if sum_next > sum_previous:
        increments += 1
    
    sum_previous = sum_next


file.close()

print("Result: {}".format(increments))
    

    


