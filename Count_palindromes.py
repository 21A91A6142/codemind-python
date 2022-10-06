def ispalin(k):
    k=str(k)
    r=k[::-1]
    if k==r:
        return True
    else:
        return False
n=int(input())
a=list(map(int,input().split()))
c=0
for i in a:
    if ispalin(i):
        c=c+1
print(c)