import sympy
from sympy import *
x = symbols('x')

print("==== Algebra Helper ====")

while True:
    
    user_choice = input(
        "\nChoose one:'solve_x', 'factor', 'solve_pro'\n"
        "or enter 'q' to quit : "
        ).lower()

    if user_choice == 'q':
        print("Existing the program...\n")
        break

    # Solving for x
    if user_choice == "solve_x":
        equation = input("\nEnter an equation to solve: 0 = ")
        equation = sympify(equation)

        eq = Eq(equation, 0)
        solutions = solve(eq, x)

        print("\nThe solutions are:")
        for number, solution in enumerate(solutions, start=1):
            print(f"x{number} = {solution}")

    # Factoring user's input expression
    elif user_choice == "factor":
        equation = input("\nEnter an expression to factor: ")
        equation = sympify(equation)

        factored_equation = factor(equation)

        print(f"\n{equation} = {factored_equation}")

    # Solving proportions
    elif user_choice == "solve_pro":
        print(
            "\nn1 = first numerator\n"
            "d1 = first denominator\n"
            "n2 = second numerator\n"
            "d2 = second denominator"
            )
        
        unknown = input("\nWhich value is unknown? n1, d1, n2, d2: ").lower()

        if unknown == "n1":
             
            d1 = float(input("Enter first denominator, d1: "))
            n2 = float(input("Enter second numerator, n2: "))
            d2 = float(input("Enter second denominator, d2: "))
            
            ans = n2 * d1 / d2
            print(f"The answer is {ans:g}.")

        elif unknown == "d1":

            n1 = float(input("Enter first numerator, n1: "))
            n2 = float(input("Enter second numerator, n2: "))
            d2 = float(input("Enter second denominator, d2: "))

            ans = n1 * d2 / n2
            print(f"The answer is {ans:g}.")

        elif unknown == "n2":

            n1 = float(input("Enter first numerator, n1: "))
            d1 = float(input("Enter first denomimator, d1: "))
            d2 = float(input("Enter second denominator, d2: "))

            ans = n1 * d2 / d1
            print(f"The answer is {ans:g}.")

        elif unknown == "d2":

            n1 = float(input("Enter first numerator, n1: "))
            d1 = float(input("Enter first denomimator, d1: "))
            n2 = float(input("Enter second numerator, n2: "))

            ans = n2 * d1 / n1
            print(f"The answer is {ans:g}.")

        else:
            print("Error: Please enter n1, d1, n2 or d2.")

    else:
        print("Error: choose one of the calculations.")