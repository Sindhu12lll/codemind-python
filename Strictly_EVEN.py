n=int(input())
a=list(map(int,input().split()))
c=0
s=len(a)
m=0
for i in range(s):
    if a[i]%2==0:
        if i%2==0:
            c+=1
        m=m+1
if m==c:
    print("True")
else:
    print("False")