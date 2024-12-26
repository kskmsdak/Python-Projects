def convert_length(value, from_unit, to_unit):
    length_conversions = {
        "millimeter": 0.001,
        "centimeter": 0.01,
        "meter": 1,
        "kilometer": 1000,
        "inch": 0.0254,
        "foot": 0.3048,
        "yard": 0.9144,
        "mile": 1609.34,
    }
    meters = value * length_conversions[from_unit]
    return meters / length_conversions[to_unit]

def convert_weight(value, from_unit, to_unit):
    weight_conversions = {
        "milligram": 0.001,
        "gram": 1,
        "kilogram": 1000,
        "ounce": 28.3495,
        "pound": 453.592,
    }
    grams = value * weight_conversions[from_unit]
    return grams / weight_conversions[to_unit]

def convert_temperature(value, from_unit, to_unit):
    if from_unit == "Celsius":
        if to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        if to_unit == "Kelvin":
            return value + 273.15
    elif from_unit == "Fahrenheit":
        if to_unit == "Celsius":
            return (value - 32) * 5/9
        if to_unit == "Kelvin":
            return (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin":
        if to_unit == "Celsius":
            return value - 273.15
        if to_unit == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32
    return value  # If conversion is not needed

def main():
    print("Welcome to the Unit Converter!")
    print("Select the type of measurement:")
    print("1. Length")
    print("2. Weight")
    print("3. Temperature")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        print("Length Units: millimeter, centimeter, meter, kilometer, inch, foot, yard, mile")
        from_unit = input("Enter the unit to convert from: ")
        to_unit = input("Enter the unit to convert to: ")
    elif choice == "2":
        print("Weight Units: milligram, gram, kilogram, ounce, pound")
        from_unit = input("Enter the unit to convert from: ")
        to_unit = input("Enter the unit to convert to: ")
    elif choice == "3":
        print("Temperature Units: Celsius, Fahrenheit, Kelvin")
        from_unit = input("Enter the unit to convert from: ")
        to_unit = input("Enter the unit to convert to: ")
    else:
        print("Invalid choice!")
        return

    value = float(input("Enter the value to convert: "))
    converted_value = None

    if choice == "1":
        converted_value = convert_length(value, from_unit, to_unit)
    elif choice == "2":
        converted_value = convert_weight(value, from_unit, to_unit)
    elif choice == "3":
        converted_value = convert_temperature(value, from_unit, to_unit)

    if converted_value is not None:
        print(f"{value} {from_unit} is equal to {converted_value} {to_unit}")
    else:
        print("Conversion not supported.")

if __name__ == "__main__":
    main()