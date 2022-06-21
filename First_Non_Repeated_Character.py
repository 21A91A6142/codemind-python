n=int(input())
#print(n)
for i in range(n):
    m=[]
    b=int(input())
    a=str(input())
    c=list(a)
    for j in a:
        if a.count(j)<2:
            m.append(j)
    if len(m)>0:
        print(m[0])
    else:
        print('-1')