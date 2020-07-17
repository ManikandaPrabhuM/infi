stri=input()
odd,eve,spl=[],[],[]
for i in stri:
    if i.isdigit() and int(i)%2==0:
        eve.append(int(i))
    elif i.isdigit() and int(i)%2==1:
        odd.append(int(i))
    elif i.isalnum()==False:
        spl.append(i)
print(spl)
if len(spl)%2==0:
    k=1
    while odd!=[]:
        val=odd.pop(0)
        eve.insert(k,val)
        k+=2
    print(*eve,sep=" ")
else:
    k=1
    while eve!=[]:
        val=eve.pop(0)
        odd.insert(k,val)
        k+=2
    print(*odd,sep=" ")
