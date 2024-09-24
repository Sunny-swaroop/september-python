# Write a Python function that takes a list and returns a new list with distinct elements from the first list.
def distinct_list():
    list1=list(input("enter the numbers:"))
    list2=[]
    for i in list1:
        if i not in list2:
            list2.append(i)
    print(list2)
        
distinct_list()

