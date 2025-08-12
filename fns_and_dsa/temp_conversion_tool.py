# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    """
    Converts a temperature from Fahrenheit to Celsius.
    """
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """
    Converts a temperature from Celsius to Fahrenheit.
    """
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit



if __name__ == "__main__":
    try:
        temp_input = input("Enter the temperature to convert: ")
        temp_value = float(temp_input)

        unit_input = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit_input == 'C':
            converted_temp = convert_to_fahrenheit(temp_value)
            print(f"{temp_value}°C is {converted_temp}°F")
        elif unit_input == 'F':
            converted_temp = convert_to_celsius(temp_value)
            print(f"{temp_value}°F is {converted_temp}°C")
        else:
            print("Invalid unit. Please enter 'C' or 'F'.")
            
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")