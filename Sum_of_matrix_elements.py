m=int(input())
n=int(input())
s=0
for i in range(m):
    a=list(map(int,input().split()))
    for j in range(n):
        s=s+a[j]
print(s)