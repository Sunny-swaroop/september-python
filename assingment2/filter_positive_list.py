
# write a python program to filter positive elements in a list
# Function to filter positive numbers from the list
def positive_numbers(lst):
    # Use list comprehension to filter positive numbers
    return [num for num in lst if num > 0]

# Sample list
list1 = [-10,-9,0,1,10,9,8,7,20,-11,-50,100,-51]

# Filtering positive numbers
positive_numbers = positive_numbers(list1)

# Display the positive numbers
print(f"Positive numbers in the list: {positive_numbers}")



