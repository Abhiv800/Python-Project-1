# This class is for the basket when books will be added 
class Basket:
    def __init__(self):
        self.items = []

# This defines the function to checked if there is a book that already exists in the basket 
    def add_item(self, book_id, title, quantity, price, total ):
# This part of the code will update the basket as the items are added and the quantity and total change as the books are added        
        for item in self.items:
            if item['book_id'] == book_id:
                item['quantity'] += quantity
                item['total'] += total
                return
# This part of the code is when the book is added into the basket and will show all the attributes
        self.items.append({
            'book_id': book_id,
            'title': title,
            'quantity': quantity,
            'price': price,
            'total': total
        })

# This defines the function to remove a item if the customer doesn't want it any more
    def remove_item(self, book_id):
        self.items = [item for item in self.items if item['book_id'] != book_id]

# This defines the function calculates the whole total of the basket
    def calculate_total(self):
        return sum(item['total'] for item in self.items)

# This defines the function to clear the basket after the user has completed their purchase 
    def clear_basket(self):
        self.items.clear()

# This class is for the invoice after the user completes the purchase and creates them with an invoice 
class Invoice:
# This part of the code will link the invoice to the basket and will fills the rest of the items with customer details
    def __init__(self, basket):
        self.basket = basket
        self.customer_name = ""
        self.customer_email = ""
        self.customer_address = ""

# This defines the function to set customer info on the invoice 
    def set_customer_info(self, name, email, address):
# This part of the code will raise an error if any of the information is empty
        if not name or not email or not address:
            raise ValueError("Customer information cannot be empty.")
        self.customer_name = name
        self.customer_email = email
        self.customer_address = address

# This defines the function to get items from the basket    
    def get_items(self):
        return self.basket.items

# This defines the function to calculate the whole total from the basket and shows on the invoice 
    def get_total_amount(self):
        return self.basket.calculate_total()


# This represents the main basket
basket_core = Basket()
# This represents the invoice that is connected to the basket
invoice_core = Invoice(basket_core)