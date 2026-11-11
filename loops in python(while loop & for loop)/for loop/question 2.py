# search for number x in a tuple using a loop.
nums=(1,49,16,25,36,49,64,81,100)
x=81
idx=0
for num in nums:
    if num==x:
        print("found at index",idx)
        break
    idx+=1
