# q_03 滑动窗口
n = int(input())
l = sorted([int(i) for i in input().split()])
s = []
n = len(l)
left = right = ret = 0

while right < n:
    s = sorted(s+[l[right]])
    while s[-1] - s[0] > 10:
        s.remove(l[left])
        left += 1
    ret = max(ret, right - left + 1)
    right += 1

print(ret)

