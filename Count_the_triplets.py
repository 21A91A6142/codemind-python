n=int(input())
for i in range(n):
    m=int(input())
    a=list(map(int,input().split()))
    b=[]
    c=0
    for i in a:
        for j in a:
            if i!=j:
                l=i+j
                b.append(l)
    for i in b:
        if i in a:
            c=c+1
    if c>0:
        print(c//2)
    else:
        print("-1")