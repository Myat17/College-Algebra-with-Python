# Solving linear equations
"""
1. x + 7 = 15
2. 5x - 9 = 16
3. 3x + 8 = 2x + 19
4. 7(x-2) = 35
"""
from sympy import symbols, solve

x = symbols('x')
eq1 = x + 7 -15
eq2 = 5*x - 9 - 16
eq3 = 3*x + 8 - 2*x -19
eq4 = 7*(x-2) - 35

solution_1 = solve(eq1, x)
print(f"Solution_1 = {solution_1[0]}")

solution_2 = solve(eq2, x)
print(f"Solution_2 = {solution_2[0]}")

solution_3 = solve(eq3, x)
print(f"Solution_3 = {solution_3[0]}")

solution_4 = solve(eq4, x)
print(f"Solution_4 = {solution_4[0]}\n")

# To reduce repeated pattern
equations = [eq1, eq2, eq3, eq4]

# Normally, for equation in equations, we get the equation but we don't automatically get their numbers
# With enumerate() > number 0, equation 1 (default)
# With start=1, number 1, equation 1
for number, equation in enumerate(equations, start=1):
    solution = solve(equation, x)
    print(f"Solution{number} = {solution[0]}")