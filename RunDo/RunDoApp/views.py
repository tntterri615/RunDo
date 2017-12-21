from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import UserProfile, FoodData, ExerciseCapacity
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
    bmr = ((4.536*request.user.userprofile.weight) + (15.88*request.user.userprofile.height) - (5*request.user.userprofile.age) + (5 if request.user.userprofile.gender == 'MALE' else -161))
    print(bmr)
    profile = get_object_or_404(UserProfile, user=request.user)
    data = FoodData.objects.filter(user=request.user)
    temp = []
    for food in data:
        speed = food.exerciseCapacity
        temp.append({
            'food': food,
            'math': food.calculate()
        })

    context = {'profile': profile, 'data': temp}
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
    if request.method == 'POST':
        print(request.POST)
        food_name = request.POST['food_name']
        serving_calories = request.POST['serving_calories']
        serving_units = request.POST['serving_units']
        serving_size = request.POST['serving_size']
        user_servings = request.POST['user_servings']
        total_calories = float(serving_calories)*float(serving_size)*float(user_servings)
        runSpeed = get_object_or_404(ExerciseCapacity, id=request.POST['runSpeed'])
        food = FoodData(user=request.user,
                        serving_calories=serving_calories,
                        serving_units=serving_units,
                        serving_size=serving_size,
                        user_servings=user_servings,
                        food_name=food_name,
                        total_calories=total_calories,
                        exerciseCapacity=runSpeed
                        )
        food.save()

    speed_list = ExerciseCapacity.objects.all()
    most_recent_history = FoodData.objects.filter(user=request.user).order_by('-timestamp')[:7]
    profile = get_object_or_404(UserProfile, user=request.user)

    temp = []
    for food in most_recent_history:
        speed = food.exerciseCapacity
        temp.append({
            'food': food,
            'math': food.calculate()
        })

    return render(request, 'RunDoApp/viewhistory.html', {'speed_list': speed_list,
                                                         'app_id': secret.app_id,
                                                         'app_key': secret.app_key,
                                                         'most_recent_history': temp})




