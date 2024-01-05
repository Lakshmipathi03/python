s=input('enter IP address:- ')
def ip (s):
    st=s.split('.')
    if len(st)==4:
        for i in st:
            if not i.isnumeric():
                out='No'
                break
            else:
                out='yes'
    else:
        out='No'
    return out
print(ip(s))
