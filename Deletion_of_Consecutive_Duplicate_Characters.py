n=int(input())
for i in range(n):
    a=input()
    c=0
    for i in range(len(a)-1):
        if a[i]!=a[i+1]:
            continue
        else:
            c=c+1
    print(c)