# Can you change the self parameter inside a class to something else like(demo or blb). Try changing self to 'slf' or 'blb' and see the effects.
from random import randint
class Train:
    
    def __init__(blb,trainNo):
        blb.trainNo=trainNo
    
    def book(slf,fromm,to):
        print(f"You Train {slf.trainNo} has been booked from {fromm} to{to}")
    
    def getStatus(self):
        print(f"Your train number is {self.trainNo}")
        
    def getFare(self,fromm,to):
        print(f"The fare of ticket fromm {fromm} to {to} is {randint(1000,9900)}")
    
obj=Train(1234)
obj.book("Nepal","Delhi")
obj.getStatus()
obj.getFare("Nepal","Delhi")

#So changing the self doesnt affect the python program as we can pass any parameter name but for the great practice is it quite better to use self only