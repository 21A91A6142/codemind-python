a=str(input())
b=a.split()
c=[]
d=[]
s1=0
s2=0
for i in b:
    c.append(min(i))
    d.append(max(i))
for i in range(len(c)):
    print(abs(ord(d[i])-ord(c[i])),end=' ')