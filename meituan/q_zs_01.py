'''
Author: Jin
Date: 2021-08-29 10:03:20
LastEditors: Jin
LastEditTime: 2021-08-29 10:55:36
Description: 
'''
# 美团秋招
# q 01
# from collections import Counter
# n = int(input().strip())
# l = [int(i) for i in input().strip().split()]
# n=10
# l=[1,1,2,2,2,3,3,3,3,1]
# res = 0
# for i,val in enumerate(l):
#     cur_c = Counter(l[0:i])
#     print(i,val,cur_c)
#     count=0
#     for j in cur_c.keys():
#         if j < val:
#             count+=1
#     res+=count
# print(res)
    

import numpy as np
n=10
l=[1,1,2,2,2,3,3,3,3,1]
res = 0
last_set=set()
for i,val in enumerate(l):
    # cur_s = set(l[0:i])
    if i==0:
        last_set.add(val)
    else:
        res+=np.sum(list(map(lambda x: x < val, list(last_set))))
        last_set.add(val)
print(int(res))
