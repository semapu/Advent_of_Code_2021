"""
NOTE:
    The common elements between steps are the pairs. Therefore, this information is what we should keep track of.
    In the first implementation, we store the polymer string which grows exponentially (BAD IDEA!!!).

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

num_steps = 40

# ==== #
# Main #
# ==== #

if __name__ == '__main__':

    # =============== #
    # Read input data #
    # =============== #

    # The first line contains the polymer
    template = file.readline().strip()
    # Get the pairs from the template
    pairs = {}
    for i in range(0, len(template)-1):
        pairs[template[i:i+2]] = 1

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

    # ============= #
    # Final polymer #
    # ============= #
    # NOTE: The final polymer (the string) is not requested. No necessary to compute it.
    #       We only take into account the characters defining this polymer

    for step in range(num_steps):
        new_pairs = {}
        char_counter = {}

        # Iterate the found pairs
        for p, n in pairs.items():

            # Get the insertion
            insertion = rules[p]

            # Compute the new pais
            #  compute first pair
            if p[0]+insertion in new_pairs:
                new_pairs[p[0]+insertion] += n
            else:
                new_pairs[p[0] + insertion] = n

            #  compute second pair
            if insertion+p[1] in new_pairs:
                new_pairs[insertion+p[1]] += n
            else:
                new_pairs[insertion+p[1]] = n

            # In the last iteration compute how many times each character appear in the string defining the polymer
            # NOTE: The last char of a new trio (pair + insertion) is equal to the first char in the following trio.
            #       However, this is not true for the last character in the polymer. Count it at the end.
            if step == num_steps-1:
                # Count the chars
                #  counting the first chars
                if p[0] in char_counter:
                    char_counter[p[0]] += n
                else:
                    char_counter[p[0]] = n
                #  counting the insertion
                if insertion in char_counter:
                    char_counter[insertion] += n
                else:
                    char_counter[insertion] = n

        pairs = new_pairs

    # Count the last char
    char_counter[template[-1]] += 1

    # ===================================== #
    # Get both most and less common element #
    # ===================================== #

    most_common_element = max(char_counter, key=char_counter.get)
    less_common_element = min(char_counter, key=char_counter.get)

    # ================ #
    # Print the result #
    # ================ #

    print("Result: {}".format(char_counter[most_common_element] - char_counter[less_common_element]))
