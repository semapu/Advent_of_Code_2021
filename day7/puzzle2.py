"""
Description:
    You quickly make a list of the horizontal position of each crab (your puzzle input).
    Crab submarines have limited fuel, so you need to find a way to make all of their horizontal positions match while
    requiring them to spend as little fuel as possible.

    Each change of 1 step in horizontal position costs 1 more unit of fuel than the last: the first step costs 1,
    the second step costs 2, the third step costs 3, and so on.

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
    # median = np.median(horizontal_positions)

    # Compute the mean value: arithmetic average of a set of numbers.
    #  This will ensure that, due to liner increment of cost respect steps, the total cost is spread.
    mean = np.mean(horizontal_positions)

    # Round the mean.
    mean_round = int(np.round(mean))

    # Compute the cost of aligning them.
    #  The answer have to be close to the mean. BUT IT IS NOT EXACTLY THE ROUND/CEIL/FLOOR OF THE MEAN
    possible_results = []
    for location in range(mean_round-5, mean_round+5):
        # Initialize the possible final result
        result = 0

        #  subtract the position and the VALUE (i) to know how many positions each one has to move,
        fuel = horizontal_positions - location
        #  compute the absolute value of those distances. It does not matter the direction,
        fuel = abs(fuel)
        #  sum all the fuel required to move to the median
        result = 0
        for consumption in fuel:
            cost_to_move_to_the_mean = list(range(1, int(consumption) + 1))
            result += np.sum(cost_to_move_to_the_mean)

        possible_results.append(result)

    # Close the file
    file.close()

    # ================ #
    # Print the result #
    # ================ #
    result = np.min(possible_results)
    print("Result: {}".format(result))
    

    


