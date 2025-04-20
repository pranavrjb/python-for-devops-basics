# Snake Water Gun game using Python
# Snake vs. Water: Snake drinks the water hence wins.
# Water vs. Gun: The gun will drown in water, hence a point for water
# Gun vs. Snake: Gun will kill the snake and win.


# In situations where both players choose the same object, the result will be a draw.

import random

computer=random.choice([-1,1,0])
user = input("Enter your choice: ")
youDict={"s":1,"w":-1,"g":0}
revDict={1:"Snake",-1:"Water",0:"Gun"}
you=youDict[user]

print(f"You chose {revDict[you]}\nComputer chose {revDict[computer]}")
 
if(computer==you):
    print("It's a draw")

else:
    if(computer ==-1 and you ==1):
        print("You Win.")
    elif(computer==-1 and you ==0):
        print("You Lose")
    elif(computer==1 and you ==-1):
        print("You Lose")
    elif(computer==1 and you ==0):
        print("You Win")
    elif(computer==0 and you ==-1):
        print("You Win")
    elif(computer==0 and you ==1):
        print("You Lose")
    else:
        print("Something went wrong!")