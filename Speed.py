for t in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    sp=l[0]
    c=1
    for i in range(1,n):
        if l[i]<=sp:
            c+=1
            sp=l[i]
    print(c)