# Write a program to find out whether a given post is talking about "John" or not

post=input("Enter the post: ")

if("john" in post.lower()):
    print("This post is talking about John")
else:
    print("Another post")