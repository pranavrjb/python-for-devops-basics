#if-else statement and elif

a = int(input("Enter your age: "))

#if statement no. 1

if(a%2==0):
    print("a is even") 
#end of statment no. 1    

#if statement no.2
if(a >=18):
    print("You are above the age of consent")
    print("Wow, that good for you.")

elif(a<0):
    print("YOu ar entering an invalid age.")

elif(a==0):
    print("You are entering 0 which is not a valid age.")
    
else:
    print("You are below the age of consent")
#end of statement no.2
print('end of program')