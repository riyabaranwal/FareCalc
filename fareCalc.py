
rates = {
    'Economy': 10,
    'Premium': 18,
    'SUV': 25
}


def calculate_fare(km, vehicletype, hour):
    if vehicletype not in rates:
        return None

    baserate = rates[vehicletype]
    totalfare = km * baserate


    if 17 <= hour <= 20:
        totalfare *= 1.5

    return totalfare



try:
    # User Inputs
    km = float(input("Enter distance (in km): "))
    vehicletype = input("Enter vehicle type (Economy / Premium / SUV): ") 
    hour = float(input("Enter hour of travel (0-23): "))

    fare = calculate_fare(km, vehicletype, hour)

    if fare is None:
        print("\n Service Not Available for selected vehicle type.")
    else:
        print("\n--- Ride Estimate Receipt ---")
        print(f"Distance Travelled : {km} km")
        print(f"Vehicle Type       : {vehicletype}")
        print(f"Base Rate (/km)    : ₹{rates[vehicletype]}")
        
        if 17 <= hour <= 20:
            print("Surge Applied      : Yes (1.5x)")
        else:
            print("Surge Applied      : No")
        
        print(f"Total Fare         : ₹{fare:.2f}")
        print("-------------------------")

except ValueError:
    print("\n Invalid input! Please enter correct numeric values.")