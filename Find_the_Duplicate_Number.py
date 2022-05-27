n=int(input())
a=list(map(int,input().split()))
b=set(a)
c=[]
for i in b:
    if a.count(i)>1:
        c.append(i)
print(*c)