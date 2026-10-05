# Jessica is walking home from a friend's house.
# After 2 mins, she is 1.4 miles from home.
# 12 mins after leaving, she is 0.9 miles from home.
# What is her rate in miles per hour?
import matplotlib.pyplot as plt
import numpy as np

x1 = 2/60
y1 = 1.4
x2 = 12/60
y2 = 0.9

# Develop the equation y = mx + b
m = (y2 - y1) / (x2 - x1)
b = y1 - m * x1
print(f"y = {m}x + {b}")

# for the graph
xmin = 0
xmax = 2
ymin = 0
ymax = 2

# For the line on the graph
y3 = m*xmin + b
y4 = m*xmax + b

# Basic setup for the graph
fig, ax = plt.subplots()
plt.axis([xmin, xmax, ymin, ymax])
plt.plot([xmin, xmax], [0, 0], 'k')
plt.plot([0, 0], [ymin, ymax], 'k')

# Add details to the graph
ax.set_xlabel("Time")
ax.set_ylabel("Distance from home")
ax.grid(True)

# Plot the linear function as a red line
plt.plot([xmin, xmax], [y3, y4], 'r')

plt.show()