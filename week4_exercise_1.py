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

y = 2*x + 1
plt.plot(x, y, 'r')

plt.show()