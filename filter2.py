def single(a):
    for i in a:
        if type(a) in [int,float,complex,bool]:
            return True
        else:
            return False
out=filter(single,[2,3,4,5,8,9,10])
print(list(out))