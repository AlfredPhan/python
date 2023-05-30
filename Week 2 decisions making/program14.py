#program No.14 for calculating area of the sphere
import math
root = int(math.sqrt(4))
print(root)
pi = 3.14
#pi = round(3.64)
#pi1 = int(3.64)
#print(pi)
#print(pi1)
r = int(input("Enter the radius of the sphere: "))
area = int(pi*r*r)
a1 = area
print("Area of the sphere is = ",area)
volume = int((4/3)*pi*r*r*r)
v1 = volume
print("Volume of the sphere is = ",volume)
if v1 <=500:
    print("Not able to fill")
elif v1 > 1000:
    print("Perfect fill")
else:
    print("Math Error ...!")
print()
input("Press return to continue ...")
