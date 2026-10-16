# 1st to 3rd base line > $20 per ticket
# others down the baseline and outfield > $10 per ticket
# 5332 fans in attendance
# $71,750 total ticket revenue
# How many tickets in each zone were sold?
from sympy import *
from sympy.plotting import plot
from sympy import sqrt

var("x y")

# first equation set equal to zero ready to solve
first = 20 * x + 10 * y - 71750

# second equation set equal to zero ready to solve
second = x + y - 5332

# Solve - can be linear or non linear equations
solutions = nonlinsolve([first, second], (x, y))
for a in range(len(solutions.args)):
    x_solution = solutions.args[a][0]
    y_solution = solutions.args[a][1]
    print(f"Solution = ({x_solution}, {y_solution})")

# Sympy syntax for equation equal to zero, ready to solve
y_first = Eq(first, 0)
y_second = Eq(second, 0)

# Sympy solve for y
y1 = solve(y_first, y)
y2 = solve(y_second, y)

# Show factored results
print(f"y = {y1[0]}")
print(f"y = {y2[0]}")

# Plot solution
x = symbols('x')
xmin = -10
xmax = 10
plot(y1[0], y2[0], (x, xmin, xmax))