# Write a program to create a dictionart of nepali words with values as their english translation. Provide user with a option to look it up!

words={
    "Namasthe":"Hello/Hi",
    "pani":"Water",
    "Ghar":"House"
}

word=input("Enter the word you want meaning of: ")

print(words[word])

#it will throw error if the word is not available in the dictionary