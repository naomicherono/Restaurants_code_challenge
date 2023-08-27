class Review:
    all_reviews = []

    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating_value = rating
        customer.reviews.append(self)
        restaurant.reviews.append(self)
        Review.all_reviews.append(self)
        
    def get_rating(self):
        return self.rating_value
    
    def get_customer(self):
        return self.customer
    
    def get_restaurant(self):
        return self.restaurant
    
    @classmethod
    def all(cls):
        return cls.all_reviews
