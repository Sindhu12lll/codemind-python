n,m=map(int,input().split())
e=[]
for i in range(n):
    b=list(map(int,input().split()))
    e.append(b)
o=[]
for i in range(n):
    o.append(sum(e[i]))
print(sum(o))