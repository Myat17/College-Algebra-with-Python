# Proportion Calculator
# A car travels 180 km using 12 liters of fuel.
# Calculate how many liters of fuel are required for user's input distance

def fuel_efficiency(distance, fuel):
    return distance / fuel

def fuel_required(travel_distance):
    return travel_distance / fuel_efficiency(180, 12)

distance = float(input("Enter a distance to calculate required fuel: "))
required_fuel = fuel_required(distance)

print(f"Fuel efficiency: {fuel_efficiency(180, 12)} km/L")
print(f"To travel {distance} km, {required_fuel} liters of fuel is required.")