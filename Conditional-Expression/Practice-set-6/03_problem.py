# A spam commnet is defined as a text contaiing following keywords:
#"make a lot of money","buy now","subscribe this","click this".
#Write a program to detect these types of spams.

p1="make a lot of money"
p2="buy now"
p3="subscribe this"
p4="click this"

message=input("Enter your comment ")

if((p1 in message)or(p2 in message)or(p3 in message)or(p4 in message)):
    print("This is a spam message:")

else:
    print("This is not a spam message")