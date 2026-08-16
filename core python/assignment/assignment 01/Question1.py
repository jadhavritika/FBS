#1. Write a program to calculate the percentage of student based on marks of any 5
#subjects.

Math = int(input('enter marks of Math subject:')) 
Science = int(input('enter marks of Science subject:')) 
History = int(input('enter marks of History subject:')) 
Marathi =int(input('enter the marks of Marathi subject:')) 
English = int(input('enter the marks of English subject:')) 

total = Math + Science + History + Marathi + English
percentage = (total/500)*100

print ("total marks is", total)
print ("percentage of student is :",(percentage))



