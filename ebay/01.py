'''
Author: Jin
Date: 2021-09-29 20:02:22
LastEditors: Jin
LastEditTime: 2021-09-29 20:22:03
Description: 
'''

# ebay_01
m,n=map(int, input().strip().split())
# m,n=1,999999
cc=0
for i in range(m,n+1):
    a='6'
    b='17'
    if a in str(i) or b in str(i):
        print(i)
        cc+=1
print(cc)


