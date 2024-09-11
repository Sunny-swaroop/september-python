# List to store the result
result = []

# Loop through the range 1000 to 2000 (both inclusive)
for num in range(1000, 2001):
    # Check if the number is divisible by 5 but not a multiple of 11
    if num % 5 == 0 and num % 11 != 0:
        result.append(str(num))

# Print the result as a comma-separated sequence
print(", ".join(result))
