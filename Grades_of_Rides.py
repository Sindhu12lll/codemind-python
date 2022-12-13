p,q,r=map(int,input().split())
if(p>50 and q>60 and r>100):
    print('10')
elif(p>50 and q>60):
    print('9')
elif(q>60 and r>100):
    print('8')
elif(p>50 and r>100):
    print('7')
elif(p>50 or q>60 or r>100):
    print('6')
else:
    print('5')