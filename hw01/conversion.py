"""
Module for unit conversions including weight, temperature, length, and area.
"""

def pound_to_kilogram(number):
    """Convert pounds to kilograms."""
    print(f"{number} lbs is {number / 2.205:.2f} kg\n")
    return round(number / 2.205, 2)

def kilogram_to_pound(number):
    """Convert kilograms to pounds."""
    print(f"{number} kg is {number * 2.205:.2f} lbs\n")
    return round(number * 2.205, 2)

def fahrenheit_to_celsius(number):
    """Convert Fahrenheit to Celsius."""
    print(f"{number}°F is {(number - 32) * 5/9:.2f}°C\n")
    return round((number - 32) * 5/9, 2)

def celsius_to_fahrenheit(number):
    """Convert Celsius to Fahrenheit."""
    print(f"{number}°C is {(number * 9/5) + 32:.2f}°F\n")
    return round((number * 9/5) + 32, 2)

def feet_to_meters(number):
    """Convert feet to meters."""
    print(f"{number} ft is {number / 3.281:.2f} m\n")
    return round(number / 3.281, 2)

def meters_to_feet(number):
    """Convert meters to feet."""
    print(f"{number} m is {number * 3.281:.2f} ft\n")
    return round(number * 3.281, 2)

def acres_to_square_feet(number):
    """Convert acres to square feet."""
    print(f"{number} acres is {number * 43560:.2f} sqft\n")
    return round(number * 43560, 2)

def square_feet_to_acres(number):
    """Convert square feet to acres."""
    print(f"{number} sqft is {number / 43560:.6f} acres\n")
    return round(number / 43560, 6)

def what_function(user_input):
    """Determine and execute the correct conversion based on user input."""
    valid_units = {"lbs", "kg", "F", "C", "ft", "m", "ac", "sqft"}

    parts = user_input.split()
    if len(parts) != 2:
        print("Invalid input. Please enter in the format: 'number' 'unit'")

    number_str, unit = parts

    if unit not in valid_units:
        print("Invalid unit. Please use: lbs, kg, F, C, ft, m, ac, or sqft.")

    try:
        number = float(number_str)
    except ValueError:
        print("Invalid number")

    conversions = {
        "lbs": pound_to_kilogram,
        "kg": kilogram_to_pound,
        "F": fahrenheit_to_celsius,
        "C": celsius_to_fahrenheit,
        "ft": feet_to_meters,
        "m": meters_to_feet,
        "ac": acres_to_square_feet,
        "sqft": square_feet_to_acres
    }

    return conversions[unit](number)

def main():
    """Main function to take user input and call the appropriate conversion."""
    while True:
        user_input = input("Enter a number and unit or type 'e' to quit:\n").strip()
        if user_input.lower() == "e":
            break
        what_function(user_input)

if __name__ == "__main__":
    main()
