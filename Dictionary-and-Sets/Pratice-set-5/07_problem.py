# If the nameof 2 friends are same; what will to the program in problem 6?

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

# Enter your name: ram
# Enter your lang: english
# Enter your name: ram
# Enter your lang: hindi
# Enter your name: hari
# Enter your lang: nepali
# Enter your name: shyam
# Enter your lang: french
# {'ram': 'hindi', 'hari': 'nepali', 'shyam': 'french'}

#It will display the last name only and remove others same name.

