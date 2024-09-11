# Function to find the factors of a given number
def factors(num):
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    return factors

# Function to find multiples of each factor in the list of factors
def multiples(factors):
    for factor in factors:
        multiples = [f for f in factors if f % factor == 0]
        print(f"Multiples of {factor} in the list of factors: {multiples}")

# Input number to find factors
number = int(input("Enter a number: "))

# Find factors of the number
factors_list = factors(number)

# Display the list of factors
print(f"Factors of {number}: {factors_list}")

# Find and display multiples of each factor in the list
multiples(factors_list)


