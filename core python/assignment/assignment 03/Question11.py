#11. Accept age of five people and also per person ticket amount and then calculate total
#amount to ticket to travel for all of them based on following condition :
#a. Children below 12 = 30% discount
#b. Senior citizen (above 59) = 50% discount
#c. Others need to pay full.

no = int(input("enter the no you want to get ticket for"))
toatal_amount= 0
while 1<=no:
    age1= int(input("enter the age of 1st person="))
    tkp1=float(input("enter the price of 1st person="))
    if age1<12:
        disco=tkp1*(30/100)
        print(f"pasenger get discount of rs{disco}")
        total_amount=total_amount+(tkp1-disco)
    elif age1>59:
        disco= tkp1*(50/100)
        print(f"pasenger get discount of rs {disco}")
        total_amount=total_amount+(tkp1-disco)
    else:
        total_amount=total_amount+tkp1
print(total_amount)            