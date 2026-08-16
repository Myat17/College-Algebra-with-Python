# Decimal to fraction code
digits = input("Enter a decimal number: ")

# Convert to fraction
exponent = int(len(digits)) - 1
n = float(digits)
numerator = int(n * 10 ** exponent)
denominator = 10 ** exponent

# reduce the fraction
factor = 1
for test_factor in range(1, denominator+1):
    if numerator%test_factor == 0 and denominator%test_factor == 0:
        factor = test_factor
print(f"Common factor: {factor}")

# Divide out greatest common factor
# Divide out greatest common factor
num = int(numerator/factor)
den = int(denominator/factor)

# Output
print(f"The decimal is {n}")
print(f"Fraction: {num} / {den}")