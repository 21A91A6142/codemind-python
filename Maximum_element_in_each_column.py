n,m=map(int,input().split())
b=[]
for i in range(n):
    a=list(map(int,input().split()))
    b.append(a)
for j in range(0,m):
    c=[]
    for i in range(0,n):
        c.append(b[i][j])
    print(max(c))