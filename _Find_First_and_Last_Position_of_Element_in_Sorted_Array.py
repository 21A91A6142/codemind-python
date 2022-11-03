n=int(input())
a=list(map(int,input().split()))
m=int(input())
k=1
b=[]
for i in range(n):
    if a[i]==m:
        b.append(i)
        break
else:
    b.append(-1)
for i in range(n-1,-1,-1):
    if a[i]==m:
        b.append(i)
        break
else:
    b.append(-1)
print(*b)