s=input()
n=int(input())
l=len(s)
k=s.count('a')
b=""
c=0
if n>l:
    c=c+k*(n//l)
    for j in range(n%l):
        if s[j]=='a':
            c=c+1
else:
    for i in range(n):
        if i=='a':
            c=c+1
print(c)