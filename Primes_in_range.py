def isprime(k):
    if k==1:
        return False
    else:
        for j in range(2,int(k**0.5)+1):
            if k%j==0:
                return False
                break
        else:
            return True
a=int(input())
b=int(input())
c=0
for i in range(a,b+1):
    if isprime(i):
        c=c+1
print(c)