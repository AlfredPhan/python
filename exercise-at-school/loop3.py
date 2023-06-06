#write a program to display the multiplication table of a number using loop
num = int(input("Enter the number: "))
for i in range(1,11):
    print(f"{num} x {i} = {num * i}")

print()
input("Press return to continue ...")
