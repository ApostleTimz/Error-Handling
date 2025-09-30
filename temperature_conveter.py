# ===== TASK 3: Temperature Converter =====
# Create a custom TemperatureError exception
# The function should convert Celsius to Fahrenheit and raise TemperatureError if:
# - Temperature is below absolute zero (-273.15°C)
# - Temperature is above the surface of the sun (5500°C)
# If input is not a number, raise ValueError with message "Error: invalid temperature"
# Keep asking until a valid temperature is entered

print("=== Task 3: Temperature Converter ===")

print("Enter temperature in Celsius (must be between -273.15°C and 5500°C)\n")
class TemperatureError(Exception):
    pass
def convert_temperature(prompt):
 while True:
        try:
            temp_str = input(prompt)
            celsius = float(temp_str)
            if celsius < -273.15:
                raise TemperatureError("Error: temperature below absolute zero")
            if celsius > 5500:
                raise TemperatureError("Error: temperature above the surface of the sun")
            return celsius
        except ValueError:
            print("Error: invalid temperature")
        except TemperatureError as e:
            print(e)

celsius = convert_temperature("Enter temperature in Celsius: ")
fahrenheit = (float(celsius) * 9/5) + 32
print(f"{celsius}°C = {fahrenheit}°F")
print()




