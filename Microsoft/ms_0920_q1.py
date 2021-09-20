# ms 0920 q1
import re
S="aaBbcd"
lc = r'[a-z]'
uc = r'[A-Z]'
llc = re.findall(lc,S)
llc = sorted(llc,reverse=True)
lup = re.findall(uc,S)
lup = sorted(lup,reverse=True)
for i in range(len(lup)):
    if lup[i].lower() in llc:
        print(lup[i])
        break
print('NO')