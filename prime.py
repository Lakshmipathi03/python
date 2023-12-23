A=eval(input('enter a value:- '))
i=1
count=0
while i<=A:
    if A%i==0:
        count+=1
    i+=1
if count ==2:
    print('it is a prime number')
else:
    print('it is not a prime number')             

