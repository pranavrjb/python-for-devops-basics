
class Employee:
    company="Apple"
    name="Default name"
    def show(self):
        print(f"The name of the employee is {self.name} and the company is {self.company}")

class Coder:
    langauge="Python"
    def printLanguage(self):
        print(f"Out of all the langauge here is our language: {self.langauge}")

class Programmer(Employee,Coder):
    company="Microsoft"
    def showLanguage(self):
        print(f"The name is {self.company} and he is good with {self.langauge} langauge.")

obj=Employee()
obj1=Programmer()

obj1.show()
obj1.showLanguage()
obj1.printLanguage()