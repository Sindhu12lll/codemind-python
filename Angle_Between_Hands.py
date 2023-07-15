a,b=map(int,input().split(':'))
ang=abs(30*a-(11/2)*b)
if ang>180:
    print(360-ang)
else:
    print(ang)