#Write a program to find out the line number where python is present from qn 6

with open("log_file.txt")as f:
    lines=f.readlines()
    
lineno=1
for line in lines:
    if("python" in line):
        print("Yes",lineno)
        break
    lineno+=1
else:
    print("No")