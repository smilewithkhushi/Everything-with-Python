
class MenuItem:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def is_available(self, quantity):
        return self.stock >= quantity


class FoodDeliverySystem:
    def __init__(self):
        self.menu = {
            1: MenuItem("Burger", 120, 10),
            2: MenuItem("Pizza", 250, 5),
            3: MenuItem("Dosa", 180, 0),  # out of stock
            4: MenuItem("Fries", 90, 7),
            5: MenuItem("vada pao", 40, 15)
        }
        self.cart = {}

    def display_menu(self):
        print("\n---- MENU ----")
        for key, item in self.menu.items():
            status = "Out of Stock" if item.stock == 0 else f"₹{item.price} | Stock: {item.stock}"
            print(f"{key}. {item.name} - {status}")
        print("--------------")

    def add_to_cart(self, item_id, quantity):
        if item_id not in self.menu:
            print("Invalid item ID.")
            return

        item = self.menu[item_id]
        if item.stock == 0:
            print(f"{item.name} is out of stock.")
            return

        if quantity > item.stock:
            print(f" Only {item.stock} {item.name}(s) available.")
            return

        if item_id in self.cart:
            self.cart[item_id]['quantity'] += quantity
        else:
            self.cart[item_id] = {'item': item, 'quantity': quantity}

        item.stock -= quantity
        print(f"Added {quantity} x {item.name} to cart.")

    def remove_from_cart(self, item_id):
        if item_id not in self.cart:
            print(" Item not in cart.")
            return

        item_info = self.cart.pop(item_id)
        item_info['item'].stock += item_info['quantity']
        print(f"Removed {item_info['item'].name} from cart.")

    def show_cart(self):
        if not self.cart:
            print("Your cart is empty.")
            return

        print("\n---- YOUR CART ----")
        total = 0
        for info in self.cart.values():
            item = info['item']
            qty = info['quantity']
            cost = qty * item.price
            total += cost
            print(f"{item.name} x {qty} = ₹{cost}")
        print(f"Total: ₹{total}")
        print("--------------------")

    def checkout(self):
        self.show_cart()
        print(" Thank you for your order!")


def main():
    system = FoodDeliverySystem()

    while True:
        system.display_menu()
        print("\nOptions:")
        print("1. Add item to cart")
        print("2. Remove item from cart")
        print("3. View cart")
        print("4. Checkout & Exit")
        print("5. Exit without checkout")

        choice = input("Enter choice: ")

        if choice == '1':
            try:
                item_id = int(input("Enter item number to add: "))
                qty = int(input("Enter quantity: "))
                system.add_to_cart(item_id, qty)
            except ValueError:
                print(" Please enter valid numbers.")

        elif choice == '2':
            try:
                item_id = int(input("Enter item number to remove: "))
                system.remove_from_cart(item_id)
            except ValueError:
                print(" Please enter a valid item number.")

        elif choice == '3':
            system.show_cart()

        elif choice == '4':
            system.checkout()
            break

        elif choice == '5':
            print(" Exiting without checkout.")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()

     
