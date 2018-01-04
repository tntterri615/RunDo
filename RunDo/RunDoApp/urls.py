from django.conf.urls import url
from django.contrib import admin


from . import views

app_name = 'RunDoApp'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^logoutUser/$', views.logoutUser, name='logoutUser'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^registration/$', views.registration, name='registration'),
    url(r'^calculate/$', views.calculatePage, name='calculatePage'),
    url(r'^getCategories/$', views.getCategories, name='getCategories'),
    url(r'^update/$', views.updateProfile, name='updateProfile'),
    url(r'^favorites/$', views.favorites, name='favorites')
]









