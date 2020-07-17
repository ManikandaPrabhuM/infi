import math
n=input()
res=[]
for i in range(len(n)):
    for j in range(i,len(n)):
        val=int(n[i:j+1])
        if val==0:
            continue
        a=int(math.sqrt(val))
        if val==(a*(a+1)):
            res.append(val)
res.sort()
print(res)
