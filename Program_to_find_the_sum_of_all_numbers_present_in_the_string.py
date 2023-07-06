s=input()
c=0
for i in s:
    if i.isdigit():
        k=int(i)
        c=c+k
print(c)