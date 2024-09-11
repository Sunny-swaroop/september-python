# Write a Python program to convert the bytes in a given string to a list of integers.

string=input("enter any name or place or anything in words:")
print(string)
bytes_array=list(string.encode())

print(f"the string converted into integers are:{bytes_array}")


