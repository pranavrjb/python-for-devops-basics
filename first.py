# import pyjokes

# print("Printing Jokes")
# joke=pyjokes.get_joke()
# print(joke)



#Pratice Set-1

# print('''Twinkle, twinkle, little star, how I wonder what you are. Up above the world so high,
# like a diamond in the sky. Twinkle, twinkle, little star, how I wonder what you are.
# When the blazing sun is set, and the grass with dew is wet. Then you show your little
# light, twinkle, twinkle all the night. Twinkle, twinkle little star, how I wonder what you
# are.
# Then the traveler in the dark thanks you for your tiny spark. How could he see where to
# go if you did not twinkle so? Twinkle, twinkle little star, how I wonder what you are.
# As your bright and tiny spark lights the traveler in the dark, though I know not what you
# are, twinkle, twinkle, little star. Twinkle, twinkle, little star, how I wonder what you are.''')

# import pyttsx3
# engine = pyttsx3.init()
# engine.say("I will speak this text")
# engine.runAndWait()

import os

# select the directory whose content you want to list
directory_path='/Web Development'

# use os module to list te directory
contents=os.listdir(directory_path)
for item in contents:
    print(item)