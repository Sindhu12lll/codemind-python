n,m=map(int,input().split())
e=[]
for i in range(n):
    b=list(map(int,input().split()))
    e.append(b)
rsum=[]
for i in range(n):
    for j in range(m):
        if(i==j or i+j==n-1):
            rsum.append(e[i][j])
print(sum(rsum))