def ispalan(k):
    q=k
    s=0
    while(q):
        r=q%10
        s=s*10+r
        q=q//10
    if s==k:
        return True
    else:
        return False
n=int(input())
j=n
y=n
while(True):
    n=n-1
    if ispalan(n):
        p=n
        break
while(True):
    j=j+1
    if ispalan(j):
        g=j
        break
if g-y>y-p:
    print(p)
elif g-y==y-p:
    print(p,g)
else:
    print(g)
    