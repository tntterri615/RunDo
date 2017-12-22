from django.contrib import admin

from .models import UserProfile, FoodData, ExerciseCategory, ExerciseCapacity

admin.site.register(UserProfile)
admin.site.register(FoodData)
admin.site.register(ExerciseCategory)
admin.site.register(ExerciseCapacity)

