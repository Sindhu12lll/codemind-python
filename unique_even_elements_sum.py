n=int(input())
arr=list(map(int,input().split()))
j=set(arr)
count=0
for i in j:
    if i%2==0:
        count+=i
print(count)