n=input()
n=list(n)
a=[]
s=0
for i in n:
    if i=="I":
        a.append(1)
    elif i=="V":
        a.append(5)
    elif i=="X":
        a.append(10)
    elif i=="L":
        a.append(50)
    elif i=="C":
        a.append(100)
    elif i=="D":
        a.append(500)
    elif i=="M":
        a.append(1000)
for i in range(len(a)-1):
    if a[i]>=a[i+1]:
        s+=a[i]
    else:
        s-=a[i]
if a[-1]<s:
    s+=a[-1]
else:
    s-=a[-1]
print(s)