import random 

diagonal_lines = ['╱', '╲']

while True:
    line = random.choice(diagonal_lines)
    # by default, everything you print, will be displayed on a new line
    # We want the lines to display on the same line, 
    # so add the end='' argument. The end argument defaults to '\n' otherwise
    print(line, end='')  

# Press Control+C to stop the program.  
# Alternatively, use a for loop that ends after a number of iterations. 