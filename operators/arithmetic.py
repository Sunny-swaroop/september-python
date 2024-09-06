#arithmetic operators
#"+","-","*","/","//","%"
#example
num1=int(input("enter the first number :"))
num2=int(input("enter the second number :"))
print("choose your option :")
a=print("a.Addition")
b=print("b.Subtraction")
c=print("c.Multiplication")
d=print("d.divison")
result=input("enter your option:")
if result=='a':
    result=num1+num2
    print(f"the sum of {num1} + {num2} = {result}")
elif result=='b':
    result=num1-num2
    print(f"the subtraction of {num1} - {num2} = {result}")
elif result=='c':
    result=num1*num2
    print(f"the multiplication of {num1} * {num2} = {result}")
elif result == 'd':
    result=num1/num2
    print(f"the division of {num1} / {num2} = {result}")
else:
    print("you have choosed the invalid option")
