# Review Lesson 01
# Proportions and Conversions
# Wind tunnel scale converter
scale_factor = 20
model_length = float(input("Enter model length or enter 0 if unknown: "))
full_length = float(input("Enter full length or enter 0 if unknown: "))

if model_length == 0.0:
    model_scale = full_length / scale_factor
    print(f"\nModel length = {model_scale} m")
elif full_length == 0.0:
    full_scale = model_length * scale_factor
    print(f"\nFull scale length = {full_scale} m")
elif model_length == 0.0 and full_length == 0.0:
    print("\nError: Both values cannot be unknown")
else:
    print("\nError: Enter 0 for exactly one unknown value")