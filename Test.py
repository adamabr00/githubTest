def convert_length(value, from_unit, to_unit):
    length_units = {
        'mm': 0.001,
        'cm': 0.01,
        'm': 1,
        'km': 1000,
        'in': 0.0254,
        'ft': 0.3048,
        'yd': 0.9144,
        'mi': 1609.34
    }
    return value * (length_units[from_unit] / length_units[to_unit])


def convert_mass(value, from_unit, to_unit):
    mass_units = {
        'mg': 0.000001,
        'g': 0.001,
        'kg': 1,
        't': 1000,
        'oz': 0.0283495,
        'lb': 0.453592
    }
    return value * (mass_units[from_unit] / mass_units[to_unit])


def convert_volume(value, from_unit, to_unit):
    volume_units = {
        'ml': 0.001,
        'L': 1,
        'm^3': 1000,
        'fl oz': 0.0295735,
        'gal': 3.78541
    }
    return value * (volume_units[from_unit] / volume_units[to_unit])


def main():
    categories = {
        '1': 'Length',
        '2': 'Mass',
        '3': 'Volume'
    }

    print("Unit Conversion Application")
    print("Select Category:")
    for key, value in categories.items():
        print(f"{key}. {value}")
    category = input("Enter the number corresponding to the category: ")

    if category == '1':
        units = ['mm', 'cm', 'm', 'km', 'in', 'ft', 'yd', 'mi']
        convert_func = convert_length
    elif category == '2':
        units = ['mg', 'g', 'kg', 't', 'oz', 'lb']
        convert_func = convert_mass
    elif category == '3':
        units = ['ml', 'L', 'm^3', 'fl oz', 'gal']
        convert_func = convert_volume
    else:
        print("Invalid category. Exiting...")
        return

    print("Available units: ", ', '.join(units))
    from_unit = input("Enter the unit to convert from: ").lower()
    to_unit = input("Enter the unit to convert to: ").lower()

    if from_unit not in units or to_unit not in units:
        print("Invalid units. Exiting...")
        return

    value = float(input("Enter the value to convert: "))
    converted_value = convert_func(value, from_unit, to_unit)

    print(f"{value} {from_unit} is equal to {converted_value} {to_unit}")


if __name__ == "__main__":
    main()
