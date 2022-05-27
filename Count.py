n=int(input())
a=list(map(int,input().split()))
c=0
for i in a:
    if i%2==0:
        c=c+1
print(c,n-c)