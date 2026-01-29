# This defines the base class that store common attributes. It will allow to create subclasses of people
class People:
# At this part of the code people hold name and phone
    def __init__(self, name, email):
# I used the protected attributes for name and email 
        self._name = name
        self._email = email

# This defines the sub class of people  
class Staff(People):
# At this part staff has inherited name and email from people and staff holds staff id and positions
    def __init__(self, name, email, staff_id, position):
# Here it means that it has got the name and email from people
        super().__init__(name, email)
# Here I used private attributes so this means that it can not be accessed easily
        self.__staff_id = staff_id
        self.__position = position

# This is the getter for staff id 
    @property
# It will allow us to read the Staff_id using the object.staff_id instead of accessing it private variable
    def staff_id(self):
        return self.__staff_id

# This is the setter for staff id     
    @staff_id.setter
# This code will help update the value more safer
    def staff_id(self, value):
        self.__staff_id = value
# This is the getter for staff position    
    @property
    def position(self):
        return self.__position
 # This is the setter for staff position   
    @position.setter
    def position(self, value):
        self.__position = value

# This defines the sub class of customer 
class Customer(People):
# At this part customer has inherited name and email from people and customer holds customer ID and address
    def __init__(self, name, email, customer_id, address):
        super().__init__(name, email)
# Here I used the private attributes sp this means that it can not be accessed easily
        self.__customer_id = customer_id
        self.__address = address
 # This is the getter for customer ID   
    @property
    def customer_id(self):
        return self.__customer_id
# This is the setter for customer Id
    @customer_id.setter
    def customer_id(self, value):
        self.__customer_id = value
# This is the getter for customer address
    @property
    def address(self):
        return self.__address
# This is the setter for customer address
    @address.setter
    def address(self, value):
        self.__address = value


# This will create an empty list to store customer objects
customer_data = []

# This defines the function to register new customers to the website
def register_customer(name, email, customer_id, address):
# This part of the code will let the user know if they haven't filled all the fields regarding the customer information
    if not name or not email or not address:
        raise ValueError("You will need to fill all the fields!")

# This will create new customer object  
    customer = Customer(name, email, customer_id, address)
# This part of the code will store newly created customers 
    customer_data.append(customer)
    return customer

# This part of the code will store the current selected customer
current_customer = None
# This defines the funcation to update the current customer with the selected customer object
def set_current_customer(customer):
    global current_customer
    current_customer = customer
# This defines the function that current selected customers to be able to move around 
# to the basket and invoice tabs and they can access it safely
def get_current_customer():
    return current_customer


    
