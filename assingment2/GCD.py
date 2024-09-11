# write a program to find the gcd of the given numbers

# finding the GCD of two positive numbers
def gcd(num1, num2):
    while num2:
        num1, num2 = num2, num1 % num2
    return num1


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

result = gcd(num1, num2)
print(f"The GCD of {num1} and {num2} is: {result}")
