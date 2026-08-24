#9. Input 5 subject marks from user and display grade(eg.First class,Second class ..)


S1 = int(input("Enter marks of Subject 1: "))
S2 = int(input("Enter marks of Subject 2: "))
S3 = int(input("Enter marks of Subject 3: "))
S4 = int(input("Enter marks of Subject 4: "))
S5 = int(input("Enter marks of Subject 5: "))

percentage = (S1 + S2 + S3 + S4 + S5) / 5

print("Percentage =", percentage)

if percentage >= 75:
    print("First Class")
elif percentage >= 60:
    print("Second Class")
elif percentage >= 50:
    print("Pass Class")
else:
    print("Fail")

