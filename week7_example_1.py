import matplotlib.pyplot as plt
import numpy as np

xmin = -10
xmax = 10
ymin = -10
ymax = 10

# Define how many points to plot
points = 10 * (xmax - xmin) # bigger multiple number, smoother the curve

# Define the array of x values once
x = np.linspace(xmin, xmax, points)

fig, ax = plt.subplots()
plt.axis([xmin, xmax, ymin, ymax])
plt.plot([xmin, xmax], [0, 0], 'k')
plt.plot([0, 0], [ymin, ymax], 'k')

# line 1
y1 = -3 * x
plt.plot(x, y1)

# line 2
y2 = x ** 3
plt.plot(x, y2)

plt.show()