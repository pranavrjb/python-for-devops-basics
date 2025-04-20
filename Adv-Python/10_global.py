
a=89
def fn():
    global a
    a=3
    print(a)
    
fn()
print(a)