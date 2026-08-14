import random
userid = input("Enter User ID: ")
password = input("Enter Password: ")

if userid == "admin" and password == "1234":

    captcha = random.randint(1000, 9999)

    print("Your CAPTCHA is:", captcha)

    user_captcha = int(input("Enter CAPTCHA: "))

    if user_captcha == captcha:
        print("Login Successful")
    else:
        print("CAPTCHA Failed")

else:
    print("Invalid User ID or Password")