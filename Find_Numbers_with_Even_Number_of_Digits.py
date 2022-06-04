def isdigit(k):
    m=0
    while(k):
        r=k%10
        m=m+1
        k=k//10
    if m%2==0:
        return True
    else:
        return False
n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(n):
    if isdigit(a[i]):
        c=c+1
print(c)