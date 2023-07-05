a,b=map(int,input().split())
c=list(map(int,input().split()))
x=list(map(int,input().split()))
s=[]
for i in c:
    if i in x:
        if i not in s:
            s.append(i)
print(*s)
