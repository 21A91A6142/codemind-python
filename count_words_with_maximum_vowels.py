def isvowel(i):
    u="aeiou"
    c=0
    i=list(i)
    for j in i:
        if j in u:
            c=c+1
    return c
n=input()
a=n.split()
b=[]
v="aeiou"
for i in a:
    i=list(i)
    c=0
    for j in i:
        if j in v:
            c=c+1
    b.append(c)
k=max(b)
s=0
for i in a:
    if isvowel(i)==k:
        s=s+1
print(s)