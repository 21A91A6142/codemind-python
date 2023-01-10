n=int(input())
a=list(map(int,input().split()))
x=0
y=0
for i in range((n//2)):
    x=x+a[i]
for i in range((n//2),n):
    y=y+a[i]
s=abs(x-y)
if s%4==0:
    print("X")
else:
    print("Y")