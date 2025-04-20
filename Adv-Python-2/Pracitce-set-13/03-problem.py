#A list contains the multiplication table of 7. WAP to convert it to a vertical string of same number
n=int(input("Enter the number: "))
table=[str(n*i) for i in range(1,11)]
s='\n'.join(table)
print(s)