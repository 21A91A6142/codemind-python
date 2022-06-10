n=str(input())
a=list(n)
for i in range(len(a)):
    if a.count(a[i])<2:
        print(i)
        break
else:
    print('-1')