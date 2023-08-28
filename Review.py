class Review:
    # A class variable to keep track of all review instances
    all_reviews = []

    def __init__(self, customer, restaurant, rating):
        # Constructor method that initializes a new Review instance
        self.customer = customer  # The associated customer of the review
        self.restaurant = restaurant  # The associated restaurant of the review
        self.rating_value = rating  # The rating value given in the review
        # Add the review to the lists of reviews for both the customer and the restaurant
        customer.reviews.append(self)
        restaurant.reviews.append(self)
        Review.all_reviews.append(self)  # Add the instance to the list of all reviews
        
    def get_rating(self):
        # Method to get the rating value of the review
        return self.rating_value
    
    def get_customer(self):
        # Method to get the customer associated with the review
        return self.customer
    
    def get_restaurant(self):
        # Method to get the restaurant associated with the review
        return self.restaurant
    
    @classmethod
    def all(cls):
        # Class method to get a list of all review instances
        return cls.all_reviews
