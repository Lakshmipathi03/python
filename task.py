print('welcome to book your show')
name=input('please enter your name:- ')
seats=eval(input('select no.of seats you want:- ' ))
option=int(input('select the class:- '))
match option:
    case 1:
        print('dimond class')
        amount=seats*200
    case 2:
        print('gold class')
        amount=seats*150
    case 3:
        print('silver class')
        amount=seats*100
    case _:
        print('enter numbers 1,2,3 only')
print (amount)    
print(f' hi{name} you have booked {seats} seats and total amount is {amount}')
print(f' thankyou {name} useing this book my show. engoy the movie!!')