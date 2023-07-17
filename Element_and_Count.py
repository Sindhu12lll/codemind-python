n=int(input())
l=list(map(int,input().split()))
s=[]
for i in l:
    m=l.count(i)
    if i not in s:
        s.append(i)
        if i in s:
            print(i,m,end=" ")