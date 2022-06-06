n=int(input())
a=list(map(int,input().split()))
s=[]
for i in a:
    if a.count(i)<2:
        s.append(i)
if len(s)>0:
    print(max(s))
else:
    print('-1')