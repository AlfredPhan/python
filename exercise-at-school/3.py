#program to find the biggest of three numbers such as a=56 b=63 c =42
a = float(input("Enter number a: "))
b = float(input("Enter number b: "))
c = float(input("Enter number c: "))
if a > b and a > c:
    print("The biggest number is: ",a)
elif b > a and b > c:
    print("The biggest number is: ",b)
else:
    print("The biggest number is: ",c)
