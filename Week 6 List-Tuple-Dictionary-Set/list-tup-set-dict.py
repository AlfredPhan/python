#Basic Python sets
my_set = {1, 2, 3}
print(my_set)

#displays output in unordered form
my_set2 = {1.0, "Hello", (1,2,3)}
print(my_set2)

my_set1 = {1, 2, 3, 4, 5, 6,7,8}
print(my_set1)

#Embedding list inside set
my_set = set([1,2,3,2]) #set is built in function
print(my_set)

my_set3 = [1,3]
print(my_set3)
#add an element
my_set3.add(2)
print(my_set3)
my_set3.add(0)
print(my_set3)
my_set3.update({5,6,7,8])
print(my_set3)

my_set3.discard(5)
print(my_set3)
my_set3.discard(4)
print(my_set3)
#my_set3.remove(4)
my_set3.remove(8)
print(my_set3)

A = {1,2,3,4,5,6}
B = {1,3,4,7,8,9}
print(A.difference(B)}


