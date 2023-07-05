a,b=map(int,input().split())
c=list(map(int,input().split()))
x=list(map(int,input().split()))
s=[]
s1=[]
for i in c:
    if i in x:
        s.append(i)
for j in x:
    if j in c:
        s1.append(j)
s2=s+s1
s3=set(s2)
print(len(s3))