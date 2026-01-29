# Here is have imported all the main components that require for my GUI
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as messagebox

# logic pages
import Bookstore_core as CustomerLogic
import Bookstore_book as BookLogic
import Bookstore_basket_invoice as BasketInvoiceLogic

# This is where the window of the Book store starts 
def showFrame(frame):
    frame.tkraise()
    
# This area here holds all the main components of the window 
window=tk.Tk()
# This is the title of the GUI
window.title("Bookstore Management")
# This is the colour i chose for my whole GUI
window.configure(bg="light blue")
# This bit of the code is where the logo is added at the top left of the GUI
icon = tk.PhotoImage(file=r"C:\Users\abhiv\OneDrive - The University of Northampton\Documents\Year 1\Semester 1\CSY1020\Assessment 2\Bookstore.png")
window.iconphoto(True, icon)
# This code controls how the main window resizes when we change the size of the window
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)

# This part of code holds the whole navigation of all tabs of the GUI
navigation = tk.Frame(window, bg="light blue")
# I have used the grid function to place all the buttons on one side
navigation.grid(row=0, column=0, sticky="ns")
# All the buttons below holds all different tabs part of GUI and can be moved around
tk.Button(navigation, text="Home", width=20, height=2, command=lambda: showFrame(home)).grid(row=1, column=0, sticky="nesw")
tk.Button(navigation, text="Books Available", width=20, height=2, command=lambda: showFrame(books_available)).grid(row=2, column=0, sticky="nesw")
tk.Button(navigation, text="Add Books", width=20, height=2, command=lambda: showFrame(add_book)).grid(row=3, column=0, sticky="nesw")
tk.Button(navigation, text="Basket", width=20, height=2, command=lambda: showFrame(basket)).grid(row=4, column=0, sticky="nesw")
tk.Button(navigation, text="Invoice", width=20, height=2, command=lambda: showFrame(invoice)).grid(row=5, column=0, sticky="nesw")
tk.Button(navigation, text="Customers", width=20, height=2, command=lambda: showFrame(customers)).grid(row=6, column=0, sticky="nesw")
tk.Button(navigation, text="Staff", width=20, height=2, command=lambda: showFrame(staff)).grid(row=7, column=0, sticky="nesw")
# This is where the GUI window starts
mainFrame = tk.Frame(window)


# Home
# This is the first window when I start the GUI
home = tk.Frame(window, bg="light blue")
# This is the lay out of the window
home.grid(row=0, column=1, sticky="nsew")
# This part of the code controls the how the columns inside of the home resizes
home.grid_columnconfigure(0, weight=0,)
home.grid_columnconfigure(1, weight=1)
# This is the logo of my book store
icon_home = tk.PhotoImage(file=r"C:\Users\abhiv\OneDrive - The University of Northampton\Documents\Year 1\Semester 1\CSY1020\Assessment 2\Bookstore.png").subsample(10, 10)
home.icon_home = icon_home
tk.Label (home, image=icon_home, bg="light blue").grid(row=0, column=0, sticky="nw", padx=0, pady=0)
# The title of the GUI
tk.Label(home, text=" Welcome to Bookstore Management ", font=("Arial", 20), bg="light blue").grid(row=0, column=1, sticky="nw", padx=20, pady=5)
# A little information for users when they use my GUI
tk.Label(home, text="Please use the navigation bar on the left to access to different sections of the website.", font=("Arial", 14), bg="light blue").grid(row=1, column=1, sticky="nw", padx=20, pady=10)


# Books available 
# This is the second window of the code, this is where all the books are kept
books_available = tk.Frame(window, bg="light blue")
# This the lay out of the window
books_available.grid(row=0, column=1, sticky="nsew")
# This part of the code controls the widgets inside this frame when it resizes
books_available.grid_rowconfigure(1, weight=1)
books_available.grid_columnconfigure(0, weight=1)

# Title of this page
tk.Label(books_available, text="Books that are available", font=("Arial", 15), bg="light blue").grid(row=0, column=0, sticky="nw", padx=20, pady=10)

