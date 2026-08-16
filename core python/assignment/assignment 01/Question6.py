#6. Write a Program to input two angles from user and find third angle of the
#triangle.

a = int(input('enter angle 1:'))
b = int (input(' enter angle 2:'))

c = 180 - (a + b)

print('third angle of triangle is :', c)
