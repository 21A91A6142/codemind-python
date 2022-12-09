def isprime(k):
    if k<=1:
        return False
    else:
        for i in range(2,int(k**0.5)+1):
            if k%i==0:
                return False
                break
        else:
            return True
n=int(input())
for i in range(n):
    a=int(input())
    p=a
    while(True):
        a=a-1
        if isprime(a):
            k=a
            break
    while(True):
        a=a+1
        if isprime(a):
            m=a
            break
    if abs(p-m)<abs(p-k):
        print(m)
    else:
        print(k)