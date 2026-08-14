P = int(input('Enter amount of principle P :'))
R = int(input('Enter rate of interest R :'))
T = int(input('Enter time (year)1:'))

amount = P*(1 + R / 100) **T
CI = amount - P

print("compound Interest is", CI)