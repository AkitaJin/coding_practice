# 输出一行若干个数 表示可能终止游戏的成语是第几个
n,m = map(int, input().strip().split())
l = input().strip().split()
# m-第几个成语
# l-成语数组
res = set()

def find_cy(m, l):
    tail_i = 4*m-1
    tail = l[tail_i]
    i_list = [i for i,x in enumerate(l) if x==tail and (i%4==0)]
    print(i_list)
    if len(i_list) == 0:
        # print(m)
        global res
        res = res.add(m)
        # return m
    else:
        return [find_cy(int((i/4)+1), l) for i in i_list if i != (4*m-1)]

# print(find_cy(m,l))
# a = find_cy(m,l)
find_cy(m, l)
print(res)
# print(a)
# a = list(set(find_cy(m,l)))
# a = " ".join(a)
# print(a)