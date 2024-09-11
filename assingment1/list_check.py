# write a program to find whether the element exists in the list

# Function to check if an element exists in the list
def element_exists(lst, element):
    return element in lst
list1 = []
num=int(input("enter the number:"))
for i in range(1,num+1):
    list1.append(i)
print(list1)
element = int(input("Enter the element to check: "))
if element_exists(my_list, element):
    print(f"{element} exists in the list.")
else:
    print(f"{element} does not exist in the list.")
