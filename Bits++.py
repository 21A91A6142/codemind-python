a=int(input())
c=0
for i in range(a):
    x=input()
    if(x.count('+')!=0):
        c+=1
    else:
        c-=1
print(c)        
        
        