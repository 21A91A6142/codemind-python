a=str(input())
b=a.lower()
c=list(b)
d=[]
f=[]
e='abcdefghijklmnopqrstuvwxyz'
for i in c:
    if i!=' ':
        if c.count(i)<2:
            d.append(i)
for i in e:
    if i in d:
        f.append(i)
g=''.join(f)
print(g)