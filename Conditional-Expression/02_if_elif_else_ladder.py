#if-else statement and elif

a = int(input("Enter your age: "))
 
if(a >=18):
    print("You are above the age of consent")
    print("Wow, that good for you.")

elif(a<0):
    print("YOu ar entering an invalid age.")

elif(a==0):
    print("You are entering 0 which is not a valid age.")
    
else:
    print("You are below the age of consent")
    
print('end of program')