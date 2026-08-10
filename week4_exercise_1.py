# Using an array as inputs
# numpy is used for numerical calculations and arrays.
import matplotlib.pyplot as plt
import numpy as np

# Define the graph boundaries
xmin = -10
xmax = 10
ymin = -10
ymax = 10

# Define how many x-points to create
points = 2 * (xmax - xmin)

# Create the x array
# linspace generates an array of evenly spaced numbers between starting value and ending value
x = np.linspace(xmin, xmax, points) # linspace(start, stop, number_of_points)

# Create a figure and axes
# Fig > overall figure, ax > plotting area, plt.subplot() > plotting environment
fig, ax = plt.subplots()

# Set the graph window
plt.axis([xmin, xmax, ymin, ymax]) # window size
plt.plot([xmin, xmax], [0, 0], 'b') # blue x axis
plt.plot([0, 0], [ymin, ymax], 'b') # blue y axis

# Setting labels
ax.set_xlabel("x values")
ax.set_ylabel("y values")
ax.set_title("Functions")
ax.grid(True)

# arrange tick mark every 2 numbers in x and y direction
ax.set_xticks(np.arange(xmin, xmax, 1))
ax.set_yticks(np.arange(ymin, ymax, 1))

y1 = x**2 + 1
y2 = x**3 + 2*x +1
plt.plot(x, y1, 'g', label='y=x^2+1') 
plt.plot([4], [6], 'ro', label="(4,6)")
plt.plot(x, y2, 'k', label="y = x^3+2x+1")
plt.legend()

plt.show()