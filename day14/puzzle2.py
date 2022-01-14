"""
NOTE:
    The implementation done is very inefficient. It should be improved.
    Start by counting the elements each time they are added to the string defining the polymer.

Description:
    The submarine manual contains instructions for finding the optimal polymer formula; specifically, it offers a
    polymer template and a list of pair insertion rules (your puzzle input).

    For example:
        The first line is the polymer template - this is the starting point of the process.

        Starting with the polymer template NNCB, the first step simultaneously considers all three pairs:

        The first pair (NN) matches the rule NN -> C, so element C is inserted between the first N and the second N.
        The second pair (NC) matches the rule NC -> B, so element B is inserted between the N and the C.
        The third pair (CB) matches the rule CB -> H, so element H is inserted between the C and the B.

            NNCB

            CH -> B
            HH -> N
            CB -> H
            NH -> C
            HB -> C
            HC -> B
            HN -> C
            NN -> C
            BH -> H
            NC -> B
            NB -> B
            BN -> B
            BB -> N
            BC -> B
            CC -> N
            CN -> C

        Template:     NNCB
        After step 1: NCNBCHB
        After step 2: NBCCNBBBCBHCB
        After step 3: NBBBCNCCNBBNBNBBCHBHHBCHB
        After step 4: NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB
Goal:
    After step 5, it has length 97; After step 10, it has length 3073. After step 10, B occurs 1749 times, C occurs
    298 times, H occurs 161 times, and N occurs 865 times; taking the quantity of the most common element (B, 1749) and
    subtracting the quantity of the least common element (H, 161) produces 1749 - 161 = 1588

    What do you get if you take the quantity of the most common element and subtract the quantity of the
    least common element?

"""
import collections

import numpy as np
import pandas as pd
import collections

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

num_steps = 10

# ==== #
# Main #
# ==== #

if __name__ == '__main__':

    # =============== #
    # Read input data #
    # =============== #

    # The firs line contains the polymer
    template = file.readline().strip()

    # Store each of the pair instructions rules in a dictionary
    rules = {}

    line = file.readline()  # Empty line
    line = file.readline()
    while line != "\n":
        pair, insert = line.strip().split("->")
        rules[pair.strip()] = insert.strip()

        line = file.readline()

    # Close the file
    file.close()

    # ========================= #
    # Compute resulting polymer #
    # ========================= #
    polymer = template

    for _ in range(num_steps):
        new_polymer = polymer[0]
        for i in range(0, len(polymer)-1):
            # Get the pair
            pair = polymer[i] + polymer[i+1]
            # Get the insertion
            insertion = rules[pair]
            # Insert
            new_polymer += insertion + polymer[i+1]

        polymer = new_polymer

    # ===================================== #
    # Get both most and less common element #
    # ===================================== #
    counter = {}
    for char in polymer:
        if char in counter:
            counter[char] += 1
        else:
            counter[char] = 1

    most_common_element = max(counter, key=counter.get)
    less_common_element = min(counter, key=counter.get)

    # ================ #
    # Print the result #
    # ================ #

    print("Result: {}".format(counter[most_common_element] - counter[less_common_element]))

    aux = 1

    


