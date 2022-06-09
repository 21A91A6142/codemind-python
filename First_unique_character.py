a=str(input())
b=a.lower()
c=list(b)
d=[]
f=[]
e='abcdefghijklmnopqrstuvwxyz'
for i in c:
    if i!=' ':
        if c.count(i)<2:
            d.append(i)
            break
if len(d)>0:
    print(*d)
else:
    print('-1')