#Store the multiplication table generated in problem 3 in a file named table.
n=int(input("Enter the number for the table: "))

table=[n*i for i in range(1,11) ]
with open("table.txt","w") as f:
    f.write(str(table) + '\n')


