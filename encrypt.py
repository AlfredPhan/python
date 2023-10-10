#Program for Caesar Cipher Crypt code generation
def encrypt_text(plaintext,n):
    ans = ""
    # iterate over the given text
    for i in range(len(plaintext)):
        ch = plaintext[i]

        # check if space is there then simply add space
        if ch == " ":
            ans += " "
        # check if a character is uppercase then encrypt it accordingly
        # ord() -> returns the ASCII code associated with letter
        elif (ch.isupper()):
            ans += chr((ord(ch) + n - 65) % 26 + 65) #A = 65
        # check if a character is lowercase then encrypt it accordingly

        else:
            ans += chr((ord(ch) + n - 97) % 26 +97) #a = 97
    return ans

plaintext = "PYTHON PROGRAM"
n = int(input("Enter the Shift Value: "))
print("Plain Text is : " + plaintext)
print("Shift pattern is : " + str(n))
print("Cypher Text is : " + encrypt_text(plaintext,n))
