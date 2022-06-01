n=int(input())
a=list(map(int,input().split()))
m=set(a)
k=list(m)
if n<3:
    print(max(a))
else:
    d=max(k)
    c=k.index(d)
    k.pop(c)
    b=max(k)
    b=k.index(b)
    k.pop(b)
    print(max(k))