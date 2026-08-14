feet = int(input("Enter feet: "))
inches = int(input("Enter inches: "))

total_inches = (feet * 12) + inches
cm = total_inches * 2.54
meter = cm / 100

print("Meters is", meter)
print("Centimeters is", cm)