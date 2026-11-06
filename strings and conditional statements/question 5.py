# WAP to find the greatest of 3 numbers entered by the user.
a=int(input("enter first number:"))
b=int(input("enter second number:"))
c=int(input("enter third number:"))
if a>=b and a>=c:
    print("greatest is",a)
elif b>=c:
    print("greatest is",b)
else:
    print("greatest is",c)
    