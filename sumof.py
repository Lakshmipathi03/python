a=[1,9,11,23,65,78,43]
if len(a)%2==0:
    out=0
    for var in a:
        out+=var
else:
    out=1
    for var in a:
        out=out*var
print(out)                