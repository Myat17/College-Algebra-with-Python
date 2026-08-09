# Graphing functions
import matplotlib.pyplot as plt

xmin = -10
xmax = 10
ymin = -10
ymax = 10

fig, ax = plt.subplots()

# Dimensions
plt.axis([xmin, xmax, ymin, ymax]) # window size
plt.plot([xmin, xmax], [0, 0], 'b') # blue x axis
plt.plot([0, 0], [ymin, ymax], 'b') # blue y axis

# Plot one point
# plt.plot([5], [4], 'ro') # x = 5 and y = 4

# Graphing and table (x,y)
# Plot serveral points
print("x \t y")
for x in range(xmin, xmax+1):
    y = 0.5*x + 1
    plt.plot([x], [y], 'ro')
    print(x, "\t", y)

plt.show()