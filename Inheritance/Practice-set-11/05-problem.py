#Write a class vector representing a vector of n dimension. Overload the + and * operatot which calculate thye sum and the dot product of them.
class Vector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    
    def __add__(self,other):
        result=Vector(self.x + other.x, self.y + other.y, self.z+other.z)
        return result
    
    def __mul__(self,other):
        result=self.x * other.x + self.y * other.y + self.z*other.z
        return result
    
    def __str__(self):
        return f"Vector({self.x},{self.y},{self.z})"
    
obj=Vector(2,3,4)
obj1=Vector(1,2,3)

print(obj+obj1)
print(obj*obj1)