import random
num=random.randint(100,1000)
while True:
    a= int(input('enter a number'))
    if a== num:
        print('congrats! you successfuly gussed the number',num)
        break
    elif a<num:
        print('enter grater number')
    elif a>num:
        print('enter lesser number')
