class Restaurant:
    def __init__(self):
        self.menu_items = {
            'fish & chips': 500,
            'Dynamite chicken': 1000,
            'Hot & Sour': 200,
            'french frise': 600,
            'Chicken karahi': 2500,
            'Chicken handi': 2300,
            'Pepsi': 100,
            '7UP': 100
        }
        self.book_table = ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A']
        self.customer_orders = []

    def add_item_to_menu(self):
        item = input("What item to be added to menu: ")
        price = float(input("Price of item: "))
        self.menu_items[item] = price
        print(f"Item '{item}' added to menu with price {price}.")

    def book_tables(self):
        print(f"Available tables: {self.book_table}")
        try:
            choice = int(input("Which table would you like to book (1-8): "))
            if 1 <= choice <= 8:
                if self.book_table[choice - 1] == 'A':
                    self.book_table[choice - 1] = 'Booked'
                    print(f"Table {choice} booked successfully.")
                else:
                    print("Table not available.")
            else:
                print("Invalid table number.")
        except ValueError:
            print("Please enter a valid number.")

    def customer_order(self):
        while True:
            order = input("What would you like to have? ")
            if order in self.menu_items:
                self.customer_orders.append(order)
                choice = input("Want to add another item (YES/NO)? ").strip().lower()
                if choice != 'yes':
                    break
            else:
                print(f"Sorry, we don't have '{order}' on the menu.")

    def print_menu(self):
        print("Menu Items:")
        for item, price in self.menu_items.items():
            print(f"{item}: {price}")

    def print_table_reservations(self):
        print("Table Reservations:")
        for i, status in enumerate(self.book_table, start=1):
            print(f"Table {i}: {status}")

    def print_customer_orders(self):
        print("Customer Orders:")
        for order in self.customer_orders:
            print(order)

restaurant = Restaurant()
restaurant.add_item_to_menu()
restaurant.book_tables()
restaurant.print_menu()
restaurant.customer_order()
restaurant.print_table_reservations()
restaurant.print_customer_orders()
