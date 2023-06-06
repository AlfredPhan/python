#program no.10
#for loop with continue statement
#break statement will forcely stop every process
#continue statement will turn again inside loop

line = int(input("How many line? "))
for counter in range(1,line+1):
    if counter == 3:
        print(counter)
        continue
    print(f"This is line {counter}")

print()
input("Press return to continue ...")
