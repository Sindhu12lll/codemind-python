def pal(n):
    rev=0
    while n!=0:
        r=n%10
        rev=rev*10+r
        n=n//10
    return rev
a=int(input())
b=int(input())
for i in range(a,b):
    if i==pal(i):
        print(i,end=" ")