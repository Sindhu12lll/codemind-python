a,b=map(int,input().split())
c=0
p=0
for i in range(a,b+1):
    if i%2==0:
        c+=1
    else:
        p+=1
print(c,p,end=" ")
        