# I used tree viwe to lay out the books
table = ttk.Treeview(books_available, columns=("ID", "Title", "Author", "Fiction/Non-Fiction", "Price", "Stock"), show="headings")
# These are the headings of the tree view
table.heading("ID", text='Book ID')
table.heading("Title", text='Title')
table.heading("Author", text='Author')
table.heading("Fiction/Non-Fiction", text='Fiction/Non-Fiction')
table.heading("Price", text='Price')
table.heading("Stock", text='Stock')
# Placement of the table
table.grid(row=1, column=0, sticky="nsew", padx=20, pady=10)
# All the code under here is books with their IDs, title, authors, if they are fiction or non fiction, price and if they are available
table.insert("", "end", values=("B001", "The Great Gatsby", "F. Scott Fitzgerald", "Fiction", "12.99", "IN STOCK"))
table.insert("", "end", values=("B002", "To Kill a Mockingbird", "Harper Lee", "Fiction", "16.99", "IN STOCK"))
table.insert("", "end", values=("B003", "Harry Potter and the Philosopher's Stone", "J.K. Rowling", "Fiction", "25.99", "OUT OF STOCK"))
table.insert("", "end", values=("B004", "The Hobbit", "J.R.R. Tolkien", "Fiction", "15.99", "IN STOCK"))
table.insert("", "end", values=("B005", "Atomics Habits", "James Clear", "Non-Fiction", "20.00", "IN STOCK"))
table.insert("", "end", values=("B006", "Educated", "Tara Westover", "Non-Fiction", "18.50", "OUT OF STOCK"))
table.insert("", "end", values=("B007", "The Millionaire Next Door", "Thomas J. Stanley", "Non-Fiction", "30.00", "IN STOCK"))
table.insert("", "end", values=("B008", "Rich Dad Poor Dad", "Robert T. Kiyosaki", "Non-Fiction", "25.99", "IN STOCK"))
table.insert("", "end", values=("B009", "The Psychology of Money", "Morgan Housel", "Non-Fiction", "22.50", "OUT OF STOCK"))
table.insert("", "end", values=("B010", "I will Teach You to Be Rich", "Ramit Sethi", "Non-Fiction", "35.00", "IN STOCK"))
table.insert("", "end", values=("B011", "GCSE Biology", "CGP Books", "Non-Fiction", "10.99", "IN STOCK"))
table.insert("", "end", values=("B012", "GCSE Mathematics", "CGP Books", "Non-Fiction", "10.99", "IN STOCK"))
table.insert("", "end", values=("B013", "GCSE English", "CGP Books", "Non-Fiction", "10.99", "OUT OF STOCK"))
table.insert("", "end", values=("B014", "A-level Physics", "CGP Books", "Non-Fiction", "15.99", "IN STOCK"))
table.insert("", "end", values=("B015", "A-level Chemistry", "CGP Books", "Non-Fiction", "15.99", "IN STOCK"))
table.insert("", "end", values=("B016", "A-level Mathematics", "CGP Books", "Non-Fiction", "15.99", "OUT OF STOCK"))
table.insert("", "end", values=("B017", "Artificial Intelligence: A Modern Approach", "Stuart Russell and Peter Norvig", "Non-Fiction", "90.00", "IN STOCK"))
table.insert("", "end", values=("B018", "Database System Concepts", "Abraham Silberschatz, Henry F. Korth, and S. Sudarshan", "Non-Fiction", "85.00", "IN STOCK"))
table.insert("", "end", values=("B019", "Introduction to Algorithms", "Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, and Clifford Stein", "Non-Fiction", "100.00", "OUT OF STOCK"))
table.insert("", "end", values=("B020", "Clean Code: A Handbook of Agile Software Craftsmanship", "Robert C. Martin", "Non-Fiction", "40.00", "IN STOCK"))

# This code creates container frame to hold the action buttons and place them neatly 
action_frame = tk.Frame(books_available, bg="light blue")
action_frame.grid(row=2, column=0, sticky="se", padx=20, pady=20)
# This code defines the function called add to basket when the button is clicked it will do exactly what is intended to do
def add_to_basket():

    selected = table.focus()
# using the if function means if the user clicks add to basked and haven't selected any it will show a controlled error
    if not selected:
