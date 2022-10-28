n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(len(a)-1):
    k=a[i]+a[i+1]
    if a[i]%2==0 and a[i+1]%2==0:
        c=c+1
print(c)