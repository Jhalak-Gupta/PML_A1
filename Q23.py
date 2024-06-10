conv=input("Enter '1' to convert from Celsius to Fahrenheit, or '2' to convert from Fahrenheit to Celsius: ")
if conv=='1':
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print("Temperature in Fahrenheit:", fahrenheit)
elif conv=='2':
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print("Temperature in Celsius:", celsius)
else:
    print("Invalid input. Please enter '1' or '2' for conversion.")
