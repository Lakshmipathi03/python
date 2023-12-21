num1= eval(input('enter the num1:- '))
num2= eval(input('enter the num2:- '))
num3= eval(input('enter the num3:- '))
if num1>num2 and num1>num3:
    if num2>num3:
        print(num2,'is second greatest')
    else:
        print(num3,'is second graestest')
elif num2>num3:
    if num1>num3:
        print(num1,'is second greastest')
    else:
        print(num3,'is second greastest')
else:
    if num1>num2:
        print(num1,'is second greastest')
    else:
        print(num2,'is second greastest')
