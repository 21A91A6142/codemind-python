a=str(input())
b=str(input())
c=a.lower()
d=b.lower()
e=c.split()
f=d.split()
g=[]
for i in f:
    if i!=' ':
        if i in e:
            g.append(i)
print(*g)