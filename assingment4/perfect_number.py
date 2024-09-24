#Write a Python function to check whether a number is "Perfect" or not. 
#According to Wikipedia :
#In number theory, a perfect number is a positive integer that is equal to the sum of its proper positive divisors,
#that is, the sum of its positive divisors excluding the number itself (also known as its aliquot sum).
#Equivalently, a perfect number is a number that is half the sum of all of its positive divisors (including itself).

def perfect(n):
    if n <= 1:
        return False
    sum_of_divisors = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            sum_of_divisors += i
    
    # Check if the sum of divisors equals the number
    return sum_of_divisors == n
number = int(input("enter a number :"))
if perfect(number):
    print(f"{number} is a perfect number.")
else:
    print(f"{number} is not a perfect number.")
