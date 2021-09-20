# roguelike迷宫

def bfs():
    n,m = [int(i) for i in input().strip().split()]
    mat, s_cor=[],[]
    for i in range(n):
        l = list(input())
        if 'S' in l:
            s_cor = [i, l.index('S')]
        mat.append(l)
    dx,dy=[1,-1,0,0],[0,0,1,-1]
    queue=[s_cor]
    visited=[[False for _ in range(n)] for _ in range(m)]
    visited[s_cor[0]][s_cor[1]]=True
    sec = 0
    while queue:
        sec+=1
        len_q = len(queue)
        for _ in range(len_q):
            q=queue.pop(0)
            for _x, _y in zip(dx,dy):
                x,y = q[0]+_x, q[1]+_y
                if x>=0 and y>=0 and x<n and y<m:
                    if not visited[x][y] and mat[x][y]!='X':
                        if mat[x][y]=='E':
                            return sec
                        queue.append([x,y])
                        visited[x][y]=True
    return -1

T = int(input())
for i in range(T):
    print(bfs())
