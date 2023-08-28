class Customer:
    # A class variable to keep track of all customer instances
    all_customers = []

    def __init__(self, given_name, family_name):
        # Constructor method that initializes a new Customer instance
        self.given_name = given_name
        self.family_name = family_name
        self.reviews = []  # List to store reviews related to this customer
        Customer.all_customers.append(self)  # Add the instance to the list of all customers
        
    def get_given_name(self):
        # Method to get the given name of the customer
        return self.given_name
    
    def get_family_name(self):
        # Method to get the family name of the customer
        return self.family_name
    
    def full_name(self):
        # Method to get the full name of the customer
        return f"{self.given_name} {self.family_name}"
    
    def restaurants(self):
        # Method to get a list of restaurant names from the customer's reviews
        return [review.restaurant.get_name() for review in self.reviews]
    
    @classmethod
    def all(cls):
        # Class method to get a list of all customer instances
        return cls.all_customers
