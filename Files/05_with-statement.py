f=open("myfile.txt")
print(f.read())
f.close()

#with statement

with open("file.txt") as f:
    print(f.read())
    
#we dont have to explicity close the file