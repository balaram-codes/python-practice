# check if a list is a palindrome .use copy() methods
nums =[1,2,3,4,5,4,3,2,1]
x = nums.copy()
x.reverse()
if nums ==x:
    print("list is palindrome")
else :
    print("list is not palindrome")
