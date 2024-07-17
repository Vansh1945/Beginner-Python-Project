def kg_to_gram(kg):
    return kg * 1000

def mtr_to_cm(mtr):
    return mtr * 100

def foot_to_inch(ft):
    return ft * 12

def km_to_mtr(km):
    return km * 1000

def hr_to_mint(hr):
    return hr * 60

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def converter_calculator():
    print("Select converter operation:")
    print("1. Kilogram to Gram")
    print("2. Meter to Centimeter")
    print("3. Foot to Inch")
    print("4. Kilometer to Meter")
    print("5. Hours to Minutes")
    print("6. Celsius to Fahrenheit")
    print("7. Kelvin to Celsius")

    while True:
        choice = input("Enter choice (1 to 7): ")

        if choice in ['1', '2', '3', '4', '5', '6', '7']:
            try:
                a = float(input("Enter the value to convert: "))
            except ValueError:
                print("Invalid input! Please enter a number.")
                continue

            if choice == '1':
                result = kg_to_gram(a)
                print(f"{a} kilograms is equal to {result} grams")

            elif choice == '2':
                result = mtr_to_cm(a)
                print(f"{a} meters is equal to {result} centimeters")

            elif choice == '3':
                result = foot_to_inch(a)
                print(f"{a} feet is equal to {result} inches")

            elif choice == '4':
                result = km_to_mtr(a)
                print(f"{a} kilometers is equal to {result} meters")

            elif choice == '5':
                result = hr_to_mint(a)
                print(f"{a} hours is equal to {result} minutes")

            elif choice == '6':
                result = celsius_to_fahrenheit(a)
                print(f"{a} degrees Celsius is equal to {result} degrees Fahrenheit")

            elif choice == '7':
                result = kelvin_to_celsius(a)
                print(f"{a} Kelvin is equal to {result} degrees Celsius")

        else:
            print("Invalid choice")

        next_calculation = input("Press for next calculation [Yes(y)/No(n)]: ")
        if next_calculation.lower() != 'y':
            break

converter_calculator()
