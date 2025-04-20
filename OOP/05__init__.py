
class Employee:
    langauge="Python"
    salary=120000
    
    def __init__(self,name,salary,language):#dunder method which is aumatically called
        self.name=name
        self.language=language
        self.salary=salary
        print(f"I am creating an object where {self.name},{self.salary} and {self.language} is been taken")
    
    def getInfo(self):
        print(f"This langauge is {self.langauge} and the salary is {self.salary}")
    
    @staticmethod
    def greet():
        print("Good Morning")

obj=Employee("John",12000,"Java")
obj.getInfo()
    