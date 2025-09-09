class Order:

    # Initialize order with empty list

    def __init__(self):
        self.items = []

    
    # Add coffee item to order
    
    def add_item(self, coffee):
        self.items.append(coffee)
        print(f"Added {coffee.name} to your order.")


    # Calculate total price of the order
    
    def total_price(self):
        return sum(item.price for item in self.items)
    

    # Show order summary
    
    def show_order(self):
        if not self.items:
            print("No items in your order.")
            return 
        print("\nYour order:")

        for i, item in enumerate(self.items, start=1):
            print(f"{i}. {item.name} - ${item.price}")

        print(f"Total: ${self.total_price()}") 


    # Handle checkout process
    
    def checkout(self):
        if not self.items:
            print("Your cart is empty.")
            return         
        self.show_order()
        
        confirm = input("Proceed to checkout? (yes/no): ").strip().lower()

        if confirm == 'yes':
            print("Order confirmed! Thank you.")
            self.items.clear()
        else:
            print("Checkout cancelled.")