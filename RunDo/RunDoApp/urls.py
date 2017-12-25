from django.conf.urls import url
from django.contrib import admin


from . import views

app_name = 'RunDoApp'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^logoutUser/$', views.logoutUser, name='logoutUser'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^registration/$', views.registration, name='registration'),
    url(r'^viewHistory/$', views.viewHistory, name='viewHistory'),
    url(r'^getCategories/$', views.getCategories, name='getCategories'),
    url(r'^savedMeals/$', views.savedMeals, name='savedMeals')
]









