
def convert_length():
    print("1. kilometer to mile: ")
    print("2. mile to kilometer: ")
    print("3. meter to feet: ")
    print("4. feet to meter: ")
    choice = int(input("enter your choice: "))
    value = float(input("enter your value: "))
    if choice == 1:
        result = value * 0.621371
        print(f"{result} miles.")
    elif choice == 2:
        result = value * 1.60934
        print(f"{result} km.")
    elif choice == 3:
        result = value * 3.28084
        print(f"{result} feets.")
    elif choice == 4:
        result = value * 0.3048
        print(f"{result} meters.")
    else:
        print("enter a valid choice.")

def convert_weight():
    print("1. kilogram to pound: ")
    print("2. pound to kilogram: ")
    print("3. gram to kilogram: ")
    print("4. kilogram to pound: ")
    choice = int(input("enter your choice: "))
    value = float(input("enter value: "))
    if choice == 1:
        result = value * 2.20462
        print(f"{result} pounds.")
    elif choice == 2:
        result = value * 0.453592
        print(f"{result} kilograms.")
    elif choice == 3:
        result = value / 1000
        print(f"{result} kilograms.")
    elif choice == 4:
        result = value * 1000
        print(f"{result} grams.")
    else:
        print("enter a valid choice.")

def convert_temperature():
    print("1. Celsius to Fahrenheit: ")
    print("2. Fahrenheit to Celsius: ")
    choice = int(input("enter your choice: "))
    value = float(input("enter value: "))
    if choice == 1:
        result = value * 9 / 5 + 32
        print(f"{result} Celsius.")
    elif choice == 2:
        result = (value - 32) * 5 / 9
        print(f"{result} Fahrenheit.")
    else:
        print("enter a valid choice.")

while True:
    print("1. Convert Length")
    print("2. Convert Weight")
    print("3. Convert Temperature")
    print("4. Exit.")
    choice = int(input("enter your choice: "))
    if choice == 1:
        convert_length()
    elif choice == 2:
        convert_weight()
    elif choice == 3:
        convert_temperature()
    elif choice == 4:
        print("Closing the program....")
        break
    else:
        print("enter a valid choice.")

