n=int(input())
for i in range(n):
    a=str(input())
    f=0
    for i in a:
        if i.isdigit():
            f=f+1
        else:
            print("False")
            break
    if len(a)==f:
        print(True)