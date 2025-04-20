#Write a program to calculate to find whether a given number is prime or not

n = int(input("Enter a number: "))

if n <= 1:
    print("Number is not a prime number")
else:
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            print("Number is not a prime number")
            break
    else:
        print("Number is prime")

# Let’s say n = 29
# → n ** 0.5 = 5.38
# → int(5.38) + 1 = 6
# → So the loop will check i = 2, 3, 4, 5

# If none of these divide 29, it's prime!