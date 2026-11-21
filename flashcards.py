flashcards = {}

def add_flashcard(question, answer):
    flashcards[question] = answer
    print(f"Flashcard for '{question}' added. Answer: {answer}")

def search_flashcards(question):
    answer = flashcards.get(question)
    if answer:
        print(f"{question} : {answer}")
    else:
        print("No flashcard found.")

def update_flashcards(question, answer):
    if question in flashcards:
        flashcards[question] = answer
        print(f"Flashcard for '{question}' updated. Answer: {answer}")
    else:
        print("No flashcard found.")

def delete_flashcard(question):
    if question in flashcards:
        del flashcards[question]
        print(f"flashcard of {question} is deleted.")
    else:
        print("No flashcard found.")

def show_flashcards():
    if not flashcards:
        print("No flashcard found.")
    else:
        print("\nYour flashcards:")
        for question, answer in flashcards.items():
            print(f"{question} : {answer}")

def main():
    while True:
        print("\n======Flashcard Generator======")
        print("1. Add flashcard.")
        print("2. Search flashcard.")
        print("3. Update flashcard.")
        print("4. Delete flashcard.")
        print("5. Show flashcard.")
        print("6. Exit")

        try:
            choice = int(input("enter your choice: "))
        except ValueError:
            print("Please enter a number.")
            continue

        if choice == 1:
            question = input("enter question: ")
            answer = input("enter answer: ")
            add_flashcard(question, answer)
        elif choice == 2:
            question = input("enter question: ")
            search_flashcards(question)
        elif choice == 3:
            question = input("enter question: ")
            answer = input("enter answer: ")
            update_flashcards(question, answer)
        elif choice == 4:
            question = input("enter question: ")
            delete_flashcard(question)
        elif choice == 5:
            show_flashcards()
        elif choice == 6:
            print("Closing the program....")
            break
        else:
            print("enter a valid choice from 1-6.")

if __name__ == "__main__":
    main()
