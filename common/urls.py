from django.urls import path

from .views import register, login, home, logout, error, profile, profile_view, about, update, production, vision

urlpatterns = [
        path('register', register,  name='register'),
        path('login', login, name='login'),
        path('logout', logout, name='logout'),
        path('submit', profile, name='profile'),
        path('profile', profile_view, name='profile_view'),
        path('update', update, name='update'),
        path('about', about, name='about'),
        path('vision', vision, name='vision'),
        path('production', production, name='production'),
        path('error', error, name='error'),
	path('',home, name='home')
        ]
