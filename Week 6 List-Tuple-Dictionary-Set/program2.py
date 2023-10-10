#Program No.2 Appending and finding the length of fruits
fruit = []
fruit.append("Banana")
fruit.append("Apple")
fruit.append("Orange")
fruit.append("Mango")
length = len(fruit)
print(length)

for i in range(length): #len function will count the values
    print(fruit[i])

print()
input("Press return to continue ...")
