# Factoring square roots
import math
import sympy

while True:
    n = input("Without the radical, enter a square root to factor or 'q' to quit: ")

    if n.lower() == 'q':
        break

    n = int(n)

    # Variables
    upper_limit = math.floor(math.sqrt(n)) + 1
    max_factor = 1

    # Find the greatest square factor
    for maybe_factor in range(1, upper_limit):
        if n % (maybe_factor ** 2) == 0:
            max_factor = maybe_factor ** 2

    # Divide out the greatest square factor
    other_factor = int(n / max_factor)
    max_factor = int(max_factor)
    square_root = int(math.sqrt(max_factor))
    output = square_root*sympy.sqrt(other_factor)
    print(f"The result of factoring square root of {n} is {output}.")