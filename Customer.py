class Customer:
    all_customers = []


    def __init__(self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name
        self.reviews = []
        Customer.all_customers.append(self)
        
    def get_given_name(self):
        return self.given_name
    
    def get_family_name(self):
        return self.family_name
    
    def full_name(self):
        return f"{self.given_name} {self.family_name}"
    
    def restaurants(self):
        return [review.restaurant.get_name() for review in self.reviews]
    
    @classmethod
    def all(cls):
        return cls.all_customers

