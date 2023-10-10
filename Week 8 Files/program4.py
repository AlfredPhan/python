#Program No.4 
#Exception handling program using "Try" and "except"
#abnormal condition if it occurs the exception will handle
def read(filename):
    """Return contents of text file as string."""
    with open(filename) as file:
        return file.read()
try:
    valid_words = read("C:\PhanMinhTri.txt").split()
    print("Spell checking...")
    while True:
        word = input("Enter a word (or hit return to cancel):")
        if len(word) == 0: #word = ""
            break
        if word.lower() in valid_words:
            print(f" '{word}' looks ok")
        else:
            print(f"'{word}' not in this dictionary")
    print("Spell checking ... finished")
except OSError as err:
    print(err)
    print("Stopping, unable to read dictionary file")