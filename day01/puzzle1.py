"""
Count the number of times a depth measurement increases from the 
previous measurement. (There is no measurement before the first measurement.)
"""

# ========= #
# Funcitons #
# ========= #

def read_file(path: str):
    
    file = open(path)
    
    return file
    

# ==== #
# Main #
# ==== #

# Open the file
file = read_file('./input.txt')

# Iterate the content looking for increment in the depth
increments = 0  # Final result. Number increases in the septh

previous_line = file.readline() # First depth in the file

while True:
    # Obtain the next line
    current_line = file.readline()
    
    # Break if no more information in the file,
    #  else, check whether increase
    if current_line=="\n":
        break
    else:
        if int(current_line) > int(previous_line):
            increments += 1
        
    # Update previous_line
    previous_line = current_line
    
file.close()

print("Result: {}".format(increments))
    

    


