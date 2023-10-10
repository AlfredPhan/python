#Program 6 Remove functionusing while loop
def print_list(items, header=None):
    if header != None:
        print(header)
    for item in items:
        print(f"{item}")
    print()
fruits = ["Banana","Orange","Apple","Mango"]
print_list(fruits,"FRUITS")
fruits.append("Banana") # again! joining
print_list(fruits, "FRUITS with an extra Banana")
favourite = input("What is your favourite fruits?")
fruits.insert(0,favourite)
print_list(fruits,"FRUITS,favourite first? ")
print(f"The list contains {fruits.count('Banana')}Bananas")
while "Banana" in fruits:
    fruits.remove("Banana")
print_list(fruits, "FRUITS with no Bananas")

print(f"The list contains {fruits.count('Banana')} Bananas")

print()
input("Press return to continue ...")
