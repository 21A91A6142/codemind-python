a=str(input())
b=a.lower()
d=list(b)
c=[]
for i in d:
    if i!=' ':
        if d.count(i)<2:
            c.append(i)
print(len(c))