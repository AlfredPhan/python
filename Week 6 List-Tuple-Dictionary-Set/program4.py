#Program No.4 List with functions
def print_list(items, header=None):
    if header != None:
        print(header)
    for i in items:
        print(str(i))
    print()

fruit = ["Orange","Apple","Mango"]
print_list(fruit)
print_list(fruit, "FRUITS")
print()
