import matplotlib.pyplot as plt
import numpy as np
import math

a = 1
b = 5
c = 6

print(f"y = {a}x**2 + {b}x + {c}")

# Vertex
vx = -b / (2 * a)
vy = a * (vx**2) + b * vx + c
print(f"Vertex: ('{vx}', '{vy}')")

xmin = -10
xmax = 10
ymin = -10
ymax = 10
points = 10 * (xmax - xmin)
x = np.linspace(xmin, xmax, points)

fig, ax = plt.subplots()
plt.axis([xmin, xmax, ymin, ymax])
plt.plot([xmin, xmax], [0, 0], 'k')
plt.plot([0, 0], [ymin, ymax], 'k')

# Graph the parabola
y1 = a*x**2 + b*x + c
plt.plot(x, y1)

# Point the vertex point
plt.plot([vx], [vy], 'ro')

# Find and plot the roots
d = b ** 2 - 4 * a * c
if d >= 0:
    root_1 = (-b + math.sqrt(d)) / (2 * a)
    root_2 = (-b - math.sqrt(d)) / (2 * a)
    plt.plot([root_1, root_2], [0, 0], 'go')
    print(f"Roots: x = {root_1} and x = {root_2}")

plt.show()