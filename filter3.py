def multiple(a):
    for i in range(1,201):
        if a%3==0 and a%5==0:
            return True
        else:
            return False
out=filter(multiple,range(1,201))
print(list(out))