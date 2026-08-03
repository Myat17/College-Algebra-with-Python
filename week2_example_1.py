import sympy
from sympy import symbols
from sympy.solvers import solve

# This creates a symbolic variable named x.
# Or Treat x as the mathematical variable x.
x = symbols('x')

# Put the equation here
# eq = x - 2 is the same with x - 2 = 0
eq = 2*x - 4

# This solves the equation eq = 0 for the variable x
# x - 2 = 0
# x - 2 + 2 = 0 + 2
# x = 2
print(f"x= {solve(eq,x)}")
# solve() will always return a list