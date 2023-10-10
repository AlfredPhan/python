#Program No.5 
#Exam Question 
#Displaying the list of files name in .py extension in the current opened directory
import os #operating System
def index_and_list(dirname, root_path_length):
    filenames = os.listdir(dirname)
    for filename in filenames:
        path = dirname + "\\" + filename
        if os.path.isdir(path): #checking the valid directory in
            index_and_list(path,root_path_length)#recursive function
        elif path.endswith(".py"):
            print(path[root_path_length:])
try:
    root_path = input("Enter the full path of the root directory\n (blank for current directory,... for parent directory):")
    if root_path == "":
        root_path = os.curdir #current directory
    elif root_path == "..":
        root_path = os.pardir #parent directory
    if os.path.isdir(root_path):
        index_and_list(root_path,len(root_path) + 1)
except OSError as err:
    print(err)
    print("Stopping, can't access files.")