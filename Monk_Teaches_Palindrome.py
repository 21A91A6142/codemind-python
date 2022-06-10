n=int(input())
for i in range(n):
    a=str(input())
    b=list(a)
    c=a[::-1]
    if c==a:
        print("YES",end=' ')
        if len(b)%2==0:
            print("EVEN")
        else:
            print('ODD')
    else:
        print('NO')