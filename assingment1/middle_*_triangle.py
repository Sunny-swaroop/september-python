# write a program to print the pyramid pattern using python

# pyramid pattern
rows = 5

# Outer loop for the number of rows
for i in range(1, rows + 1):
    print(" " * (rows - i), end="")
    # Printing stars
    print("*" * (2 * i - 1))
