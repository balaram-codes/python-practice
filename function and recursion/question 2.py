# waf to print the elements of a list in a single line ( list is the parameters).

def print_list (items):
    for item in items:
        print(item, end=" ")
    print()
print_list(["delhi", "mumbai", "chennai", "noida"])