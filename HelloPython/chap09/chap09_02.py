# UTF-8
# Author: Liu Mengdi
# Date: 2024-06-21
# Function:

class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant name: {self.restaurant_name}")
        print(f"Cuisine type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open now.")


restaurant_1 = Restaurant("KFC", "Fast food")
restaurant_1.describe_restaurant()

restaurant_2 = Restaurant("McDonald's", "Fast food")
restaurant_2.describe_restaurant()

restaurant_3 = Restaurant("Chicken Pot", "Home cooking")
restaurant_3.describe_restaurant()