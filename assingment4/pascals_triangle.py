# Write a Python function that prints out the first n rows of Pascal's triangle.
def pascals_triangle(num):
    if num <= 0:
        return
    triangle = [] 
    for row in range(num):
        new = [1] * (row + 1)
        for j in range(1, row):
            new[j] = triangle[row - 1][j - 1] + triangle[row - 1][j]
        
        triangle.append(new)

        print(' '.join(map(str, new)).center(num * 2))
num=int(input("enter a number:"))        
pascals_triangle(num)
