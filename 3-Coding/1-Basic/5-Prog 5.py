#Python Program for compound interest
#A = P(1 + R/100)**t

p=int(input("Enter principle amount"))
t=int(input("Enter time"))
r=float(input("Enter rate"))

amount=(p*(1+(r/100))**t)

print("Compound interest is ",amount)