def compound_interest(p,t,r):
    A = P(1+R/100)**t
    CI = A-P
P = int(input("enter the principle amount:"))
R = int(input("enter the interest rate:"))
T = int(input("enter the time period:"))
compound_interest(1000,12,2)