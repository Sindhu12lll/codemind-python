def compound_interest(principle, rate, time):
    Amount = principle*(pow((1 +(rate/100)),time))
    CI = Amount-principle
    return Amount
principle,rate,time=map(int,input().split())
comp=compound_interest(principle, rate, time)
print("%.2f" %comp)
