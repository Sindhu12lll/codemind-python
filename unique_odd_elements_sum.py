n=int(input())
arr=list(map(int,input().split()))
s=set(arr)
count=0
for i in s:
    if(i%2!=0):
        count+=i
print(count)