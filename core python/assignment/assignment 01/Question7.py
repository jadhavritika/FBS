#7. Program to Find the Roots of a Quadratic Equation

a = int(input('enter the value of a:'))
b= int (input('enter the value of b:'))
c= int (input('enter the value of c:'))

d = (b * b) - (4 * a * c) 

root1 = (-b + 0.5**(d)) / (2 * a)
root2 = (-b - 0.5**(d)) / (2 * a)

print("first root is", root1)
print("second root is", root2)