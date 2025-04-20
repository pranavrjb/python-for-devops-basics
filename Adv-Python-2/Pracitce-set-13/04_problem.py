#WAP to filter a list of number which are divisible by 5

li=[2,4,5,10,15,14,17,22,25]
def fn(n):
    if(n%5==0):
        return True
    return False
div=filter(fn,li)
print(list(div))
