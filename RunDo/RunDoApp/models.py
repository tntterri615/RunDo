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
    user = models.OneToOneField(User)

    def __str__(self):
        return self.userName


class ExerciseCategory(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class ExerciseCapacity(models.Model):
    mets = models.FloatField()
    description = models.CharField(max_length=30)
    category = models.ForeignKey(ExerciseCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.description + ", " + str(self.mets) + " mets"


class FoodData(models.Model):
        food_name = models.CharField(max_length=100)
        serving_size = models.FloatField()                 #'3' oz, '5' cup, etc.
        serving_units = models.CharField(max_length=30)       #tbsp, oz, cup, etc
        serving_calories = models.FloatField()
        user_servings = models.FloatField()           #how much user ate
        total_calories = models.FloatField()
        user = models.ForeignKey(User)
        timestamp = models.DateTimeField(default=timezone.now)
        exerciseCapacity = models.ForeignKey(ExerciseCapacity, on_delete=models.CASCADE)
        time_to_run = models.FloatField()

        def calculate(self):
            bmr = ((4.536 * self.user.userprofile.weight) + (15.88 * self.user.userprofile.height) - (
                    5 * self.user.userprofile.age) + (5 if self.user.userprofile.gender == 'MALE' else -161))
            calories = self.total_calories
            mets = self.exerciseCapacity.mets
            self.time_to_run = calories / (bmr * mets / 24)


        def __str__(self):
            return self.food_name + " " + str(self.total_calories)
        # try
        # except Exception as e:
        #    print e

        def get_readable_time(self):
            time_hours = self.time_to_run
            minutes = round(time_hours * 60)
            if minutes < 60:
                return str(minutes) + ' minutes'
            hours = int(minutes / 60)
            minutes -= hours * 60
            output = ''
            if hours == 1:
                output += '1 hour'
            else:
                output += str(hours) + ' hours'
            if minutes > 0:
                output += ' and ' + str(minutes) + ' minutes'
            return output



