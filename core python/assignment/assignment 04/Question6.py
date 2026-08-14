n = int(input("Enter a number: "))

count = 0

for i in range(2, n):
    if n % i == 0:
        count = count + 1

if n > 1 and count == 0:
    print("Prime Number")
else:
    print("Not a Prime Number")