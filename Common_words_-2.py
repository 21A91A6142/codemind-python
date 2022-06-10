s1=str(input())
s2=str(input())
a=s1.split()
b=s2.split()
c=[]
d=[]
e=[]
for i in a:
    if a.count(i)<2:
        c.append(i)
for i in b:
    if b.count(i)<2:
        d.append(i)
for i in c:
    if i!=' ':
        if i in d:
            e.append(i)
print(len(e))