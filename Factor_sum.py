def sumoffact(k):
    s=0
    for i in range(1,k+1):
        if k%i==0:
            s+=i
    return s
n=input()
n=list(n)
a=[]
for i in n:
    if i!=',':
        a.append(int(i))
b=[]
for i in a:
    if(sumoffact(i) in a):
        b.append(i)
if len(b)>0:
    b=sorted(b)
    print(*b)
else:
    print(-1)