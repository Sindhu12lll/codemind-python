t=int(input())
for i in range(t):
    n=int(input())
    p=1
    for j in range(0,n):
        f=n-j
        p=p*f
    print(p)
        