#Program - 4 Type Casting
"""
Conversion of one data type into another another primitive data type
in python is called as Type Casting
"""

x = int(1.5)
y= float(3)
z = str("5690")

print(x)
print(y)
print(z)

name = input("What is your name? ")
age = input("What is your age? ")
numericalage = int(age)
year = 2023
year_of_birth = year - numericalage
print("Hello " + age + " year old " + name)
print("You were born in " + str(year_of_birth))

print()
input("Press return to continue ...")

