def reverse(k):
    s=0
    q=k
    while(q!=0):
        r=q%10
        s=s*10+r
        q=q//10
    return s
n=int(input())
a=list(map(int,input().split()))
b=[]
for i in a:
    b.append(reverse(i))
print(*b)