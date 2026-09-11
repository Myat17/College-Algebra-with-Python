# Review Lesson03
# Decimal, fraction and percent
while True:
    digit = input("Enter a decimal number or 'q' to quit: ")

    if digit.lower() == 'q':
        break

    try:
        whole, decimal = digit.split(".")

        exponent = len(decimal)
        n = float(digit)
    
        numerator = int(n * 10**exponent)
        denominator = 10 ** exponent
        percent = n * 100
    except ValueError:
        print("Enter only a decimal number or 'q'.")
    else:
        print(f"Decimal: {n}")
        print(f"Fraction: {numerator} / {denominator}")
        print(f"Percent: {percent}%")