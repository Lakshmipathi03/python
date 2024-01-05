seats=int(input('enter no.of seats:- '))
option=int(input('enter your class:- '))
match option:
    case 1:
        print('dimond class')
        amt=seats*200
    case 2:
        print('gold class')
        amt=seats*150
    case 3:
        print('silver class')
        amt=seats*100
    case _:
        print('invalid option')
        amt=None
print(amt)        