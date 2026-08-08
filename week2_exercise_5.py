# Solving for a variable
from sympy import *

# Identify all variables
a,b,c,x = symbols('a b c x')

# Identify left and right side of the equal sign
left = a*x**2 + b*x + c
right = 0

# Variable to solve for 
variable = x

# Sympy equation left and right
eq = Eq(left, right)

# Sympy solve for that variable
solutions = solve(eq, variable)

# Show factored results
for solution in solutions:
    print(f"{variable} = {solution}")