# The message box is to show user warnings if something isn't done right
        messagebox.showwarning("No Selection", "Please select a book to add to the basket.")
        return
# This code helps to get all the data from the selected book in the table
    book_values = table.item(selected, "values")
    book_id, title, author, fiction_non_fiction, price, stock = book_values
# If the user picks a book that is out of stock it show a controlled error
    if stock == "OUT OF STOCK":
# This message box is to show users that they wouldn't be able to add the book and will also show the title
        messagebox.showerror("Out of Stock", f"The book '{title}' is currently out of stock.")
        return

# This part of the code is when the user picks the books it will take the following information and adds to the basket    
    BasketInvoiceLogic.basket_core.add_item(
# ID of the book
        book_id=book_id,
# Title of the book
        title=title,
# Number of books added to the basket
        quantity=1,
# The price is that comes from the table is a string and into a floating point for the total
        price=float(price),
        total=float(price)
    )
    refresh_basket()
# This message box is to show that book has been added to the basket
    messagebox.showinfo("Added to Basket", f"The book '{title}' has been added to your basket.")
    
# This is a button in the window so when the customer slectes the book and click on 'add to basket' it will do that
tk.Button(action_frame, text="Add to Basket", width=15, command=add_to_basket).grid(row=0, column=2, padx=5)

# This code defines as function, when a user wants to add a book to available book it will move to a different tab
def move_to_add_book():
# This code is where it will point the user to the tab it is connected to
    showFrame(add_book)
# This button will allow the user to go to add book tab to add books to available book
tk.Button(action_frame, text="Need to add Books", width=15, command=move_to_add_book).grid(row=0, column=1, padx=5)
# This part of the code controls how the widget move when the frame resizes
books_available.grid_rowconfigure(2, weight=1)
books_available.grid_columnconfigure(0, weight=1)


# Add Books
# This is the third tab of the GUI
add_book = tk.Frame(window, bg="light blue")
# This is the lay out of the window
add_book.grid(row=0, column=1, sticky="nsew")
# This is the title of the window
tk.Label(add_book, text="Add Books to Inventory", font=("Arial", 15), bg="light blue").grid(row=0, column=0, sticky="nw", padx=20, pady=10)
# This is a label that show what information needs to be added 
tk.Label(add_book, text="Book Title:", font=("Arial", 12), bg="light blue").grid(row=2, column=0, sticky="w", pady=10, padx=50)
# This is where the user will add the information 
title_entry = tk.Entry(add_book, width=60)
title_entry.grid(row=3, column=0, sticky="w", pady=5, padx=50)
# This is a label that show what information needs to be added
tk.Label(add_book, text="Author:", font=("Arial", 12), bg="light blue").grid(row=4, column=0, sticky="w", pady=10, padx=50)
# This is where the user will add the information 
author_entry = tk.Entry(add_book, width=60)
author_entry.grid(row=5, column=0, sticky="w", pady=5, padx=50)
# This is a label that show what information needs to be added
tk.Label(add_book, text="Fiction/Non-Fiction:", font=("Arial", 12), bg="light blue").grid(row=6, column=0, sticky="w", pady=10, padx=50)
# This is where the user will add the information
fiction_non_fiction_entry = tk.Entry(add_book, width=60)
fiction_non_fiction_entry.grid(row=7, column=0, sticky="w", pady=5, padx=50)
# This is a label that show what information needs to be added
tk.Label(add_book, text="Price £:", font=("Arial", 12), bg="light blue").grid(row=8, column=0, sticky="w", pady=10, padx=50)
# This is where the user will add the information 
price_entry = tk.Entry(add_book, width=60)
price_entry.grid(row=9, column=0, sticky="w", pady=5, padx=50)

# This code defines a function to generate a new ID when a new book is added 
def generate_book_id():
# This code will get a list of all the items in the tree view in books available
    children = table.get_children()
# Using the if function to check if the table is empty 
    if not children:
# If there is a book that is already started with B001 then it will take the next available number or ID
        return "B001"
# This will check the last book that is added to the table
    last_item = table.item(children[-1])['values'][0]
# This will check the last id so then it can pick new id with the available number
    last_id_num = int(last_item[1:])
