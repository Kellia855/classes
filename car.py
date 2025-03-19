#!/usr/bin/env python3

class Car:
    #initialize the car's attributes
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year

    def start_engine(self):
        print('The engine has started')

    def display_info(self):
         print(f"Car details: {self.brand}, {self.model}, {self.year}")

    def __str__(self):
        return f"{self.year} {self.brand} {self.model}"