a=str(input())
b=a.lower()
c=list(b)
d=[]
f=[]
e='abcdefghijklmnopqrstuvwxyz'
for i in c:
    if i!=' ':
        if i not in d:
            d.append(i)
print(len(d))