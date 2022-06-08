n=str(input())
c='aeiou'
b=list(n)
d=[]
e=[]
k=[]
for i in b:
    if i in c:
        d.append(i)
for i in d:
    if i not in e:
        e.append(i)
for i in c:
    if i not in e:
        k.append(i)
if len(k)>0:
    print(*k)
else:
    print('0')