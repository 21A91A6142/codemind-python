a=str(input())
b=str(input())
c=list(a)
d=[]
for i in a:
    if i==b:
        d.append(a.count(b))
f=set(d)
if len(f)>0:
    print(*f)
else:
    print('-1')