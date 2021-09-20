# ms 0920 q3
# A,X,Y=[5,3,8,3,2],2,5 #7 OK
# A,X,Y=[4,2,7],4,100 #12
A,X,Y=[2,2,1,2,2],2,3 #8 OK
# A,X,Y=[4,1,5,3],5,2 #4
A=sorted(A,reverse=True)
c,i=0,0
def minCost(A,X,Y,c,i):
    print(A,c,i,sum(A))
    if sum(A)<=0:
        return c
    else:
        Ax,Ay=A.copy(),A.copy()
        Ax[i]=0
        cx=c+X
        Ay[i]=-Ay[i]
        cy=c+Y
        i+=1
        return min(minCost(Ax,X,Y,cx,i), minCost(Ay,X,Y,cy,i))


print(minCost(A,X,Y,c,i))