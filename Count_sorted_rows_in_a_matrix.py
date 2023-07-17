n,m=map(int,input().split())
e=[]
for i in range(n):
    b=list(map(int,input().split()))
    e.append(b)
s=0
for i in range(n):
    if e[i]==sorted(e[i]) or e[i]==sorted(e[i],reverse=True):
        s+=1
print(s)