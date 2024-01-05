def main(a):
    out=[]
    for i in a:
        out=out+[i]
    print(out)
main(range(1,10))




#comprehension
a=[ i*i for i in range (11,21)]
print(a)



#fact
from math import factorial
def fact(a):
    if a==1:
        return 1
    return a*fact(a-1)
a=[fact(i)  for i in range(1,10)]
print(a)