def checkWord(x,s):
    for i in range(len(x)):
        if x[i]!=s[i]:
            return False
    return True

a,b = list(input().split())

print(checkWord(a,b))