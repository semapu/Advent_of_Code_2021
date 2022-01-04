"""
Description:

    Now, discard the corrupted lines. The remaining lines are incomplete.

    Incomplete lines don't have any incorrect characters - instead, they're missing some closing characters at the end
    of the line. To repair the navigation subsystem, you just need to figure out the sequence of closing characters
    that complete all open chunks in the line.

    You can only use closing characters (), ], }, or >), and you must add them in the correct order so that only legal
    pairs are formed and all chunks end up closed.

Goal:

    Start with a total score of 0. Then, for each character, multiply the total score by 5 and then increase
    the total score by the point value given for the character in the following table:

        ): 1 point.
        ]: 2 points.
        }: 3 points.
        >: 4 points.

    Autocomplete tools are an odd bunch: the winner is found by sorting all of the scores and then taking the
    middle score. (There will always be an odd number of scores to consider.)
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

# Define the possible opening elements
opening = "({[<"
# Define the possible closing
closing = ")}]>"

opposites = {
    '(': ')',
    '{': '}',
    '[': ']',
    '<': '>'
}

scores = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}

# ==== #
# Main #
# ==== #

scores_incomplete_lines = []

if __name__ == '__main__':

    # ========================================== #
    # TODO: Comment when no debugging the code
    # line = "[({(<(())[]>[[{[]{<()<>>\n"  # Complete by adding }}]])})]  # 288957 total points
    # ========================================== #

    # ================================== #
    # Identify the incomplete characters #
    # ================================== #

    # Read first line
    line = file.readline()
    while line != '\n':
        # At the beginning each line is considered as incomplete
        valid_sequence = True

        # Initialize a Stack to store the seen chars
        stack = []

        # Analyze each character
        for char in line:

            # Check if we have analyzed the entire sequence,
            #  if it is not the end,
            if char != '\n':
                # If opening char, store it in the stack
                if char in opening:
                    stack.append(char)
                # If closing char, check if it is valid
                else:
                    previous_opening = stack.pop()
                    if char == opposites[previous_opening]:
                        continue
                    else:
                        # Illegal sequence
                        valid_sequence = False
                        break
            #  if analyzed the entire sequence.
            else:
                # Compute the closing sequence
                closing_sequence = []

                while stack:
                    char = stack.pop()
                    closing_sequence.append(opposites[char])

        # ============================= #
        # Compute score incomplete line #
        # ============================= #

        if valid_sequence:
            # Compute the closing score
            score = 0
            for char in closing_sequence:
                score = 5*score + scores[char]

            # Store the closing score
            scores_incomplete_lines.append(score)

        # Read next line
        line = file.readline()

    # Close the file
    file.close()

    # ==================== #
    # Get the middle score #
    # ==================== #
    scores_incomplete_lines.sort()
    idx = int(np.floor(len(scores_incomplete_lines)/2))

    middle_score = scores_incomplete_lines[idx]


    # ================ #
    # Print the result #
    # ================ #

    print("Result: {}".format(middle_score))
    

    


