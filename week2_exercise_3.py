# Factoring
import sympy
from sympy import symbols
from sympy import *

var('x y')

# Equation set equal to zero, read to solve
eq = 2*x + 10*y + 4

# eq = x**3 - 2*x**2 - 5*x + 6

sympy.factor(eq)