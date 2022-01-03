"""
Description:
    
    It seems like the submarine can take a series of commands like forward 1, down 2, or up 3:
    
        forward X increases the horizontal position by X units.
        down X increases the depth by X units.
        up X decreases the depth by X units.
    
    Note that since you're on a submarine, down and up affect your depth, 
    and so they have the OPPOSITE result of what you might expect.
    
    Your horizontal position and depth both start at 0.
    
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

# Read the entire file
inputs = file.read() 

# Split the long sring into each instruction
instructions = np.array(
    [[line.split(" ")[0], line.split(" ")[1]] for line in inputs.split("\n") if line!=""]
    )

# Obtain indexes of each instruction
foreward_idx = np.where(instructions[:, 0] == 'forward')
down_idx = np.where(instructions[:, 0] == 'down')
up_idx = np.where(instructions[:, 0] == 'up')

# Obtain quantity each instruction
foreward_quantity = [int(quantity) for quantity in instructions[foreward_idx, 1][0]]
down_quantity = [int(quantity) for quantity in instructions[down_idx, 1][0]]
up_quantity = [int(quantity) for quantity in instructions[up_idx, 1][0]]

# Compute final results
horizontal = np.sum(foreward_quantity)
depth = np.sum(down_quantity) - np.sum(up_quantity)


# Close the file
file.close()

# Print the result
print("Result: {}".format(horizontal*depth))
    

    