# This will increment the id by 1 and return the new book id as B###
    return f"B{last_id_num + 1:03d}"

# This code defines a function to add the book into available book tab
def gui_add_book_inventory():
# Using the try function to catch any errors that may occur 
    try:
# This will give a new Id for the book that has recently been added to books available
        new_id = generate_book_id()
# This will call the core logic function to create a new book
        book = BookLogic.add_book(
# This is a unique book ID
            new_id,
# This code will get the information that customer has entered in this field
            title_entry.get(),
# This code will get the information that customer has entered in this field
            author_entry.get(),
# This code will get the information that customer has entered in this field
            price_entry.get(),
# This code will get the information that customer has entered in this field
            fiction_non_fiction_entry.get(),
# This code will be a default information
            extra_info="N/A"   
        )

# This code helps to insert the infoamtion that the user adds to the table in books available
        table.insert("", "end", 
            values=(
# This is the unique book id
                book.book_id,
# This is the title of the book
                book._title,
# This is the authors name
                book._author,
# This will be either fiction or non fiction
                fiction_non_fiction_entry.get(),
# This is the price of the book
                book._price,
# This is the default add in when the book is added 
                "IN STOCK"
           )
        )
# This will remove all the that was perviously added after the book has been added to books available and will be available to add another book and so on
        title_entry.delete(0, tk.END)
        author_entry.delete(0, tk.END)
        fiction_non_fiction_entry.delete(0, tk.END)
        price_entry.delete(0, tk.END)
# This message box will let the user know that book as been added
        messagebox.showinfo("Success", "Book added successfully!")
# This will catch out any error may occur when adding information of a book
    except ValueError as e:
        messagebox.showerror("Error", str(e))

# This button is for to add the book to books available when all the fields has been entered 
tk.Button(add_book, text="Add Book to Inventory", width=20, command=gui_add_book_inventory).grid(row=10, column=0, padx=50, pady=20)


# Basket
# This is the forth window of the GUI
basket = tk.Frame(window, bg="light blue")
# The lay out of the window
basket.grid(row=0, column=1, sticky="nsew")
# This is the title of the window 
tk.Label(basket, text="Items in your Basket", font=("Arial", 15), bg="light blue").grid(row=0, column=0, sticky="nw", padx=20, pady=10)
# I used the Tree view function to build a table for all the books the users will add
basket_frame = ttk.Treeview(basket, columns=("ID", "Title", "Quantity", "Price", "Total"), show="headings")
# All the headings of the tree viwe table
for column in ("ID", "Title", "Quantity", "Price", "Total"):
    basket_frame.heading(column, text=column)
    basket_frame.column(column, anchor="center")

basket_frame.grid(row=1, column=0, columnspan=3, sticky="nsew")

# This is a Thinker variable that will hold the basket total as a string and value starts from 0
total_var = tk.StringVar(value="0.00")
# This variable is store the shipping method that has been selected by the users
shipping_method = tk.StringVar(value="Not Selected")
# This variable is to store the price of the shipping that has been selected
shipping_cost = tk.DoubleVar(value=0.00)
# This is a static label for total 
tk.Label(basket, text= "Total (£):", font=("Arial", 12), bg="light blue").grid(row=2, column=0, sticky="w", pady=10)
# This label is a dynamic label that shows the current basket total 
tk.Label(basket, textvariable=total_var, font=("Arial", 12), bg="light blue").grid(row=2, column=1, sticky="w", pady=10)


# This part of the code is where the invoice is linked to the basket so what ever is the basket it will show on the invoice
invoice_core = BasketInvoiceLogic.Invoice(BasketInvoiceLogic.basket_core)
# This defines the function to make the invoice after clicking the purchase button
def make_invoice():
# This if functions to make sure that the user selects themselves before completing the order
    if not customer_confirmed:
        messagebox.showwarning("Customer Information required", "Please confirm a customer before completing the purchase")
        return
# This will take all the information from the customer tab and put it on the invoice 
    invoice_customer_name.set(invoice_core.customer_name)
    invoice_customer_email.set(invoice_core.customer_email)
    invoice_customer_address.set(invoice_core.customer_address)

