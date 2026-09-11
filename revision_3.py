# Review Lesson02
# Equation solver
from sympy import symbols, solve
x = symbols('x')
equation = input("Enter an equation to solve, 0 = ")
solutions = solve(equation, x)
for number, solution in enumerate(solutions, start=1):
    print(f"x{number} = {solution}")

