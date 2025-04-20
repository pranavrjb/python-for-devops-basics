#Create a class programmer for storing information of few programmers working at microsoft.

class Programmer:
    company="Microsoft"
    
    
    def __init__(self,name,salary,pin):
        self.name=name
        self.salary=salary
        self.pin=pin
        print(f"{self.name},{self.salary},{self.pin},{self.company}")
        
Programmer("John",1200000,245234)
Programmer("Alicer",124000,234434)
