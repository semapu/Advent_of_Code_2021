"""
Description:

    Each digit of a seven-segment display is rendered by turning on or off any of seven segments named a through g.
          0:      1:      2:      3:      4:
         aaaa    ....    aaaa    aaaa    ....
        b    c  .    c  .    c  .    c  b    c
        b    c  .    c  .    c  .    c  b    c
         ....    ....    dddd    dddd    dddd
        e    f  .    f  e    .  .    f  .    f
        e    f  .    f  e    .  .    f  .    f
         gggg    ....    gggg    gggg    ....

           5:      6:      7:      8:      9:
         aaaa    aaaa    aaaa    aaaa    aaaa
        b    .  b    .  .    c  b    c  b    c
        b    .  b    .  .    c  b    c  b    c
         dddd    dddd    ....    dddd    dddd
        .    f  e    f  .    f  e    f  .    f
        .    f  e    f  .    f  e    f  .    f
         gggg    gggg    ....    gggg    gggg

    For example, here is what you might see in a single entry in your notes:
        acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab |
        cdfeb fcadb cdfeb cdbaf

    Each entry consists of ten unique signal patterns, a | delimiter, and finally the four digit output value.

    Using this information, you should be able to work out which combination of signal wires
    corresponds to each of the ten digits.

    Because 7 is the only digit that uses three segments, dab in the above example means that to
    render a 7, signal lines d, a, and b are on.
    Because 4 is the only digit that uses four segments, eafb means that to
    render a 4, signal lines e, a, f, and b are on

Goal:

    Determine all the digits from all sequences.

    Add up all the output values.

Notes:
    The problems has been solved using common segments between different numbers, starting from those that have
    a unique number of segments.
        For instance, to identify a 5, the sequence that defines it must contain all the elements remaining when
        we "subtract" 4 and 1. Moreover:
            * 1 and 4 are uniques,
            * 5 is composed by 5 segments,
            * the other numbers with 5 segments d not share the remaining ones when 1 is subtracted to 4
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


def get_key(my_dict, val):
    """
    Return key given value.

    Args:
        my_dict: Dictionary where search val
        val: Value of interest in the dictionary

    Returns:
        Key in the dictionary that matches the argument 'val'
    """
    for key, value in my_dict.items():
        if val == value:
            return key


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

# Define how many segments are active in each number
num_segments_digits = {
    '0': 6,
    '1': 2,
    '2': 5,
    '3': 5,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 3,
    '8': 7,
    '9': 6
}

# Define the specific segments that needs to be active to create a number
#              1111
#             2    3
#             2    3
#              4444
#             5    6
#             5    6
#              7777
active_segments_per_number = {
    '0': [1, 2, 3, 5, 6, 7],
    '1': [3, 6],
    '2': [1, 3, 4, 5, 7],
    '3': [1, 3, 4, 6, 7],
    '4': [2, 3, 4, 6],
    '5': [1, 2, 4, 6, 7],
    '6': [1, 2, 4, 5, 6, 7],
    '7': [1, 3, 5],
    '8': [1, 2, 3, 4, 5, 6, 7],
    '9': [1, 2, 3, 4, 6, 7]
}

# Initialize Lists to store both all input and output sequences
input_sequences = []
output_sequences = []

# Initialize a List to store all the decoded output sequences
output_values = []

# ==== #
# Main #
# ==== #

if __name__ == '__main__':

    # =============== #
    # Read input data #
    # =============== #

    # Read first line
    line = file.readline().strip()

    # Read until line is null
    while line != '\n':
        # Slip entry/exit pattern
        split = line.split("|")
        entry = split[0].strip().split(" ")
        output = split[1].strip().split(" ")

        # Add new entry sequence
        input_sequences.append(entry)
        # Add new output sequence
        output_sequences.append(output)

        # Read next line
        line = file.readline()

    # Close the file
    file.close()

    # ========================================== #
    # Decode both the input and output sequences #
    # ========================================== #

    # ========================================== #
    # TODO: Comment when no debugging the code
    # input_sequences = [["acedgfb", "cdfbe", "gcdfa", "fbcad", "dab", "cefabd", "cdfgeb", "eafb", "cagedb", "ab"]]
    # output_sequences = [["cdfeb", "fcadb", "cdfeb", "cdbaf"]]

    # input_sequences = [["be", "cfbegad", "cbdgef", "fgaecd", "cgeb", "fdcge", "agebfd", "fecdb", "fabcd", 'edb']]
    # output_sequences = [["fdgacbe", "cefdb", "cefbgd", "gcbe"]]

    # input_sequences = [["edbfga", "begcd", "cbg", "gc", "gcadebf", "fbgde", 'acbgfd', "abcde", 'gfcbed', 'gfec']]
    # output_sequences = [["fcgedb", "cgb", 'dgebacf', "gc"]]
    # ========================================== #

    # Decode both the input and output sequences
    for input_sequence, output_sequence in zip(input_sequences, output_sequences):

        # ===================== #
        # Decode input sequence #
        # ===================== #

        # Initialize a dictionary to store decoded numbers
        decoded_numbers = {}

        # Iterate to decode the number with unique segments
        for entry in input_sequence:

            # Sort the entry sequence
            entry = "".join(sorted(entry))

            # Decoded 1
            if len(entry) == 2:
                decoded_numbers['1'] = entry
            # Decoded 4
            elif len(entry) == 4:
                decoded_numbers['4'] = entry
            # Decoded 7
            elif len(entry) == 3:
                decoded_numbers['7'] = entry
            # Decoded 8
            elif len(entry) == 7:
                decoded_numbers['8'] = entry

        # Compute some useful features for numbers with 5 segments
        # Subtract 1 to 4
        remaining_elements_4_minus_1 = decoded_numbers['4']  # Initialize remaining elements to 4
        for char in decoded_numbers['1']:
            remaining_elements_4_minus_1 = remaining_elements_4_minus_1.replace(char, "")  # Subtract 1

        # Iterate again to use the numbers with unique segments to decode numbers with 5 segments
        for entry in input_sequence:

            # Sort the entry sequence
            entry = "".join(sorted(entry))

            # Decoded {2, 3, 5}
            if len(entry) == 5:

                # Decode 3: It contains 1 with a length of 5
                if all([char in entry for char in decoded_numbers['1']]):
                    decoded_numbers['3'] = entry

                    # Compute some useful features for numbers with 6 segments
                    # Subtract 8 to 3
                    remaining_elements_8_minus_3 = decoded_numbers['8']  # Initialize remaining elements to 8
                    for char in decoded_numbers['3']:
                        remaining_elements_8_minus_3 = remaining_elements_8_minus_3.replace(char, "")

                # Decode 5: It has to contain all remaining elements of 4, if we subtract to it 1
                elif all([char in entry for char in remaining_elements_4_minus_1]):
                    decoded_numbers['5'] = entry

                # If it does not match previous statements, and it has a length equal to 5, it is 2
                else:
                    decoded_numbers['2'] = entry

        # Iterate again to use the numbers with unique segments to decode numbers with 6 segments
        for entry in input_sequence:

            # Sort the entry sequence
            entry = "".join(sorted(entry))

            # Decoded {0, 6, 9}
            if len(entry) == 6:
                # Decode 0 or 6
                if all([char in entry for char in remaining_elements_8_minus_3]):  # Entry contains segments {2, 5}
                    # Decode 0: It has to contain 8 minus 3, and {1}
                    if all([char in entry for char in decoded_numbers['1']]):
                        decoded_numbers['0'] = entry
                    # Decode 6: It has to contain {8 minus 3}, but no {1}
                    else:
                        decoded_numbers['6'] = entry
                # Decode 9: It has to contain 1, but no 8 minus 3
                if all([char in entry for char in decoded_numbers['1']]):
                    aux = entry
                    if not all([char in entry for char in remaining_elements_8_minus_3]):
                        decoded_numbers['9'] = entry

        # ====================== #
        # Decode output sequence #
        # ====================== #

        # Initialize the decoded number from the sequence
        number_sequence = ""

        # Iterate to decode the output_sequence
        for output in output_sequence:

            # Sort the output sequence
            output = "".join(sorted(output))

            # Get the key associated to the value
            number_sequence += get_key(decoded_numbers, output)

        # Convert the decoded number to integer and add it to the finial list
        output_values.append(int(number_sequence))

    # ======================= #
    # Sum all decoded numbers #
    # ======================= #
    result = np.sum(output_values)

    # ================ #
    # Print the result #
    # ================ #

    print("Result: {}".format(result))
