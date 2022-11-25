n=int(input())
a=list(map(int,input().split()))
b=sorted(a)
c=[]
for i in range(len(b)-2,0,-2):
    c.append(b[i])
    c.append(b[i+1])
for i in b:
    if i not in c:
        c.append(i)
print(*c)