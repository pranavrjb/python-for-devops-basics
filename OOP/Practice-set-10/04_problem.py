#Add a staic method in problem 2 to greet the user with hello

class Calculator:
    def __init__(self,n):
        self.n=n
    
    def square(self):
        print(f"{self.n*self.n}")
        
    def cube(self):
        print(f"{self.n*self.n*self.n}")
        
    def squareroot(self):
        print(f"{self.n**1/2}")
    
    @staticmethod
    def greet():
        print("Hello")
    

obj=Calculator(4)
obj.greet()
obj.square()
obj.cube()
obj.squareroot()