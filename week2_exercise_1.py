# Prompt for user to enter the equation and then solve
import sympy
from sympy import symbols
from sympy.solvers import solve

x = symbols("x")
eq = input("Enter equation: 0 = ")

# for multiple answers
solution = solve(eq, x)
for answer in solution:
    print(f"x = {answer}")