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

    Low points are 2, 1, 6, and 6.

    ============================================================

    Next, you need to find the largest basins so you know what areas are most important to avoid.

    A basin is all locations that eventually flow downward to a single low point.
    Therefore, every low point has a basin, although some basins are very small.
    Locations of height 9 do not count as being in any basin, and all other locations will always be part of
    exactly one basin.

    The size of a basin is the number of locations within the basin, including the low point.
    The example above has four basins.

    The top-left basin, size 3:
        2199943210
        3987894921
        9856789892
        8767896789
        9899965678

    The top-right basin, size 9:
        2199943210
        3987894921
        9856789892
        8767896789
        9899965678

Goal:
    Find the three largest basins and multiply their sizes together. In the above example, this is 9 * 14 * 9 = 1134.
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

    # ========================================== #
    # TODO: Comment when no debugging the code
    # input_sequences = np.array([[2, 1, 9, 9, 9, 4, 3, 2, 1, 0],
    #                             [3, 9, 8, 7, 8, 9, 4, 9, 2, 1],
    #                             [9, 8, 5, 6, 7, 8, 9, 8, 9, 2],
    #                             [8, 7, 6, 7, 8, 9, 6, 7, 8, 9],
    #                             [9, 8, 9, 9, 9, 6, 5, 6, 7, 8]])
    # ========================================== #

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
    basins = []

    # Initialize a set() to store the locations already seen
    seen = set()

    # Iterate from row 1 to row -1, and column 1 and column -1 due to the applied padding
    for row in range(1, input_sequences.shape[0]-1):
        for col in range(1, input_sequences.shape[1]-1):

            # Extract the sub-array we want to evaluate
            sub_array = input_sequences[row-1:row+2, col-1:col+2]

            # Apply the mask
            elements_to_compare = sub_array[mask == 1]

            # ========================== #
            # Find the size of the basin #
            # ========================== #

            # Extract the center of the low point
            center = input_sequences[row, col]

            # Check if the center is a low point
            if all(center < elements_to_compare):

                # A new basin has been found
                size = 0

                # Create a Queue to store the locations that must be checked
                locations_to_check = []
                # Add to the queue the centre
                locations_to_check.append((row, col))

                # Look surrounding location from positions in locations_to_check
                while locations_to_check:
                    # Pop a center to be checked
                    r, c = locations_to_check.pop()

                    # Check if it has been already seen
                    if (r, c) in seen:
                        continue

                    # Store the location we are going to check
                    seen.add((r, c))

                    # Increase the size of the basin
                    size += 1

                    # Extract the sub-array we want to evaluate
                    new_sub_array = input_sequences[r - 1:r + 2, c - 1:c + 2]

                    # Check the surroundings of the center,
                    #  check left
                    if input_sequences[r, c-1] < 9 and (r, c-1) not in seen:
                        locations_to_check.append((r, c-1))
                    #  check right
                    if (input_sequences[r, c+1] < 9) and (r, c+1) not in seen:
                        locations_to_check.append((r, c+1))
                    #  check up
                    if input_sequences[r-1, c] < 9 and not (r-1, c) in seen:
                        locations_to_check.append((r-1, c))
                    #  check down
                    if input_sequences[r+1, c] < 9 and not (r+1, c) in seen:
                        locations_to_check.append((r+1, c))

                # Store the size of the basin
                basins.append(size)

    # Sort all the basins found
    basins.sort()

    # ================ #
    # Print the result #
    # ================ #

    result = basins[-1]*basins[-2]*basins[-3]
    print("Result: {}".format(result))
    

    


