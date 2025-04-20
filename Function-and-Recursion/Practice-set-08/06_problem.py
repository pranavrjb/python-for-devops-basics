# Write a python function which converts inches into cms

def inches_to_cms(inch):
    return inch*2.54

n=int(input("enter the number: "))
print(f"The corresponding are {inches_to_cms(n)}")