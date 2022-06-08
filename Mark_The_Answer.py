a,b=map(int,input().split())
c=list(map(int,input().split()))
#print(a,b)
#print(c)
p=0
m=0
for i in range(0,a):
    if p<2:
        if c[i]<=b:
            m=m+1
        else:
            p=p+1
    else:
        break
print(m)