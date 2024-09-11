#finding a leap year
year=int(input("Enter the year :"))
if year > 0:
    result=year%4
    if result==0:
        print(f"The {year} is an Leap year")
    else:
        print(f"The {year} is not an Leap year")
