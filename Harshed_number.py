n=int(input())
q=n
add=0
while q!=0:
    r=q%10
    add=add+r
    q=q//10
if n%add==0:
    print("True")
else:
    print("False")