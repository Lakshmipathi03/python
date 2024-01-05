rows=int(input('no of rows:- '))
col=int(input('no of cols:- '))
for i in range(rows):
    for j in range(col):
        print('+',end=' ')
    print()


#empty speelle 
    rows=int(input('no of rows:- '))
    col=int(input('no of cols:- '))
    for i in range(rows):
        for j in range(col):
            if i==0 or j==rows-1:
                print('+',end=' ')
            else:
                if i==0 or j==col-1 or j==i:
                    print('+',end=' ')
                else:
                    print(' ',end=' ')
        print()
