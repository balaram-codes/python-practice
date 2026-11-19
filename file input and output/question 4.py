# write a function to find in which line of the word "learning" occurs first . print -1 if not found.
def check_line (word):
    line_no=1
    with open ("practice.txt", "r") as f:
        for line in f:
            if word in line:
                return line_no
            line_no += 1
    return -1

print(check_line("learning"))
print(check_line("hello"))

