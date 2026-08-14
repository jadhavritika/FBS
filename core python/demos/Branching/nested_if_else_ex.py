num = int(input('enter number:'))
if(num <= 0):
    print("less than equal to zero.")
else:
    if(num <= 250):
        if (num <= 150):
            if (num <= 100):
                if(num <= 50):
                   
                   print("1 - 50") 
                else:
                    print("51 - 100")
            else:
                print("101 - 150")
        else:
            print("151 - 250")
    else:
        print("greater than 250")        


