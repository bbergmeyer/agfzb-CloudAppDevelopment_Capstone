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
        return self.make_name + " " + self.make_description

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
        return self.model_name + " " + self.model_type



# <HINT> Create a plain Python class `CarDealer` to hold dealer data
#class CarDealer(models.Model):
#    car_dealer = models.CharField(null=True, max_length=100)


# <HINT> Create a plain Python class `DealerReview` to hold review data
#class DealerReview(models.Model):
#    dealer_review = models.CharField(null=True, max_length=100)
