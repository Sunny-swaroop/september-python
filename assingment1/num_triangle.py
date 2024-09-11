# write a program to print the number sequence in python

# Input number of rows for the pattern
rows = 5

# Outer loop for the rows
for i in range(1, rows + 1):
    # Inner loop for the numbers
    for j in range(1, i + 1):
        print(j, end=" ")
    print()  # Move to the next line after each row
