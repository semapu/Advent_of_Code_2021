"""
Description;
    You need to use the binary numbers in the diagnostic report to generate 
    two new binary numbers (called the gamma rate and the epsilon rate). 
    The power consumption can then be found by multiplying the gamma rate 
    by the epsilon rate.
    
    Each bit in the gamma rate can be determined by finding the most common 
    bit in the corresponding position of all numbers in the diagnostic report.
    
    The epsilon rate is calculated in a similar way; rather than use the most 
    common bit, the least common bit from each position is used.
    
Goal:
    Conpute the power rate.
    
"""

import numpy as np
import pandas as pd

# ========= #
# Funcitons #
# ========= #

def open_file(path: str):
    
    file = open(path)
    
    return file

def read_file_as_data_frame(path: str):
    
    inputs = pd.read_csv(path, sep="\n", skiprows=-1, dtype=str)
        
    return inputs

# ==== #
# Main #
# ==== #

# Open the file
file = open_file('./input.txt')

# Read the entire file
# inputs = read_file_as_data_frame("./input.txt")
inputs = file.read()

inputs = [line for line in inputs.split("\n") if line!=""]

# Results
gamma_rate = ""
epsilon_rate = ""

# Extract the most frequent bit
num_bits_per_sample = len(inputs[0])

for idx in range(num_bits_per_sample):
    
    sum_bits = 0
    
    for diagnostic in inputs:
        
        sum_bits += int(diagnostic[idx])
      
    if sum_bits > len(inputs)/2:
        gamma_rate = gamma_rate + "1"
        epsilon_rate = epsilon_rate + "0"
    else:
        gamma_rate = gamma_rate + "0"
        epsilon_rate = epsilon_rate + "1"
    

# Convert binary number into decimals
gamma_rate = int(gamma_rate, 2)
epsilon_rate = int(epsilon_rate, 2)
    

# Close the file
file.close()


power_consuption = gamma_rate * epsilon_rate

# Print the result
print("Result: {}".format(power_consuption))
    

    


