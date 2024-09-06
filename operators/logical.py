#logical operators
#"and","or","not".
a=int(input("enter a number:"))
b=int(input("enter second number:"))
c=int(input("enter the third number:"))
if a<b and a<c: #and operator and also if condition to check the statement is true or false
    print(f"{a} is smaller number")
elif b<c:
    print(f"{b} is smaller number")
else:
    print(f"{c} is smaller number")

#this is also an example for maximum number from 3 numbers
