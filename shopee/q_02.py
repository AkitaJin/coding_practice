# 数组平衡点

def balance_point(thy_list):
    num = len(thy_list)
    for i in range(num):
        if i == 0:
            pass
        else:
            list1 = thy_list[:i]  # 将传入的列表切片，将一个列表分成2个列表
            list2 = thy_list[i+1:]
            sum1 = sum(list1)   # 对切片后的列表分别求和
            sum2 = sum(list2)
            if sum1 == sum2:
                return i