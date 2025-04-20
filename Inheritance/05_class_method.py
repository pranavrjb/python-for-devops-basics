
class Employee:
    a=1
    @classmethod
    def show(cls): #cls defines the class attributes instead of instance attributes
        print(f"The clas attributes for a is{cls.a}")
    
e=Employee()
e.a=33
e.show()  