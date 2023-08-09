n=int(input())
for i in range(n):
    a=input()
    a=list(a)
    b=[]
    for i in a:
        b.append(int(i))
    k=max(b)
    l=min(b)
    if k-l==len(b)-1:
        print("YES")
    else:
        print("NO")
    