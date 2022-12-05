n=int(input())
a=[]
for i in range(n):
    b=list(map(int,input().split()))
    a.append(b)
s=0
for i in range(n):
    for j in range(n):
        if i==j:
            s+=a[i][j];
        else:
            if i+j==n-1 and i!=j:
                s+=a[i][j]
print(s)