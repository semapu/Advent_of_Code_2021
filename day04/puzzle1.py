"""
Description:
    Bingo is played on a set of boards each consisting of a 5x5 grid of numbers. 
    Numbers are chosen at random, and the chosen number is marked on all 
    boards on which it appears. (Numbers may not appear on all boards.) 
    
    If all numbers in any row or any column of a board are marked, 
    that board wins. (Diagonals don't count.)

Goal:
    The score of the winning board can now be calculated. 
    Start by finding the sum of all unmarked numbers on that board; 
    in this case, the sum is 188. Then, multiply that sum by the number that 
    was just called when the board won, 24, to get the final score, 188 * 24 = 4512.

"""

import numpy as np
import pandas as pd
import re

# ========= #
# Functions #
# ========= #


def open_file(path: str):

    file = open(path)

    return file


def read_file_as_data_frame(path: str):

    inputs = pd.read_csv(path, sep="\n", dtype=str)

    return inputs


# =================== #
# Read the input data #
# =================== #

inputs = read_file_as_data_frame("./input.txt")

# file = open_file('./input.txt')
# inputs = file.read()


# ========== #
# Parameters #
# ========== #

# Define the size of the grids
board_shape = {
    "num_rows": 5,
    "num_columns": 5,
    }

num_boards = int(inputs.shape[0] / board_shape["num_rows"])
boards = np.zeros((num_boards, board_shape["num_rows"], board_shape["num_columns"]))

numbers = inputs.columns[0].split(',')
numbers_drawn = boards.copy()

# ==== #
# Main #
# ==== #

if __name__ == '__main__':

    # Fill the matrix with the input data
    idx_board = 0  # Index to know which board we are filling
    idx_board_row = 0

    for i in range(inputs.shape[0]):
        row = inputs.iloc[i, 0].strip()
        row_split = re.split('\s+', row)

        # for j in range(board_shape['num_rows']):
        boards[idx_board, idx_board_row, :] = row_split

        idx_board_row += 1

        if idx_board_row%board_shape["num_rows"] == 0:
            idx_board += 1
            idx_board_row = 0

    # Iterate the numbers
    for n in numbers:
        n = int(n)
        first_complete_board = None

        # Search board en which appears the number
        locations = np.where(boards == n)

        # Mark locations of numbers that has appeared
        numbers_drawn[locations] = 1

        # Search complete boards
        for j in range(boards.shape[0]):
            # board = boards[j]

            # Check complete rows
            num_numbers_drawn_rows = np.sum(numbers_drawn[j], axis=0)
            if any(num_numbers_drawn_rows == 5):
                first_complete_board = j
                break

            # Check complete columns
            num_numbers_drawn_columns = np.sum(numbers_drawn[j], axis=1)
            if any(num_numbers_drawn_columns == 5):
                first_complete_board = j
                break

        if first_complete_board is not None:
            break

    # Extract the unmarked values in the final board
    final_board = boards[first_complete_board]
    unmarked_values_final_board = final_board[np.where(numbers_drawn[first_complete_board] == 0)]

    # Sum all the unmarked numbers
    sum_unmarked_values_final_board = np.sum(unmarked_values_final_board)

    # Compute de final result
    result = sum_unmarked_values_final_board * n

    print(result)
