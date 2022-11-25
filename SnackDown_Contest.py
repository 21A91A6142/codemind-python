n=int(input())
for i in range(n):
    m=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    k=len(set(a))
    c=0
    for i in b:
        if i not in a:
            c=c+1
    if k+c>=m:
        print("YES")
    else:
        print("NO")