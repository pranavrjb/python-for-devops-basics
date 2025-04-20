# Write a program to fill in a letter template given below with a name and date.

letter='''Dear <|Name|>
You are selected!
<|Date|>.'''
            
print(letter.replace('<|Name|>','John').replace('<|Date|>','10th March'))
