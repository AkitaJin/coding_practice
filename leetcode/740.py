'''
Author: Jin
Date: 2021-10-15 13:59:46
LastEditors: Jin
LastEditTime: 2021-10-15 14:35:54
Description: 
'''

# 740. 删除并获得点数
# 给你一个整数数组 nums ，你可以对它进行一些操作。

# 每次操作中，选择任意一个 nums[i] ，删除它并获得 nums[i] 的点数。之后，你必须删除 所有 等于 nums[i] - 1 和 nums[i] + 1 的元素。

# 开始你拥有 0 个点数。返回你能通过这些操作获得的最大点数。

# 示例 1：

# 输入：nums = [3,4,2]
# 输出：6
# 解释：
# 删除 4 获得 4 个点数，因此 3 也被删除。
# 之后，删除 2 获得 2 个点数。总共获得 6 个点数。
# 示例 2：

# 输入：nums = [2,2,3,3,3,4]
# 输出：9
# 解释：
# 删除 3 获得 3 个点数，接着要删除两个 2 和 4 。
# 之后，再次删除 3 获得 3 个点数，再次删除 3 获得 3 个点数。
# 总共获得 9 个点数。

# nums = [3,4,2]
# nums = [2,2,3,3,3,4]
nums = [8,10,4,9,1,3,5,9,4,10] #37

def deleteAndEarn(nums):
    import collections
    d = collections.Counter(nums)
    n=len(d)
    nm=max(nums)+1
    if n==1:
        return sum(nums)
    # cs[i]表示nums[i]的数量之和
    # dp[i]表示保留nums[i]的最大点数
    cs,dp = [0]*nm,[0]*nm
    for k in d:
        cs[k]=d[k]*k
    for i in range(nm):
        if i<=1:
            dp[i]=cs[i]
        else:
            dp[i]=max(dp[i-2]+cs[i],dp[i-1])
    print(n,sorted(nums),cs,dp)
    return dp[nm-1]

print(deleteAndEarn(nums))