#Write a program to find the maximum of the numbers in a list using the reduce function.
from functools import reduce
li=[2,4,5,10,15,14,17,22,25]

def max(a,b):
    if(a>b):
        return a
    return b
print(reduce(max,li))