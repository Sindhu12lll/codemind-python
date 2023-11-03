def is_possible_to_split(arr):
    e=0
    o=0
    for i in arr:
        if i%2==0:
            e+=1
        else:
            o+=1
    if e%2==0 and o%2==0:
        return 1
    else:
        return 0
n=int(input())
arr=list(map(int,input().split()))
r=is_possible_to_split(arr)
print(r)