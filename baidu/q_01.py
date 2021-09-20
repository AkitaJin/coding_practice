# a,b,x,y = map(int, input().strip().split())
a,b,x,y = 10,12,2,5
print([i//j for i in [a,b] for j in [x,y]])
# cmax=-1

# for i in range(a//x,0,-1):
#     print(i)
#     ax = i

