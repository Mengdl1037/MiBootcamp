# UTF-8
# Author: Liu Mengdi
# Date: 2024-06-21
# Function:

"""A class that can be used to represent a restaurant."""
class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Restaurant name: {self.restaurant_name}")
        print(f"Cuisine type: {self.cuisine_type}")
        print(f"Number served: {self.number_served}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open now.")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, increment_number):
        self.number_served += increment_number
