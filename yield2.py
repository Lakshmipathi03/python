def str_char(a):
    for i in range(0,len(a)):
        if a[i] in 'aeiouAEIOU':
            yield a[i]
            yield i
out=str_char('good morning to all')
res=''
for i in out:
    res+=str(i)
print(res)            
