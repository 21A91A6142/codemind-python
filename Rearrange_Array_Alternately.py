m=int(input())
for k in range(m):
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    b=[]
    c=[]
    j=len(a)-1
    i=0
    while(i<=j):
        b.append(a[j])
        b.append(a[i])
        j=j-1
        i=i+1
    for i in b:
        if i not in c:
            c.append(i)
    print(*c)