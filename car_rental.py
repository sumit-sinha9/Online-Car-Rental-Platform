#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import datetime

class CarRental:
    CAR_MODELS = {
        1: {"name": "Compact", "hourly_rate": 10, "daily_rate": 50, "weekly_rate": 200},
        2: {"name": "Sedan", "hourly_rate": 12, "daily_rate": 60, "weekly_rate": 250},
        3: {"name": "SUV", "hourly_rate": 15, "daily_rate": 75, "weekly_rate": 300}
    }

    def __init__(self, stock=0):
        self.stock = stock

    def display_stock(self):
        print("We have currently {} cars available to rent.".format(self.stock))
        return self.stock

    def rent_car(self, n, model, category):
        if n <= 0:
            print("Number of cars should be positive!")
            return None
        elif n > self.stock:
            print("Sorry! We have currently {} cars available to rent.".format(self.stock))
            return None
        elif model not in self.CAR_MODELS:
            print("Invalid car model selection!")
            return None
        else:
            car_info = self.CAR_MODELS[model]
            now = datetime.datetime.now()
            model_name = car_info["name"]
            hourly_rate = car_info["hourly_rate"]
            daily_rate = car_info["daily_rate"]
            weekly_rate = car_info["weekly_rate"]

            if category == 1:
                rate = hourly_rate
                basis = "hourly"
            elif category == 2:
                rate = daily_rate
                basis = "daily"
            elif category == 3:
                rate = weekly_rate
                basis = "weekly"

            print("You have rented {} {} car(s) on {} basis today at {}:{}:{}".format(n, model_name, basis, now.hour, now.minute, now.second))
            print("You will be charged ${} for each {} per car.".format(rate, basis))
            print("We hope that you enjoy our service.")
            self.stock -= n
            return now

    def return_car(self, request):
        rentalTime, rentalBasis, numOfCars, model, category = request
        bill = 0

        if rentalTime and rentalBasis and numOfCars and model and category:
            self.stock += numOfCars
            now = datetime.datetime.now()
            rentalPeriod = now - rentalTime

            car_info = self.CAR_MODELS[model]
            if rentalBasis == 1:
                rate = car_info["hourly_rate"]
            elif rentalBasis == 2:
                rate = car_info["daily_rate"]
            elif rentalBasis == 3:
                rate = car_info["weekly_rate"]

            bill = round(rentalPeriod.seconds / 3600) * rate * numOfCars

            if 3 <= numOfCars <= 5:
                print("You are eligible for a family rental promotion of 30% discount.")
                bill = bill * 0.7

            print("Thanks for returning your car. Hope you enjoyed our service!")
            print("That would be ${}".format(bill))
            return bill
        else:
            print("Are you sure you rented a car with us?")
            return None

