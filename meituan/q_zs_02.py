'''
Author: Jin
Date: 2021-08-29 11:12:19
LastEditors: Jin
LastEditTime: 2021-08-29 11:43:16
Description: 
'''
# 美团秋招
# q02

import numpy as np
n=4
a=[1,2,3,4]
b=[2,4,3,4]
c=[0]*n
b=sorted(b)
for i,val in enumerate(b):
    if i > 0:
        if b[i] == b[i-1]:
            c[i] = c[i-1]-1
        else:
            cur = np.sum(list(map(lambda x: x <= val, a)))
            c[i] = cur-i
    else:
        cur = np.sum(list(map(lambda x: x <= val, a)))
        c[i] = cur
res=1
for x in c:
    res*=x
print(res)
        
