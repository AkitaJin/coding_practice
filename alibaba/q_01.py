import sys
from bisect import bisect_left
T = int(input())
for _ in range(T):
    n = int(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    a = sorted(zip(x, y))
    total = 0
    q=[0] * 100005
    for i in range(n):
    	ind = bisect_left(a=q, x=a[i][1], lo=0, hi=total)
    	# print('ind', ind)
    	if ind == total:
    		total += 1
		q[t] = a[i][1]
	print(total)