a=sorted([2,1,3,6,5,4])
print(a)


#reverse sorted
a=sorted([1,3,4,5],reverse=True)
print(list(a))





#reduce()
from functools import reduce
a=[1,2,3,4,5]
def add (a,b):
    return a+b
out=reduce(add,a)
print(out)