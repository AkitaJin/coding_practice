# m,n = map(int,input().strip().split(","))
m,n=3,3
# l = [int(i) for i in input().strip().split()]
l = [3,2,2,0,1,0,1,1,1]
mat=[]
for i in range(m):
    tmp = l[i*n:i*n+n]
    mat.append(tmp)

# 判断当前能否跳到(m-1,n-1)
# step:当前步数
# x,y:当前坐标
def canReach(move,jump,x,y):
    if (x==m-1) and (y==n-1):
        return move
    # 仍有步数可以前进
    elif  (x>m-1) or (y>n-1):
        return 99
    elif jump>0:
        return min(canReach(move,jump-1,x,y+1),
        canReach(move,jump-1,x+1,y),
        canReach(move+1,mat[x][y],x,y))



print(canReach(2,1,2,1))