# Reviewing Lesson05
# Slope and Intercept
# At wind speed of 2 m/s, lift force = 5 N
# At wind speed of 8 m/s, lift force = 17 N
import matplotlib.pyplot as plt
import numpy as np

x1 = 2
y1 = 5
x2 = 8
y2 = 17

m = (y2 - y1)/(x2 - x1)
b = y1 - m * x1

xmin = 0
xmax = 10
ymin = 0
ymax = 20

fig, ax = plt.subplots()

plt.axis([xmin, xmax, ymin, ymax])
plt.plot([xmin, xmax], [0, 0], 'k')
plt.plot([0, 0], [ymin, ymax], 'k')

ax.set_xlabel("Wind Speed (m/s)")
ax.set_ylabel("Lift force (N)")
ax.set_title("Lift Force over Wind Speed")

ax.set_xticks(np.arange(xmin, xmax, 1))
ax.set_yticks(np.arange(ymin, ymax, 2))

y3 = m * xmin + b
y4 = m * xmax + b
plt.plot([xmin, xmax], [y3, y4], 'g', label="y = mx + b")
plt.plot([x1, x2], [y1, y2], 'ro', label="Data Points")
plt.legend()
plt.show()