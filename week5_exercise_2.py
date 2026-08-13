# The number of people afflicted with the common cold in the winter months dropped steadily by 50 each year since 2004 until 2010
# In 2004, 875 people were inflicted

# When will no one be afflicted?

import matplotlib.pyplot as plt
import numpy as np
from sympy import symbols
from sympy.solvers import solve

x1 = 2004 # assume 2004 is a starting year
y1 = 875
x2 = 2005
y2 = y1 - 50

m= (y2 - y1) / (x2 - x1)
b = y1 - m * x1
print(f"y = {m}x + {b}")

xmin = 2004
xmax = 2024
ymin = 0
ymax = 1000

y3 = m * xmin + b
y4 = m * xmax + b

fig, ax = plt.subplots()
plt.axis([xmin, xmax, ymin, ymax])
plt.plot([xmin, xmax], [0, 0], 'k')
plt.plot([0, 0], [ymin, ymax], 'k')

ax.set_xlabel("Time")
ax.set_ylabel("cases")
ax.set_title("Number of people afflicted with common cold in the winter over time")
ax.grid(True)

ax.set_xticks(np.arange(xmin, xmax, 2))
ax.set_yticks(np.arange(ymin, ymax, 100))

# Plot the linear function on the graph as yellow line
plt.plot([xmin, xmax], [y3, y4], 'y')

plt.show()