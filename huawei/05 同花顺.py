# 05 同花顺
# 同花顺，有一个字符串是数组，有5个元素，每个元素有字符和数字组成，字符是A, B,C,D这种，
# 例如A1,A2,A3,A4,A5是一个同花顺，A1,A2,C3,A4,A5就不是同花顺，如果有0，代表大小王，大小王可以变成任意牌，C1,C2,C3,0,C5这种也是同花顺
# l=['A1','A2','A3','A4','A5']
# l=['A1','A2','C3','A4','A5']
# l=['C1','C2','C3','0','C5']
l=['A1','0','0','0','A8']
f=True


def flush(l):
    l1=[i[0] for i in l if len(i)>1]
    l2=[int(i[1]) for i in l if len(i)>1]
    c0=5-len(l2) #大小王的个数
    if c0 >=4: return True
    if len(set(l1))>1: return False
    if len(set(l2))+c0<5: return False
    if max(l2)-min(l2)>c0+1: return False
    else: return True

print(flush(l))

