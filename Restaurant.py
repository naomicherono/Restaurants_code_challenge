class Restaurant:
    # A class variable to keep track of all restaurant instances
    all_restaurants = []

    def __init__(self, name):
        # Constructor method that initializes a new Restaurant instance
        self.restaurant_name = name
        self.reviews = []  # List to store reviews related to this restaurant
        Restaurant.all_restaurants.append(self)  # Add the instance to the list of all restaurants
        
    def get_name(self):
        # Method to get the name of the restaurant
        return self.restaurant_name
    
    def get_reviews(self):
        # Method to get the list of reviews for the restaurant
        return self.reviews
    
    def customers(self):
        # Method to get a list of customer full names from the restaurant's reviews
        return [review.customer.full_name() for review in self.reviews]
    
    def average_star_rating(self):
        # Method to calculate the average star rating of the restaurant based on reviews
        if not self.reviews:
            return 0
        total_ratings = sum(review.get_rating() for review in self.reviews)
        return total_ratings / len(self.reviews)
    
    @classmethod
    def all(cls):
        # Class method to get a list of all restaurant instances
        return cls.all_restaurants
