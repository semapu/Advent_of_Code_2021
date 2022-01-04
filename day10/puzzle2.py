"""
Description:

    The navigation subsystem syntax is made of several lines containing chunks.
    There are one or more chunks on each line, and chunks contain zero or more other chunks.
    Adjacent chunks are not separated by any delimiter; if one chunk stops, the next chunk (if any) can immediately start.
    Every chunk must open and close with one of four legal pairs of matching characters:

        If a chunk opens with (, it must close with ).
        If a chunk opens with [, it must close with ].
        If a chunk opens with {, it must close with }.
        If a chunk opens with <, it must close with >.

    So, () is a legal chunk that contains no other chunks, as is [].
    More complex but valid chunks include ([]), {()()()}, <([{}])>, [<>({}){}[([])<>]], and even (((((((((()))))))))).

    Examples of corrupted chunks include (], {()()()>, (((()))}, and <([]){()}[{}]).
    Such a chunk can appear anywhere within a line, and its presence causes the whole line to be considered corrupted.

    To calculate the syntax error score for a line, take the first illegal character on the line and look it up
    in the following table:
        ): 3 points.
        ]: 57 points.
        }: 1197 points.
        >: 25137 points.

Goal:

    [({(<(())[]>[[{[]{<()<>>
    [(()[<>])]({[<{<<[]>>(
    {([(<{}[<>[]}>{[]{[(<()>
    (((({<>}<{<{<>}{[]{[]{}
    [[<[([]))<([[{}[[()]]]
    [{[{({}]{}}([{[{{{}}([]
    {<[[]]>}<{[{[{[]{()[[[]
    [<(<(<(<{}))><([]([]()
    <{([([[(<>()){}]>(<<{{
    <{([{{}}[<[[[<>{}]]]>[]]

    In the above example, an illegal ) was found twice (2*3 = 6 points), an illegal ] was found once (57 points),
    an illegal } was found once (1197 points), and an illegal > was found once (25137 points).
    So, the total syntax error score for this file is 6+57+1197+25137 = 26397 points!
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
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

# ==== #
# Main #
# ==== #

illegal_characters = []

if __name__ == '__main__':

    # ========================================== #
    # TODO: Comment when no debugging the code
    input_sequence = "{([(<{}[<>[]}>{[]{[(<()>\n"  # Expected ], but found } instead
    # ========================================== #

    # =============================== #
    # Identify the illegal characters #
    # =============================== #

    # Initialize a Stack to store the seen chars
    stack = []

    # Read first line
    line = file.readline()
    while line != '\n':
        for char in line.strip():
            if char in opening:
                stack.append(char)
            else:
                previous_opening = stack.pop()
                if char == opposites[previous_opening]:
                    continue
                else:
                    # Illegal character
                    illegal_characters.append(char)
                    # Break the loop
                    break

        # Read next line
        line = file.readline()

    # Close the file
    file.close()

    # ================== #
    # Total syntax error #
    # ================== #
    score = 0
    for char in illegal_characters:
        score += scores[char]

    # ================ #
    # Print the result #
    # ================ #

    print("Result: {}".format(score))
    

    


