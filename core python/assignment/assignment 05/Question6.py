#6. Write a program to print first n prime numbers.

n = int(input("Enter how many prime numbers: "))

count = 0
num = 2

while count < n:

    divisor = 0

    for i in range(1, num + 1):

        if num % i == 0:
            divisor = divisor + 1

    if divisor == 2:
        print(num)
        count = count + 1

    num = num + 1