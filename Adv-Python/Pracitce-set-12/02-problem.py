#WAP to print third, fifth, and seventh element from a list using enumrate function.

li=[1,2,3,4,5,6,7,8,9]

for i, item in enumerate(li):
    if i==2 or i==4  or i ==6:
        print(item)