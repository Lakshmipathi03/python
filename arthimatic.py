a=int(input('enter a num1:- '))
b=int(input('enter a num2:- '))
option=int(input('enter your option:- '))
match option:
    case 1:
        print('add')
        out=a+b
    case 2:
        print('sub')
        out=a-b
    case 3:
        print('mul')
        out=a*b
    case 4:
        print('div')
        out=a/b
    case _:
        print('invalid option')
        out=None
print(out)        