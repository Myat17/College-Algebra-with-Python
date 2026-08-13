# Slope
import matplotlib.pyplot as plt
x1 = 2
y1 = 3
x2 = 6
y2 = 8

# The slope is "m"
m = (y2 - y1) / (x2 - x1)

# The y intercept is "b"
b = y1 - m * x1

# The full equation
print(f"y = {m}x + {b}")

# For the graph
xmin = -10
xmax = 10
ymin = -10
ymax = 10

# For the line on the graph
y3 = m * xmin + b
y4 = m * xmax + b

# Basic setup for the graph
fix, ax = plt.subplots()
plt.axis([xmin, xmax, ymin, ymax])
plt.plot([xmin, xmax], [0, 0], 'b')
plt.plot([0, 0], [ymin, ymax], 'b')

# Plot the linear function as a red line
plt.plot([xmin, xmax], [y3, y4], 'r')

plt.show()