# After the customer is finsihed the invoice will clear all fields for the next customer
    invoice_table.delete(*invoice_table.get_children())
# This loops through each item that is in the basket
    for item in BasketInvoiceLogic.basket_core.items:
# It will calculate the total
        total = item['price'] * item['quantity']
# This part of the code will enter all new items for every new customer 
        invoice_table.insert("", "end", values=(
        item['title'],
        item['quantity'],
        f"{item['price']:.2f}",
        f"{total:.2f}"
    ))
# This part of the code shows the full invoice and the total of the basket  
    final_total = BasketInvoiceLogic.basket_core.calculate_total() + shipping_cost.get()
    invoice_total.set(f"{final_total:.2f}")
# This will take to the Invoice tab
    showFrame(invoice)
# This defines the function to clear the basket after the customer is finished with their and items so it is free for the next customer 
def refresh_basket():
    basket_frame.delete(*basket_frame.get_children())
# This will loop through every items that is stored in the basket
    for item in BasketInvoiceLogic.basket_core.items:
# This will calculate the total by multiplying the price and the quantity
        total=item['price'] * item['quantity']
# This will insert a new row in the basket
        basket_frame.insert("", "end", values=(
            item['book_id'],
            item['title'],
            item['quantity'],
            f"{item['price']:.2f}",
            f"{total:.2f}"
        ))
# This will show the total of the whole basket
    total_var.set(f"{BasketInvoiceLogic.basket_core.calculate_total():.2f}")

# This button is when the customer has fully finished with their shopping 
complete_purchase_btn = tk.Button(basket, text="Complete Purchase", width=20, state=tk.DISABLED, command=make_invoice)
complete_purchase_btn.grid(row=6, column=4, padx=5)

# This defines the function to remove any book that is not needed for the customer 
def remove_selected_item():
    selected = basket_frame.selection()
# This if function is to catch any error
    if not selected:
# This message box lets the user know if they press the remove item and they haven't selected then 
# it will let them know that it hasn't removed anything because noting was selected
        messagebox.showwarning("No Selection", "Please select an item to remove from the basket.")
        return
# This will get the tree view row number from the selected item
    tree_item_id = selected[0]
# This get all the information from the selected row in the basket
    tree_values = basket_frame.item(tree_item_id, "values")
# This get the book ID from the first bit of the tree view
    book_id = tree_values[0]
# This loop will go through each part of the item and when removing it should prevent from error
    for item in BasketInvoiceLogic.basket_core.items[:]:
# This will check the basket item is matched with selected book id
        if item.get("book_id") == book_id or item.get("id") == book_id:
# This part of the code will remove the book from the basket and stop searching further searching
            BasketInvoiceLogic.basket_core.items.remove(item)
            break
    refresh_basket()
# This button will remove the item when it is selected
tk.Button(basket, text="Remove Selected Item", width=20, command=remove_selected_item).grid(row=6, column=3, padx=5)

# This code here is to check if the customer details has been confirmed 
customer_confirmed = False
# This defines the function to confirm the customer details
def confirm_customer_details():
    global customer_confirmed

# This part of the code checks if the customer has been selected
    if not current_customer:
# This message box lets the customer know they will need to select them selfs
        messagebox.showwarning("Select Customer", "Please select a customer from the Customers tab.")
# This code will move to customer tab
        showFrame(customers)
        return
# This code here will store the details of the customer  
    invoice_core.set_customer_details(
        current_customer._name,
        current_customer._email,
        current_customer._address
    )
# This code here confirms that a customer has been selected
    customer_confirmed = True
# The purchase button will enable for the customer to finish
    complete_purchase_btn.config(state=tk.NORMAL)
# Let the customer know its been successful
    messagebox.showinfo("Customer Confirmed", "Customer details have been confirmed for the invoice.")
# This is the button which will finish the customers order
tk.Button(basket, text="Confirm Customer Details", width=20, command=confirm_customer_details).grid(row=6, column=2, padx=5)

# The layout of the window
delivery_frame = tk.Frame(basket, bg="light blue")
delivery_frame.grid(row=4, column=0, columnspan=3, sticky="w", pady=10)

