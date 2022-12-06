n=input()
a=""
b=[]
for i in n:
    if i.isnumeric():
        a+=i
        k=int(i)
        if k%2==0:
            b.append(k)
if len(b)==0:
    print("-1")
else:
    c=""
    d=""
    a=sorted(a)
    k=min(b)
    for i in a:
        if i not in c:
            c+=i
    c=c[::-1]
    for i in c:
        if i not in d and i!=str(k):
            d+=i
    print(d+str(k))
            