#Write a program usning function to convert celsius to fahrenhit

def f_to_c(f):
    return 5*(f-32)/9

n=int(input("Enter the temperature: "))
c=f_to_c(n)
print(f"{round(c,2)}C")