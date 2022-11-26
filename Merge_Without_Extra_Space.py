n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    c=list(map(int,input().split()))
    d=list(map(int,input().split()))
    k=sorted(c+d)
    print(*k)