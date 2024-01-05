a=[1,3,4,5,6,7,8,9]
def add_int(var,i=0):
    if len(a)-1==i:
        return a[i]
    return a[i]+add_int(var,i+1)    
out=add_int(a)  
print(out)