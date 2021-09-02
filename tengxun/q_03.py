# 腾讯 q 03
n = int(input())
l = sorted([int(i) for i in input().split()])
lset = set(l)
llset = len(lset)
unique_l = sorted(list(lset))
mat = [[0]*11 for _ in range(llset)]
for s,x in enumerate(unique_l):
    cur_count = 0
    last_num = -1
    for y in range(11):
        tmp = l.count(x+y)
        if tmp > 0:
            cur_count+=1
            if last_num == -1:
                last_num = x+y
            mat[s][y] = l.count(x+y)
        # 遇到十以内的第三个值：4、7、9中，4遇到9，需要给7对应位置赋值
        if cur_count > 1:
            try:
                mat[s+cur_count-1][x+y-last_num] = tmp
            except:
                print(s+cur_count-1, x+y-last_num)
        last_num = x+y
print(mat)
print(max([sum(ll) for ll in mat]))
