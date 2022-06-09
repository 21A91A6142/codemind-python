a=str(input())
b=a.lower()
c=list(b)
e=[]
d='abcdefghijklmnopqrstuvwxyz'
for i in c:
    if i!=' ':
        if i not in d:
            e.append(i)
print(len(e))

        