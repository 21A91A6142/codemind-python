n=int(input())
a=list(map(int,input().split()))
b=[]
for i in range(len(a)-1):
    for j in range(i+1,len(a)):
        s=0
        for k in range(i,j+1):
            s+=a[k]
        b.append(s)
b.extend(a)
b.append(a[len(a)-1]+a[0])
print(max(b))