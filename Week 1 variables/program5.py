# Program - 5 Using f string for displaying Run time inputs
# f -> format
name = input("What is your name? ")
age = input("What is your age? ")
numerical_age = int(age) #type casting 
year = 2023
year_of_birth = year - numerical_age
print(f"Hello {age} year old {name}") #f strings command
print(f"You were born in {year_of_birth}") # concatenation(joining)

print()
input("Press return to continue ...")
