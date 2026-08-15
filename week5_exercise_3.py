import matplotlib.pyplot as plt
import numpy as np

# the starting year, x0 = 1980
x1 = 5 # 5 years after 1980
y1 = 10 # 10 means 10 millions
x2 = 25 # 25 years after 1980
y2 = 4 # 4 means 4 millions

# Develop the equation
m = (y2 - y1) / (x2 - x1)
b = y1 - (m * x1)
print(f"y = {m}x + {b}")

# For the graph
xmin = 0
xmax = 50
ymin = 0
ymax = 15

# For the line on the graph
y3 = m*xmin + b
y4 = m*xmax + b

# Basic setup for the graph
fig, ax = plt.subplots()
plt.axis([xmin, xmax, ymin, ymax]) # Window size
plt.plot([xmin, xmax], [0,0], 'k') # Black x axis
plt.plot([0, 0], [ymin, ymax], 'k') # Black y axis

# Add details to the graph
ax.set_xlabel("Time")
ax.set_ylabel("Profit")
ax.set_title("Profit of a company over time")
ax.grid(True)

ax.set_xticks(np.arange(xmin, xmax, 2))
ax.set_yticks(np.arange(ymin, ymax, 1))

plt.plot([xmin, xmax], [y3, y4], 'r')

plt.show()

