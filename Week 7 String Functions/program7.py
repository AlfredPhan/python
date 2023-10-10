#Program No.7 String with Loops
string = "Hello Python!"
#index   0123456789101112
print(string)
print()

#print each character on a new line
for c in string:
    print(c)
print()

#print each character separated by a space
for c in string:
    print(c,end = "   ")#H e l l o
print()
print()

#print each character unseparated effectively just print out the
for c in string:
    print(c, end="")#helloword
print()
print()
#print each character separated by a *
for c in string:
    print(c,end="*")#h*e*l*l*o*
print()
print()
#print every other character separated by a *
for c in string[::2]:
    print(c,end="*")
print()
