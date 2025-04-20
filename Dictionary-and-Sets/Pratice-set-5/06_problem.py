# Create an empty dictionary. ALlow 4 friends to enter thier favorite langauge as values and use key as thier names. Assume that the name are unique.

d={}

name=input("Enter your name: ")
lang=input("Enter your lang: ")
d.update({name:lang})
name=input("Enter your name: ")
lang=input("Enter your lang: ")
d.update({name:lang})
name=input("Enter your name: ")
lang=input("Enter your lang: ")
d.update({name:lang})
name=input("Enter your name: ")
lang=input("Enter your lang: ")
d.update({name:lang})
print(d)