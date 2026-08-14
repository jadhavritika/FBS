basic = int(input("Enter basic salary:"))

da = basic * 10 / 100
ta = basic * 12 / 100
hra = basic * 15 / 100

total_salary = basic + da + ta + hra

print("DA is", da)
print("TA is", ta)
print("HRA is", hra)
print("Total Salary is", total_salary)