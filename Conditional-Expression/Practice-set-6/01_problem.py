# Write a program to find greatest of four numbers enterd by the user.

a1=int(input("Enter the number: "))
a2=int(input("Enter the number: "))
a3=int(input("Enter the number: "))
a4=int(input("Enter the number: "))

if(a1>a2 and a1>a3 and a1>a4):
    print("The greatest number is: ", a1)

elif(a2>a1 and a2>a3 and a2>a4):
    print("The greatest number is: ",a2)

elif(a3>a1 and a3>a2 and a3>a4):
    print("The gretest number is: ",a3)

else:
    print("The greatest number is: ",a4)
    
