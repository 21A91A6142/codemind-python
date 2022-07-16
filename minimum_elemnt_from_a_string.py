n=input()
n=n.split()
a=list(n[len(n)-1])
k=min(a)
b=k.lower()
for i in a:
    if i==b:
        print(b)
        break
else:
    print(k)