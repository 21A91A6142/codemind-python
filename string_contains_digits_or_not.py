n=int(input())
for i in range(n):
    s=str(input())
    f=0
    for i in s:
        if i.isdigit():
            f=1
    if f==1:
        print('Yes')
    else:
        print('No')