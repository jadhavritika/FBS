#without passing parameter
#with returning value

def addition():
    num1 = int(input('enter number 1:'))
    num2 = int(input('enter number 2:'))

    add = num1 + num2

    return add

res = addition()
print(res)