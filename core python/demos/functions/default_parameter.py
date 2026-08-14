#1. to make parameter optional 
#2. parameter - default (assigning value to parameter in function defination)
#3.if we pass value to default parameter, it takes passed value
   #if we dont pass value to default parameter, it takes default value
#4.flow of default parameter from right to left
#5.flow of positional parameter is left to right
 

def emp(id, name ='', sal = 0, dept = 'backoffice'):
    print('ID:', id)
    print('NAME:', name)
    print('sal:', sal)
    print('DEPARTMENT:', dept)

emp(101, 'ABC', 50000, 'IT')
print('################')
emp(102, 'XYZ', 10000)   