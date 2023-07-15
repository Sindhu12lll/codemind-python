s=input()
f=1
l=[]
for i in s:
    if s.count(i)==1:
        f=0
        l.append(s.index(i))
if f==0:
    print(l[0])
else:
    print("-1")
    