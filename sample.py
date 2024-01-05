a=10
def outer():
    def inner():
        nonlocal b
        c=10
        b=100
        print(b)
        print(c)
    print(b)    
    inner()
    print(b)    
outer()        