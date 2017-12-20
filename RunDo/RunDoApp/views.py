from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import UserProfile, FoodData
from .choices import FITNESS_CHOICES
import datetime
# from django.contrib.auth.decorators import login_required, permission_required


from . import secret

def index(request):
    if request.method == 'POST':
        user = request.POST['user_name']
        password = request.POST['user_password']
        user = authenticate(request, username=user, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('RunDoApp:profile'))
    return render(request, 'RunDoApp/index.html', {})


def profile(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':
        print(request.POST)
        food_name = request.POST['food_name']
        serving_calories = request.POST['serving_calories']
        serving_units = request.POST['serving_units']
        serving_size = request.POST['serving_size']
        user_servings = request.POST['user_servings']
        food = FoodData(user=request.user,
                        serving_calories=serving_calories,
                        serving_units=serving_units,
                        serving_size=serving_size,
                        user_servings=user_servings,
                        food_name=food_name,
                        total_calories=float(serving_calories)*float(serving_size)*float(user_servings))
        food.save()

    text = ''
    for choice in FITNESS_CHOICES:
        if profile.fitnessLevel == choice[0]:
            text = choice[1]
            break
    context = {'profile': profile,
               'fitnessLevelText': text,
               'app_id':secret.app_id,
               'app_key':secret.app_key}
    return render(request, 'RunDoApp/profile.html', context)


def logoutUser(request):
    logout(request)
    return HttpResponseRedirect(reverse('RunDoApp:index'))


def registration(request):
    if request.method == 'POST':
        userName = request.POST['user_name']
        email = request.POST['user_email']
        password = request.POST['user_password']
        age = request.POST['age']
        gender = request.POST['gender']
        height = request.POST['height']
        weight = request.POST['weight']
        fitnessLevel = request.POST['fitnessLevel']
        user = User.objects.create_user(userName, email, password)
        profile = UserProfile(age=age, gender=gender, height=height, weight=weight, fitnessLevel=int(fitnessLevel), user=user, userName=userName)
        profile.save()
        login(request, user)
        return HttpResponseRedirect(reverse('RunDoApp:profile'))
    return render(request, 'RunDoApp/registration.html')


def viewHistory(request):
    most_recent_history = FoodData.objects.order_by('-timestamp')[:7]
    return render(request, 'RunDoApp/viewhistory.html', {'most_recent_history': most_recent_history})




3