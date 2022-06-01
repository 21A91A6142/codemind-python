a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=0
m=0
for i in range(0,len(a)):
    if a[i]>b[i]:
        c=c+1
    elif a[i]<b[i]:
        m=m+1
print(c,m)