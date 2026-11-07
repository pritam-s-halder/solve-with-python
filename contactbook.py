#contact management system

phonebook = {}
def add_contact(name, number):
    phonebook[name] = number
    print(f"{name} and {number} are added.")

def search_contact(name):
    number = phonebook.get(name.lower())
    if number:
        print(f"{name}: {number}")
    else:
        print(f"{name} not found.")

def update_contact(name, number):
    if name in phonebook:
        phonebook[name] = number
        print(f"{name} and {number} are updated.")
    else:
        print(f"{name} does not exist.")

def delete_contact(name):
    if name in phonebook:
        del phonebook[name]
        print(f"{name} has been deleted.")
    else:
        print(f"{name} is not exist.")

def show_contacts():
    for name, number in phonebook.items():
        print(f"{name}: {number}")

def main():
    while True:
        print("Contact Management System. \n")
        print("1. Add contact")
        print("2. Search contact")
        print("3. Update contact")
        print("4. Delete contact")
        print("5. Show contacts")
        print("6. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            name = input("Enter contact name: ")
            number = input("Enter contact number: ")
            add_contact(name, number)
        elif choice == "2":
            name = input("Enter contact name: ")
            search_contact(name)
        elif choice == "3":
            name = input("Enter contact name: ")
            number = input("Enter contact number: ")
            update_contact(name, number)
        elif choice == "4":
            name = input("Enter contact to be deleted: ")
            delete_contact(name)
        elif choice == "5":
            show_contacts()
        elif choice == "6":
            print("Closing the program...")
            break
        else:
            print("Please enter a valid choice.")
if __name__ == "__main__":
    main()

