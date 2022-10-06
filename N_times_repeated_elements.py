n=int(input())
a=list(map(int,input().split()))
d=set(a)
b=int(input())
c=[]
for i in d:
    if a.count(i)==b:
        c.append(i)
if(len(c)>0):
    print(*c)
else:
    print("-1");