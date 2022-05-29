n=int(input())
b=list(map(int,input().split()))
c=[]
for j in range(1,n+1):
    c.append(j)
for k in c:
    if k not in b:
        print(k)
        break