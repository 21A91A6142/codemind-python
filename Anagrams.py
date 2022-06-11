s1=str(input())
s2=str(input())
g=s1.lower()
f=s2.lower()
a=set(g)
b=set(f)
c=[]
for i in a:
    if i!=' ':
        if i in b:
            c.append(i)
if len(c)==len(b) or len(c)==len(a):
    print(True)
else:
    print(False)