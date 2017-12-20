import datetime
from django.db import models
from django.contrib.auth.models import User
from .choices import *
from django.utils import timezone


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
    food_name = models.CharField(max_length=100)
    serving_size = models.FloatField()
    serving_units = models.CharField(max_length=30)
    serving_calories = models.FloatField()
    user_servings = models.FloatField()
    total_calories = models.FloatField()
    user = models.ForeignKey(User)
    timestamp = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.food_name + " " + str(self.total_calories)          # food name is not displayed in database


class ExerciseCapacity(models.Model):
    mets = models.FloatField()
    description = models.CharField(max_length=30)






    # fourthree_minmile =
    # five_minmile =
    # fivehalf_minmile=
    # six_minmile =
    # sixhalf_minmile=
    # seven_minmile =
    # sevenhalf_minmile=
    # eight_minmile =
    # eighthalf_minmile=
    # nine_minmile =
    # ninehalf_minmile=
    # ten_minmile =
    # elevenhalf_minmile=
    # twelve_minmile =
    # fifteen_minmile=