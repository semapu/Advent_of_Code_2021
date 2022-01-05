"""
Description:
    There are 100 octopuses arranged neatly in a 10 by 10 grid. Each octopus slowly gains energy over time
    and flashes brightly for a moment when its energy is full.
    Although your lights are off, maybe you could navigate through the cave without disturbing the octopuses
    if you could predict when the flashes of light will happen.

    Each octopus has an energy level - your submarine can remotely measure the energy level of each octopus
    (your puzzle input). For example:
        5483143223
        2745854711
        5264556173
        6141336146
        6357385478
        4167524645
        2176841721
        6882881134
        4846848554
        5283751526

    The energy level of each octopus is a value between 0 and 9. Here, the top-left octopus has an energy level of 5,
    the bottom-right one has an energy level of 6, and so on.

    You can model the energy levels and flashes of light in steps. During a single step, the following occurs:

    First, the energy level of each octopus increases by 1.
    Then, any octopus with an energy level greater than 9 flashes.
        This increases the energy level of all adjacent octopuses by 1, including octopuses that are diagonally adjacent.
        If this causes an octopus to have an energy level greater than 9, it also flashes.
        This process continues as long as new octopuses keep having their energy level increased beyond 9.
        (An octopus can only flash at most once per step.)
    Finally, any octopus that flashed during this step has its energy level set to 0, as it used all of its energy to flash.

    Adjacent flashes can cause an octopus to flash on a step even if it begins that step with very little energy.
    Consider the middle octopus with 1 energy in this situation:

    Before any steps:
        11111
        19991
        19191
        19991
        11111

    After step 1:
        34543
        40004
        50005
        40004
        34543

    After step 2:
        45654
        51115
        61116
        51115
        45654

Goal:
    In the initial example, after 100 steps, there have been a total of 1656 flashes.

    How many total flashes are there after 100 steps?
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

size_grid = {
    'num_rows': 10,
    'num_columns': 10
}

num_steps = 100

mask = np.array([
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]
])

# ==== #
# Main #
# ==== #

if __name__ == '__main__':

    # Initialize the grid
    grid = []

    # Counting flashes
    num_flashes = 0

    # ========= #
    # Read data #
    # ========= #

    # Read the input file
    line = file.readline()

    while line != '\n':
        grid.append([int(digit) for digit in line.strip()])
        line = file.readline()

    # Convert the grid into an array
    grid = np.array(grid)

    # Close the file
    file.close()

    # ======= #
    # Padding #
    # ======= #

    padding_row = -1*np.ones((1, size_grid['num_columns']))
    padding_column = -1*np.ones((1, size_grid['num_rows']+2))  # +2 because we have added two rows when padding

    # Insert rows
    grid = np.insert(grid, 0, padding_row, axis=0)
    grid = np.insert(grid, grid.shape[0], padding_row, axis=0)

    # Insert columns
    grid = np.insert(grid, 0, padding_column, axis=1)
    grid = np.insert(grid, grid.shape[1], padding_column, axis=1)

    # ===== #
    # Steps #
    # ===== #

    # Set a variable to detect when all octopuses flash at the same time
    all_flashed = False

    # Initialize a counter
    steps = 0

    while not all_flashed:

        # Keep track of the octopuses that have flashed. They only flash ones per step
        octopuses_already_flashed = set()
        octopuses_required_to_flash = []

        # Apply step,
        #  increase the energy levels by 1 (expect padding)
        grid[np.where(grid != -1)[0], np.where(grid != -1)[1]] += 1

        # Store the octopuses flashing by themselves
        flashing = np.where(grid > 9)
        if len(flashing[0] > 0):
            for r, c in zip(flashing[0], flashing[1]):
                octopuses_required_to_flash.append((r, c))

        # Make all the required octopuses to flush
        while octopuses_required_to_flash:
            r, c = octopuses_required_to_flash.pop(0)

            # Restore its energy level to zero and marked as flashed
            grid[r, c] = 0
            octopuses_already_flashed.add((r, c))

            # Count the octopus as flashed
            num_flashes += 1

            # Increase the energy level of adjacent octopuses
            for rr in range(r-1, r+2):
                for cc in range(c-1, c+2):
                    if grid[rr, cc] != -1 and (rr, cc) not in octopuses_already_flashed:
                        grid[rr, cc] += 1

            # Check if more octopuses will flash due to the previous flush,
            also_flashing = np.where(grid > 9)

            # If any has to flash, store it
            if len(also_flashing[0] > 0):
                for rrr, ccc in zip(also_flashing[0], also_flashing[1]):
                    if (rrr, ccc) not in octopuses_required_to_flash:
                        # Set the octopus as required to flash,
                        #  add the new coordinates taking into account the current location of study
                        aux = r+rrr
                        aux2 = c+ccc
                        octopuses_required_to_flash.append((rrr, ccc))

        # Check if all octopuses flashed at the same time
        if np.sum(grid[1:-2, 1:-2]) == 0:
            steps += 1  # Count the last step done
            all_flashed = True
            break

        # Increase the number of steps
        steps += 1

    # ================ #
    # Print the result #
    # ================ #

    print("Result: {}".format(steps))
    

    


