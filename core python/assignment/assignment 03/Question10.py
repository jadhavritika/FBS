#10. Write a program to check if person is eligible to marry or not (male age >=21 and
#female age>=18)


gender = input ('enter gender(M/F):')
age = int(input('enter age:'))

if(gender == 'F'):
    if(age >= 18):
        print('girls is eligible for marriage.')
    else:
        print('pehle padhai kar le.')
else:
    if(age >= 21):
        print('boy is eligible for marriage.')
    else:
        print('pehle kama lo.')    