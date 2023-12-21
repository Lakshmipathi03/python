valu= int(input('enter your marks'))
if valu>=90 and valu<100:
    print('your grade is A+')
elif valu>=80 and valu<90:
    print('your grade is A')
elif valu>=70 and valu<80:
    print('your grade is B') 
elif valu>=60 and valu<70:
    print('your grade is c')
elif valu>=35 and valu<60:
    print('you are pass')
elif valu<35:
    print('fail')
else:
    print('invalid marks')
