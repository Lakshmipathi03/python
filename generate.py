def list_num(a):
    for i in a:
        if type(i) in [list,tuple,str,set,dict]:
            yield len(i)
        else:
            yield i    
out=list_num([1,{4,5,6},(7,8),'feg',{'a':2},9.5,12]) 
print(list(out))   