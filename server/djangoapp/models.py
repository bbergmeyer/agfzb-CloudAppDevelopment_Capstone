import datetime
from django.db import models
from django.utils.timezone import now
import uuid
import json


# Create your models here.

# model for make of cars in dealership
class CarMake(models.Model):
    make_name = models.CharField(null=False, max_length=100)
    make_description = models.CharField(null=False, max_length=100)

    def __str__(self):
        return self.make_name

# model for car model related to car make
class CarModel(models.Model):
    model_name = models.CharField(null=False, max_length=100)
    dealer_id = models.CharField(null=True, max_length=100)
    SEDAN = 'Sedan'
    SUV = 'SUV'
    WAGON = 'Wagon'
    VAN = 'Van'
    COUPE = 'Coupe'
    TRUCK = 'Truck'
    model_types =  [
        (SEDAN, 'Sedan'),
        (SUV, 'SUV'),
        (WAGON, 'Wagon'),
        (VAN, 'Van'),
        (COUPE, 'Coupe'),
        (TRUCK, 'Truck')
        ]
    model_type = models.CharField(null=False, max_length=20, choices=model_types, default='SEDAN')
    model_year = models.DateField(null=False, default=now)
    model_make = models.ForeignKey(CarMake, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.model_name



class CarDealer:

    def __init__(self, address, city, full_name, id, lat, long, short_name, st, zip):
        # Dealer address
        self.address = address
        # Dealer city
        self.city = city
        # Dealer Full Name
        self.full_name = full_name
        # Dealer id
        self.id = id
        # Location lat
        self.lat = lat
        # Location long
        self.long = long
        # Dealer short name
        self.short_name = short_name
        # Dealer state
        self.st = st
        # Dealer zip
        self.zip = zip

    def __str__(self):
        return "Dealer name: " + self.full_name

class DealerReview(models.Model):

    def __init__(self, dealership, name, purchase, review, purchase_date, car_make, car_model, car_year, sentiment):
        self.dealership = dealership
        self.name = name
        self.purchase = purchase
        self.review = review
        self.purchase_date = purchase_date
        self.car_make = car_make
        self.car_model = car_model
        self.car_year = car_year
        self.sentiment = sentiment
        self.id = ""

    def __str__(self):
        return "Review: " + self.review 


