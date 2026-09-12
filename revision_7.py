# Review Lesson 06
# Factoring and Square Factors
import math
import sympy

integer = int(input("Enter an integer: "))

upper_limit = math.floor(math.sqrt(integer)) + 1
max_factor = 1

print("Factors:")
for test_factor in range(1, integer + 1):
    if integer % test_factor == 0:
        print(test_factor)

for maybe_factor in range(1, integer):
    if integer % (maybe_factor**2) == 0:
        max_factor = maybe_factor**2
print(f"\nGreatest square factor: {max_factor}")

other_factor = int(integer / max_factor)
square_root = int(math.sqrt(max_factor))
factor = square_root * sympy.sqrt(other_factor)
print(f"\nThe square factor of {integer} is {factor}.")