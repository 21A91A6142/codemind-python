a=str(input())
b=list(a)
c=[]
for i in b:
    if i!=' ':
        c.append(i)
r=c[::-1]
print(*r)