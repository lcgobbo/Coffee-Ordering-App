from product import Coffee
from order import Order

# Display menu and handle user input

def main():

    menu = [
        Coffee("Espresso", 2.5),
        Coffee("Latte", 3.5),
        Coffee("Cappuccino", 3.0),
        Coffee("Americano", 2.0)
    ]

    order = Order()

    # User interaction

    while True:
        print("\n--- Coffee Menu ---")

        for i, coffee in enumerate(menu, 1):
            print(f"{i}. {coffee.name} - ${coffee.price}")

        print("5. View Order")
        print("6. Checkout")
        print("7. Exit")

        choice = input("Choose an option: ")
        if choice in ['1', '2', '3', '4']:
            order.add_item(menu[int(choice)-1])
        elif choice == '5':
            order.show_order()
        elif choice == '6':
            order.checkout()
        elif choice == '7':
            print("Thanks for visiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()