#Write a program to mine a log file and find out whether it contains " python or not"

with open("log_file.txt") as f:
    content=f.read()

if("python" in content):
    print("Yes")
else:
    print("No")

