# write a program to find the sum of the digits of a given number


number=int(input("enter the number:"))
num1=0
while number>0:
    last_digit=number%10
    num1+=last_digit
    number=number//10

print("the sum of digits of a given number is:",num1)

