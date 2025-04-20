#Write a python program to remove a given word from a list and strip it al the same time.

def remove(li,word):
    n=[]
    for item in li:
        if not(item==word):
            n.append(item.strip(word))
    return n
li=["John","Rahul","Aayush","Aakash"]

print(remove(li,"sh"))