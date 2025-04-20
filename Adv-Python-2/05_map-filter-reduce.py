from functools import reduce
#Map example

li=[1,3,5,7,9,11,2]

square = lambda x:x*x
sqList=map(square,li)
print(list(sqList))

#filter example

def even(n):
    if(n%2==0):
        return True
    return False

onlyEven=filter(even,li)
print(list(onlyEven))

#reduce example
def sum(a,b):
    return a+b

mul=lambda x,y:x*y

print(reduce(sum,li))
print(reduce(mul,li))