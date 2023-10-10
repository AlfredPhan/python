#Program No.10 String searching Built-in functions
string = "Hello World!"

if string.find("or") != -1: #-1 and 0 are same priority
    print(f"'{string}' contains 'or'")
else:
    print(f"'{string}' does not contain 'or'")

if string.startswith("He"):
    print(f"'{string}' starts with 'He'")
else:
    print(f"'{string}' does not start with 'He'")

if string.endswith("!"):
    print(f"'{string}' ends with '!'")
else:
    print(f"'{string}' does not end with 'world'")

print(f"'{string}' contains {string.count('1')} '1' characters")
print(f"'{string}' contains {string.count('or')} 'or' substrings")

print()
input("Press return to continue")
