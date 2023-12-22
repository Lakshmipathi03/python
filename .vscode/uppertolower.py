user=input('enter a string:- ')
out=''
for char in user:
    if char.islower():
        out+=char.upper()
    elif char.isupper():
        out+=char.lower()
    else:
        out+=char
print('out')




    