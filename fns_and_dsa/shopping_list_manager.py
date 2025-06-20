# shopping_list_manager.py

# Function to display the menu options
def display_menu():
    print("Shopping List Manager")       # Required exact string
    print("1. Add Item")                # Required exact string
    print("2. Remove Item")             # Required exact string
    print("3. View List")               # Required exact string
    print("4. Exit")                    # Required exact string

def main():
    shopping_list = []

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("Enter the item to add: ").strip()
            shopping_list.append(item)
            print(f"'{item}' has been added to the list.")
        elif choice == '2':
            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from the list.")
            else:
                print(f"'{item}' not found in the shopping list.")
        elif choice == '3':
            if shopping_list:
                print("\nCurrent Shopping List:")
                for idx, item in enumerate(shopping_list, start=1):
                    print(f"{idx}. {item}")
            else:
                print("Your shopping list is currently empty.")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
