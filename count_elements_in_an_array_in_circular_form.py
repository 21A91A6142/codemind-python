n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(len(a)-2):
    if((a[i]%2==0 and a[i+2]%2!=0) or (a[i]%2!=0 and a[i+2]%2==0)):
        c=c+1
if((a[1]%2==0 and a[n-1]%2!=0) or (a[1]%2!=0 and a[n-1]%2==0)):
    c=c+1
if((a[0]%2==0 and a[n-2]%2!=0) or (a[0]%2!=0 and a[n-2]%2==0)):
    c=c+1
print(c)