n,m=map(int,input().split())
e=[]
for i in range(n):
    b=list(map(int,input().split()))
    e.append(b)
rsum=[]
for i in range(n):
    rsum.append(sum(e[i]))
print(max(rsum))