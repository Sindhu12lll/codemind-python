n=int(input())
l=list(map(int,input().split()))
count=0
s=[]
for i in l:
    if l.count(i)==1:
        count+=1
        s.append(i)
if count:
    print(max(s))
else:
    print("-1")
        