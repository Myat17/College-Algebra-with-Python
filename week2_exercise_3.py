# Factoring
import sympy
from sympy import symbols
from sympy import *

x,y = symbols("x y")

# Equation set equal to zero, read to solve
# eq = x**2 - 4

eq = x**3 - 2*x**2 - 5*x + 6

print(sympy.factor(eq))