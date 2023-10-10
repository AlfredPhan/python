#Program No.3 Files speliing checker
def read(filename):
    """Return contents of text file as string."""
    with open(filename) as file:
        return file.read()
valid_words = read("C:\PhanMinhTri.txt").split()
print(valid_words)
print("Spell checking...")
while True:
    word = input("Enter a word (or hit return to cancel): ")
    if word == "":
        break
    if word.lower() in valid_words:
        print(f"'{word}' looks ok")
    else:
        print(f" '{word}' not in this dictionary")
print("Spell checking ... finished")