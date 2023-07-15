n=int(input())
a=0
b=1
for i in range(n):
    s=a+b
    a=b
    b=s
    if n==s:
        print("True")
        break
else:
    print("False")