# This defines the function to add the shipping fee for the customer to complete 
def shipping_fee(method, cost):
    shipping_method.set(method)
    shipping_cost.set(cost)
    total = BasketInvoiceLogic.basket_core.calculate_total() + cost
    total_var.set(f"{total:.2f}")
tk.Button(delivery_frame, text="Shipping Fee (£3.00)", width=20, command=lambda: shipping_fee("Standard Shipping", 3.00)).grid(row=0, column=0, padx=5)
tk.Button(delivery_frame, text="Fast Delivery Fee (£5.00)", width=20, command=lambda: shipping_fee("Fast Delivery", 5.00)).grid(row=0, column=1, padx=5)


# conformation order/invoice
# This is the fifth window of my GUI
invoice = tk.Frame(window, bg="light blue")
# This is the lay out of my tab
invoice.grid(row=0, column=1, sticky="nsew")
# The title for GUI Window
tk.Label(invoice, text="Your Invoice", font=("Arial", 15), bg="light blue").grid(row=0, column=0, sticky="nw", padx=20, pady=10)
# The number of the invoice 
tk.Label(invoice, text="Invoice No: 00001", bg="light blue").grid(row=1, column=0, sticky="w")
# This part of code will store customer data on the invoice 
invoice_customer_name = tk.StringVar()
invoice_customer_email = tk.StringVar()
invoice_customer_address = tk.StringVar()

# The subtitle for the invoice that will be filled with customer details
tk.Label(invoice, text="Customer Details", font=("Arial", 12), bg="light blue").grid(row=2, column=0, sticky="w", padx=20, pady=5)
# This part of the code is where the customer details will be laid for customers to confirm their invoice
tk.Label(invoice, text="Name:", bg="light blue")\
    .grid(row=3, column=0, sticky="w", padx=20)

tk.Label(invoice, textvariable=invoice_customer_name, bg="light blue")\
    .grid(row=3, column=1, sticky="w")

tk.Label(invoice, text="Email:", bg="light blue")\
    .grid(row=4, column=0, sticky="w", padx=20)

tk.Label(invoice, textvariable=invoice_customer_email, bg="light blue")\
    .grid(row=4, column=1, sticky="w")

tk.Label(invoice, text="Address:", bg="light blue")\
    .grid(row=5, column=0, sticky="w", padx=20)

tk.Label(invoice, textvariable=invoice_customer_address, bg="light blue", wraplength=400)\
    .grid(row=5, column=1, sticky="w")

# This will part of the code shows which shipping type the customer chose
tk.Label(invoice, text="Shipping Details", font=("Arial", 12), bg="light blue").grid(row=6, column=0, sticky="w", padx=20, pady=5)
# This will show which type of shipping the customer picked and how much they paid 
tk.Label(invoice, text="Method:", bg="light blue")\
    .grid(row=7, column=0, sticky="w", padx=20)

tk.Label(invoice, textvariable=shipping_method, bg="light blue")\
    .grid(row=7, column=1, sticky="w")

tk.Label(invoice, text="Cost (£):", bg="light blue")\
    .grid(row=8, column=0, sticky="w", padx=20)

tk.Label(invoice, textvariable=shipping_cost, bg="light blue")\
    .grid(row=8, column=1, sticky="w")

# This is the tree view table which will show all the items the customer has bought
invoice_table = ttk.Treeview(invoice, columns=("Title", "Quantity", "Price", "Total"), show="headings", height=8)
# This all the heading for the table
for column in ("Title", "Quantity", "Price", "Total"):
    invoice_table.heading(column, text=column)
    invoice_table.column(column, anchor="center")
invoice_table.grid(row=9, column=0, columnspan=3, sticky="nsew")
# This will automatically update the total price the customer has paid for
invoice_total = tk.StringVar(value="0.00")
tk.Label(invoice, text="Total (£)", font=("Arial", 12), bg="light blue").grid(row=10, column=1, sticky="e", pady=10)
tk.Label(invoice, textvariable=invoice_total, font=("Arial", 12), bg="light blue").grid(row=10, column=2, sticky="w", pady=10)

