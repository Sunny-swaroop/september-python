# Write a Python function to sum all the numbers in a list.
def sum(list1):
    result=0
    for i in list1:
        result=result+i
    print(result)
    list2=[]
    list2.append(result)
    print(list2)
list1=[]
num=int(input("enter a number to form list:"))
for l in range(1,num+1):
    list1.append(l)
print(list1)
sum(list1)
