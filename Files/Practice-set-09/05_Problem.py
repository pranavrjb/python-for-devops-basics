#repeat program no 4 for a list of such words to be censored.

word=["donkey",'bad',"censored"]

with open("file.txt","r") as f:
    content=f.read()
for words in word:
    content=content.replace(words,"#" *len(word))
with open("file.txt","w") as f:
    f.write(content)