# This defines the function that the user is happy to see their invoice and goes back to the home page 
def confirm_invoice():
    global customer_confirmed, current_customer
# This part will empty the basket after the customer has confirmed invoice
    BasketInvoiceLogic.basket_core.items.clear()
# This will clear all the tables in basket as well as the invoice
    basket_frame.delete(*basket_frame.get_children())
    invoice_table.delete(*invoice_table.get_children())
# This will set all the totals to 0 so the next customer can start adding their items
    total_var.set("0.00")
    invoice_total.set("0.00")
# This part of the code will reset the shipping information
    shipping_method.set("Not Selected")
    shipping_cost.set(0.00)
 # This code helps to remove all customer infromation 
    customer_confirmed = False
    current_customer = None
# This code here will disable the complete the purchase until the next customer confirms 
    complete_purchase_btn.config(state=tk.DISABLED)

# This code here will take you back home
    showFrame(home)
# This button is to finish the customers invoices
tk.Button(invoice, text="Confirm Invoice", width=20, command=confirm_invoice).grid(row=8, column=2, padx=5)


# Customers
# This is the sixth window of my GUI
customers = tk.Frame(window, bg="light blue")
# The lay out of window 
customers.grid(row=0, column=1, sticky="nsew")
# The title for the window
tk.Label(customers, text="Customers", font=("Arial", 15), bg="light blue").grid(row=0, column=0, sticky="nw", padx=20, pady=10)
# This is the tree view table creations
customer_table = ttk.Treeview(customers, columns=("ID", "Name", "Email", "Address"), show="headings")
# These are all the headings that will be in the table 
customer_table.heading("ID", text='Customer ID')
customer_table.heading("Name", text='Name')
customer_table.heading("Email", text='Email')
customer_table.heading("Address", text='Address')
# Where the table sits on the window
customer_table.grid(row=1, column=0, sticky="nsew", padx=20, pady=10)
# I've added some customer names already into the table
customer_table.insert("", "end", values=("C001", "Daniel Roberts", "daniel.roberts@email.com", "78 Maple Street, Milton Keynes, MK9 2HF"))
customer_table.insert("", "end", values=("C002", "Sophie Turner", "sophie.turner@email.com", "12 Oak Avenue, London, NW1 2AB"))
customer_table.insert("", "end", values=("C003", "James Wilson", "james.wilson@email.com", "45 Pine Road, Birmingham, B1 2CD"))
customer_table.insert("", "end", values=("C004", "Olivia Johnson", "olivia.johnson@email.com", "33 Cedar Lane, Manchester, M1 3EF"))
customer_table.insert("", "end", values=("C005", "Liam Smith", "liam.smith@email.com", "55 Elm Street, Leeds, LS1 4GH"))

# This code here insures that there is no default customer that has been already selected
current_customer = None
# This defines the function once the user as selected the customer they can go back to the basket
def go_to_basket():
    global current_customer, customer_confirmed
# This part of the code shows that once the customer selection is done then it will be focused on the customer information
    selected = customer_table.focus()
# This will stop the user from going back to the basket if they dont select a customer
    if not selected:
# This message box is to show the customer they have selected anything
        messagebox.showwarning("No Selection", "Please select a customer to proceed to basket.")
        return
    
# This part of the code will gether all the information from selected customer 
    customer_id, name, email, address = customer_table.item(selected, "values")
# This part of the code will store the customer information that has been selected
    current_customer = CustomerLogic.Customer(name, email, customer_id, address)

# This will attach the customer details to the invoice after the customer has been chosen
    invoice_core.set_customer_info(name, email, address)
# This part of the code will enable the complete the purchase button when the customer has been chosen
    customer_confirmed = True
    complete_purchase_btn.config(state=tk.NORMAL)

# Goes back to basket
    showFrame(basket)

# This button will direct the user to basket tab
tk.Button(customers, text="Go to Basket", width=15, command=go_to_basket).grid(row=2, column=0, padx=5, pady=10)

