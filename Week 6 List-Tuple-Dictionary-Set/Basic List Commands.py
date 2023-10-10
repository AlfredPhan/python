#Basic List Commands
my_list = [] #empty list
my_list = [1,2,3,4]
print(my_list)
my_list = [1,2,3,4,"python",[34,78,90]]
print(my_list)
print(my_list[4])
print(my_list[5])
n_list = ["happy","sad","angry","c","Java"]
print(n_list[-1])
print(n_list[-5]),

#List Slicing
my_list = ['p','q','r','s','t','u','v']
print(my_list[2:5]) #Lấy các phần tử trong list từ 2 đến 5
print(my_list[2:]) #Lấy tất cả các phần tử trong list trừ 2 phần tử đầu tiên
print(my_list[-5:])
print(my_list[:-5]) # Loại bỏ 5 phần tử cuối
print(my_list[-6:-1])

my_list1 = ['p','q','r','s',['python']]
print(my_list1[2:4])
print(my_list1[4:]) # Loại trừ 4 phần tử đầu tiên
print(my_list1[:]) # Lấy tất cả các phần tử
print(my_list1[:-4]) # Loại trừ 4 phần tử phía sau
print(my_list1[-4:]) # Lấy 4 phần tử đếm từ cuối danh sách
print(my_list1[-4:-1])


#changing of list values
my_list[0] = "t"
print(my_list[0:])

#Appeding and Extending the values
my_list.append("Java") #append means join
print(my_list[:])

#concatenating and extending into large values
odd = [1,3,5]
print(odd + [9,7,5]) #[1,3,5,9,7,5]
print(["re"] * 3)
odd.insert(2,4) #first number is index and second is value
print(odd)
odd[2:2] = [5,7]
print(odd)
#For deleting the item in list
del odd[2]
print(odd)
odd.sort() #arranging in ascending order (low to high value)
print(odd)
my_list.reverse()
print(my_list)
#adding the two lists
a = [1,3]
b = [4,5]
a += b
print("The value is = ",a)
#inserting the values in the middle
vowel = ['a','e','i','u','i']
vowel.insert(3,'o')
print('List: ',vowel)
vowel.remove('i')
vowel.remove('i')
print(vowel)
index = vowel.index('u');
print(index)
vowel = list(dict.fromkeys(vowel)) #removing duplicate values
print(vowel)
consonant = ['b','d','f','f','g','g','g','123']
print(consonant)
consonant = list(dict.fromkeys(consonant))
print(consonant)

#Name of the list -> Elegant List
#Embedding the loop / branching statements in list

pow1 = [2 ** x for x in range(10)]
print(pow1)
pow2 = [2 ** x for x in range(10) if x > 5]
print(pow2)
odd = [x for x in range(20) if x % 2 != 0] # x%2 == 1
print(odd)

#usage of in operator in list
my_list = ['p','r','o','b','l','e','m']
print('p' in my_list)
print('a' in my_list)
print('c' not in my_list)

for fruit in ['apple','orange','mango']:
    print("I like ",fruit)
fruit = ['apple','stawberry','mango','mango']
print(fruit[-3])
