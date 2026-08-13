# Town's population
# In 2010, the population is 55,000

import matplotlib.pyplot as plt
import numpy as np

x1 = 0 # 2010 is a starting year
y1 = 55 # 55,000 / 1,000
# by 2012, the population had increased to 76,000
x2 = 2 # 2 years increased from 2010\
y2 = 76 # 76,000/ 1,000

# Find slope "m"
m = (y2 - y1) / (x2 - x1)

# Find y intercept "b"
b = y1 - m * x1

# The full equation
print(f"y = {m}x + {b}")

# for the graph
xmin = 0
xmax = 10
ymin = 0
ymax = 160

# for the line on the graph
y3 = m*xmin + b
y4 = m*xmax + b

# Basic setup for the graph
fix, ax = plt.subplots()
plt.axis([xmin, xmax, ymin, ymax])
plt.plot([xmin, xmax], [0,0], 'k')
plt.plot([0, 0], [ymin, ymax], 'k')

# Add details to the graph
ax.set_xlabel("time")
ax.set_ylabel("population")
ax.set_title("Population over time")
ax.grid(True)
ax.set_xticks(np.arange(xmin, xmax, 2))
ax.set_yticks(np.arange(ymin, ymax, 2))

# plot the linear function as a green line
plt.plot([xmin, xmax], [y3, y4], 'g')

plt.show()