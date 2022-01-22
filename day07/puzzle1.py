"""
Description:
    You quickly make a list of the horizontal position of each crab (your puzzle input).
    Crab submarines have limited fuel, so you need to find a way to make all of their horizontal positions match while
    requiring them to spend as little fuel as possible.

Goal:
    Determine the horizontal position that the crabs can align to using the least fuel possible.
    How much fuel must they spend to align to that position?

"""

import numpy as np
import pandas as pd

# ========= #
# Functions #
# ========= #


def open_file(path: str):
    
    file = open(path)
    
    return file


def read_file_as_data_frame(path: str):
    
    inputs = pd.read_csv(path, sep="\n", skiprows=-1, dtype=str)
        
    return inputs
  

# =================== #
# Read the input data #
# =================== #

# Open the file conventionally,
file = open_file('./input.txt')
#  read the entire file,
inputs = file.read()
#  read the next line.
# line = file.readline()

# Read the entire file as a DataFrame
# inputs = read_file_as_data_frame("./input.txt")


# ========== #
# Parameters #
# ========== #


# ==== #
# Main #
# ==== #

if __name__ == '__main__':
    horizontal_positions = list(map(int, inputs.split(',')))

    # TODO: Comment following line. Usage for development
    # horizontal_positions = [16,1,2,0,4,2,7,1,2,14]

    # Convert list into array
    horizontal_positions = np.array(horizontal_positions)

    # Compute the median: middle point of a number set, in which half the numbers are above the median
    #  and half are below
    median = np.median(horizontal_positions)

    # Compute the cost of aligning them to the median,
    #  subtract the position and the median to know how many positions each one has to move,
    fuel = horizontal_positions - median
    #  compute the absolute value of those distances. It does not matter the direction,
    fuel = abs(fuel)
    #  sum all the fuel required to move to the median
    result = np.sum(fuel)

    # Close the file
    file.close()

    # ================ #
    # Print the result #
    # ================ #

    print("Result: {}".format(result))
    

    


