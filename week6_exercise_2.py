# Dividing out factors
import math
import sympy
from sympy import symbols

n = int(input("Enter an integer to factor: "))
upper_limit = math.floor(math.sqrt(n)) + 1
square_root = 1
max_factor = 1
other_factor = 1

for maybe_factor in range(1, upper_limit):
    if n % (maybe_factor**2) == 0:
        max_factor = maybe_factor ** 2

other_factor = int(n / max_factor)
print(f"{n} = {max_factor} * {other_factor}")