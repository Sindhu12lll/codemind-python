a=input()
d=a.split()
b='aeiouAEIOU'
c=0
for i in d:
    if i[0] in b and i[len(i)-1] not in b:
        c+=1
print(c)