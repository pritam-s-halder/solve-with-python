#contact management system
phonebook = {}

def add_phone(name, number):
    phonebook[name] = number
    print(f"{name} and {number} added.")

def update_phone(name, number):
    if name in phonebook:
        phonebook[name] = number
        print(f"{name} and {number} updated.")
    else:
        print(f"{name} not found.")

def delete_phone(name):
    if name in phonebook:
        del phonebook[name]
        print(f"{name} deleted.")
    else:
        print(f"{name} not found.")

def display_phone():
    for name, number in phonebook.items():
        print(f"{name} : {number}")

def main():
    while True:
        print("contact management system.\n")
        print("1. Add new contact")
        print("2. Update contact")
        print("3. Delete contact")
        print("4. View contact")
        print("5. Exit")

        choice = input("Enter your choice (1-5) : ")
        if choice == "1":
            name = input("Enter contact name: ")
            number = input("Enter contact number: ")
            add_phone(name, number)
        elif choice == "2":
            name = input("Enter contact name: ")
            number = input("Enter contact number: ")
            update_phone(name, number)
        elif choice == "3":
            name = input("Enter contact name: ")
            delete_phone(name)
        elif choice == "4":
            display_phone()
        elif choice == "5":
            print("Closing the program...")
            break
        else:
            print("Please enter a valid choice.")


if __name__ == "__main__":
    main()