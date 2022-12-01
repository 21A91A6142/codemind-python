n=int(input())
m=int(input())
a=[]
b=[]
for i in range(n,m+1):
    a.append(i)
for i in range(len(a)-1):
    for j in range(i+1,len(a)):
        s=0
        for k in range(i,j+1):
            s+=a[k]
        b.append(s)
b.extend(a)
c=0
for i in b:
    if i%2!=0:
        c=c+1
print(c)