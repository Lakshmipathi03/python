def cal(a,b):
    for i in range(a,b+1):
        yield i**2
        yield i*2
out=cal(5,15)
print(list(out))