#Program No.6 Calculating the number of lines in each files
import os
def readlines(filename):
    """Return contents of text file as a list of lines"""
    with open(filename) as file:
        return file.readlines()
def index_and_count_lines(dirname,root_path_length):
    filenames = os.listdir(dirname)
    for filename in filenames:
        path = dirname + "\\" + filename
        if os.path.isdir(path):
            index_and_count_lines(path,root_path_length)
        elif path.endswith(".py"):
            lines = readlines(path) #recursion
            count = 0 
            for line in lines:
                if len(line.strip()) > 0:
                    count += 1 #count = count + 1
            print(f"{count:3} {path[root_path_length:]}")
try:
    root_path = os.pardir #Parent directory
    if os.path.isdir(root_path):
        index_and_count_lines(root_path, len(root_path) + 1)
except OSError as err:
    print(err)
    print("Stopping, can't access files.")