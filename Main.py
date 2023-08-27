from Customer import Customer
from Restaurant import Restaurant
from Review import Review

if __name__ == "__main__":
     # Creating customers names
    customer1 = Customer("Naomi", "Cherono")
    customer2 = Customer("Leonard", "Mutai")


    # Creating different restaurants 
    restaurant1 = Restaurant("Restaurant A")
    restaurant2 = Restaurant("Restaurant B")

     # Create reviews with customers remarks
    review1 = Review(customer1, restaurant1, 4)
    review2 = Review(customer2, restaurant1, 5)
    review3 = Review(customer1, restaurant2, 3)

     # Testing methods
    print(customer1.full_name())  # Output: Naomi Cherono
    print(restaurant1.get_name())  # Output: Restaurant A
    print(review1.get_rating())    # Output: 4
    print(customer1.restaurants()) # Output: ['Restaurant A', 'Restaurant B']
    print(restaurant1.customers()) # Output: ['Naomi Cherono', 'Leonard Mutai']
    print(restaurant1.average_star_rating())  # Output: 4.5





