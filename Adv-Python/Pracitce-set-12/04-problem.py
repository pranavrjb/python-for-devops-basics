#Write a program to display a/b where a and b are integers. If b=0, display infinite by handling the zeroDivisionError.

a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))

if(b==0):
    raise ZeroDivisionError("infinite")
else:
    print(a/b)