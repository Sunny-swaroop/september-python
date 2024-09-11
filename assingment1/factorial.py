#factorial of a number
def Factorial(num):
    i=1
    result=1
    while i<=num:
        result=result*i
        i+=1
    return (result)
num=int(input("enter a number:"))
factorial=Factorial(num)
print(f"the factorial of {num} = {factorial}")

