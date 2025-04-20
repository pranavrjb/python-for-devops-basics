#Write a program to input name,marks,and phone number of a student and format it using the format function like below:
# "The name of the student is John, his marks are 72 and phone umber is 988989898"

name=input("Enter the name: ")
marks=int(input("Enter the marks: "))
phone=int(input("Enter the phone-number: "))

a="The name of the student is {},his makrs are {} and phone number is {}".format(name,marks,phone)
print(a)
