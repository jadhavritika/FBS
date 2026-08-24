#2. Write a program to input any alphabet and check whether it is vowel or consonant.

ch = input("Enter an alphabet: ")

if ch in "aeiou":
    print("It is a Vowel")
else:
    print("It is a Consonant")