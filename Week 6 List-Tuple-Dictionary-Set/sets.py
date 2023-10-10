#Sets
#Basic Python sets
my_set = {1,2,3}
print(my_set)

#displays output in unordered form
my_set2 = {1.0, "Hello", (1,2,3)}
print(my_set2)

my_set1 = {1,2,3,4,3,2}
print(my_set1)

#Embedding list inside set
my_set = set([1,2,3,2]) #set is built in function
print(my_set)

my_set3 = {1,3}
print(my_set3)
#add an element
my_set3.add(2)
print(my_set3)
my_set3.add(0)
print(my_set3)
my_set3.update({5,6,7,8}) #updation of elements in set
print(my_set3)

my_set3.discard(5)#discard dont bother about unknown elements
print(my_set3)
my_set3.discard(4)
print(my_set3)
#my_set3.remove(4) #remove will shows error for unknown elements
my_set3.remove(8)
print(my_set3)

a = {1,2,3,4,5,6}
b = {1,3,4,7,8,9}
print(a.difference(b)) #a-b =
print("A∩B = ",a.intersection(b))
print("AUB = ",a.union(b))

my_set4 = set("apple")
print('p' in my_set4)
print('o' not in my_set4)
print('l' not in my_set4)
print('e' not in my_set4)

for spell in ('fuck you'):
    print(spell)
    #print(spell[2]) #set does not support indexing
