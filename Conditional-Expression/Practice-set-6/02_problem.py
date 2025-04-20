#Write a program to find out weather a student is pass or fail, if it requires total 40% and at least 33% in each subject to pass.Assume 3 subject and take marksd as an input from the user

sub1=int(input("Enter marks: "))
sub2=int(input("Enter marks: "))
sub3=int(input("Enter marks: "))

#check for the total %

total_percentage = (100*(sub1+sub2+sub3))/300

if (total_percentage>=40 and sub1>=33 and sub2>=33 and sub3>=33 ):
    print("The student is pass", total_percentage)

else:
    print("The student is failed",total_percentage)