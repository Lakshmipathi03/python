a=['abcd',{1:2},[4,5,6],{4,7},(9,8,7)]
b=[len(i) for i in a]
print(b)



#cube
a=[i**3 for i in range(1,25) if i%3==0]
print(a)


#
a=[ i for i in range(1,100) if i%3==0 if i%2==0]
print(a)


#A
A=[i**2 if i%2==0 else i**3 for i in range(1,20)]
print(A)