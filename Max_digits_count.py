n=int(input())
a=list(map(int,input().split()))
m=max(a)
m=str(m)
c=0
for i in a:
    i=str(i)
    if len(m)==len(i):
        c=c+1
print(c)