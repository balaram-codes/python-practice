# from a file containing numbers separated by commas , print the count of even numbers.
# suppose numbers.txt contain : 1,2,3,4,5,6,7,8,9,10,12,15
count =0 

with open ("numbers.txt", "r") as f :
    data = f.read()

nums = data.split(",")
for num in nums :
        if int(num) %2 == 0:
            count += 1

print("even numbers:",count)


