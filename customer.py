#!/usr/bin/env python
# coding: utf-8

from car_rental import CarRental

class Customer:

    def __init__(self):
        self.cars = 0
        self.rentalBasis = 0
        self.rentalTime = 0
        self.bill = 0
        self.carModel = 0
        self.carCategory = 0

    def request_car(self):
        cars = input("How many cars would you like to rent?")
        try:
            cars = int(cars)
        except ValueError:
            print("That's not a positive integer!")
            return -1

        if cars < 1:
            print("Invalid input. Number of cars should be greater than zero!")
            return -1
        else:
            self.cars = cars
            print("Available car models:")
            for model, info in CarRental.CAR_MODELS.items():
                print("{}: {} (Hourly: ${}, Daily: ${}, Weekly: ${})".format(
                    model, info["name"], info["hourly_rate"], info["daily_rate"], info["weekly_rate"]))
            self.carModel = int(input("Choose a car model (Enter the corresponding number): "))
            self.carCategory = int(input("Choose a rental category (1: Hourly, 2: Daily, 3: Weekly): "))
        return self.cars

    def return_car(self):
        if self.rentalBasis and self.rentalTime and self.cars and self.carModel and self.carCategory:
            return self.rentalTime, self.rentalBasis, self.cars, self.carModel, self.carCategory
        else:
            return 0, 0, 0, 0, 0
