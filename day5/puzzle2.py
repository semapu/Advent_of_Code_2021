"""
Description:
    Each line of vents is given as a line segment in the format x1,y1 -> x2,y2
    where x1,y1 are the coordinates of one end the line segment and x2,y2 are the coordinates of the other end.
    These line segments include the points at both ends.

    The lines in your list will only ever be horizontal, vertical, or a diagonal line at exactly 45 degrees.

Goal:
    To avoid the most dangerous areas, you need to determine the number of points where at least two lines overlap

Notes:
    A more efficient approach would be to NO DISTINGUISH between types of lines.
    Then, Create the corresponding range(), only checking if the X or Y values are decreasing.
        The checking is required to use range(..., step=-1) for the decreasing coordinates.
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

# Open the file
# inputs = read_file_as_data_frame("./input.txt")
file = open_file('./input.txt')

# ========== #
# Parameters #
# ========== #

# Create the ocean floor,
#  A better approach to determine the size should be found.
size_grid = {
    'rows': 1000,
    'columns': 1000
}

ocean_flour = np.zeros((size_grid['rows'], size_grid['columns']))

# ==== #
# Main #
# ==== #

if __name__ == '__main__':
    # Read the first line.
    #  NOTE: the file ends with \n
    line = file.readline()

    while line != '\n':

        # Split the input line
        input_segment = line.split("->")

        # Extract the origin coordinates
        origin = [int(coord) for coord in input_segment[0].strip().split(",")]
        # Extract the end coordinates
        end = [int(coord) for coord in input_segment[1].strip().split(",")]

        # Extract X and Y coordinates. Sort them.
        x = [origin[0], end[0]]
        y = [origin[1], end[1]]

        # Sort the coordinates.
        #  Required to be able to indicate the origin/end locations.
        x.sort()
        y.sort()

        # Add new horizontal line,
        #  check if both X coordinates are equal
        if len(set(x)) == 1:
            ocean_flour[y[0]:y[1]+1, x[0]] += 1

        # Add a new vertical line
        #  check if both Y coordinates are equal
        elif len(set(y)) == 1:
            ocean_flour[y[0], x[0]:x[1]+1] += 1  # +1 to cover the last X coordinate

        # Add diagonal line,
        #  create each specific coordinate.
        else:
            diagonal_x = list(range(x[0], x[1]+1))
            diagonal_y = list(range(y[0], y[1] + 1))

            # Check if any array must be flip.
            #  Diagonal line decreasing in one direction
            if origin[0] > end[0]:
                diagonal_x = np.flipud(diagonal_x)
            if origin[1] > end[1]:
                diagonal_y = np.flipud(diagonal_y)

            ocean_flour[diagonal_y, diagonal_x] += 1

        # Read a new line
        line = file.readline()

    # Find all coordinates where at least two lines overlap
    overlapped_coordinates = np.where(ocean_flour > 1)

    # Count the resulting coordinates:
    #  check how many X coordinates overlap
    print(len(overlapped_coordinates[0]))

    # Close the file
    file.close()

    # Print the result
    # print("Result: {}".format(result))
    

    


