a=str(input())
b=a.split()
c=[]
d=[]
s1=0
s2=0
for i in range(len(b)):
    c.append(min(b[0]))
    c.append(max(b[len(b)-1]))
    break
print(*c)