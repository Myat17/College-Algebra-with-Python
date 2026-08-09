# Quadratic and Cubic equations
# Use factor() and solve()
import sympy
from sympy import *

x = symbols('x')

# Request user input
equation = input("Enter an equation: ")

# Convert the user's input into a SymPy expression
equation = sympify(equation)

# Factoring the expression
factored_eq = sympy.factor(equation)

print(
    f'\nThe expression "{equation}" becomes'
    f'"{factored_eq}" after factoring.'
    )

# Set the equation to 0
eq = Eq(factored_eq, 0)

# Solve for x
solutions = solve(eq, x)

print("\nThe solutions are:")

for number, solution in enumerate(solutions, start=1):
    print(f"\tx{number} = {solution}")