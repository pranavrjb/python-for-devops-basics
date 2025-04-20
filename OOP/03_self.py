class Employee:
    lang="Python" #Here, language and salary are the class attrubutes
    salary=1000000
    
    def getInfo(self):
        print(f"The langauge is {self.lang}. the salary {self.salary} ")
    
obj=Employee()
obj.getInfo()
obj.name="John"  #Here, name is object or instance attributes
obj.lang="JavaScript"
obj.getInfo() 
# print(obj.name,obj.lang,obj.salary)
      
      