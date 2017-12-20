from django.contrib import admin

from .models import UserProfile, FoodData, ExerciseCapacity

admin.site.register(UserProfile)
admin.site.register(FoodData)
admin.site.register(ExerciseCapacity)

