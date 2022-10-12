def interest(p,t,r):
    si=(p*t*r)//100
    return si
p,t,r=map(int,input().split())
result=interest(p,t,r)
print(result)