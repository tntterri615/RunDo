from django.contrib import admin

from .models import UserProfile, FoodData

admin.site.register(UserProfile)
admin.site.register(FoodData)

