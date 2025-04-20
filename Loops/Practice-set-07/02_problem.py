# Write a program to greet all the person names stored in a list l1 and which starts with s

li=["John","Rahul","Sachin","Sammi","Sohan"]

for name in li:
    if(name.startswith("S")):
        print(f"Hello {name}")