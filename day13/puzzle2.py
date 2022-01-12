"""
Description:
    Finish folding the transparent paper according to the instructions. The manual says the code is always eight
    capital letters.

Goal:
    What code do you use to activate the infrared thermal imaging camera system?
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


# ==== #
# Main #
# ==== #

if __name__ == '__main__':
    # Store the dots
    data = set()
    # Keep track of the fold
    folds = []

    # Read data
    # start reading the coordinates
    line = file.readline()
    while line != "\n":
        if line != "\n":
            x, y = line.strip().split(",")
            data.add((int(x), int(y)))

        line = file.readline()

    # then read the folds
    line = file.readline()
    while line != "\n":
        elements = line.strip().split("=")
        axis = elements[0][-1]
        value = elements[1]

        folds.append((axis, int(value)))

        line = file.readline()

    # Close the file
    file.close()

    # Create an array to store the dots
    # get the maximum values of x and y
    max_x = np.max([x for x, _ in data])
    max_y = np.max([y for _, y in data])
    # create and picture as a string
    picture = []
    for y in range(0, max_y+1):
        row = []
        for x in range(max_x+1):
            if (x, y) in data:
                row.append("#")
            else:
                row.append(" ")
        picture.append(row)

    # Apply the first fold
    for axis, value in folds:

        # vertical fold
        if axis == "x":
            for y in range(0, max_y+1):
                for x in range(max_x+1):
                    if x > value:
                        if picture[y][x] == "#":
                            # compute horizontal distance between the folding line and the dot
                            distance_between_value_and_point = x - value
                            # the new dot must be at the same distance at the left of the folding line
                            new_x_position = value - distance_between_value_and_point
                            picture[y][new_x_position] = "#"

            # Get the new picture
            picture = [row[0:value] for row in picture]
            max_x = value-1

        # horizontal fold
        if axis == "y":
            for x in range(max_x + 1):
                for y in range(0, max_y + 1):
                    if y > value:
                        if picture[y][x] == "#":
                            # compute vertical distance between the folding line and the dot
                            distance_between_value_and_point = y - value
                            # the new dot must be at the same distance at the top of the folding line
                            new_y_position = value - distance_between_value_and_point
                            picture[new_y_position][x] = "#"

            # Get the new picture
            picture = picture[0:value]
            max_y = value-1

    # ================ #
    # Print the result #
    # ================ #
    # Print the final picture because it is easier to see
    for y in range(0, max_y + 1):
        for x in range(max_x + 1):
            if picture[y][x] == "#":
                print("#", end="")
            else:
                print(" ", end="")
        print()
