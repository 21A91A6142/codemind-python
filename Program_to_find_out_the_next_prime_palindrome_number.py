def isprime(k):
    if k==1:
        return False
    else:
        for j in range(2,k//2+1):
            if k%j==0:
                return False
        else:
            return True
def ispalan(h):
    q=h
    s=0
    while q!=0:
        r=q%10
        s=s*10+r
        q=q//10
    if s==h:
        return True
    else:
        return False
n=int(input())
while(True):
    n=n+1
    if isprime(n) and ispalan(n):
        print(n)
        break
