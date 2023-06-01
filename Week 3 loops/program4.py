#Program No.4 Counting in while loop
numstarts = int(input("How many starts? "))
counter = 0
output = ""
while counter < numstarts:
    output += "*"
    print(output,end ="\n")
    counter += 1
print(output)
