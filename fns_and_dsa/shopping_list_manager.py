"""A function for shopping simulation"""
def display_menu():
    """A module to display a shopping list"""

    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")


def main():
    """The main function of the module"""

    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            item_name = input("Enter the item to add: ")
            shopping_list.append(item_name)
            pass
        elif choice == '2':
            # Prompt for and remove an item
            remove_item = input("Enter the name of the item to remove: ")
            if remove_item not in shopping_list:
                print(f"{remove_item} item was not found in cart")
            else:
                shopping_list.remove(remove_item)
            
            pass
        elif choice == '3':
            # Display the shopping list
            print(shopping_list)
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()