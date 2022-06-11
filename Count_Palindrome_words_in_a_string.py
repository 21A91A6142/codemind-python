a=str(input())
c=a.lower()
b=c.split()
c=0
for i in b:
    d=i[::-1]
    if d==i:
        c=c+1
print(c)