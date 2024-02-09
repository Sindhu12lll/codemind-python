n=int(input())
sum=0
p=0
c=0
s=0
while n!=0:
    rem=n%10
    sum=sum+rem
    p+=rem**2
    n=n//10
s=p-sum
for i in range(1,s+1):
    if s%i==0:
        c+=1
if c>2:
    print("Not Prime")
else:
    print("Prime")
