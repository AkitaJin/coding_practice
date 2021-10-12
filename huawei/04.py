'''
Author: Jin
Date: 2021-10-12 13:33:55
LastEditors: Jin
LastEditTime: 2021-10-12 14:05:21
Description: 
'''

# A公司需要在项目中引入某开源工程，需要评估该开源工程中某模块的编译时间。
# 当前已知该项目中每个模块的编译时间以及其依赖的模块列表，在拥有无限数量的并行任务的情况下，求某个指定模块的最短编译时间。
# 若模块间存在循环依赖或者依赖的模块不存在，则无法完成编译，返回-1。
# 输入描述：
# 第一行输入为目标模块名，以后每行输入定义一个模块，包含模块的名字，编译时间，依赖模块列表，用逗号隔开，若依赖模块列表不存在，则表示可以独立编译，例如：
# module2，10，module1
# module1,10
# 模块名只包含字母和数字且至少包含一个字符
# 模块数量不超过50000个
# 输出描述：
# 输出最短编译时间，若无法完成编译则输出-1
# 示例1：
# module3
# module1,10
# module2,5
# module3,10,module1,module2
# 输出：20
# 说明：module1编译需要10ms，module2编译需要5ms,module3编译依赖module1,和module2,同时自身编译也需要10ms,所以总的编译时间为10+max(10,5) = 20ms
# 示例2：
# module2
# module2,10,module1
# 输出：-1
# 说明:module1没有定义，无法完成编译，所以输出-1

# ———————————case1——————————
# tm='m3'
# tt={'m1':[10],
#     'm2':[5],
#     'm3':[10,'m1','m2']}
# ———————————case2——————————
tm='m2'
tt={'m2':[10,'m1']}

def dfs(m):
    if m not in tt.keys(): return -1
    if len(tt[m])==1: return tt[m][0]
    res=0
    for mm in tt[m][1:]:
        res+=dfs(mm)
    return res
        
print(dfs(tm))