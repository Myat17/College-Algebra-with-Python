# Fractions
from sympy import symbols, solve

"""x/4 = 9
3x/5 = 18
(x+4)/3 = 10"""

x = symbols('x')

eq5 = x / 4 -9
eq6 = 3*x / 5 - 18
eq7 = (x+4)/3 - 10

equations = [eq5, eq6, eq7]

for number, equation in enumerate(equations, start=5):
    solution = solve(equation, x)
    print(f"Solution_{number} = {solution[0]}")