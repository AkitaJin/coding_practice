# ms 0920 q3
# A,X,Y=[5,3,8,3,2],2,5 #7 OK
# A,X,Y=[4,2,7],4,100 #12
# A,X,Y=[2,2,1,2,2],2,3 #8 OK
A,X,Y=[4,1,5,3],5,2 #4
A=sorted(A,reverse=True)
# X,Y=2,5
c=0

for i,val in enumerate(A):
    if sum(A)-val<=0:
        c+=X
        A[i]=0
        break
    elif sum(A)-2*val<=0:
        c+=Y
        A[i]=-val
        break
    else:
        A[i]=-val
        c+=Y
print(c,A)