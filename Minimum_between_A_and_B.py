n=int(input())
a=list(map(int,input().split()))
n,m=map(int,input().split())
s=0
l=[]
for i in a:
    if i>=n and i<=m:
        s=1
        l.append(i)
        d=min(l)
if s==1:
    print(d)
else:
    print("-1")