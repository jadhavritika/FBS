#1. to pass multiple values with meaning to function
#2. mention 2 asterisk symbols before parameter name in function definatiom
#3.passed data stored in dictionary format
#4. use for loop on dict.items() to get values and keys


def emp(**data):
    for key, val in data.items():
        print(key, ':', val)

emp(id = 101, age = 35, add = 'pune', sal = 50000, dept = 'Admin')