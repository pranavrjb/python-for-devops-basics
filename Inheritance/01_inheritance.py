
class Employee:
    company="Apple"
    def show(self):
        print(f"The name of tyhe employee is {self.name} and the salary is {self.salary}")
        
class Programmer(Employee):
    company="Microsoft"
    def showLangauge(self):
        print(f"The name is {self.name} and he is good with {self.langauge} langauge.")

obj=Employee()
obj1=Programmer()
print(obj.company,obj1.company)