# This part of the code where the customers can register them selves
add_customer = tk.Frame(customers, bg="light blue")
add_customer.grid(row=3, column=1, sticky="nsew", padx=20, pady=10)
tk.Label(add_customer, text="Register New Customer", font=("Arial", 15), bg="light blue").grid(row=0, column=0, sticky="nw", padx=20, pady=10)
# This where the customer needs to add their name 
tk.Label(add_customer, text="Name:", font=("Arial", 12), bg="light blue").grid(row=2, column=0, sticky="w", pady=10, padx=50)
name_entry = tk.Entry(add_customer, width=60)
name_entry.grid(row=3, column=0, sticky="w", pady=5, padx=50)
# This is where the customer needs to add their email
tk.Label(add_customer, text="Email:", font=("Arial", 12), bg="light blue").grid(row=4, column=0, sticky="w", pady=10, padx=50)
email_entry = tk.Entry(add_customer, width=60)
email_entry.grid(row=5, column=0, sticky="w", pady=5, padx=50)
# This is where the customer needs to add their address 
tk.Label(add_customer, text="Address:", font=("Arial", 12), bg="light blue").grid(row=6, column=0, sticky="w", pady=10, padx=50)
address_entry = tk.Entry(add_customer, width=60) 
address_entry.grid(row=7, column=0, sticky="w", pady=5, padx=50)

# This defines the function when a new customer is added it will need to give a new customer id 
def generate_customer_id():
    children = customer_table.get_children()
# This will confirm that in the table if there is free customer id
    if not children:
        return "C001"
# This part of the code will create a new id after checking the pervious 
    last_item= customer_table.item(children[-1])['values'][0]
    last_id_num = int(last_item[1:])
    return f"C{last_id_num + 1:03d}"

# This defines the function the register the customer 
def gui_register_customer():
    try:
# It will make a new ID
        new_id = generate_customer_id()
# This will validate and create a new customer using the core logic layer
        customer = CustomerLogic.register_customer(
            name_entry.get(),
            email_entry.get(),
            new_id,
            address_entry.get()
        )
# This part if the code will display the registered customer on the table
        customer_table.insert("", "end", 
            values=(
                customer.customer_id,
                customer._name,
                customer._email,
                customer.address
           )
        )
# After the customer is registered the fields will be cleared for new inputs
        name_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        address_entry.delete(0, tk.END)
# It will let the user know they have been successfully registered
        messagebox.showinfo("Success", "You have been registered successfully!")

    except ValueError as e:
        messagebox.showerror("Error", str(e))

# This button here is to finish registering the customer and displaying on the table
tk.Button(add_customer, text="Register", width=20, command=gui_register_customer).grid(row=8, column=0, padx=50, pady=20)


# staff
# This is the seventh window of my GUI
staff = tk.Frame(window, bg="light blue")
# The lay out of the tab
staff.grid(row=0, column=1, sticky="nsew")
# The heading of the window 
tk.Label(staff, text="Staff", font=("Arial", 15), bg="light blue").grid(row=0, column=0, sticky="nw", padx=20, pady=10)
# This is the treeview table of staff
staff_table = ttk.Treeview(staff, columns=("ID", "Name", "Email", "Position"), show="headings")
# The headings for the staff table
staff_table.heading("ID", text='Staff ID')
staff_table.heading("Name", text='Name')
staff_table.heading("Email", text='Email')
staff_table.heading("Position", text='Position')
staff_table.grid(row=1, column=0, sticky="nsew", padx=20, pady=10)

# This is all the staff members works at bookstore 
staff_table.insert("", "end", values=("S001", "John Smith", "jsmith@bookstore.com", "Manager"))
staff_table.insert("", "end", values=("S002", "Emily Johnson", "ejohnson@bookstore.com", "Online Staff"))
staff_table.insert("", "end", values=("S003", "Sarah Williams", "swilliams@bookstore.com", "Online Staff"))
staff_table.insert("", "end", values=("S004", "David Patel", "dpatel@bookstore.com", "IT Support"))
staff_table.insert("", "end", values=("S005", "Laura Brown", "lbrown@bookstore.com", "System Engineer"))
staff_table.insert("", "end", values=("S006", "Michael Davis", "mdavis@bookstore.com", "Payment support"))

# when starting the program it will show the home page
showFrame(home)
# This is the tkinter event loop
window.mainloop()