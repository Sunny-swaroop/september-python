#Given a list, write a Python program to swap first and last element of the list. 


# Function to swap the first and last element of a list
def swap_first_last(lst):
    if len(lst) < 2:
        return lst  # No need to swap if the list has less than 2 elements
    
    # Swapping the first and last element
    lst[0], lst[-1] = lst[-1], lst[0]
    
    return lst
list1 = []
num=int(input("enter the number:"))
for i in range(1,num+1):
    list1.append(i)
print(list1)
swapped_list = swap_first_last(list1)
print(f"List after swapping: {swapped_list}")




