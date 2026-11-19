 # search if the word "learning" exists in the file or not.
word = "learning"
with open ("practice.txt", "r") as f :
    data = f.read()
    if word in data:
        print("found")
    else:
        print("not found")
        