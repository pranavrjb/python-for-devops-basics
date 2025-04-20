#Write  program to calculate the gactorial of a given number using for loop

n=int(input("Enter the number: "))
product=1
for i in range(1,n+1):
    product = product*i
    
print(f"THe factorial of {n} is {product}")