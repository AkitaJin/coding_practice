# wangyi q_02

names = list(input().strip().split())
nameset = set(names)
s = list(input().strip())
count = 0

def checkWord(x,s):
    for i in range(len(x)):
        if x[i]!=s[i]:
            return False
    return True

for i,x in enumerate(s):
    for name in nameset:
        if i+len(name) <= len(s):
            # print(name, s[i:])
            if checkWord(name,s[i:]):
                count+=1
print(count)
