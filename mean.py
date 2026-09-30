#code for calculator using def function
a=float(input("enter your number"))
b=float(input("enter your number"))
print(f"1. addition 2.subtraction 3.multiplication 3.division")
choice = int(input("choose from above option which operatiion do you want run and press the number"))
def addition (a,b):
    c=a+b
    return c
def subtraction (a,b):
    c=a-b
    return c
def multiplication(a,b):
    c=a*b
    return c
def division(a,b):
    c=a/b
    return c
if (choice==1):
    result=addition (a,b)
    print(result)
elif(choice==2):
    result=subtraction(a,b)
    print(result)
elif(choice==3):
    result=multiplication(a,b)
    print(result)
elif(choice==4):
    result=division(a,b)
    print(result)
else:
    print("invalid operation")
    