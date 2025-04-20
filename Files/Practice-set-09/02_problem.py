#the game() function in a program lets a user play a game and returns the score as an integer. You need to read a file "Hiscore.txt" which is either balcnk or contains the previous Hi-score. You need to write a progeam to upadate the Hi-score whenever game() breaks kthe Hi-score

import random

def game():
    print("You are playing a game...")
    score=random.randint(1,99)
    #fetch the hiscore.txt
    with open("hiscore.txt") as f:
        hiscore=f.read()
        if(hiscore!=""):
            hiscore=int(hiscore)
        else:
            return 0
    print(f"The score:{score}")
    if(score>hiscore):
        with open("hiscore.txt","w") as f:
            f.write(str(score))
    return score
    
    
game()