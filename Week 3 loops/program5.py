#Program No.5 cumculative counting of starts using for loop
starts = int(input("How many starts? "))
output = ""
for counter in range(starts):
    #output += "*"        #horizontal display
    output += "\n*"       #vertical display  
print(output)
