a=int(input("enter the value of a"))
b=int(input("enter the value of b"))
c=int(input("enter the value of c"))
if(a>b):
    if(a>c):
        print("a is greatest")
    else:
        print("c is the greatest")
else:
    if(b>c):
        print("b is greatest")
    else:
        print("c is greatest")
