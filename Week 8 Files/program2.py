#Program No.2
#Reading the file content by using user defined function.
def read(filename):
    with open(filename) as file: #to handle exceptions
        return file.read() #recursive function
#You have to create a txt file in 'D' or 'E' directory
#Exception means Abnormal Errors or Condition

contents = read("C:\PhanMinhTri.txt")#mention your filename here
print(contents)

words = contents.split()
for word in words:
    print(word)
