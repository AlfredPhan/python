#Calculate the cube of all numbers from 1 to the given number.
num = int(input("Enter a number: "))

# Using a for loop to calculate the cubes of numbers from 1 to num
for i in range(1, num+1):
    cube = i ** 3
    print(f"{i}^3 = {cube}")
