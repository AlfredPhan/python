#Program No.13 Nested Loop for Right angled Triangle

size = int(input("What is the size of triangle? "))
for row in range(size):
    output = ""
    for col in range(row + 1):
        #print("\t")
        output += "^" #output = output + "\t" + *
    print("\t",output)

print()
input("Press return to continue ...")
