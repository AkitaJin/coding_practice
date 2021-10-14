s='abc'

def dfs(s=''):
    if len(s)<=1:
        return [s]
    sl=[]
    for i in range(len(s)):
        for j in dfs(s[0:i]+s[i+1:]):
            sl.append(s[i]+j)
    return sl

print('['+", ".join(dfs("".join(sorted(s))))+']')