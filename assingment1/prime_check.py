#checking prime or not
def Prime(num1):
    p=0
    for i in range(1,num1+1):
        z=num1%i
        if z==0:
            p+=1
    if p==2:
        print(f"the number {num1} is a prime number")
    else:
        print(f"the number {num1} is not a prime number")
num1=int(input("enter a number :"))
Prime(num1)


