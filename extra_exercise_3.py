# Proportions
"""
x/8 = 6/12
15/x = 3/7
x/25 = 16/20
4/9 = x/27
"""

print("=== Proporitons solver ===")
print()
print("n1 = first numerator")
print("d1 = first denomimator")
print("n2 = second numerator")
print("d2 = second denominator")

unknown = input("\nWhich value is unknown? Enter n1, d1, n2, or d2: ").lower()

if unknown == "n1":
    d1 = float(input("Enter first denomimator, d1: "))
    n2 = float(input("Enter second numerator, n2: "))
    d2 = float(input("Enter second denominator, d2: "))

    ans = n2*d1 / d2
    print(f"The answer is {ans:g}.")

elif unknown == "d1":
    n1 = float(input("Enter first numerator, n1: "))
    n2 = float(input("Enter second numerator, n2: "))
    d2 = float(input("Enter second denominator, d2: "))

    ans = n1*d2 / n2
    print(f"The answer is {ans:g}")

elif unknown == "n2":
    n1 = float(input("Enter first numerator, n1: "))
    d1 = float(input("Enter first denomimator, d1: "))
    d2 = float(input("Enter second denominator, d2: "))

    ans = n1*d2 / d1
    print(f"The answer is {ans:g}")

elif unknown == "d2":
    n1 = float(input("Enter first numerator, n1: "))
    d1 = float(input("Enter first denomimator, d1: "))
    n2 = float(input("Enter second numerator, n2: "))

    ans = n2*d1 / n1
    print(f"The answer is {ans:g}.")

else:
    print("Error: Please enter n1, d1, n2 or d2.")