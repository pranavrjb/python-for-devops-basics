# Write a program to find whether a given username contains less than 10 character ot not.

username=input("Enter username: ")

if(len(username)<10):
    print("It is less than 10 character")

else:
    print("It is equal or higher than 10 character")