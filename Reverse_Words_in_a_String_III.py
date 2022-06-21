n=str(input())
a=n.split()
c=[]
for i in a:
    b=i[::-1]
    c.append(b)
print(*c)