#4. Write a program to enter P, T, R and calculate simple Interest.

P = int(input('Enter amount of principle p :'))
R = int(input('Enter rate of interest R :'))
T = int(input('Enter time (year)T:'))

Si = (P * R * T)/100

print('simple interest is',Si)