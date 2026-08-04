# solving in other ways
from sympy import var, Eq, solve, symbols

# This creates two symbolic variables
# var('x y')
x, y = symbols('x y')

# First equation set equal to zero, ready to solve
first_eq = 2*x - y

# Sympy syntax for equation equal to zero, ready to factor
# Eq means create a mathematical equation
# So 2*x-y becomes 2*x-y = 0
eq1 = Eq(first_eq, 0)

# Sympy solve for x
sol = solve(eq1, x)

# Show factored results
print(f"x = {sol[0]}")