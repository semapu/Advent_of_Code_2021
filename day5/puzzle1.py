"""
Description:
    Each line of vents is given as a line segment in the format x1,y1 -> x2,y2
    where x1,y1 are the coordinates of one end the line segment and x2,y2 are the coordinates of the other end.
    These line segments include the points at both ends.

    For now, only consider horizontal and vertical lines: lines where either x1 = x2 or y1 = y2.
Goal:
    To avoid the most dangerous areas, you need to determine the number of points where at least two lines overlap

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
        # TODO: I do not know why it does not work
        # x = x.sort()
        # y = y.sort()

        # Add new horizontal line,
        #  check if both X coordinates are equal
        if len(set(x)) == 1:
            # check which Y coordinate is smaller,
            if y[0] < y[1]:
                ocean_flour[y[0]:y[1]+1, x[0]] += 1
            else:
                ocean_flour[y[1]:y[0]+1, x[0]] += 1

        # Add a new vertical line
        #  check if both Y coordinates are equal
        if len(set(y)) == 1:
            # check which X coordinate is smaller,
            if x[0] < x[1]:
                ocean_flour[y[0], x[0]:x[1]+1] += 1  # +1 to cover the last X coordinate
            else:
                ocean_flour[y[0], x[1]:x[0]+1] += 1  # +1 to cover the last X coordinate

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
    

    


