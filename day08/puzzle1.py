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
    Using this information, you should be able to work out which combination of signal wires corresponds
    to each of the ten digits. Then, you can decode the four digit output value.

    Because the digits 1, 4, 7, and 8 each use a unique number of segments, you should be able to tell which
    combinations of signals correspond to those digits. Counting only digits in the output values
    (the part after | on each line), in the above example, there are 26 instances of digits that use a unique
    number of segments (highlighted above).

    In the output values, how many times do digits 1, 4, 7, or 8 appear?

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

# Set names input columns
input_columns = ['Seq_' + str(i) for i in range(10)]
# Set output columns
output_columns = ['Seq_' + str(i) for i in range(4)]

input_sequences = []
output_sequences = []

# ==== #
# Main #
# ==== #

if __name__ == '__main__':

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

    # Convert list into DataFrame
    # input_sequences = pd.DataFrame(input_sequences, columns=input_columns)
    # output_sequences = pd.DataFrame(output_sequences, columns=output_columns)

    # Convert the lists into a np.array()
    input_sequences = np.array(input_sequences)
    output_sequences = np.array(output_sequences)

    # Set the length's word we want to check
    desired_num_segments = [num_segments_digits['1'], num_segments_digits['4'],
                            num_segments_digits['7'], num_segments_digits['8']]

    # Count digits with unique number of segments in the output_sequences
    count = 0
    for output_sequence in output_sequences:
        for output in output_sequence:
            if len(output) in desired_num_segments:
                count += 1

    # Print the result
    print("Result: {}".format(count))
    

    


