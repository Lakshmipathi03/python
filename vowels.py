A=input('enter a string:- ')
i=0
count=0
while i<len(A):
    if A[i] in "aeiouAEIOU":
        count+=1
    i+=1
print(count)        
