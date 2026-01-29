# This the parent class for books
class Book:
# These are all the items that the main class holds 
    def __init__ (self, book_id, title, author, price):
# This is a private attribute for book ID
        self.__book_id = book_id
# This is a protected attribute for book title
        self._title = title
# This is a protected attribute for book author
        self._author = author
# # This is a public attribute for book price
        self.price = price

# This is the getter for the book ID
    @property   
    def book_id(self):
        return self.__book_id
 # This is the setter for book ID   
    @book_id.setter
    def book_id(self, value):
        self.__book_id = value
# This is the getter for price
    @property
    def price(self):
        return self._price
# This is the setter for price
    @price.setter
    def price(self, value):
# This will try to convert the input into a number if it fails then it raise a error
        try:
            value = float(value)
# This part of the code will stop the any invalid inputs and needs to be numeric value
        except ValueError:
            raise ValueError("Price must be a number.")
# This will stop the price going into negative 
        if value < 0:
            raise ValueError("Price cannot be negative.")
# This will validate the price safely in the object 
        self._price = value

# This is the sub class for book
class Fiction(Book):
    def __init__(self, book_id, title, author, price, genre):
        super().__init__(book_id, title, author, price)
# This is the private attribute for book genre
        self.__genre = genre

# This is the getter for genre
    @property
    def genre(self):
        return self.__genre

# This is the setter for genre
    @genre.setter
    def genre(self, value):
        self.__genre = value

# This is the sub class for book
class NonFiction(Book):
    def __init__(self, book_id, title, author, price, subject):
        super().__init__(book_id, title, author, price)
# This is a private attribute for book subject
        self.__subject = subject

# This is the getter for subject
    @property
    def subject(self):
        return self.__subject
    
# This is the setter for subject
    @subject.setter
    def subject(self, value):
        self.__subject = value

# This will create an empty list to store book objects
book_inventory = []

# This defines the function to add a book into inventory
def add_book (book_id, title, author, price, book_type, extra_info):
# This part of the code will let the user know if they missed any fields while adding a book 
    if not all([book_id, title, author, price, book_type, extra_info]):
        raise ValueError("All fields must be filled to add a book to the inventory!")

# This part of the code will create a fiction object when the user types fiction
    if book_type == "Fiction":
        book = Fiction(book_id, title, author, price, extra_info)

# This part of the code will create a non fiction object when the user types non fiction
    elif book_type == "Non-Fiction":
        book = NonFiction(book_id, title, author, price, extra_info)

# This part of the will raise if the user doesn't input fiction or non fiction 
    else:
        raise ValueError("Invalid book type! Must be 'Fiction' or 'Non-Fiction'.")

# This code will store the book in the table 
    book_inventory.append(book)
    return book


