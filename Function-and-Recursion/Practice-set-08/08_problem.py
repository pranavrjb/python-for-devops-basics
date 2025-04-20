#Write a python function to the print multiplication table of a given number.

def multi(n):
    for i in range(1,11):
        print(f"{n}X{i}:{n*i}")

    
multi(3)