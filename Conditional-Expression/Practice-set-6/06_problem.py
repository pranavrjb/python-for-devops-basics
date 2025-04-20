# wap to calcualte the grade of a student from his marks from the following scheme:

mark1=int(input("Enter your mark: "))
mark2=int(input("Enter your mark: "))
mark3=int(input("Enter your mark: "))

total_percentage=(mark1+mark2+mark3)/3

if(total_percentage <= 100 and total_percentage>=90):
   grade = "Ex"
elif(total_percentage <= 90 and total_percentage>=80):
    grade="A"
elif(total_percentage <= 80 and total_percentage>=70):
    grade="B"
elif(total_percentage <= 70 and total_percentage>=60):
    grade="C"
elif(total_percentage <= 60 and total_percentage>=50):
    grade="D"
else:
    grade="F"
    
print(grade)