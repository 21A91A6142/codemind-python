a=str(input())
b=list(a)
c=a.lower()
d=list(c)
m=[]
for i in b:
    if i!=' ':
        if i in d:
            m.append(i)
print(len(m))