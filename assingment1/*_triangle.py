# write a program to print the lower triangle 

# Input number of rows for the triangle
rows =5
for i in range(1, rows + 1):
      # Inner loop for the stars
      for j in range(i):
          print("*", end=" ")
      print()  # Move to the next line after each row
