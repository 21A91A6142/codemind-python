n=int(input())
a=list(map(int,input().split()))
b=[]
for i in range(len(a)-1):
    c=1
    for j in range(i+1,len(a)):
        if a[i]<a[j]:
            b.append(c)
            break
        else:
            c=c+1
    else:
        b.append(0)
b.append(0)
print(*b)