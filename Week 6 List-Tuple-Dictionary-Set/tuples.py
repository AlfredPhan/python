#BASIC TUPLES
#Empty tuple
my_tuple = ()
print(my_tuple)

#Tuple having integers
my_tuple1 = (1,2,3)
print(my_tuple1)

#Tuple with mixed datatypes
my_tuple2 = (1,"Hello",3.4)
print(my_tuple2)

#Nested tuple
my_tuple3 = ("mouse", [8,4,6], (1,2,3))
print(my_tuple3)
print(my_tuple3[0][2]) #two dimensional array position
print(my_tuple3[2][2])

#tuple packing
tuple4 = 3,4.5,78,"python"
print(tuple4)

tuple5 = (12,45,78,90)
print(tuple5[1])
print(tuple5[0])
print(tuple5[-3])
#Tuple Slicing
print(tuple5[1:4])
print(tuple5[-4:])
print(tuple5[:])
#tuple5[2] = 66 #changing the tuple values
del tuple5 #entire tuple is deleted

#concatenating the tuple
T1 = (1,2,3)
T2 = (4,5,6)
T3 = T1 + T2
print(max(T1))
print(min(T2))

for name in ('John','Kate'):
    print("Hello",name)

