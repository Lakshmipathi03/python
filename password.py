#password is consist of 8 char and atleast 1 uppercase ,lowercase,number,special charecter.
password= input('enter a pasword:- ')
validate={'upper':False,'lower':False,'number':False,'char':False,'space':False}
if len(password)>=8:
    for char in password:
        if 'A'<=char<='Z':
            validate['upper']=True
        elif'a'<=char<='z':
            validate['lower']=True
        elif '0'<=char<='9':
            validate['num']=True
        elif char !=' ':
            validate['char'] =True
        elif char ==' ':
            validate['space']=True    
    if(validate['upper']and validate['lower']and validate['char']and validate['num']and not validate['space']):
        print('password is validate')
    else:
        print('password is invalid')
else:
    print('password is invalid')
