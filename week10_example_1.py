# Coefficient value
import math
a = 1
b = 5
c = 6

print(f"y = {a}x**2 + {b}x + {c}")

# Vertex
vx = -b / (2 * a)
vy = a * (vx**2) + b * vx + c
print(f"Vertex: ('{vx}', '{vy}')")

# roots
d = b ** 2 - 4 * a * c
if d >= 0:
    root_1 = (-b + math.sqrt(d)) / (2 * a)
    root_2 = (-b - math.sqrt(d)) / (2 * a)
    print(f"Roots: x = {root_1} and x = {root_2}")
else:
    print("No real roots")