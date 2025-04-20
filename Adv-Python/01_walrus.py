
#using walrus operator
if(n:=len([1,2,4,3,5]))>3:
    print(f"List is too long({n} elements, exprected <=3)")