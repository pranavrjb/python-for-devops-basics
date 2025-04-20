# Can we have a set with 18(int) and "18"(str) as a values in it? 
#Yes, the reason behind it is that, both value are different as one is string and another is integer

s=set()
s.add(18)
s.add("18")
print(s,type(s))