# waf to find the factorial of n.( n is the para)
def factorial(n):
    fact = 1
    for i in range (1,n+1):
        fact*=i
    return fact
print( factorial(8))
