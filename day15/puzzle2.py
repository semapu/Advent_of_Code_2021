"""
Description:
    The entire cave is actually five times larger in both dimensions than you thought; the area you originally scanned
    is just one tile in a 5x5 tile area that forms the full map.

        1163751742
        1381373672
        2136511328
        3694931569
        7463417111
        1319128137
        1359912421
        3125421639
        1293138521
        2311944581

    Your original map tile repeats to the right and downward; each time the tile repeats to the right or downward,
    all of its risk levels are 1 higher than the tile immediately up or left of it.

    However, risk levels above 9 wrap back around to 1. So, if your original map had some position with a risk level
    of 8, then that same position on each of the 25 total tiles would be as follows:

        8 9 1 2 3
        9 1 2 3 4
        1 2 3 4 5
        2 3 4 5 6
        3 4 5 6 7

    Each single digit above corresponds to the example position with a value of 8 on the top-left tile. Because the full
    map is actually five times larger in both dimensions, that position appears a total of 25 times, once in each
    duplicated tile, with the values shown above.

Goal:

    Equipped with the full map, you can now find a path from the top left corner to the bottom right corner with the
    lowest total risk.

Notes:
    1. The goal of this implementation is to use basic Python libraries. This makes the current implementation
    no efficient as it should be. The problem come from the priority queue we are using,
        a. Using a **heapq** the runtime should improve a lot.
"""

import numpy as np
import pandas as pd
import math
from dijkstra import dijkstra_algorith

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
file = open_file('./input_simple.txt')
#  read the entire file,
# inputs = file.read()
#  read the next line.
# line = file.readline()

# Read the entire file as a DataFrame
# inputs = read_file_as_data_frame("./input.txt")

# ========== #
# Parameters #
# ========== #

starting_node = (0, 0)
expansion_times = 5

# ======= #
# Helpers #
# ======= #


def translate_risk(risk, coord_x, coord_y, original_tile_width, original_tile_height):
    x_translation = math.floor(coord_x / original_tile_width)
    y_translation = math.floor(coord_y / original_tile_height)

    risk_translation = (risk + x_translation + y_translation - 1) % 9 + 1

    return risk_translation

# ==== #
# Main #
# ==== #


if __name__ == '__main__':

    # =============== #
    # Read input data #
    # =============== #

    # Convert input data into a list of lists.
    tile = []

    line = file.readline()
    while line != '\n':
        tile.append([int(risk) for risk in line.strip()])
        line = file.readline()

    tile_width = len(tile[0])
    grid_width = tile_width * 5
    tile_height = len(tile)
    grid_height = tile_height * 5

    grid = [[] for y in range(grid_height)]

    for y in range(grid_height):
        for x in range(grid_width):
            grid[y].append(
                translate_risk(tile[y % tile_height][x % tile_width], x, y, tile_width, tile_height))

    # Close the file
    file.close()

    # Set the end node
    end_node = (len(grid)-1, len(grid[0])-1)  # End node in the bottom right corner

    # ==================== #
    # Dijkstra's algorithm #
    # ==================== #

    visited_set = dijkstra_algorith(grid, starting_node, end_node)

    # ================ #
    # Print the result #
    # ================ #

    print("Result: {}".format(visited_set[end_node]))
    

    


