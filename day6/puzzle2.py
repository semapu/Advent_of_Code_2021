"""
Description:
    Each lanternfish creates a new lanternfish once every 7 days.

    However, this process isn't necessarily synchronized between every lanternfish - one lanternfish might have 2 days
     left until it creates another lanternfish, while another might have 4.
     So, you can model each fish as a single number that represents the number of days until it creates
     a new lanternfish.

    A lanternfish that creates a new fish resets its timer to 6, not 7 (because 0 is included as a valid timer value).
    The new lanternfish starts with an internal timer of 8 and does not start counting down until the next day.

    Each day, a 0 becomes a 6 and adds a new 8 to the end of the list,
     while each other number decreases by 1 if it was present at the start of the day.

Goal:
    How many lanternfish would there be after 256 days?

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
inputs = file.read()
#  read the next line.
# line = file.readline()

# Read the entire file as a DataFrame
# inputs = read_file_as_data_frame("./input.txt")


# ========== #
# Parameters #
# ========== #

number_of_days_simulation = 256


# ==== #
# Main #
# ==== #

if __name__ == '__main__':
    # Split the inputs to know the age of each fish
    initial_state = inputs.split(',')
    # Map the states to a list of integer
    initial_state = list(map(int, initial_state))

    # TODO: Use it to test the code
    # initial_state = [3,4,3,1,2]
    # number_of_days_simulation = 80  # Result: 5934

    # Array to count how many fish are in each age,
    #  0 is included as a valid timer value
    timer_values = np.zeros(8+1)

    # Initialize the timer values, given the initial state
    for state in initial_state:
        timer_values[state] += 1

    # Simulate
    for i in range(0, number_of_days_simulation):

        # Number new fish,
        #  all fish with timer equal to zero create a new fish
        num_new_fish = timer_values[0]

        # Number fish have restarted the time,
        #  all fish that have created a new fish, restart timer to six
        num_fish_restart_timer = timer_values[0]

        # Subtract a day to all states,
        #  equivalent to move one location to the left the list
        timer_values = np.append(timer_values[1:], [0])

        # Add the number of new fish, and the restarted
        timer_values[6] += num_fish_restart_timer
        timer_values[8] += num_new_fish

    # Close the file
    file.close()

    # Print the result
    result = np.sum(timer_values)
    print("Result: {}".format(result))
