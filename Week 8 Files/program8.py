#Program No.8 CRUU -> Create Read Update Delete
import os
def read (filename):
    with open (filename) as file:
        return file.read()
def end():
    print()
    input("Press any key to continue...")
try:
    file=open("fpt.txt", "w") #Createing the file demo txt
    file.write ("Hello world!\n")
    file.write ("Hello Python..\n")
    file.close()
    print("hcmc.txt:")
    print(read("fpt.txt"))

    input("Press return to continue...")
    print()
    file = open ("hcmc.txt", "a") #a->appending the content
    file.write("Hello again!\n")
    file.write("Hello JAVA\n")
    file.write("Hello C#\n")
    file.close()
    print("hcmc.txt:")
    end()
    print("deleting hcmc.txt")
    os.remove("hcmc.txt")
except OSError as err:
    print(err)
    print("Stoping, can not access demo.txt")
end()