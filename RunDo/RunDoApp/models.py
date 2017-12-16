from django.db import models
from django.contrib.auth.models import User
from .choices import *


class UserProfile(models.Model):
    userName = models.CharField(max_length=30)
    age = models.IntegerField()
    gender = models.CharField(choices=GENDER_CHOICES, max_length=6)
    height = models.IntegerField()
    weight = models.IntegerField()
    fitnessLevel = models.IntegerField(choices=FITNESS_CHOICES)
    user = models.OneToOneField(User)

    def __str__(self):
        return self.userName


class FoodData(models.Model):
    foodName = models.CharField(max_length=100)            # need to eventually change to input from api**************
    servingSize = models.IntegerField()
    caloriesPerServing = models.IntegerField()
    user = models.ForeignKey(User)

    def __str__(self):
        return self.foodName

