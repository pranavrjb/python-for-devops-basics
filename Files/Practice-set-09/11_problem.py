#WAP to rename a file to "rename_file.txt"

with open("this_copy.txt")as f:
    le=f.read()
    
with open("this_copy__.txt","w") as f:
    f.write(le)