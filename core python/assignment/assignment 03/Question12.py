#12. Write a program to check if given 3 digit number is a palindrome or not.

num = int(input("Enter a 3 digit number: "))

a = num // 100
b = (num // 10) % 10
c = num % 10

if a == c:
        print("Number is Palindrome")
else:
        print("Number is Not Palindrome")
