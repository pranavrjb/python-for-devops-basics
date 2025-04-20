with open("this.txt")as f:
    f1=f.read()
with open("this_copy.txt")as f:
    f2=f.read()

if(f1==f2):
    print("Yes")
else:
    print("No")
    
    