n=str(input())
b=n.lower()
a=b.split()
e='aeiou'
for i in a:
    s=0
    c=list(i)
    for j in c:
        if j in e:
            s=s+1
    print(s,end=' ')