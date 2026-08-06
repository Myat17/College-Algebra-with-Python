# Get strin input, which will include a decimal point
digits = input("Enter a decimal number to convert: ")

# Get number of decimal places as an integer
# len(digits) is counting the length of string.
# So, the decimal sign "." is also counted. That's why there is -1.
exponent = int(len(digits))-1

# Convert the input to a float number
n = float(digits)

# Use the exponent to get the number
numerator = int(n * 10**exponent)

# Use the exponent to get the denominator
denominator = 10**exponent

# percent is the first two decimal places
percent = n * 100

# output
print(f"The decimal is {n}.")
print(f"The fraction is {numerator} / {denominator}.")
print(f"The percent is {percent} %.")