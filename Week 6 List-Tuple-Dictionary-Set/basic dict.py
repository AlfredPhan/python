#Basic dictionary commands
#Empty Dictionary
my_dict = {}
print(my_dict)

#Dictionary with integer keys
my_dict1 = {1: 'apple',2: 'ball'}
print(my_dict1)

#Dictionary with mixed keys
my_dict2 = {'name': 'Tri',1: [2,3,4]}
print(my_dict2['name'])

#using dict()
my_dict3 = dict({1:'apple',2:'ball'})
print(my_dict3[2])

#From sequence having each item as a pair
my_dict4 = dict([(1,'apple'), (2,'ball')])
print(my_dict4)

my_dict = {'name':'Tri','age': 23}
print(my_dict['name'])
print(my_dict.get('age'))

#updating the keys value
my_dict['age'] = 24
print(my_dict)

#adding the item
my_dict['address'] = "HocMon"
print(my_dict)

#removing the item from the dictionary
squares = {1:23,2:34,3:78,4:16,5:90}
print(squares)
print(squares.popitem())
print(squares)
del squares[1] #delete a particular item
print(squares)
squares.clear() #remove all items
print(squares)
del squares #Entirely delete the dictionary

#for assigning the same value for all the items
marks = {}.fromkeys(['Math','English','Science'],100)
print(marks)
for item in marks.items():
    print(item)

squares = {1:1,3:9,5:25,7:49,9:81}
print(len(squares)) #Size of the dictionary đếm tổng số có trong chuỗi
print(sorted(squares)) #It will arrange the elements xếp theo thứ tự
print(all(squares)) 
