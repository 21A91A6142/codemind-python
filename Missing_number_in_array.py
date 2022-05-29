n=int(input())
for i in range(n):
    a=int(input())
    b=list(map(int,input().split()))
    c=[]
    for j in range(1,a+1):
        c.append(j)
    for k in c:
        if k not in b:
            print(k)
