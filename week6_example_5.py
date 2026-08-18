# Using sympy for factoring
import math
import sympy
from sympy import symbols

n = 24

# Variables
upper_limit = math.floor(math.sqrt(n)) + 1
max_factor = 1
other_factor = 1
square_root = 1

# Different variable strategy
for maybe_factor in range(1, upper_limit):
    if n % (maybe_factor**2) == 0:
        max_factor = maybe_factor ** 2

# Divide out the greatest square factor
other_factor = n / max_factor

# Output variables
square_root = int(math.sqrt(max_factor))
other_factor = int(other_factor)
output = square_root * sympy.sqrt(other_factor)

print(output)