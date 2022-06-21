n=str(input())
n=n.lower()
a='aeiou'
b='1234567890'
v=0
c=0
w=0
d=0
for i in n:
    if i in a:
        v=v+1
    elif i not in a and i not in b and i!=' ':
        c=c+1
    elif i==" ":
        w=w+1
    else:
        d=d+1
print('Vowels:',v)
print('Consonants:',c)
print('Digits:',d)
print('White spaces:',w)