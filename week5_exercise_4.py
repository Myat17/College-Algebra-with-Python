# In 2004, school population was 1,700
# By 2012, the population had grown to 2500
# Assume the population is changing linearly
# Q1. How much did the population grow between 2004 and 2012?
# Q2. What is the average population growth per year?
# Q3. Find an equation for the population, P of the school t years after 2004
import matplotlib.pyplot as plt
import numpy as np

x1 = 0 # Assume 2004 is a starting year
y1 = 17 # 17 means 1,700
x2 = 8
y2 = 25

print(f"The population grow {(y2-y1)*100} between 2004 and 2012.")
print(f"The average population growth per year = {((y2 + y1)/x2)*100}")

# Setup the equation
m = (y2 - y1) / (x2 - x1)
b = y1 - m * x1
print(f"y = {m}x + {b}")

# For the graph
xmin = 0
xmax = 20
ymin = 0
ymax = 50

# Line on the graph
y3 = m * xmin + b
y4 = m * xmax + b

# Basic setup for the graph
fig, ax = plt.subplots()
plt.axis([xmin, xmax, ymin, ymax]) # window size
plt.plot([xmin, xmax], [0, 0], 'k')
plt.plot([0, 0], [ymin, ymax], 'k')

# Add details to the graph
ax.set_xlabel("Time")
ax.set_ylabel("Population")
ax.set_title("School population over time")
ax.grid(True)

ax.set_xticks(np.arange(xmin, xmax, 2))
ax.set_yticks(np.arange(ymin, ymax, 2))

plt.plot([xmin, xmax], [y3, y4], 'g')

plt.show()