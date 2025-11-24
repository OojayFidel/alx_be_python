# 1. Define Global Conversion Factors
# Instruction: Define two global variables at the top of the script
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

# 2. Implement Conversion Functions
def convert_to_celsius(fahrenheit):
    """
    Takes a temperature in Fahrenheit and returns Celsius.
    Uses the global FAHRENHEIT_TO_CELSIUS_FACTOR.
    Formula: (F - 32) * 5/9
    """
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """
    Takes a temperature in Celsius and returns Fahrenheit.
    Uses the global CELSIUS_TO_FAHRENHEIT_FACTOR.
    Formula: (C * 9/5) + 32
    """
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# 3. User Interaction
def main():
    try:
        # Instruction: Prompt the user to enter a temperature
        # We capture this as a string first, then try to convert to float
        temp_input = input("Enter the temperature: ")
        temperature = float(temp_input)

        # Instruction: Specify whether it's in Celsius or Fahrenheit
        unit = input("Is this Celsius or Fahrenheit? (Enter C or F): ").strip().upper()

        # Instruction: Based on input, call the appropriate function
        if unit == "C":
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is equal to {converted_temp:.2f}°F")
            
        elif unit == "F":
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature}°F is equal to {converted_temp:.2f}°C")
            
        else:
            print("Please enter a valid unit (C or F).")

    except ValueError:
        # Instruction: If the user entered a wrong input, print this EXACT error message
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()