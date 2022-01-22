"""
Description:
    If you can model how the smoke flows through the caves, you might be able to avoid it and be that much safer.
    The submarine generates a heightmap of the floor of the nearby caves for you (your puzzle input).

    Each number corresponds to the height of a particular location, where 9 is the highest and 0 is the lowest a
    location can be.

        2199943210
        3987894921
        9856789892
        8767896789
        9899965678

Goal:
    Your first goal is to find the low points - the locations that are lower than any of its adjacent locations.
    Most locations have four adjacent locations (up, down, left, and right); locations on the edge or corner of the map
    have three or two adjacent locations, respectively. (Diagonal locations do not count as adjacent.)

    The risk level of a low point is 1 plus its height. In the above example, the risk levels of the low points
    are 2, 1, 6, and 6. The sum of the risk levels of all low points in the heightmap is therefore 15.

    Find all the low points on your heightmap.
    What is the sum of the risk levels of all low points on your heightmap?
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
# inputs = file.read()
#  read the next line.
# line = file.readline()

# Read the entire file as a DataFrame
# inputs = read_file_as_data_frame("./input.txt")


# ========== #
# Parameters #
# ========== #

mask = np.array([
    [0, 1, 0],
    [1, 0, 1],
    [0, 1, 0]
])

# ==== #
# Main #
# ==== #

if __name__ == '__main__':

    # ========================================== #
    # TODO: Comment when no debugging the code
    # input_sequences = np.array([[2, 1, 9, 9, 9, 4, 3, 2, 1, 0],
    #                             [3, 9, 8, 7, 8, 9, 4, 9, 2, 1],
    #                             [9, 8, 5, 6, 7, 8, 9, 8, 9, 2],
    #                             [8, 7, 6, 7, 8, 9, 6, 7, 8, 9],
    #                             [9, 8, 9, 9, 9, 6, 5, 6, 7, 8]])
    # ========================================== #

    # =============================== #
    # Load and process the input file #
    # =============================== #

    # Initialize storage
    input_sequences = []

    # Read information in the input file
    line = file.readline()
    while line != '\n':
        # Strip the line to remove \n at the end, convert each digit into an integer
        line = [int(num) for num in line.strip()]

        input_sequences.append(line)

        line = file.readline()

    # Convert the storage into an array
    input_sequences = np.array(input_sequences)

    # Close the file
    file.close()

    # ================================ #
    # Padding with 10 the input matrix #
    # ================================ #

    padding_row = 10*np.ones((1, input_sequences.shape[1]))
    padding_column = 10*np.ones((1, input_sequences.shape[0]+2))  # +2 because we have added two rows when padding

    # Insert rows
    input_sequences = np.insert(input_sequences, 0, padding_row, axis=0)
    input_sequences = np.insert(input_sequences, input_sequences.shape[0], padding_row, axis=0)

    # Insert columns
    input_sequences = np.insert(input_sequences, 0, padding_column, axis=1)
    input_sequences = np.insert(input_sequences, input_sequences.shape[1], padding_column, axis=1)

    # ================= #
    # Search low points #
    # ================= #

    # Initialize list to store all low point
    low_points = []

    # Iterate from row 1 to row -1, and column 1 and column -1 due to the applied padding
    for row in range(1, input_sequences.shape[0]-1):
        for col in range(1, input_sequences.shape[1]-1):

            # Extract the sub-array we want to evaluate
            sub_array = input_sequences[row-1:row+2, col-1:col+2]

            # Apply the mask
            elements_to_compare = sub_array[mask == 1]

            # Check if center is the smallest
            center = input_sequences[row, col]
            if all(center < elements_to_compare):
                low_points.append(center + 1)

    # ================ #
    # Print the result #
    # ================ #

    result = np.sum(low_points)
    print("Result: {}".format(result))
    

    


