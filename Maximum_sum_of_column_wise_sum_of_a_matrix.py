n,m=map(int,input().split())
e=[]
for i in range(n):
    b=list(map(int,input().split()))
    e.append(b)
rsum=[]
for i in range(m):
    c=0
    for j in range(n):
        c+=e[j][i]
    rsum.append(c)
print(max(rsum))