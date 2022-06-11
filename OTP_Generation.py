n=str(input())
a=list(n)
b=[]
c=[]
for i in a:
    if i!=' ':
        if i.isdigit():
            if int(i)%2!=0:
                b.append(int(i)*int(i))
for i in b:
    c.append(str(i))
d=''.join(c)
print(d)