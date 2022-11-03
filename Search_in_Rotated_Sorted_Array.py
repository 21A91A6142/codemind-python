n=int(input())
a=list(map(int,input().split()))
b=int(input())
for i in range(len(a)):
    if b==a[i]:
        print(i)
        break
else:
    print("-1")