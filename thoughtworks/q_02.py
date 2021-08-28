'''
Author: Jin
Date: 2021-08-28 20:03:36
LastEditors: Jin
LastEditTime: 2021-08-28 20:39:56
Description: 
'''
# thoughtworks q_02

def countVotes(vd,vc):
    # vds = sorted(vd)
    res = [vc.count(i) for i in vd]
    inv = len(vc) - sum(res)
    ret = ""
    for letter in sorted(vd):
    # for i in range(len(vd)):
        i = vd.index(letter)
        ret = ret+vd[i]+"="+str(res[i])+" "


    ret = ret+"invalidVotes="+str(inv)+" "
    if inv > max(res) or sum(res)==0:
        winner = 'N/A'
    else:
        winner = vd[res.index(max(res))]
    ret = ret+"Winner="+winner
    return ret

vd = ['A','C','B']
# print(sorted(vd))
vc = ['A','B','B','C','C']
print(countVotes(vd,vc))