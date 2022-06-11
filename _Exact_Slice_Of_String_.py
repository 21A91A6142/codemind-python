a=str(input())
b=int(input())
c=int(input())
d=list(a)
e=[]
for i in range(b,c+1):
    e.append(d[i])
f=''.join(e)
print(f)