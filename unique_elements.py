n=int(input())
a=list(map(int,input().split()))
#print(a)
b=[]
for i in a:
    if i not in b:
        b.append(i)
print(*b)