n=int(input())
n1=0
n2=1
for i in range(n):
    n3=n1+n2
    n1=n2
    n2=n3
    if n3==n:
        print(True)
        break
else:
    print(False)