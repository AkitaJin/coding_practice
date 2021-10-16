'''
Author: Jin
Date: 2021-10-13 11:25:12
LastEditors: Jin
LastEditTime: 2021-10-13 14:17:12
Description: leetcode 1301
'''
# 给你一个正方形字符数组 board ，你从数组最右下方的字符 'S' 出发。
# 你的目标是到达数组最左上角的字符 'E' ，数组剩余的部分为数字字符 1, 2, ..., 9 或者障碍 'X'。
# 在每一步移动中，你可以向上、向左或者左上方移动，可以移动的前提是到达的格子没有障碍。
# 一条路径的 「得分」 定义为：路径上所有数字的和。
# 请你返回一个列表，包含两个整数：第一个整数是 「得分」 的最大值，第二个整数是得到最大得分的方案数，请把结果对 10^9 + 7 取余。
# 如果没有任何路径可以到达终点，请返回 [0, 0] 。
# 示例 1：
# 输入：board = ["E23","2X2","12S"]
# 输出：[7,1]
# 示例 2：
# 输入：board = ["E12","1X1","21S"]
# 输出：[4,2]
# 示例 3：
# 输入：board = ["E11","XXX","11S"]
# 输出：[0,0]

mod=10**9+7
board = ["E23","2X2","12S"]
# board = ["E12","1X1","21S"]
# board = ["E11","XXX","11S"]
m=len(board)
n=len(board[0])
dps,dpc=[[0]*n for _ in range(m)],[[0]*n for _ in range(m)]
dirs=[[-1,0],[0,-1],[-1,-1]]
    
# 从E走向S
for i in range(m):
    for j in range(n):
        cur = board[i][j]
        # print(cur)
        if cur=='E':
            dps[i][j]=0
            dpc[i][j]=1
        elif cur=='X':
            dps[i][j]=0
            dpc[i][j]=0
        # 棋盘的值是数字或S
        # 找出(左/左上/上)中最大的值及对应的路径数
        else:
            cursl,curcl=[],[]
            for d in dirs:
                ni,nj=i+d[0],j+d[1]
                if ni>=0 and nj>=0:
                    cursl.append(dps[ni][nj])
                    curcl.append(dpc[ni][nj])
                    # print(cursl,curcl)
            # 如果三个方向都没有值，则无法走通，dps为0
            if sum(curcl)==0 and sum(cursl)==0:
                dps[i][j]=0
                dpc[i][j]=0
            else:
                # dps赋值为三个方向的最大值
                if cur=='S':
                    dps[i][j]=max(cursl)
                else:
                    dps[i][j]=int(board[i][j])+max(cursl)
                # dpc赋值为路径和为最大的路径数量的和
                c=0
                for id,v in enumerate(cursl):
                    if v==max(cursl):
                        c+=curcl[id]
                dpc[i][j]=c
        # print(i,j,dps,dpc)
        # print('*****************')
print([dps[m-1][n-1]%mod,dpc[m-1][n-1]%mod])