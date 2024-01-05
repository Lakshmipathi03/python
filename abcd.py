def upper(a):
    if 'A'<=a<='Z':
        return True
    else:
        return False
out=filter(upper,"aBFFGGJKL;OIUag668920")
print(list(out))    