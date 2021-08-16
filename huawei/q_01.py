n,m = map(int, input().split())
word = input().strip()
# print(n,m,word)
mat = []
for _ in range(n):
    cur_line = list(input().strip())
    mat.append(cur_line)

# 用于记录走过的矩阵点
check_mat = [0] * (n * m)

def findpath(word, x, y, mat,check_mat):
    #走出界了
    global n,m
    if x > n or y > m or x < 0 or y < 0:
        return False
    # 走到底了
    elif len(word) == 1 and mat[x][y] == word[0] and check_mat[x][y] == 0:
        return True
    # 在界内，当下可以吃
    elif len(word) > 0 and mat[x][y] == word[0] and check_mat[x][y] == 0:
        check_mat[x][y] = 1
        return (findpath(word[1:], x+1,y,mat,check_mat) or
        findpath(word[1:], x-1,y,mat,check_mat) or
        findpath(word[1:], x,y+1,mat,check_mat) or
        findpath(word[1:], x,y-1,mat,check_mat))
    # 在界内，当下不能吃
    else:
        
        return False

flag = 0
for x in range(n):
    for y in range(m):
        if findpath(word, x, y, mat,check_mat):
            flag = 1

if flag == 1:
    print('YES')
else:
    print('NO')