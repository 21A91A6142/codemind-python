n=str(input())
a=list(n)
b=a.count('z')
c=a.count('o')
if 2*b==c:
    print('Yes')
else:
    print('No')