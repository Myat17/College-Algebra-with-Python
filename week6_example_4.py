# Factoring out square root
import math

# Number to factor
n = 12

# This variable will change
max_factor = 1

# The key ingredient
# math.floor rounds a number down to the nearest integer less than or equal to the input
upper_limit = math.floor(math.sqrt(n)) + 1

# Find square factors
for maybe_factor in range(1, upper_limit):
    if n % (maybe_factor**2) == 0:
        max_factor = maybe_factor

# Results so far
print(f"n = {n}")
print(f"Square rooted factor = {max_factor}")
print(f"Square factor = {max_factor**2}")
print(f"Integer = {n/(max_factor**2)}")