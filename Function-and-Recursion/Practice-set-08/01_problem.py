#Write a program using function to find grestest of three number

def greatest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c
    
print(greatest(7,23,44))