#Create a class with a class attribute a;create an objecty from it and set a directly using object a=0. Does this change the class attriburtes


#no this doesnot change the class attributes 
class Demo:
    a=5
    
obj=Demo()
print(obj.a)
obj.a=0
print(obj.a)