#Program No.12 Nested Loop Rectangle
rows = int(input("How many rows? "))
cols = int(input("How many columns? "))

for row in range(rows):
    output = ""
    for col in range(cols):
        output += "|"
        print("\t",output)

print()
input("Press return to continue ...")
