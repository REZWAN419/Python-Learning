

print("Hello World ! Welcome to Temperature Converter 🌡️\n")
print("1.Kelvin to Celcius") 
print("2.Celsius to Kelvin")
print("3.Celsius to Fahrenheit")
print("4.Fahrenheit to Celsius")
print("5.Fahrenheit to Kelvin")
print("6.Kelvin to Fahrenheit\n")

choice = float(input("Choose an option : "))

print("")

try:

    if choice == 1:
        K = float(input("Kelvin ? ")) 
        print(f"{K}° Kelvin = {K-273:.2f}° Celsius")
    elif choice == 2:
        C = float(input("Celsius ? "))
        print(f"{C}° Celsius = {C+273:.2f}° Kelvin")
    elif choice == 3:
        C = float(input("Celsius ? "))
        print(f"{C}° Celsius = {(C*9)/5+32:.2f}° Fahrenheit")
    elif choice == 4:
        F = float(input("Fahrenheit ? "))
        print(f"{F}° Fahrenheit = {((F-32)/9)*5:.2f}° Celsius") 
    elif choice == 5:
        F = float(input("Fahrenheit ? "))
        print(f"{F}° Fahrenheit = {((F-32)/9)*5+273:.2f}° Kelvin")  
    elif choice == 6:
        K = float(input("Kelvin ? "))
        print(f"{K}° Kelvin = {((K-273)/5)*9+32:.2f}° Fahrenheit")     
    else:
        print("❌ Invalid choice. Please select between 1 to 6.")

except ValueError:
    ("⚠️ Please enter numeric input only.")
