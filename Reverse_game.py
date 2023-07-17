def pal(n):
    rev=0
    temp=n
    while n:
        r=n%10
        rev=rev*10+r
        n=n//10
    return rev
n=int(input())
l=list(map(int,input().split()))
s=[]
for i in range(len(l)):
    s.append(pal(l[i]))
print(*s)