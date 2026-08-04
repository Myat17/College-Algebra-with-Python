# Money exchange converters

exchange_rate = float(input("Enter exchange rate (1 USD to THB): "))
usd_amount = float(input("Enter USD amount (enter 0 if unkown): "))
thb_amount = float(input("Enter THB amount (enter 0 if unknown): "))

# Put a zero in for unknown value
if usd_amount == 0 and thb_amount > 0:
    usd_amount = thb_amount / exchange_rate
    print(f"{thb_amount:.2f} THB = {usd_amount:.2f} USD")

elif thb_amount == 0 and usd_amount > 0:
    thb_amount = usd_amount * exchange_rate
    print(f"{usd_amount:.2f} USD = {thb_amount:.2f} THB")
else:
    print("Error: Enter 0 for exactly one amount.")