#program No.13 Logic for leap year century years?
while True:
year = input("Enter the year: ")
print("The User given year is = ",year)
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0) and year.isdigit():
    year = int(year)
    print("The given year is a leap year")
    break
else:
    print(" Type wrong, type again")
    print("The given year is not a leap year")
print()
input("Press return to continue ...")
# != -> means not equal to 



