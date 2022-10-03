n=int(input())
a=list(map(int,input().split()))
c=0
b=[]
for i in a:
    if i==1:
        c=c+1
    else:
        c=0
    b.append(c)
print(max(b))