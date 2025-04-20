# What will be the length of following set s length:

s=set()
s.add(20)
s.add(20.0)  #here, 20 == 20.0 is true
s.add("20")

print(len(s))