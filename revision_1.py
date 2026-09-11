# Revision for Lesson01
# Proportions, ratios and conversions
# Conversion of km to miles
km_mile = 0.62137119
def km_to_mile(distance):
    return distance * km_mile

def mile_to_km(distance):
    return distance / km_mile

number = float(input("Enter number to convert from km to mile: "))
result = km_to_mile(number)
print(f"{number} km  = {result:.2f} mile")

number2 = float(input("Enter number to convert from mile to km: "))
result2 = mile_to_km(number2)
print(f"{number2} mile  = {result2:.2f} km")