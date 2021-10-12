'''
Author: Jin
Date: 2021-10-12 08:50:32
LastEditors: Jin
LastEditTime: 2021-10-12 13:35:08
Description: 
'''
# 题目描述
# 有一个M*N的梅花桩，每个桩都有允许跳跃的最大步数，用户从(0,0)的位置开始跳跃，允许向右和向下两个方向跳跃，求最少要跳跃多少次能到达(M-1,N-1)的位置。
# 无法到达目的地时返回-1。M<=100, N<=100，每个桩上允许跳跃的最大步数均为小于10的正整数，0表示不允许跳跃到该位置。
# 输入描述:
# 第1行为M和N，用”，”号隔开:
# 第2行为M*N的梅花桩(格式参考样例)，数组位置为允许跳跃的最大步数，0表示该位置为空，不能跳跃到该位置
# 输出描述:
# 最少跳跃的步数
# 示例
# 输入
# 3,3
# 3 2 2 0 1 0 1 1 1
# 输出
# 2

m,n=3,3
mat=[[3,2,2],[0,1,0],[1,1,1]]
dirs=[[1,0],[0,1]]
dp=[[9999]*n for _ in range(m)]
dp[0][0]=0

# 给定坐标点和步数，更新可移动范围内的矩阵数值
'''
description: 
param {*} x 坐标
param {*} y 坐标
param {*} s 可移动步数
param {*} p 当前已跳次数
return {*}
'''
def jump(x,y,s,p):
    if s>0:
        for d in dirs:
            nx,ny=x+d[0],y+d[1]
            if nx<=m-1 and ny<=n-1 and mat[nx][ny]!=0:
                dp[nx][ny]=min(dp[nx][ny], p)
                jump(nx,ny,s-1,p)

for i in range(m):
    for j in range(n):
        if mat[i][j]!=0 or ~(i==m-1 and j==n-1):
            jump(i,j,mat[i][j],dp[i][j]+1)

print(dp)
print(dp[m-1][n-1])
