#Write a Python program to calculate the difference between a given number and 23. If the number is greater than 23, return twice the absolute difference. 

# Function to calculate the difference and apply the condition
def calculate_difference(num):
    difference = num - 23
    if num > 23:
        return 2 * abs(difference)
    else:
        return abs(difference)

num = float(input("Enter a number: "))
result = calculate_difference(num)
print(f"The result is: {result}")
