n=int(input())
a=list(map(int,input().split()))
b=a
s=1
c=[]
for i in a:
    for j in b:
        if i!=j:
            s=s*j
    c.append(s)
    s=1
print(*c)