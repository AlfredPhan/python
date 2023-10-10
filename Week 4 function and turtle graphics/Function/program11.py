#Program No.11 Checking the character or number
def character(value):
    letter = input(value)
    return letter

def check(ch):
    if ch >= 'a' and ch <= 'z':
        print(f"{ch} is an Alphabet")
    elif ch >= 'A' and ch <= 'Z':
        print(f"{ch} is an Alphabet")
    else:
        print("Not an Alphabet")

ch1 = character("Enter an input either number or alphabet: ")
check(ch1)
