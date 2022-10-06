n=int(input())
a=list(map(int,input().split()))
m=min(a)
m=str(m)
c=0
for i in a:
    i=str(i)
    if len(i)==len(m):
        c=c+1
print(c)