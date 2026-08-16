# Using the modulus (%) in a loop to find factors
number = 12

# Find all factors
for test_factor in range(1, number+1):
    if number%test_factor == 0:
        print(test_factor)