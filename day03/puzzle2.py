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
inputs = read_file_as_data_frame("./input.txt")
inputs.columns = ["Bits"]

# Create the number of columns
num_bits_per_sample = len(inputs['Bits'].iloc[0])

# Create an empty datafrmae
clomuns_names_inputs_split = ["Bit_" + str(bit_num) for bit_num in range(num_bits_per_sample)]
inputs_split = pd.DataFrame(columns=clomuns_names_inputs_split)

# Split the sequences of bits by columns,
# iterate each bit's position,
for idx_row in range(inputs.shape[0]):
    
    # Initialize the split row
    row = {}
    
    # split and fill the data,
    for idx_bit in range(num_bits_per_sample):
        
        row["Bit_" + str(idx_bit)] = int(inputs['Bits'].loc[idx_row][idx_bit])

    inputs_split = inputs_split.append(row, ignore_index=True)

    
# Determine the oxygen generator rating
inputs_to_check_oxygen = inputs_split.copy()
for idx_bit in range(num_bits_per_sample):
    name_column = "Bit_" + str(idx_bit)
    sum_values_bits_column = inputs_to_check_oxygen[name_column].sum()
    print("From column {}, {} samples and {} ONES (half: {})".format(name_column, 
                                                                     inputs_to_check_oxygen.shape[0],
                                                                     sum_values_bits_column, 
                                                                     inputs_to_check_oxygen.shape[0]/2))
    
    # Check required samples
    if sum_values_bits_column >= inputs_to_check_oxygen.shape[0]/2:
        print("From column {} keep {}".format(name_column, 1))
        inputs_to_check_oxygen = inputs_to_check_oxygen.loc[inputs_split[name_column] == 1]
    else:
        print("From column {} keep {}".format(name_column, 0))
        inputs_to_check_oxygen = inputs_to_check_oxygen.loc[inputs_split[name_column] == 0]
    
    # Check if another round is requiered
    if inputs_to_check_oxygen.shape[0] == 1:
        break
    

print("---------------------")
# Determine the CO2 generator rating
inputs_to_check_co2 = inputs_split.copy()
for idx_bit in range(num_bits_per_sample):
    name_column = "Bit_" + str(idx_bit)
    sum_values_bits_column = inputs_to_check_co2[name_column].sum()
    print("From column {}, {} samples and {} ONES (half: {})".format(name_column, 
                                                                    inputs_to_check_co2.shape[0],
                                                                    sum_values_bits_column,
                                                                    inputs_to_check_co2.shape[0]/2))
    
    if sum_values_bits_column < inputs_to_check_co2.shape[0]/2:
        print("From column {} keep {}".format(name_column, 1))
        inputs_to_check_co2 = inputs_to_check_co2.loc[inputs_split[name_column] == 1]
    else:
        print("From column {} keep {}".format(name_column, 0))
        inputs_to_check_co2 = inputs_to_check_co2.loc[inputs_split[name_column] == 0]
    
    # Check if another round is requiered
    if inputs_to_check_co2.shape[0] == 1:
        break

print("---------------------")
# Convert binary number into decimals
index_remaining_samples_oxigen = inputs_to_check_oxygen.index.values[0]
sample_oxygen = inputs.loc[index_remaining_samples_oxigen].values[0]
oxygen_decimal = int(sample_oxygen, 2)
print("Oxigen value: {}".format(oxygen_decimal))

index_remaining_samples_co2 = inputs_to_check_co2.index.values[0]
sample_co2 = inputs.loc[index_remaining_samples_co2].values[0]
co2_decimal = int(sample_co2, 2)
print("Oxigen value: {}".format(co2_decimal))
    

# Close the file
file.close()

print("---------------------")
# Print the result
print("Result: {}".format(oxygen_decimal * co2_decimal))
    

    


