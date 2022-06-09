a=str(input())
b=a.split()
c=[]
d=[]
s1=0
s2=0
for i in b:
    c.append(min(i))
    c.append(max(i))
print(*c)