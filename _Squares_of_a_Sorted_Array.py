n=int(input())
a=list(map(int,input().split()))
for i in range(n):
    if a[i]<0:
        a[i]=a[i]*-1
c=sorted(a)
for j in c:
    print(j*j,end=' ')