def prime(k):
    for j in range(2,i//2+1):
        if i%j==0:
            return False
            break
    else:
        return True
n=int(input())
k=0
c=1
for i in range(2,n+1):
    if n%i==0:
        c=c+1
        if prime(i):
            k=k+1
print(c-k)