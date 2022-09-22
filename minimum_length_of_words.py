a=input()
a=a.split();
b=[]
for i in a:
    b.append(len(i))
print(min(b))