def simple_interest(p,t,r):
    si = (p*t*r)/100
print("the principle amount", p)
print("the time period", t)
print("the interest rate", r)
print("the simple interest is", si)
p = int(input("Enter the principle amount:"))
t = int(input("Enter the time period:"))
r = int(input("Enter the interest rate:"))
simple_interest(p,t,r)