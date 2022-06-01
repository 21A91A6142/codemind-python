n=int(input())
s=[]
for i in range(n):
    a=int(input())
    s.append(a)
b=int(input())
c=0
m=0
for i in range(len(s)):
    if s[i]<=b:
        c=c+1
    else:
        m=m+2
print(c+m)
    