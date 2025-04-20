a=int(input("Enter a number: "))
b=int(input("Enter the 2nd number: "))

if(b==0):
    raise ZeroDivisionError("Jery our program is not meant to divide number by zero")
else:
    print(f"The division a/b is {a/b}")