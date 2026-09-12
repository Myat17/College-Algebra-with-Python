# Revision Lesson 04
# Functions and using two variables
import matplotlib.pyplot as plt
import numpy as np

# Dimension
xmin = -20
xmax = 20
ymin = -20
ymax = 20

points = 2 * (xmax - xmin)
x = np.linspace(xmin, xmax, points)

fig, ax = plt.subplots()

# Set the graph
plt.axis([xmin, xmax, ymin, ymax])
plt.plot([xmin, xmax], [0, 0], 'k')
plt.plot([0, 0], [ymin, ymax], 'k')

# Set the labels
ax.set_xlabel("x values")
ax.set_ylabel("y values")
ax.set_title("x vs y graph")
ax.grid(True)

ax.set_xticks(np.arange(xmin, xmax, 2))
ax.set_yticks(np.arange(ymin, ymax, 2))

# Plot two equations
y1 = 3 * x + 2
y2 = x**2 - 4

plt.plot(x, y1, 'g', label="3x + 2")
plt.plot(x, y2, 'r', label="x**2 - 4")
plt.plot([2], [8], 'yo', label="(2, 8)")
plt.legend()

plt.show()