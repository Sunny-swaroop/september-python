# write a program to delete an element in the list


# Function to delete an item by its value
def delete_by_value(lst, value):
    if value in lst:
        lst.remove(value)
        return True
    else:
        return False
list1 = []
num=int(input("enter the number to form a list:"))
for i in range(1,num+1):
    list1.append(i)
print(list1)
value = int(input("Enter the value to delete: "))
if delete_by_value(list1, value):
    print(f"Value {value} has been deleted.")
else:
    print(f"Value {value} not found in the list.")

print(f"List after deletion: {list1}")

