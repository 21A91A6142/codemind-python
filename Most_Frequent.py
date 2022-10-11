n=int(input())
a=list(map(int,input().split()))
b=a.count(a[0])
c=[]
for i in a:
    if a.count(i)>b:
        b=a.count(i)
for i in a:
    if a.count(i)==b:
        c.append(i)
c=set(c)
if len(c)>=2:
    print(min(c))
else:
    print(*c)