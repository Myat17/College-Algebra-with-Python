# Fraction
while True:
    digit = input("Enter a decimal number to convert or 'q' to quit: ")

    if digit.lower() == 'q':
        break

    try:
        n = float(digit)

        whole, decimal = digit.split(".")
        
        exponent = len(decimal)
        numerator = round(n * (10 ** exponent))
        denominator = 10 ** exponent

        percent = n * 100

    except (ValueError, IndexError):
        print("Enter only a decimal number or q")

    else:
        print(f"The decimal is {n}.")
        print(f"The fraction is {numerator} / {denominator}.")
        print(f"The percent is {percent:g}%.")