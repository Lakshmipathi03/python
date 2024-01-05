def main(a,b,c):
    out=[]
    for i,j,k in zip(a,b,c):
        out+=[i]+[j]+[k]
        print(out)
main([1,2,3,4],[2,3,4,5],[3,4,5,6])
