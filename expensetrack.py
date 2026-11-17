from datetime import date
expenses = []

def add_expenses():
    category = input("Enter expense category: ").strip()
    description = input("Enter description: ").strip()
    amount = float(input("Enter amount: "))

    expense = {
        "date": date.today().isoformat(),
        "category": category,
        "description": description,
        "amount": amount
    }
    expenses.append(expense)
    print("Expense added!")

def view_expenses():
    if not expenses:
        print("No expense added yet.")
        return
    print("\nAll Expenses")
    for index, expense in enumerate(expenses, start=1):
        print(
            f"{index}. [{expense['date']}] {expense['category']} - "
            f"{expense['description']}: ₹{expense['amount']:.2f}"
        )

def view_total():
    total = sum(expense["amount"] for expense in expenses)
    print(f"\nTotal Expenses: ₹{total:.2f}")

def main():
    while True:
        print("\n===== Expense Tracker =====")
        print("1. Add expense")
        print("2. View expenses")
        print("3. View total")
        print("4. Exit")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_expenses()
        elif choice == 2:
            view_expenses()
        elif choice == 3:
            view_total()
        elif choice == 4:
            print("Closing the program...")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
