

class Employee:
    lang="Python" #Here, language and salary are the class attrubutes
    salary=1000000
    
obj=Employee()
obj.name="John"#Here, name is object or instance attributes 
obj.lang="JavaScript" #Here, it gives priority to the instance attributes over the class attributes
print(obj.name,obj.lang,obj.salary)
      
      