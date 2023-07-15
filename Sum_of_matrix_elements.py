a=int(input())
b=int(input())
c=[list(map(int,input().split()))for i in range(a)] 
sum=0
for i in range(0,a):
    for j in range(0,b):
        sum=sum+c[i][j]
print(sum)