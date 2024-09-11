def fibonacci_sequence(n):
    """Generate Fibonacci sequence up to n terms."""
    sequence = []
    a, b = 0, 1
    while a <= n:
        sequence.append(a)
        a, b = b, a + b
    return sequence

def is_fibonacci_number(x):
    """Check if a number is a Fibonacci number and return its term position."""
    if x < 0:
        return False, -1
    a, b = 0, 1
    index = 1
    while a < x:
        a, b = b, a + b
        index += 1
    if a == x:
        return True, index
    return False, -1

def main():
    # Define the number up to which we want the Fibonacci sequence
    maximum_number = int(input("Enter the maximum number for the Fibonacci sequence: "))
    fibonacci_seq = fibonacci_sequence(maximum_number)
    print("Fibonacci sequence up to", maximum_number, "is:", fibonacci_seq)
    
    # Input number to check
    number_check = int(input("Enter a number to check if it is in the Fibonacci sequence: "))
    found, term = is_fibonacci_number(number_check)
    
    if found:
        print(f"{number_check} is a Fibonacci number and it is term {term}.")
    else:
        print(f"{number_check} is not a Fibonacci number.")
if __name__ == "__main__":
 main()

