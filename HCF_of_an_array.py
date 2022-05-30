n=int(input())
a=list(map(int,input().split()))
for i in range(0,n):
    c=0
    for j in range(0,n):
        if a[j]%a[i]==0:
            c=c+1
    if c==n:
        print(a[i])
        break
else:
    print('1')