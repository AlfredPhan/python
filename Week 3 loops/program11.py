#program no.11 SquareStar-for-loop
#Nested Loop (Loop within Loop)
#If outer for loop gets false, then it will jump out of program
#For every interation of outer for loop inner for loop will
#continue from the beginning value 0
size = int(input("What size square? "))
for row in range(size):
    output = ""
    for col in range(size):
        output += "*"
        print("\t", output)

print()
input("Press return to continue ...")
