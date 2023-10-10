#Program No.1 Opening and reading the files 

file = open("C:\PhanMinhTri.txt") # give your file name
contents = file.read()

print(contents)

words = contents.split()
for word in words:
    print(word)
