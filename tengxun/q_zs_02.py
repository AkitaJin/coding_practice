# shopee 正式校招 02
# 子串乘最大值


def get_max(words):
    leng=len(words)
    dis_alpha=len(set([w for w in words]))
    res=0
    for i in range(leng): #枚举的起点
        l1=set() #本轮枚举出的独立字母
        cur=words 
        s2=0
        for j in range(leng):#枚举的长度
            if i+j>=leng:#起点+长度>字符串长度就结束
                break
            if words[i+j] not in l1:
                l1.add(words[i+j])
                if len(l1) == dis_alpha: #如果已经枚举的字母中保护全部的字母，那么另外一边肯定无元素可用，长度肯定为0，肯定len(s1)*len(s2)=0
                    break
                cur=cur.replace(words[i+j]," ")#替换所有被枚举字母为空，
                s2=max([len(c) for c in cur.split()]) #以空作为切换分隔符，切割字符串，找到长度最大就是最大的S2
                s1=j+1 #s1的长度就是 j+1 
                res=max(res,s1*s2)
            else:
                s1 = j + 1
                res = max(res, s1 * s2)
            print(i,j,res,s1 * s2,l1,dis_alpha)
    return res


words='adcbadcbedbadedcbacbcadbc'
s=get_max(words)
print(s)
