'''
Author: Jin
Date: 2021-09-27 15:17:21
LastEditors: Jin
LastEditTime: 2021-09-27 15:26:28
Description: 
'''

# 假设只有2个广告位(a,b)和3个广告(0,1,2)
a=[1,2,3]
b=[5,3,2]
sum=-1

for i,aa in enumerate(a):
    for j,bb in enumerate(b):
        if i != j:
            if aa+bb>sum:
                sum=aa+bb

def findMax(i,j,a,b):
    if a[i]+b[j]>sum: return a[i]+b[j]
    else:
        return max(findMax(i+1,j,a,b),
        findMax(i,j+1,a,b),)