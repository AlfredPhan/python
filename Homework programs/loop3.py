#Print the following pattern
#1
#12
#123
#1234
#12345
#123456

for i in range(1,7):
    for j in range(1,i+1):
        print(j,end="")
    print()
