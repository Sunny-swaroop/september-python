
# write a program to swap the elements at the given positions

# Function to swap elements at given positions
def swap_elements(lst, num1, num2):
    # Swap the elements at num1 and num2
    lst[num1], lst[num2] = lst[num2], lst[num1]
    return lst

list2 = []
num=int(input("enter a number:"))
for i in range(1,num+1):
    list2.append(i)
print(list2)
# Input positions to swap (1-based index for user input, convert to 0-based index)
num1 = int(input("Enter the first position to swap: ")) - 1
num2 = int(input("Enter the second position to swap: ")) - 1
swapped_list = swap_elements(list2, num1, num2)
print(f"List after swapping: {swapped_list}")

