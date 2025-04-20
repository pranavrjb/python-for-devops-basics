#Write a class calculator capable of findinf sq, cube and sqroot of a number:

class Calculator:
    def __init__(self,n):
        self.n=n
    
    def square(self):
        print(f"{self.n*self.n}")
        
    def cube(self):
        print(f"{self.n*self.n*self.n}")
    
    def sqroot(self):
        print(f"{self.n**1/2}")
    
obj=Calculator(5)
obj.square()
obj.cube()
obj.sqroot()
