#WAP to read the text from a given file "poems.txt" and find out wheather it contains the words twinkle

f=open("poems.txt")
content=f.read()
if("twinkle" in content):
    print("The word twinkle is present in the poem")
else:
    print("The twinkle is not present in the content")

f.close()
    
