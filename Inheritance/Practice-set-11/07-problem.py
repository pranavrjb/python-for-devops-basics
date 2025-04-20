#Override the __len__() method on Vecotr of problem 5 to display the dimension of the vector.

class Vector:
    
    def __init__(self,li):
        self.li=li
        
    # def __add__(self,other):
    #     result=Vector(self.x + other.x, self.y + other.y, self.z + other.z)
    #     return result
    
    # def __mul__(self,other):
    #     result= self.x * other.x+ self.y * other.y+ self.z * other.z  
    #     return result
    
    # def __str__(self):
    #     return f"Vector({self.x},{self.y},{self.z})"
    
    def __len__(self):
        return len(self.li)
    
a=Vector([1,4,7,9,11])
print(len(a))

