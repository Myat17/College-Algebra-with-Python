# Solving a system of linear equations
from sympy import *
from sympy.plotting import plot

x,y = var('x y')

# First equation set equal to zero, ready to solve
first = -2 * x + y - 2

# Second equation set equal to zero, ready to solve
second = 2 * x - 2 * y + 8

# Solve
solution = linsolve([first, second], (x, y))
x_solution = solution.args[0] [0]
y_solution = solution.args[0] [1]
print(f"({x_solution}, {y_solution})")

# Sympy syntax for equation equal to zero, ready to factor
y_first = Eq(first, 0)

# Sympy solve for y
y1 = solve(y_first, y)

# Same two steps for second equation
y_second = Eq(second, 0)
y2 = solve(y_second, y)

# Show factored results
print("y = ", y1[0])
print("y = ", y2[0])

# Plot solution
x = symbols('x')
plot(y1[0], y2[0], (x, -10, 10))