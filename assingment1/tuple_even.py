# write a program to add only even numbers into the tuple

# Initialize an empty list to collect even numbers
even_numbers = []
for num in range(1, 21):
    if num % 2 == 0:
        even_numbers.append(num)

tuple1 = tuple(even_numbers)
print(f"Tuple with even numbers from 1 to 20:{tuple1}")
