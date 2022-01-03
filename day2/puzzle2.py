"""
Description:
    
    In addition to horizontal position and depth, you'll also need to track a 
    third value, aim, which also starts at 0. The commands also mean something 
    entirely different than you first thought:

    down X increases your aim by X units.
    up X decreases your aim by X units.
    forward X does two things:
        It increases your horizontal position by X units.
        It increases your depth by your aim multiplied by X.

Goal:
    What do you get if you multiply your final horizontal position 
    by your final depth?
"""

import numpy as np

# ========= #
# Funcitons #
# ========= #

def read_file(path: str):
    
    file = open(path)
    
    return file
    

# ==== #
# Main #
# ==== #

# Open the file
file = read_file('./input.txt')

# Results
horizontal = 0
depth = 0
aim = 0

# Read the entire file
inputs = file.read() 

# Split the long string into single instructions
instructions = np.array(
    [[line.split(" ")[0], line.split(" ")[1]] for line in inputs.split("\n") if line!=""]
    )

# Compute final results
for instruction, quantity in instructions:
    # Convert quantity into a int
    quantity = int(quantity)
    
    # Performe the calculations
    if instruction == "forward":
        horizontal += quantity
        depth += quantity * aim
    elif instruction == "down":
        aim += quantity
    elif instruction == "up":
        aim -= quantity
        

# Close the file
file.close()

# Print the result
print("Result: {}".format(horizontal*depth))
    

    


