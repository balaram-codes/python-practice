# search for a number x in a tuple using a loop.
nums=(1,49,16,25,36,49,64,81,100)
x=64
idx=0
while idx<len(nums):
    if nums[idx]==x:
        print("found at index",idx)
    idx+=1
