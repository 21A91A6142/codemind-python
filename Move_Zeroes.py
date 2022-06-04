n=int(input())
a=list(map(int,input().split()))
#print(a)
c=[]
b=[]
for i in a:
    if i==0:
        b.append(i)
for j in a:
    if j!=0:
        c.append(j)
print(*(c+b))
#print(b)