"""
Description:
    The first section is a list of dots on the transparent paper. 0,0 represents the top-left coordinate.
    The first value, x, increases to the right. The second value, y, increases downward.
    So, the coordinate 3,0 is to the right of 0,0, and the coordinate 0,7 is below 0,0.
        ...#..#..#.
        ....#......
        ...........
        #..........
        ...#....#.#
        ...........
        ...........
        ...........
        ...........
        ...........
        .#....#.##.
        ....#......
        ......#...#
        #..........
        #.#........

    Then, there is a list of fold instructions. Each instruction indicates a line on the transparent paper and wants
    you to fold the paper up (for horizontal y=... lines) or left (for vertical x=... lines). In this example, the
    first fold instruction is fold along y=7, which designates the line formed by all of the positions
    where y is 7 (marked here with -):

        ...#..#..#.
        ....#......
        ...........
        #..........
        ...#....#.#
        ...........
        ...........
        -----------
        ...........
        ...........
        .#....#.##.
        ....#......
        ......#...#
        #..........
        #.#........

    Because this is a horizontal line, fold the bottom half up. Some of the dots might end up overlapping after the
    fold is complete, but dots will never appear exactly on a fold line. The result of doing this fold looks like this:

        #.##..#..#.
        #...#......
        ......#...#
        #...#......
        .#.#..#.###
        ...........
        ...........

        Now, only 17 dots are visible.

    Notice that some dots can end up overlapping; in this case, the dots merge together and become a single dot.
Goal:
    After the first fold in the example above, 17 dots are visible.

    How many dots are visible after completing just the first fold instruction on your transparent paper?

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

        if axis == "x":
            for y in range(0, max_y+1):
                for x in range(max_x+1):
                    if x > value:
                        if picture[y][x] == "#":
                            distance_between_value_and_point = x - value
                            new_x_position = value - distance_between_value_and_point
                            picture[y][new_x_position] = "#"

            # Get the new picture
            picture = [row[0:value] for row in picture]

        if axis == "y":
            for x in range(max_x + 1):
                for y in range(0, max_y + 1):
                    if y > value:
                        if picture[y][x] == "#":
                            distance_between_value_and_point = y - value
                            new_y_position = value - distance_between_value_and_point
                            picture[new_y_position][x] = "#"

            # Get the new picture
            picture = picture[0:value]

        # break at the end of the first loop to only apply the first fold
        break

    # ================ #
    # Print the result #
    # ================ #
    locations_with_dots = np.where(np.array(picture) == "#")

    print("Result: {}".format(len(locations_with_dots[0])))