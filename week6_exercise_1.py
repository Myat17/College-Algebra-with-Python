# Finding square factors
import math

n = int(input("Enter an integer to find the greatest square factor: "))

max_factor = 1
upper_limit = math.floor(math.sqrt(n)) + 1

for maybe_factor in range(1, upper_limit):
    if n % (maybe_factor**2) == 0:
        max_factor = maybe_factor

print(f"The greatest square factor of {n} is {max_factor**2}")