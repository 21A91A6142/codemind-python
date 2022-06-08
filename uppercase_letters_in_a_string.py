a=str(input())
b=list(a)
c=a.upper()
d=list(c)
k=[]
for i in b:
    if i!=' ':
        if i in d:
            k.append(i)
print(len(k))