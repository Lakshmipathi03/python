#add to all numbers present in given string
a = input('enter a string:- ')
out = 0
for var in a:
    if '0'<=var<='9':
        out = out+int(var)
print(out)         