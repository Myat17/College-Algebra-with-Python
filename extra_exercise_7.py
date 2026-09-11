def adding(num1, num2):
    return num1 + num2

def subtracting(num1, num2):
    return num1 - num2

def multiplying(num1, num2):
    return num1 * num2

def dividing(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        print("The denominator cannot be 0.")

def prime_num(num1):
    if num1 < 2:
        return False

    for i in range(2, num1):
        if num1 % i == 0:
            return False
        
    return True

def prime_factor(num1):
    print(f"Prime factors of {num1} are:")

    for num in range(2, num1 + 1):
        if num1 % num == 0 and prime_num(num):
            print(f'\t {num}')

def sqrt_root(num1):
    import sympy
    import math

    if num1 <= 0:
        print("Enter a positive number.")
        return

    upperlimit = math.floor(math.sqrt(num1)) + 1
    max_factor = 1

    for maybe_factor in range(1, upperlimit):
        if num1 % (maybe_factor**2) == 0:
            max_factor = maybe_factor ** 2

    other_factor = int(num1 / max_factor)
    max_factor = int(max_factor)
    square_root = int(math.sqrt(max_factor))
    output = square_root*sympy.sqrt(other_factor)
    print(f"The simplified square root of {num1} is {output}.")

def solve_var(eq1):

    from sympy import symbols, sympify, solve

    x = symbols('x')

    eq = sympify(eq1)
    
    solution = solve(eq, x)

    print("The solutions are: ")
    for num in solution:
        print(f"\t{num}")

num_1 = float(input('Enter a number: '))
num_2 = float(input("Enter a number: "))
print(f"{num_1} + {num_2} = {adding(num_1, num_2)}")
print(f"{num_1} - {num_2} = {subtracting(num_1, num_2)}")
print(f"{num_1} * {num_2} = {multiplying(num_1, num_2)}")
print(f"{num_1} / {num_2} = {dividing(num_1, num_2)}")

num_3 = int(input("Enter a number to find its prime factor: "))
prime_factor(num_3)

num_4 = int(input("Enter a number to find square root: "))
sqrt_root(num_4)

equation = input("Enter an equation to find the variable, 0 = ")
solve_var(equation)