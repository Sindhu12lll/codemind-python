for t in range(int(input())):
    a,b=map(int,input().split())
    l1=list(map(int,input().split()))
    l2=list(map(int,input().split()))
    s=l1+l2
    s.sort()
    print(*s)