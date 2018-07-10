from django.urls import path

from .views import register, login, home, logout, error, profile, profile_view

urlpatterns = [
        path('register', register,  name='register'),
        path('login', login, name='login'),
        path('logout', logout, name='logout'),
        path('submit', profile, name='profile'),
        path('profile', profile_view, name='profile_view'),
        path('error', error, name='error'),
	path('',home, name='home')
        ]
