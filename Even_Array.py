s=int(input())
l=list(map(int,input().split()))
c=0
k=len(l)
for i in l:
    if i%2==0:
        c+=1
if c==k:
    print("True")
else:
    print("False")