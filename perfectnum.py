a=eval(input('enter a num:- '))
out=0
for i in range(1,a):
    if a%i==0:
        out=out+i
    if out==a:
        print('perfect num')
    else:
        print('not perfect num')
                
