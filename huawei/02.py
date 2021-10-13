# 二叉树分割最大差值
# 给出一颗二叉树，每个节点有一个编号和个值，该值可能为负数，
# 请你找出个最优节点(除根节点外)，使得在该节点将树分成两棵树后(原来的树移除这个节点及其子节点，新的树以该节点为根节点)，
# 分成的两棵树各节点的和之间的差绝对值最大。请输出该节点编号，如有多个相同的差，输出编号最小的节点。

# 输入：
# 4
# 4 9 -7 -8
# 0 1
# 0 3
# 1 2
# 第一行，四个节点，编号0-3，范围1-10000
# 第二行，节点0-3权值
# 第三行到第五行，表示二叉树各节点间的父子关系
# 0 1 节点0的左节点是1
# 0 3 节点0的右节点是3
# 1 2 节点1的左节点是2
# 注意：左节点永远出现在右节点之前

# 输出：
# 节点编号，示例中编号为3的节点是最优节点

l=[1,3,4,5,-1,-5,2]
b={0:[6,1],1:[4,5],6:[2,3]}
# br = {v:k for k,v in b.items()}
# def get_key (value):
#     return [k for k, v in b.items() if value in v]

def dfsum(n):
    res=0
    if n in b.keys():
        for i in range(len(b[n])):
            res+=dfsum(b[n][i])
    res+=l[n]
    return res

maxd = -1
node = 10001
for i in b.keys():
    p=l[i]
    psum=dfsum(i)
    et=sum(l)-psum

    for j in b[i]:
        t1sum=dfsum(j)
        curd=abs(psum-2*t1sum+et)
        print("i:%s,j:%s,p:%s,psum:%s,t1sum=%s,curd=%s,maxd=%s,node=%s" % (i,j,p,psum,t1sum,curd,maxd,node))
        if curd>maxd:
            maxd=curd
            node=j
            print("i:%s,j:%s,p:%s,psum:%s,t1sum=%s,curd=%s,maxd=%s,node=%s*&***" % (i,j,p,psum,t1sum,curd,maxd,node))
        if curd==maxd and j<node:
            node=j
            print("i:%s,j:%s,p:%s,psum:%s,t1sum=%s,curd=%s,maxd=%s,node=%s*&***" % (i,j,p,psum,t1sum,curd,maxd,node))

print(node,maxd)
