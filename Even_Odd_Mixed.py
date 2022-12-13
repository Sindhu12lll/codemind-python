n=int(input())
ec=0
od_c=0
while n>0:
    r=n%10
    if(r%2==0):
        ec+=1
    else:
        od_c+=1
    n=n//10
if(ec==0):
    print("Odd")
elif(od_c==0):
    print("Even")
else:
    print("Mixed")