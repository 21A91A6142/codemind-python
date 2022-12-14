n=input()
n=n.split()
a=""
v="aeiouAEIOU"
for i in range(len(n)):
    k=n[i]
    k=list(k)
    if k[0] in v:
        k.append("ma")
    else:
        k.append(k[0])
        k.remove(k[0])
        k.append("ma")
    for j in range(i+1):
        k.append('a')
    m="".join(k)
    a+=m
    a+=" "
for i in range(len(a)-1):
    print(a[i],end="")