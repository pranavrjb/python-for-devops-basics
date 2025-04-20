#Write a recursive fuunction to calcualte the sumof first n natural numbers.

def recursive(n):
    if(n==1):
        return 1
    return recursive(n-1) +n
print(recursive(4))