# Reduce fractions to lowest terms
numerator = 12
denominator = 24
factor = 1

# Find greatest common factor
for test_factor in range(1, denominator+1):
    if numerator%test_factor == 0 and denominator%test_factor == 0:
        factor = test_factor
print(f"Common factor: {factor}")

# Divide out greatest common factor
n = int(numerator/factor)
d = int(denominator/factor)

print(f"Original: {numerator} / {denominator}")
print(f"reduced: {n} / {d}")