'''
factorial(1)=1
factorial(2)=2x1
factorial(3)=3x2x1
factorial(4)=4x3x2x1
factorial(5)=5x4x3x2x1

factorial(n)= n x n-1 x......3x 2 x 1

factorial(n)=n*factorial(n-1)
'''
def fact(n):
    if(n==1 or n==0):
        return 1
    return (n*fact(n-1))

n = int(input("Enter a number: "))
print(fact(n))