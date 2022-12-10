n,m=map(int,input().split())
a=[]
for i in range(n):
    b=list(map(int,input().split()))
    s=0
    for j in b:
        s+=j
    a.append(s)
print(max(a))