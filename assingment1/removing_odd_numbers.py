# write a program to remove the odd numbersin the list

# Function to remove all odd numbers from the list
def remove_odd_numbers(lst):
    
    return [num for num in lst if num % 2 == 0]

my_list = []
num1=int(input("enter the number to form a list:"))
for i in range(1,num1+1):
    my_list.append(i)
print(my_list)
filtered_list = remove_odd_numbers(my_list)
print(f"List after removing odd numbers: {filtered_list}")
